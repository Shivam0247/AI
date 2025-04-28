import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load dataset
file_path = r"C:\SEM VI\AI LAB\Practical 1\house_price\house_price_dataset.csv"  
df = pd.read_csv(file_path)

# 1. Handle Missing Values
df.fillna(df.median(numeric_only=True), inplace=True)  # Fill missing numeric values with median

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Feature Engineering
df["Price_per_sqft"] = df["Price"] / df["Area_sqft"]  # New feature: price per sqft
df["Total_rooms"] = df["Bedrooms"] + df["Bathrooms"]  # New feature: total rooms

# Convert Age to Categories
df["Age_Group"] = pd.cut(df["Age_years"], bins=[0, 10, 30, 100], labels=["New", "Moderate", "Old"])

# One-hot encode categorical features
df_encoded = pd.get_dummies(df, columns=['Location', 'House_Type', 'Age_Group'], drop_first=True)

# Separate features and target variable
X = df_encoded.drop(columns=['Price'])
y = df_encoded['Price']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the deep learning model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=16, validation_data=(X_test, y_test), verbose=1)

# Evaluate the model
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=1)
print(f"Test Mean Absolute Error: {test_mae}")

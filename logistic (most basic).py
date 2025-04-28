
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 2. Create a Simple Dataset
data = {
    'Age': [22, 25, 47, 52, 46, 56, 56, 60, 62, 65],
    'Salary': [15000, 29000, 48000, 60000, 52000, 61000, 64000, 70000, 72000, 80000],
    'Purchased': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]  # 0 = No, 1 = Yes
}

df = pd.DataFrame(data)
print("Dataset:\n", df)


# 4. Feature and Label Separation
X = df[['Age', 'Salary']]  # Features
y = df['Purchased']        # Label

# 5. Split into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 6. Create Logistic Regression Model
model = LogisticRegression()

# 7. Train the Model
model.fit(X_train, y_train)

# 8. Predict on Test Set
y_pred = model.predict(X_test)

# 9. Evaluate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy on Test Set:", accuracy)

# 10. Final: Predict on New Data
new_data = np.array([[30, 40000]])  # New person: Age=30, Salary=40000
prediction = model.predict(new_data)
print("\nPrediction for Age=30, Salary=40000:", "Purchased" if prediction[0]==1 else "Not Purchased")

import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=1, epochs=2):
        self.weights = np.zeros(input_size + 1)  # +1 for the bias term
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        return 1 if x > 0 else -1

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Adding bias input
        net_input = np.dot(self.weights, x_with_bias)
        return self.activation_function(net_input)

    def train(self, X, y):
        print("Initial Weights:", self.weights)
        for epoch in range(self.epochs):
            print(f"\nEPOCH-{epoch + 1}")
            for i, (x, target) in enumerate(zip(X, y)):
                x_with_bias = np.insert(x, 0, 1)
                net_input = np.dot(self.weights, x_with_bias)
                output = self.activation_function(net_input)
                error = target - output

                print(f"\nInput: {x}, Target: {target}")
                print(f"Net Input: {net_input}, Output: {output}, Error: {error}")

                if error != 0:
                    # Weight update rule
                    self.weights += self.learning_rate * error * x_with_bias
                    print(f"Updated Weights: {self.weights}")
                else:
                    print("No weight change.")


    def test(self, X):
        print("\nTesting Perceptron:")
        for x in X:
            result = self.predict(x)
            print(f"Input: {x} -> Output: {result}")



X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])

y = np.array([1, -1, -1, -1])

# Create Perceptron instance
perceptron = Perceptron(input_size=2)

# Train the Perceptron
perceptron.train(X, y)

# Test the Perceptron
perceptron.test(X)

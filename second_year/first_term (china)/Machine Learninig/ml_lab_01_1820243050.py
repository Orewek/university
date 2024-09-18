import numpy as np

from sklearn.datasets import load_iris


def custom_train_test_split(X, y, test_size=0.2, random_state=None) -> (float, float, float, float):
    """Define custom functions for data splitting"""
    np.random.seed(random_state)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    split_idx = int(len(indices) * (1 - test_size))
    train_idx, test_idx = indices[:split_idx], indices[split_idx:]
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    return (X_train, X_test, y_train, y_test)


def custom_standardize(X_train, X_test) -> (float, float):
    """Define custom function for standardization"""
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    X_train_standardized = (X_train - mean) / std
    X_test_standardized = (X_test - mean) / std
    return (X_train_standardized, X_test_standardized)


def softmax(x) -> float:
    """Define the softmax activation function"""
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)


def relu(x) -> float:
    """Define the ReLU activation function"""
    return np.maximum(0, x)


def sigmoid(x) -> float:
    """Define the sigmoid activation function"""
    return 1 / (1 + np.exp(-x))


def tanh(x) -> float:
    """Define the tanh activation function"""
    return np.tanh(x)

class NeuralNetwork:
    """Define the neural network architecture"""
    def __init__(self, input_size, hidden_size, output_size, activation_func=relu):
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.activation_func = activation_func

    def forward(self, X):
        self.hidden_input = np.dot(X, self.weights_input_hidden)
        self.hidden_output = self.activation_func(self.hidden_input)
        self.output = softmax(np.dot(self.hidden_output, self.weights_hidden_output))
        return self.output

    def backward(self, X, y, output, learning_rate):
        error = y - output

        # Update weights for the output layer
        delta_output = error

        # Calculate gradients for the hidden layer
        delta_hidden = delta_output.dot(self.weights_hidden_output.T) * (self.hidden_output > 0)

        # Update weights using gradients and learning rate
        self.weights_hidden_output += self.hidden_output.T.dot(delta_output) * learning_rate
        self.weights_input_hidden += X.T.dot(delta_hidden) * learning_rate


def train(X_train, y_train, activation_func, learning_rate, epochs) -> (float, float):
    """Train the neural network"""
    input_size = X_train.shape[1]
    hidden_size = 10
    output_size = len(np.unique(y_train))

    nn = NeuralNetwork(input_size, hidden_size, output_size, activation_func)

    y_onehot = np.eye(output_size)[y_train]

    for epoch in range(epochs):
        output = nn.forward(X_train)

        # Calculate loss
        loss = -np.mean(y_onehot * np.log(output + 1e-10))

        # Backpropagation
        nn.backward(X_train, y_onehot, output, learning_rate)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss}")

    return (nn, loss)


def test(model, X_test) -> list[float]:
    """Test the trained model"""
    output = model.forward(X_test)
    predictions = np.argmax(output, axis=1)
    return predictions


def main() -> None:
    # Load and preprocess the data
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Custom train-test split
    X_train, X_test, y_train, y_test = custom_train_test_split(X, y, test_size=0.2, random_state=42)

    # Custom standardization
    X_train, X_test = custom_standardize(X_train, X_test)

    # Set hyperparameters
    learning_rate = 0.001
    epochs = 10000

    # Train models with different activation functions
    model_relu, loss_relu = train(X_train, y_train, activation_func=relu, learning_rate=learning_rate, epochs=epochs)
    model_softmax, loss_softmax = train(X_train, y_train, activation_func=softmax, learning_rate=learning_rate, epochs=epochs)
    model_sigmoid, loss_sigmoid = train(X_train, y_train, activation_func=sigmoid, learning_rate=learning_rate, epochs=epochs)
    model_tanh, loss_tanh = train(X_train, y_train, activation_func=tanh, learning_rate=learning_rate, epochs=epochs)

    # Test models
    predictions_relu = test(model_relu, X_test)
    predictions_softmax = test(model_softmax, X_test)
    predictions_sigmoid = test(model_sigmoid, X_test)
    predictions_tanh = test(model_tanh, X_test)

    # Evaluate models
    accuracy_relu = np.mean(predictions_relu == y_test)
    accuracy_softmax = np.mean(predictions_softmax == y_test)
    accuracy_sigmoid = np.mean(predictions_sigmoid == y_test)
    accuracy_tanh = np.mean(predictions_tanh == y_test)

    print(f"""
           Accuracy (ReLU): {accuracy_relu}\n'
           Accuracy (Softmax): {accuracy_softmax}\n'
           Accuracy (Sigmoid): {accuracy_sigmoid}\n'
           Accuracy (Tanh): {accuracy_tanh}
           """)


if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt


inp = np.load("save/colors.npy")
weights = np.load("save/weights.npy")
alpha = 0.25
batch_size = 16
error_sum = 0
inp_sum = np.array([0.0, 0.0, 0.0])

error_log = []
weight_log = [[], [], []]

sigmoid = lambda x: 1 / (1 + np.exp(-x))


def w_sum(layer, w):
    return layer.dot(w)


for i in range(1, 1 + 2**14):
    index = i % len(inp)
    if index == 0:
        np.random.shuffle(inp)
    data = inp[index]
    inp_sum += data[0:3]
    error_sum += data[3] - sigmoid(w_sum(data[0:3], weights))
    if not bool(i % batch_size):
        error_average = error_sum/batch_size
        inp_average = inp_sum/batch_size
        delta = [inp_average[k]*error_average/np.sum(inp_average)*alpha for k in range(3)]

        for weight in range(len(weights)):
            weights[weight] += delta[weight]

        print(f"{int(i/batch_size)} - Error: {error_average**2}; Weights: {weights}")
        error_log.append(error_average**2)
        weight_log[0].append(weights[0])
        weight_log[1].append(weights[1])
        weight_log[2].append(weights[2])

        # Reset
        error_sum = 0
        inp_sum = np.array([0.0, 0.0, 0.0])

np.save("save/weights.npy", weights)


plt.plot(weight_log[2])
plt.plot(error_log)
plt.plot(weight_log[1])
plt.plot(weight_log[0])

plt.legend(["B", "Error", "G", "R"])

plt.show()

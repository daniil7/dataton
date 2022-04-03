import numpy as np

class Net:

    def __init__(self, n, threshold):
        self.n = n
        self.threshold = threshold
        self.weights = np.array( [0.0 for i in range(n)] )

    def perceptron(self, Sensor):
        s = 0
        for i in range(self.n):
            s += int(Sensor[i]) * self.weights[i]
        if s >= self.threshold:
            return True
        else:
            return False

    def decrease(self, Sensor):
        for i in range(self.n):
            if int(Sensor[i]) == 1:
                self.weights[i] -= 0.1

    def increase(self, Sensor):
        for i in range(self.n):
            if int(Sensor[i]) == 1:
                self.weights[i] += 0.1

    def train(self, Sensor, hit):
        if(self.perceptron(Sensor)):
            if(hit == False):
                self.decrease(Sensor)
        else:
            if(hit == True):
                self.increase(Sensor)

import numpy as np
from operator import itemgetter
import copy

class HyperPipe:

    def __init__(self):
        self.n_dimensions = 0
        self.numerical_bounds = []

    def fit(self, data_x, target_class):
        self.target_class = target_class
        self.n_dimensions = data_x.shape[1]
        #print("\n\n\n self.n_dimensions = ", self.n_dimensions)
        self.attributes = np.zeros((self.n_dimensions, len(data_x)))

        for j in range(self.n_dimensions):
            for i in range(len(data_x)):
                self.attributes[j][i]=data_x[i][j]

        # Initializes bounds
        for i in range(self.n_dimensions):
            bounds = []
            bounds.append(np.amax(self.attributes[i]))  # lower bound
            bounds.append(np.amin(self.attributes[i]))  # upper bound
            self.numerical_bounds.append(bounds)
            print("\n\n\n numerical_bounds = ", self.numerical_bounds)

        # Add instances
        for i in range(data_x.shape[0]):
            self.__add_instance__(data_x[i])

        return None

    def __add_instance__(self, data_x):
        #check boundaries
        for i in range(self.n_dimensions):
            if(data_x[i] < self.numerical_bounds[i][0]):
                self.numerical_bounds[i][0] = data_x[i]
            if(data_x[i] > self.numerical_bounds[i][1]):
                self.numerical_bounds[i][1] = data_x[i]

        return None

    def partial_contains(self, data_x):
        print("\n\n\n\n\n\n__________________________PARTIAL CONTAINS")
        print("tentativa classe = ", self.target_class)
        #print(len(data_x))
        print(data_x)
        #print(self.n_dimensions)
        print(self.numerical_bounds)
        count = 0
        for attribute in data_x:
            #print(attribute)
            for i in range(self.n_dimensions):
                #print(i)
                #print(data_x[i])
                print(attribute[i])
                if(attribute[i] > self.numerical_bounds[i][0] and attribute[i] < self.numerical_bounds[i][1]):
                #if (all(item > self.numerical_bounds[i][0] and item < self.numerical_bounds[i][1] for item in data_x[i])):
                    count += 1
                    #print("count = ", count)
        score = float(count) / self.n_dimensions
        print("score = ", score)

        return (score, self.target_class)


class HyperPipes:

    def __init__(self, hp=None):
        self.hyper_pipes = []


    def fit(self, data_x, data_y):
        self.y_unique_values, self.y_unique_indices = np.unique(
            data_y, return_inverse=True)
        #print("\n\nself.y_unique_values = ", self.y_unique_values)
        #print("\n\nself.y_unique_indices = ", self.y_unique_indices)

        self.n_y_unique = self.y_unique_values.shape[0]
        #print("\n\nself.n_y_unique = ", self.n_y_unique)

        self.hyper_pipes = [HyperPipe() for i in range(self.n_y_unique)]
        #print("\n\nself.hyper_pipes = ", self.hyper_pipes)

        for i in range(self.n_y_unique):
            target_class = self.y_unique_values[i]
            target_class_indices = np.where(data_y == target_class)
            print("\n\ntarget_class_indices = ", target_class_indices)
            print("\n\n\n data_x = ", data_x)
            """pega os atributos da classe"""
            data_x_filtered = data_x[target_class_indices]
            #print("\n\ndata_x_filtered = ", data_x_filtered )
            self.hyper_pipes[i].fit(data_x_filtered, target_class)

        return self.hyper_pipes

    def predict(self, data_x):
        scores = []
        for i in range(self.n_y_unique):
            scores.append(self.hyper_pipes[i].partial_contains(data_x))
        print("\n\n\n Hyperpipes scores = ", scores)
        classe = max(scores,key=itemgetter(0))[1]
        return classe

    def predict2(self, hyperpipes, data_x):
        scores = []
        for i in range(hyperpipes):
            scores.append(hyperpipes[i].partial_contains(data_x))
        print("\n\n\n Hyperpipes scores = ", scores)
        classe = max(scores,key=itemgetter(0))[1]
        return classe

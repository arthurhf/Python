import csv
import numpy as np
from hyperpipes import hyperPipes
from sklearn.datasets import load_iris


class Subset:


    def createsubset(self, dataset,wantedSize, percentageatt, percentageinst, classes):

        subset = []

        ncol = len(dataset[0])
        numLinha = len(dataset)

        print("\n\n{} colunas no DataSet".format(ncol))
        print("{} linhas no DataSet".format(numLinha))

        array = np.array(dataset)
        print("Printing 2D Array")
        print(array)
        print("Choose {} multiple random row from 2D array".format(wantedSize))
        randomRows = np.random.randint(5, size=wantedSize)

        for i in randomRows:
            subset.append(array[i,:])

        print(np.array(subset))

def main():
    iris = load_iris()
    data = iris.data
    s=Subset()
    s.createsubset(data, 10, 1.5, 1.5, 1.5)

if __name__ == '__main__':
    main()

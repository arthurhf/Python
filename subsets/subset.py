import csv
import numpy as np
from hyperpipes import hyperPipes
from sklearn.datasets import load_iris

'juntar o dataset com as classes para não perder os atributos que pertencem àquela classe'
'depois de selecionar as linhas, inverter linhas e colunas para selecionar as colunas (não misturar com as classes)'
'inverter de novo para devolver as linhas como linhas e colunas como colunas'

class Subset:

    def createsubset(self, dataset,wantedSize, percentageatt, percentageinst, classes):

        setWithClasses = dataset.tolist()
        listOListClasses = []
        'transforma a lista com as classes numa nova lista de listas [[c1],[c2]...]'
        for item in classes:
            listOListClasses.append([item])
        'adiciona as classes no dataset'
        setWithClasses = np.append(setWithClasses, listOListClasses, axis=1)
        'pega as linhas'
        partialSubset = self.reduceDataset(setWithClasses,wantedSize, percentageatt, percentageinst, classes)
        aux = np.array(partialSubset)
        'inverte linhas e colunas'
        aux = aux.transpose()
        'pega as colunas depois de pegar as linhas - tirar as classes'
        'problema: numero de linhas é diferente do número de colunas'
        almostSubset = self.reduceDataset(aux, wantedSize, percentageatt, percentageinst, classes)
        subset = np.array(almostSubset)
        subset = subset.transpose()
        print(subset)

    def reduceDataset(self, dataset,wantedSize, percentageatt, percentageinst, classes):

        subsetAux = []

        ncol = len(dataset[0])
        numLinha = len(dataset)

        print("\n\n{} colunas no DataSet".format(ncol))
        print("{} linhas no DataSet".format(numLinha))

        array = np.array(dataset)
        print("Printing 2D Array")
        print(array)
        print("Choose {} multiple random row from 2D array".format(wantedSize))
        randomRows = np.random.randint(numLinha, size=wantedSize)

        for i in randomRows:
            subsetAux.append(array[i,:])

        print(np.array(subsetAux))
        return np.array(subsetAux)

def main():
    iris = load_iris()
    data = iris.data
    s=Subset()
    s.createsubset(data, 10, 1.5, 1.5, iris.target.tolist())

if __name__ == '__main__':
    main()

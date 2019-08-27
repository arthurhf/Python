import csv
import numpy as np
from hyperpipes import hyperPipes
from sklearn.datasets import load_iris

'juntar o dataset com as classes para não perder os atributos que pertencem àquela classe'
'depois de selecionar as linhas, inverter linhas e colunas para selecionar as colunas (não misturar com as classes)'
'inverter de novo para devolver as linhas como linhas e colunas como colunas'

class Subset:
    'atributos = colunas'
    'instancias = linhas'
    def createsubset(self, dataset, percentageatt, percentageinst, classes):

        setWithClasses = dataset.tolist()
        data = dataset.tolist()
        listOListClasses = []
        'transforma a lista com as classes numa nova lista de listas [[c1],[c2]...]'
        for item in classes:
            listOListClasses.append([item])
        'adiciona as classes no dataset'
        setWithClasses = np.append(data, listOListClasses, axis=1)
        'pega as linhas'
        partialSubset = self.reduceInstance(setWithClasses, percentageinst)
        aux = np.array(partialSubset)
        'inverte linhas e colunas'
        aux = aux.transpose()
        'pega as colunas depois de pegar as linhas - tirar as classes'
        'problema: numero de linhas é diferente do número de colunas'
        almostSubset = self.reduceAttributes(aux, percentageatt)
        subset = np.array(almostSubset)
        subset = subset.transpose()
        print(subset)

    def reduceInstance(self, dataset, percentage):

        subsetAux = []

        ncol = len(dataset[0])
        numLinha = len(dataset)

        print("\n\n{} colunas no DataSet".format(ncol))
        print("{} linhas no DataSet".format(numLinha))

        array = np.array(dataset)
        print("Printing 2D Array")
        print(array)
        print("Choose {} multiple random row from 2D array".format(int(percentage*numLinha)))
        randomRows = np.random.randint(numLinha, size=int(percentage*numLinha))
        randomRowsList = randomRows.tolist()
        arrayList = array.tolist()

        for i in randomRowsList:
            if not arrayList[i] in subsetAux:
                subsetAux.append(arrayList[i])

        print(np.array(subsetAux))
        print("Fim reduceInstance \n\n")
        return np.array(subsetAux)

    def reduceAttributes (self, dataset, percentage):
        subsetAux = []
        classes = dataset[-1]
        array = dataset[:-1].copy()
        # print(classes)
        ncol = len(array[0])
        numLinha = len(array)

        print("\n\n{} colunas no DataSet".format(ncol))
        print("{} linhas no DataSet".format(numLinha))

        print("Printing 2D Array")
        print(array)
        print("Choose {} multiple random row from 2D array".format(int(percentage*numLinha)))
        randomRows = np.random.randint(numLinha, size=int(percentage*numLinha))

        randomRowsList = randomRows.tolist()
        arrayList = array.tolist()

        for i in randomRows:
            if not arrayList[i] in subsetAux:
                subsetAux.append(arrayList[i])

        print(np.array(subsetAux))
        print(np.array(subsetAux.append(classes)))
        return np.array(subsetAux)


def main():
    iris = load_iris()
    data = iris.data
    s=Subset()
    s.createsubset(data, 0.8, 0.2, iris.target.tolist())

if __name__ == '__main__':
    main()

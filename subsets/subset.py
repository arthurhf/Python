import csv
import numpy as np
from sklearn.datasets import load_iris

class Subset:
    'atributos = colunas'
    'instancias = linhas'

    def __init__ (self, dataset, percentage):
        numLinha = len(dataset[0])
        self.nAttributes= np.random.randint(numLinha, size=int(percentage*numLinha))

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
        almostSubset, attributes = self.reduceAttributes(aux, percentageatt)
        subset = np.array(almostSubset)
        subset = subset.transpose()
        #print("dento do createsubset = ", subset)
        return subset,attributes

    def reduceInstance(self, dataset, percentage):

        subsetAux = []

        ncol = len(dataset[0])
        numLinha = len(dataset)

        #print("\n\n{} colunas no DataSet".format(ncol))
        #print("{} linhas no DataSet".format(numLinha))

        array = np.array(dataset)
        #print("Printing 2D Array")
        #print(array)
        #print("Choose {} multiple random row from 2D array".format(int(percentage*numLinha)))
        randomRows = np.random.randint(numLinha, size=int(percentage*numLinha))
        randomRowsList = randomRows.tolist()
        arrayList = array.tolist()

        for i in randomRowsList:
            if not arrayList[i] in subsetAux:
                subsetAux.append(arrayList[i])

        #rint(np.array(subsetAux))
        #print("Fim reduceInstance \n\n")
        return np.array(subsetAux)

    def reduceAttributes (self, dataset, percentage):
        subsetAux = []
        classes = dataset[-1]
        array = dataset[:-1].copy()
        # print(classes)
        ncol = len(array[0])
        numLinha = len(array)

        #print("\n\n{} colunas no DataSet".format(ncol))
        #print("{} linhas no DataSet".format(numLinha))

        #print("Printing 2D Array")
        #print(array)
        #print("Choose {} multiple random row from 2D array".format(int(percentage*numLinha)))
        #print("\n\n\n self.nAttributes = ", self.nAttributes)
        randomRows = np.random.randint(numLinha, size=int(percentage*numLinha)) #mudar para fazer np.random.randint(numLinha, size=int(percentage*numLinha))

        randomRowsList = randomRows.tolist()
        arrayList = array.tolist()

        for i in randomRows:
            if not arrayList[i] in subsetAux:
                subsetAux.append(arrayList[i])

        #subsetAux = np.array(subsetAux.append(classes))
        #print(np.array(subsetAux))
        print(np.array(subsetAux.append(classes)))
        return subsetAux,np.unique(randomRows)

    def ajustPrediction(self, array):
        #print("\n\n\n\n ajustPrediction, ")
        # print("\n\n\n self.nAttributes = ", self.nAttributes)
        arrayAux= []
        #print("\n\n\n array = ", array)
        trans = array.transpose()
        #print("\n\n\n tranposta = ", trans)
        transList = trans.tolist()
        #print(transList)
        randomRows = self.nAttributes

        for i in randomRows:
            if not transList[i] in arrayAux:
                arrayAux.append(transList[i])
        #print(arrayAux)
        listAux = np.array(arrayAux).transpose().tolist()
        #print(listAux)
        return listAux
        #criar função para reduzir o tamanho do objeto a ser previsto

def main():
    iris = load_iris()
    data = iris.data
    s=Subset()
    s.createsubset(data, 0.8, 0.2, iris.target.tolist())

if __name__ == '__main__':
    main()

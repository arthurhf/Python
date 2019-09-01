import statistics
from statistics import mode
from hyperpipes.hyperPipes import HyperPipes
from randomforest.randomForest import RandomForest
from subsets.subset import Subset
from sklearn.datasets import load_iris
import random
import numpy as np

class HybridForest:

    def __init__ (self,data, nDeClassificadores, percentageatt, percentageinst):
        self.nDeClassificadores = nDeClassificadores
        self.percentageatt = percentageatt
        self.percentageinst = percentageinst
        self.bd =[]
        self.clf =[]
        self.obj = Subset(np.array(data), self.percentageatt)


    def fit (self, data_x, classes):

        for i in range (self.nDeClassificadores):
            #print("iteração i = ")
            #print(i)
            #print(self.nDeClassificadores)
            self.bd.append(self.obj.createsubset(data_x, self.percentageatt, self.percentageinst, classes))
            # data_x_filtered, classes_filtered = bd[i] ver se separa objetos das classes
            print("\n\n\nself.bd[i] =")
            print(self.bd[i])
            array = np.array(self.bd[i]).transpose()
            print("\n\n\n array = ")
            print(array)
            data_x_filtered = array[0:(len(array)-1)] #errado: usar numpy array no bd, fazer o transpose do bd, tirar a ultima linha e transpor de novo bd[0:(len(bd)-1)]
            #print(data_x_filtered)
            classes_filtered = array[-1]# errado: usar o transpose do bd para pegar a ultima linha bd[-1]
            data_x_list = data_x_filtered.transpose()
            classes_list = classes_filtered.transpose()
            print("\n\n\n classes = ")
            print(classes_filtered)
            classificador = random.randint(1,3)
            #print("\n\n\n Classificador = ")
            #print(classificador)
            hp = HyperPipes()
            rf = RandomForest()
            print("\n\n\ndata_x_list = ")
            print(data_x_list)
            print("\n\n\nclasses_list = ")
            print(classes_list)
            if classificador == 1:
                self.clf.append(rf.fit(data_x_list,classes_list)) # testar
                #print("\n\n\n entrou hp, ", self.clf)
            else:
                self.clf.append(rf.fit(data_x_list,classes_list))
                #print("\n\n\n entrou rf, ",self.clf)

    def predict (self, newObject): # newObject é uma lista com os atributos
        classeCalculada = []
        classes = []
        newObj = self.obj.ajustPrediction(np.array(newObject))
        for i in range (self.nDeClassificadores):
            classeCalculada.append(self.clf[i].predict(newObj))
        for item in classeCalculada:
            classes.append(item[0])

        print(self.bd)
        print(classes)
        print("\n\n\n classe do novo objeto = ")
        return mode(classes)

def main():
    iris = load_iris()
    data = iris.data
    target = iris.target
    hf=HybridForest(data, 10, 0.8, 0.2)
    hf.fit(data, target)
    print(hf.predict([[5.5, 2.4, 3.7, 1.0]]))

if __name__ == '__main__':
    main()

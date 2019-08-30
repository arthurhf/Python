import statistics
from statistics import mode
from hyperpipes.hyperPipes import HyperPipes
from randomforest.randomForest import RandomForest
from subsets.subset import Subset
from sklearn.datasets import load_iris
import random

class HybridForest:

    def __init__ (self, nDeClassificadores, percentageatt, percentageinst):
        self.nDeClassificadores = nDeClassificadores
        self.percentageatt = percentageatt
        self.percentageinst = percentageinst
        self.bd =[]
        self.clf =[]


    def fit (self, data_x, classes):

        for i in range (self.nDeClassificadores):
            print("iteração i = ")
            print(i)
            print(self.nDeClassificadores)
            subset = Subset()
            self.bd.append(subset.createsubset(data_x, self.percentageatt, self.percentageinst, classes))
            # data_x_filtered, classes_filtered = bd[i] ver se separa objetos das classes
            data_x_filtered = self.bd[i][0:(len(self.bd[i])-1)] #errado: usar numpy array no bd, fazer o transpose do bd, tirar a ultima linha e transpor de novo bd[0:(len(bd)-1)]
            print(data_x_filtered)
            classes_filtered = self.bd[i][(len(self.bd[i])-1)]# errado: usar o transpose do bd para pegar a ultima linha bd[-1]
            print("\n\n\n classes = ")
            print(classes_filtered)
            classificador = random.randint(1,3)
            print("\n\n\n Classificador = ")
            print(classificador)
            hp = HyperPipes()
            rf = RandomForest()
            print("\n\n\ndata_x_filtered = ")
            print(data_x_filtered)
            print("\n\n\nclasses_filtered = ")
            print(classes_filtered)
            if classificador == 1:
                self.clf.append(hp.fit(data_x_filtered,classes_filtered)) # testar
            else:
                self.clf.append(rf.fit(data_x_filtered,classes_filtered))

    def predict (self, newObject): # newObject é uma lista com os atributos
        classeCalculada = []
        for i in range (self.nDeClassificadores):
            classeCalculada.append(self.clf[i].predict(newObject))

        return mode(classeCalculada)

def main():
    iris = load_iris()
    data = iris.data
    target = iris.target
    hf=HybridForest(1, 0.8, 0.2)
    hf.fit(data, target)
    print(hf.predict([5.5, 2.4, 3.7, 1.0]))

if __name__ == '__main__':
    main()

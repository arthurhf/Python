import collections
from collections import Counter
from hyperpipes.hyperPipes import HyperPipes, HyperPipe
from randomforest.randomForest import RandomForest
from subsets.subset import Subset
from sklearn.datasets import load_iris
import random
import numpy as np
from operator import itemgetter

class HybridForest:

    def __init__ (self,data, nDeClassificadores, percentageatt, percentageinst):
        self.nDeClassificadores = nDeClassificadores
        self.percentageatt = percentageatt
        self.percentageinst = percentageinst
        self.bd =[]
        self.clf =[]
        self.obj = Subset(np.array(data), self.percentageatt)
        self.att = []

    def fit (self, data_x, classes):
        print("data_x = ",data_x)
        print("classes = ", classes)
        for i in range (self.nDeClassificadores):
            print("iteração i = ", i)
            #print(i)
            #print(self.nDeClassificadores)
            sbd, att = self.obj.createsubset(data_x, self.percentageatt, self.percentageinst, classes)
            print("sbd = ", sbd)

            self.bd.append(sbd)
            self.att.append(att)
            # data_x_filtered, classes_filtered = bd[i] ver se separa objetos das classes
            #print("\n\n\nself.bd[i] =")
            #print(self.bd[i])
            array = np.array(self.bd[i]).transpose()
            #print("\n\n\n array = ")
            #print(array)
            data_x_filtered = array[0:(len(array)-1)] #errado: usar numpy array no bd, fazer o transpose do bd, tirar a ultima linha e transpor de novo bd[0:(len(bd)-1)]
            #print(data_x_filtered)
            classes_filtered = array[-1]# errado: usar o transpose do bd para pegar a ultima linha bd[-1]
            data_x_list = data_x_filtered.transpose()
            classes_list = classes_filtered.transpose()
            #print("\n\n\n classes = ")
            #print(classes_filtered)
            classificador = random.randint(1,3)
            #print("\n\n\n Classificador = ")
            #print(classificador)
            hp = HyperPipes()
            rf = RandomForest()
            #print("\n\n\ndata_x_list = ")
            #print(data_x_list)
            #print("\n\n\nclasses_list = ")
            print(classes_list)
            if classificador == 1:
                self.clf.append(hp.fit(data_x_list,classes_list)) # testar
                #print("\n\n\n entrou hp, ", self.clf)
            else:
                self.clf.append(rf.fit(data_x_list,classes_list))
                #print("\n\n\n entrou rf, ",self.clf)

    def predict (self, newObject): # newObject é uma lista com os atributos
        print("\n\n\n\n\n _____________________________________ ENTROU PREDICT__________________")
        classeCalculada = []
        scoresHp=[]
        classes = []
        #newObj = self.obj.ajustPrediction(np.array(newObject))
        for i in range (self.nDeClassificadores):
            #print("att[] = ", self.att[i])
            #print("newObject = ", newObject)
            arr = np.array(newObject)
            newObj = arr[:,self.att[i]]
            #print(np.array(self.clf))
            #print(len(self.clf))
            print("\n\n\n\n\n clf[i] = ", self.clf[i] )
            if isinstance(self.clf[i], list):
                for pipe in self.clf[i]:
                    scoresHp.append(pipe.partial_contains(newObj))
                print("scoresHp = ", scoresHp)
                classeCalculada.append(max(scoresHp,key=itemgetter(0))[1])
                scoresHp=[]
            else:
                pred = self.clf[i].predict(newObj)
                print("pred = ", pred)
                classeCalculada.append(pred[0].tolist())

        #print(self.bd)
        print("classes possiveis = ",classeCalculada)
        print("\n\n\n")
        return Counter(classeCalculada).most_common(1)

def main():
    iris = load_iris()
    data = iris.data
    target = iris.target
    hf=HybridForest(data, 10, 0.8, 0.2)
    hf.fit(data, target)
    new = [[ 5.1,  3.8,  1.9,  0.4], [ 6.9,  3.1,  4.9,  1.5],[ 6.9,  3.2,  5.7,  2.3] ]
    preds = []
    for item in new:
        print("novo objeto= ", item)
        pred = hf.predict([item])
        print("classe = ", pred)
        preds.append(pred)
    print("preds = ", preds)
if __name__ == '__main__':
    main()

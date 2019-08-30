import statistics
from statistics import mode
from hyperpipes import hyperPipes
from randomforest import randomForest
from subsets import subset
from sklearn.datasets import load_iris

class HybridForest:
    bd = []
    clf = []
    nDeClassificadores = 0
    percentageatt = 0
    percentageinst = 0

    def __init__ (self, nDeClassificadores, percentageatt, percentageinst):
        self.nDeClassificadores = nDeClassificadores
        self.percentageatt = percentageatt
        self.percentageinst = percentageinst

    def fit (self, data_x, classes):

        for i in range (self.nDeClassificadores):
            subset = Subset()
            self.bd.append(subset.createsubset(data_x, percentageatt, percentageinst, classes))
            # data_x_filtered, classes_filtered = bd[i] ver se separa objetos das classes
            data_x_filtered = bd[i][0:(len(bd[i])-1)]
            print(data_x_filtered)
            classes_filtered = bd[i][(len(bd[i])-1)]
            print("\n\n\n classes = ")
            print(classes_filtered)
            classificador = random.randint(1,3)
            print("\n\n\n Classificador = ")
            print(classificador)
            hp = HyperPipes()
            rf = RandomForest()
            if classificador == 1:
                clf.append(hp.fit(data_x_filtered,classes_filtered)) # testar
            else:
                clf.append(rf.fit(data_x_filtered,classes_filtered))

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

import statistics
from statistics import mode
from hyperpipes import hyperPipes
from randomforest import randomForest
from subsets import subset

class HybridForest:
    bd = []
    clf = []
    nDeClassificadores = 0
    percentageatt = 0
    percentageinst = 0

    def __init__ (nDeClassificadores, percentageatt, percentageinst):
        self.nDeClassificadores = nDeClassificadores
        self.percentageatt = percentageatt
        self.percentageinst = percentageinst

    def fit (data_x, classes):

        for i in range (nDeClassificadores):
            subset = Subset()
            self.bd.append(subset.createsubset(data_x, percentageatt, percentageinst, classes))
            # data_x_filtered, classes_filtered = bd[i] ver se separa objetos das classes
            data_x_filtered = bd[i][0:(len(bd[i])-1)]
            classes_filtered = bd[i][(len(bd[i])-1)]
            classificador = random.randint(1,3)
            hp = HyperPipes()
            rf = RandomForest()
            if classificador == 1:
                clf.append(hp.fit(data_x_filtered,classes_filtered)) # testar
            else:
                clf.append(rf.fit(data_x_filtered,classes_filtered))

    def predict (newObject): # newObject é uma lista com os atributos
        classeCalculada = []
        for i in range (self.nDeClassificadores):
            classeCalculada.append(self.clf[i].predict(newObject))

        return mode(classeCalculada)

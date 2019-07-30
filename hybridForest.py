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
            self.bd.append(subset(data_x, percentageatt, percentageinst, classes))
            data_x_filtered, classes_filtered = bd[i]
            classificador = random.randint(1,3)
            if classificador == 1:
                clf.append(HyperPipe.fit(data_x,classes))
            else clf.append(ArvoreDeDecisao) #implementar

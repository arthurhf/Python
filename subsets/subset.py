import csv
import numpy as np
from hyperpipes import hyperPipes


class Subset:


    def createsubset(self, dataset, percentageatt, percentageinst, classes):

        set = dataset

        numLinha = 0
        #set = []
        subset = []

        #with open(file, 'r') as ficheiro:
        #    reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)

            #for linha in reader:
            #    ncol = len(linha)
            #    set.append(linha)
            #    numLinha += 1
        for linha in set:
            ncol = len(linha)
            set.append(linha)
            numLinha += 1
        print(set)

        print("\n\n{} colunas no DataSet".format(ncol))
        print("{} linhas no DataSet".format(numLinha))
        for index in set:
            print(index)

            # ini = random.randrange(0, numLinha, 1)
            # print("\n\n{} linhas no SubSet".format(ini))

            # for i in range(ini):
            # print(i)
            # print(set[i])
            #   subset.append(set[i])
            # print(subset)

            # for indexx in subset:
            #   print(indexx)

        #mudar a forma de pegar linhas e colunas: aleatoriamente e não no intervalo
        amostraAt = np.sort(np.random.choice(numLinha, round(numLinha * percentageatt), replace=False))
        # amostraAt = np.sort(np.random.choice(numLinha, 5, replace=False))
        # amostraInst = np.sort(np.random.choice(percentageinst, 3, replace=False))???????????
        amostraInst = np.sort(np.random.choice(ncol, round(ncol * percentageinst), replace=False))

        # print("\n\n" + amostraAt + "\n\n" + amostraInst)

        for i in amostraAt:
            # print(i)
            # print(set[i])
            subset.append(set[i])
            print(i)

        print(subset)
        #return subset

        subsetInst = np.array(set)[amostraInst, :]
        subsetAtr = np.array(set)[:, amostraAt]

        print(subsetAtr)
        print(subsetInst)


        #retornar uma tupla ([atributos], [classes])

        #hyper = HyperPipes()
        #hyper.fit(subset[:, 0:ncol-1], subset[:, ncol-1])
        #return hyper

import csv
import numpy as np
from hyperpipes import HyperPipes


class Subset:

    def createsubset(self, dataset, percentageatt, percentageinst):

        numLinha = 0
        set = []
        subset = []

        with open('multiTimeline.csv', 'r') as ficheiro:
            reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)

            for linha in reader:
                ncol = len(linha)
                set.append(linha)
                numLinha += 1
            ficheiro.close()
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

        subsetInst = np.array(set)[amostraInst, :]
        subsetAtr = np.array(set)[:, amostraAt]

        hyper = HyperPipes()
        hyper.fit(subset[:, 0:ncol-1], subset[:, ncol-1])
        return hyper

#creates a subdataset from an existing csv dataset
import csv
import numpy as np
import random

numLinha = 0
set = []
subset = []

with open('multiTimeline.csv', 'r') as ficheiro:
    reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)

    for linha in reader:
        set.append(linha)
        numLinha += 1

    ficheiro.close()

print("\n\n{} linhas no DataSet".format(numLinha))
for index in set:
    print(index)

#ini = random.randrange(0, numLinha, 1)
#print("\n\n{} linhas no SubSet".format(ini))

#for i in range(ini):
    #print(i)
    #print(set[i])
 #   subset.append(set[i])
    #print(subset)

#for indexx in subset:
 #   print(indexx)

amostraAt = np.sort(np.random.choice(numLinha, 5, replace=False))
amostraInst = np.sort(np.random.choice(3, 3, replace=False))
print(amostraAt, amostraInst)

for i in amostraAt:
    #print(i)
    #print(set[i])
    subset.append(set[i])
    print(subset)

#subsetInst = np.array(set)[amostraInst,:]
#subsetAtr = np.array(set)[:, amostraAt]

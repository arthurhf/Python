import csv
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

ini = random.randrange(0, numLinha, 1)
print("\n\n{} linhas no SubSet".format(ini))

for i in range(ini):
    #print(i)
    #print(set[i])
    subset.append(set[i])
    #print(subset)

for indexx in subset:
    print(indexx)

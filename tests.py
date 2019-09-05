from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from hyperpipes.hyperPipes import HyperPipes, HyperPipe
from randomforest.randomForest import RandomForest
from sklearn.datasets import load_iris
from hybridForest import HybridForest
from sklearn.model_selection import train_test_split
import numpy as np

def crossVal(model, data, classes):
    return cross_val_score(model, data, classes)

def main():
    scores_hf = []
    scores_hp = []
    scores_rf = []
    iris = load_iris()
    data = iris.data
    target = iris.target
    hf=HybridForest(data, 10, 0.8, 0.2)
    hf.fit(data, target)

    hp = HyperPipes()
    hps = hp.fit(data, target)

    rf=RandomForest()
    rf.fit(data, target)

    complete = []
    classes = []
    for item in target:
        classes.append([item])

    complete = np.append(data, classes)

    X_train, X_test, y_train, y_test = train_test_split(data, classes,test_size=0.33, random_state=42)


    new = [[ 6.6,3.,4.4,1.4]]
    for i in range(10):
        scores_hf.append(hf.predict(X_test))
        scores_hp.append(hp.predict(X_test))
        scores_rf.append(rf.predict(X_test))

    print(X_train)
    print(X_test)
    print("scores_hf = ", scores_hf)
    print("scores_hp = ", scores_hp)
    print("scores_rf = ", scores_hf)

if __name__ == '__main__':
    main()

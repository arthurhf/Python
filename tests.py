from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from hyperpipes.hyperPipes import HyperPipes, HyperPipe
from randomforest.randomForest import RandomForest
from sklearn.datasets import load_iris
from hybridForest import HybridForest

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

    new = [[ 6. ,  3. ,  4.8,  1.8],
       [ 6.9,  3.1,  5.4,  2.1],
       [ 6.7,  3.1,  5.6,  2.4],
       [ 6.9,  3.1,  5.1,  2.3],
       [ 5.8,  2.7,  5.1,  1.9],
       [ 6.8,  3.2,  5.9,  2.3],
       [ 6.7,  3.3,  5.7,  2.5],
       [ 6.7,  3. ,  5.2,  2.3],
       [ 6.3,  2.5,  5. ,  1.9],
       [ 6.5,  3. ,  5.2,  2. ],
       [ 6.2,  3.4,  5.4,  2.3],
       [ 5.9,  3. ,  5.1,  1.8]]
       
    for i in range(10):
        scores_hf.append(hf.predict(new))
        scores_hp.append(hp.predict(new))
        scores_rf.append(rf.predict(new))
    print("scores_hf = ", scores_hf)
    print("scores_hp = ", scores_hp)
    print("scores_rf = ", scores_hf)

if __name__ == '__main__':
    main()

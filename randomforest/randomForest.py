from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
class RandomForest:

    def __init__ (self):

        self.clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0, criterion="entropy")

    def fit (self, data, target):
        self.clf.fit(data, target)
        #print(self.clf)
        return self.clf

    def predict (self, obj):
        #print(self.clf.feature_importances_)
        return self.clf.predict(obj)

def main():
    iris = load_iris()
    data = iris.data
    target = iris.target
    rf=RandomForest()
    rf.fit(data, target)
    print(rf.predict([[5.5, 2.4, 3.7, 1.0]]))

if __name__ == '__main__':
    main()

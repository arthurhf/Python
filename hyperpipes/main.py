from numpy import genfromtxt, array
from hyperPipes import HyperPipes

'''file_name = 'datasets/iris'''''
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
data = iris.data
n_cols = data.shape[1]
#print('\n\n\n\nncols= ', n_cols)

data_x = data
#print('\n\n\n\ndata_x ', data_x)


data_y = iris.target
#print('\n\n\n\ndata_y ', data_y)

test_instance_x = array([[5.5, 2.4, 3.7, 1.0]])
test_instance_y = array([2.0])

classifier = HyperPipes()
cl = classifier.fit(data_x, data_y)
prediction = classifier.predict(test_instance_x)
print(classifier)
print(cl)
print(test_instance_x)
print("classe do novo objeto= ",prediction)

# hp_plt = HyperPipesPlot(points)
# hp_plt.add_plot_point(point)
# hp_plt.plot()

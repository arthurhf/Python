from numpy import genfromtxt, array
from hyperPipes import HyperPipes

file_name = '..\\..\\datasets\\simple_separated.csv'

data = genfromtxt(file_name, delimiter=',')
n_cols = data.shape[1]
data_x = data[:,0:n_cols-1]
data_y = data[:,n_cols-1]

test_instance_x = array([2.1, 2.3])
test_instance_y = array([2.0])

classifier = HyperPipes()
classifier.fit(data_x, data_y)
prediction =  classifier.predict(test_instance_x)

print prediction

# hp_plt = HyperPipesPlot(points)
# hp_plt.add_plot_point(point)
# hp_plt.plot()

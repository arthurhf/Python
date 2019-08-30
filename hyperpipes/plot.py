from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


class HyperPipesPlot:

    def __init__(self, points):
        self.classes_len = len(points)
        self.points = points
        self.colors = ['b', 'g', 'c', 'm', 'k', 'y']
        self.figure = plt.figure()

    def __getVisualHyperPipe__(self, x, y, color):
        min_x, max_x = min(x), max(x)
        min_y, max_y = min(y), max(y)
        return Rectangle((min_x, min_y), (max_x - min_x), (max_y - min_y), fill=None, alpha=1, edgecolor=color)

    def plot(self):
        currentAxis = plt.gca()

        for i in range(self.classes_len):
            x = self.points[i][0]
            y = self.points[i][1]
            rect = self.__getVisualHyperPipe__(x, y, self.colors[i])
            currentAxis.add_patch(rect)
            class_plot, = plt.plot(
                x, y, self.colors[i] + 's', label="Class " + str(i + 1))

        plt.title('HyperPipes Model')
        plt.ylabel('Y Axis')
        plt.xlabel('X Axis')
        plt.legend()
        plt.show()

    def add_plot_point(self, point):
        plt.plot(point[0], point[1], 'rs', label="Validation")
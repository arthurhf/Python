from subset import Subset


class Ensemble:

    def create(self, dataset, nhyperpipes, percentageatt, percentageinst):
        s = Subset()
        print(dataset + "" + nhyperpipes+'' + percentageatt+"" + percentageinst)
        ensemble = []

        for i in range(nhyperpipes):

            ensemble.append(s.createsubset(dataset, percentageatt, percentageinst))

        return ensemble

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import sklearn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib.pyplot import figure
from dtreeviz.trees import dtreeviz


class Getcohort:
    def __init__(self, data, metrics_column):
        self.data = data
        self.metrics_column = metrics_column

    def _get_rolled_up_data(self, data, metrics_column):
        df_roll_tmp = data.copy()
        df_roll_x = df_roll_tmp.drop(metrics_column, 1)
        df_roll_x = pd.get_dummies(df_roll_x)
        df_roll_y = df_roll_tmp[metrics_column]
        return df_roll_x, df_roll_y

    def _fit_model(self, df_x, df_y, model='DecisionTreeRegressor', max_depth=6):
        if model == 'DecisionTreeRegressor':
            tree = DecisionTreeRegressor(max_depth=max_depth)
            modelfit = tree.fit(df_x, df_y)
            return modelfit

    def _plot_dt(self, model, df_roll_x, df_roll_y, featurenames):
        plt.figure(figsize=(15, 12))  # set plot size (denoted in inches)
        # sklearn.tree.plot_tree(model, feature_names=featurenames, fontsize=10)
        viz = dtreeviz(model, df_roll_x, df_roll_y, target_name=self.metrics_column, feature_names=featurenames)
        return viz

    def plot_cohorts(self, model='DecisionTreeRegressor', max_depth=6):
        df_roll_x, df_roll_y = self._get_rolled_up_data(self.data, self.metrics_column)
        modelfit = self._fit_model(df_roll_x, df_roll_y, model, max_depth)
        viz = self._plot_dt(modelfit, df_roll_x, df_roll_y, df_roll_x.columns)
        return viz

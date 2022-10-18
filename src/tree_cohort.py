import pandas as pd
import pandasql as ps
from sklearn.tree import DecisionTreeRegressor
import sklearn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from matplotlib.pyplot import figure

class Getcohort:
    def __init__(self, data, metrics_column):
        self.data = data
        self.metrics_column = metrics_column

    def _get_rolled_up_data(self, data, metrics_column):
        df_roll_tmp = data.copy()
        df_roll_x = df_roll_tmp.drop(metrics_column, 1)
        df_roll_x = pd.get_dummies(df_roll_x[cat_columns])
        df_roll_y = df_roll_tmp[metrics_column]
        return  df_roll_x , df_roll_y

    def _fit_model(self, df_x, df_y, model='DecisionTreeRegressor', max_depth=6):
        if model == 'DecisionTreeRegressor':
            tree = DecisionTreeRegressor(max_depth=max_depth)
            modelfit = tree.fit(df1_roll_x, df1_roll_y)
            return modelfit

    def _plot_dt(self, model, featurenames):
        plt.figure(figsize=(15, 12))  # set plot size (denoted in inches)
        sklearn.tree.plot_tree(model, feature_names, fontsize=10)
        plt.show()

    def plot_cohorts(self, data, metrics_column, model='DecisionTreeRegressor', max_depth=6):
        df_roll_x , df_roll_y = _get_rolled_up_data(self.data, self.metrics_column)
        modelfit = _fit_model(df_roll_x, df_roll_y, model, max_depth)
        _plot_dt(modelfit, df_roll_x.columns)








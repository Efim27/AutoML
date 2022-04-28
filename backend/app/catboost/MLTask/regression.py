import catboost as cb
import numpy as np
import shap
from app.catboost.DatasetLoaders.csv import CsvLoader
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


class RegressionModel:
    def __init__(self, project_path, filename, dataset_origin):
        self.project_path = project_path
        self.dataset_name = filename
        self.dataset_origin = dataset_origin

        self.full_dataset = None
        self.train_dataset = None
        self.test_dataset = None
        self.model = None

    def grid_search(self):
        grid = {'iterations': [1000, 2000],
                'learning_rate': [0.01, 0.1]}

        self.model.grid_search(grid, self.train_dataset)

    def train(self):
        self.load_dataset()

        self.model = cb.CatBoostRegressor(loss_function='RMSE')
        self.grid_search()

    def save_graph_evaluate(self):
        _, X_test, _, Y_test = self.full_dataset
        sorted_feature_importance = self.model.feature_importances_.argsort()
        plt.barh(list(X_test.columns),
                 self.model.feature_importances_[sorted_feature_importance],
                 color='turquoise')
        plt.xlabel("Влияние параметров датасета")
        plt.savefig(f'{self.project_path}/scratch0.png')

        explainer = shap.TreeExplainer(self.model)
        shap_values = explainer.shap_values(X_test)
        shap.summary_plot(shap_values, X_test, feature_names=list(X_test.columns), show=False)
        plt.savefig(f'{self.project_path}/scratch1.png')

    def evaluate(self):
        if self.model is None:
            return

        _, X_test, _, Y_test = self.full_dataset
        pred = self.model.predict(X_test)
        rmse = (np.sqrt(mean_squared_error(Y_test, pred)))
        r2 = r2_score(Y_test, pred)

        self.save_graph_evaluate()

    def load_dataset(self):
        csv_loader = CsvLoader(f'{self.project_path}/{self.dataset_name}')
        csv_loader.load()

        self.full_dataset = csv_loader.split(
            self.dataset_origin)
        X_train, X_test, Y_train, Y_test = self.full_dataset
        self.train_dataset = cb.Pool(X_train, Y_train)
        self.test_dataset = cb.Pool(X_test, Y_test)

    def save(self) -> str:
        model_name = "model.cbm"
        self.model.save_model(f'{self.project_path}/{model_name}')
        return model_name

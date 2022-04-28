import pandas as pd
from sklearn.model_selection import train_test_split


class CsvLoader:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset = None

    def read(self, dataset_path):
        return pd.read_csv(dataset_path, na_values='?', skipinitialspace=True, on_bad_lines='skip')

    def prepare(self, raw_dataset):
        raw_dataset = raw_dataset.select_dtypes(exclude=['object'])

        return raw_dataset.dropna()

    def load(self):
        raw_dataset = self.read(self.dataset_path)
        self.dataset = self.prepare(raw_dataset)

        return self.dataset

    def split(self, origin_column):
        if self.dataset is None:
            return None

        X, Y = self.dataset.drop(origin_column, axis=1), self.dataset[origin_column]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.2)

        return X_train, X_test, Y_train, Y_test

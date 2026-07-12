import os
import pandas as pd


class DatasetBuilder:

    def __init__(self):

        self.file = "data/ml_dataset.csv"

    def append(self, row):

        df = pd.DataFrame([row])

        if os.path.exists(self.file):

            df.to_csv(
                self.file,
                mode="a",
                header=False,
                index=False
            )

        else:

            df.to_csv(
                self.file,
                index=False
            )
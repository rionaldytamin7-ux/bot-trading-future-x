import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


class AITrainer:

    def __init__(self):

        self.dataset = "data/ml_dataset.csv"

        self.model = "data/rio_ai_model.pkl"

        version = datetime.now().strftime(
            "rio_model_%Y%m%d_%H%M.pkl"
        )

        joblib.dump(
            model,
            f"data/models/{version}"
        )
##
        manager = ModelManager()

        model = manager.load_active()

    def train(self):

        df = pd.read_csv(self.dataset)

        X = df.drop(columns=["win"])

        y = df["win"]

        model = RandomForestClassifier(

            n_estimators=300,

            random_state=42

        )

        model.fit(X, y)

        joblib.dump(

            model,

            self.model

        )

        return model
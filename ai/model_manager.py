import os
import joblib


class ModelManager:

    def __init__(self):

        self.folder = "data/models"

        self.active = "data/models/active_model.txt"

        os.makedirs(self.folder, exist_ok=True)

    def get_active_model(self):

        if not os.path.exists(self.active):
            return None

        with open(self.active, "r") as f:
            return f.read().strip()

    def load_active(self):

        model = self.get_active_model()

        if model is None:
            return None

        return joblib.load(
            os.path.join(
                self.folder,
                model
            )
        )

    def activate(self, filename):

        with open(self.active, "w") as f:
            f.write(filename)
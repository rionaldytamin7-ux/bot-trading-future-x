import joblib
import pandas as pd


class AIPredictor:

    def __init__(self):

        self.model = joblib.load(

            "data/rio_ai_model.pkl"

        )


    def predict(

        self,

        features

    ):

        df = pd.DataFrame([features])

        probability = self.model.predict_proba(df)

        prediction = self.model.predict(df)

        return {

            "prediction": int(prediction[0]),

            "confidence": float(

                probability[0][1]

            )

        }
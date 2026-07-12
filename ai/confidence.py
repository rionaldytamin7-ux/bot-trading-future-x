class AIConfidence:

    def evaluate(self, prediction):

        confidence = float(prediction["confidence"])

        if confidence >= 90:
            level = "VERY_HIGH"

        elif confidence >= 80:
            level = "HIGH"

        elif confidence >= 70:
            level = "MEDIUM"

        elif confidence >= 60:
            level = "LOW"

        else:
            level = "VERY_LOW"

        return {

            "confidence": confidence,

            "level": level,

            "allow_trade": confidence >= 80

        }
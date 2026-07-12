class BreakoutDetector:


    def detect(self, df):


        result = {

            "pattern":"NONE",

            "confidence":0

        }


        if len(df)<20:

            return result



        resistance = df["high"].tail(20).max()


        current = df["close"].iloc[-1]



        if current > resistance:


            result["pattern"]="BREAKOUT"


            result["confidence"]=75



        return result
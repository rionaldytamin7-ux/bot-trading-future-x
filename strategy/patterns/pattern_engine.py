from strategy.patterns.double_bottom import DoubleBottomDetector

from strategy.patterns.breakout import BreakoutDetector

from strategy.patterns.support_resistance import SupportResistance



class PatternEngine:


    def __init__(self):

        self.double_bottom = DoubleBottomDetector()

        self.breakout = BreakoutDetector()

        self.sr = SupportResistance()



    def analyze(self,df):


        patterns=[]


        patterns.append(

            self.double_bottom.detect(df)

        )


        patterns.append(

            self.breakout.detect(df)

        )



        sr = self.sr.analyze(df)



        return {


            "patterns":patterns,


            "support":sr["support"],


            "resistance":sr["resistance"]


        }
class AIDecision:


    def __init__(self):

        pass



    def decide(self, score):


        if score >= 80:


            return "LONG"



        elif score <= 20:


            return "SHORT"



        else:


            return "WAIT"
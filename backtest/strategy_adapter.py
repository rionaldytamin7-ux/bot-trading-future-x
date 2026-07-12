from ai.scoring import AIScoring
from ai.decision import AIDecision

from strategy.patterns.pattern_engine import PatternEngine

from analytics.timeframe_engine import MultiTimeframeEngine

from market_context.context_engine import MarketContextEngine



class BacktestStrategy:


    def __init__(self):

        self.ai = AIScoring()

        self.decision = AIDecision()

        self.pattern = PatternEngine()

        self.mtf = MultiTimeframeEngine()

        self.context = MarketContextEngine()



    def analyze(self, df):


        # =====================
        # PATTERN
        # =====================

        pattern_result = self.pattern.analyze(
            df
        )


        # =====================
        # MARKET CONTEXT
        # =====================

        context_result = self.context.analyze({

            "btc_trend":"NEUTRAL",

            "btc_dominance":"UNKNOWN",

            "eth_btc":"UNKNOWN"

        })


        # =====================
        # MULTI TF
        # =====================

        mtf_result = self.mtf.analyze({

            "trend_4h":"NEUTRAL",

            "structure_1h":"NONE",

            "pattern_15m":"NONE",

            "entry_5m":"WAIT",

            "execution_1m":"WAIT"

        })


        # =====================
        # AI SCORE
        # =====================

        score = self.ai.calculate({

            "market_context":
            context_result,


            "pattern":
            pattern_result["patterns"][0],


            "multi_tf":
            mtf_result,


            "volume_status":
            "NORMAL"

        })


        decision = self.decision.decide(
            score
        )


        return {


            "decision":
            decision,


            "score":
            score,


            "pattern":
            pattern_result

        }
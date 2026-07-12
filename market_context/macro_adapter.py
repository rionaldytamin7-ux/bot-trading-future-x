# from macro.summary import get_macro


"""
RIO AI FUTURES
Macro Data Adapter

Menghubungkan data macro
dengan Market Context Engine
"""


class MacroAdapter:


    def __init__(self):

        pass

    def get_macro_data(self):

        """
        Tempat mengambil:

        - DXY
        - NASDAQ
        - SP500
        - Fear Greed
        - ETF Flow

        """

        try:

            # nanti kita sambungkan
            # langsung dari module macro lama

            data = {

                "dxy": None,

                "nasdaq": None,

                "sp500": None,

                "fear_greed": None,

                "etf_flow": None
            }
            return data
        
        except Exception as e:
            return {
                "error": str(e)

            }
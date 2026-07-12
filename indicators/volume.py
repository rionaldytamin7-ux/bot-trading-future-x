class Volume:


    @staticmethod
    def calculate(df):


        current_volume = (
            df["volume"]
            .iloc[-1]
        )


        avg_volume = (
            df["volume"]
            .rolling(20)
            .mean()
            .iloc[-1]
        )


        ratio = (
            current_volume /
            avg_volume
        )


        if ratio >= 1.5:

            status = "HIGH"


        elif ratio <= 0.7:

            status = "LOW"


        else:

            status = "NORMAL"



        return {


            "volume": current_volume,


            "volume_ratio": ratio,


            "volume_status": status

        }
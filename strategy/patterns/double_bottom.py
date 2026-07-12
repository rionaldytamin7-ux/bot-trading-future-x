import numpy as np



class DoubleBottomDetector:


    def detect(self, df):

        result = {


            "pattern":
            "NONE",


            "confidence":
            0

        }


        if len(df) < 20:

            return result



        lows = df["low"].tail(20).values


        volumes = df["volume"].tail(20).values



        first_low = np.min(
            lows[:10]
        )


        second_low = np.min(
            lows[10:]
        )



        # cek lower area sama

        difference = abs(
            first_low - second_low
        ) / first_low



        if difference < 0.015:


            volume_first = np.mean(
                volumes[:10]
            )


            volume_second = np.mean(
                volumes[10:]
            )


            result["pattern"] = "DOUBLE_BOTTOM"



            result["confidence"] = 70



            # volume meningkat
            if volume_second > volume_first:

                result["confidence"] = 85



        return result
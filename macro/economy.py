import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = "9c051735498ec1f8f6c415da3182608d"

BASE = "https://api.stlouisfed.org/fred/series/observations"



def get_latest(series_id):

    try:

        r = requests.get(
            BASE,
            params={
                "series_id": series_id,
                "api_key": API_KEY,
                "file_type": "json",
                "sort_order": "desc",
                "limit": 2
            },
            timeout=10
        )


        data = r.json()

        obs = data["observations"]


        current = float(obs[0]["value"])

        previous = float(obs[1]["value"])


        return current, previous


    except Exception as e:

        print("ERROR :", e)

        raise




def calc_change(current, previous):

    return ((current - previous) / previous) * 100





def get_economy():


    cpi_current, cpi_previous = get_latest("CPIAUCSL")

    ppi_current, ppi_previous = get_latest("PPIACO")



    cpi_actual = calc_change(
        cpi_current,
        cpi_previous
    )


    ppi_actual = calc_change(
        ppi_current,
        ppi_previous
    )



    return {


        "cpi_current": round(cpi_current,3),

        "cpi_previous": round(cpi_previous,3),

        "cpi_actual": round(cpi_actual,2),



        "ppi_current": round(ppi_current,3),

        "ppi_previous": round(ppi_previous,3),

        "ppi_actual": round(ppi_actual,2)

    }
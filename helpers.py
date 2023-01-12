import requests


def get_menu(res_identifier: str):
    """
    Get the list of dishes from a restaurant.

    Args:
        res_identifier (str): The restaurant identifier in the menu aggregator.
    """
    req = requests.get(f"https://menu.dckube.scilifelab.se/api/restaurant/{res_identifier}")

    if req.status_code != 200:
        return {}

    data = req.json()
    menu = [entry["dish"] for entry in data["restaurant"]["menu"]]

    name = data["restaurant"]["title"].strip()

    return {"name": name, "menu": menu}

import requests

def get_name_day():
    url = "https://www.kamisi.pl/projekty/imieniny/api"
    response = requests.get(url)

    if response.status_code == 200:
        script_content = response.json()
        if script_content:
            return f'{script_content["data"]}\n{script_content["solenizanci"]}'
        else:
            return f"No information about name day was found."
    else:
        return "There was a problem with obtaining name day data."
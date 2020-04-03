import requests


def get_world_data() -> str:
    url = 'https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats'
    response = requests.get(url).json()
    date = response['data']['last_update']
    cases = response['data']['total_cases']
    return "World status on " + date + " cases: " + str(cases)


def get_pl_data() -> str:
    url = 'https://api.covid19api.com/live/country/poland/status/confirmed'
    response = requests.get(url).json()[-1]
    date = response['Date']
    cases = response['Cases']
    return "Status in Poland on " + date + " cases: " + str(cases)


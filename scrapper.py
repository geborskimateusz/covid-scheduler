import requests

general_stats_url = 'https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats'
poland_status_url = 'https://api.covid19api.com/live/country/poland/status/confirmed'
poland_daily_difference_url = 'https://api.covid19api.com/dayone/country/poland/status/confirmed/live'


def get_world_data() -> str:
    global general_stats_url

    print("Fetching data from " + general_stats_url)
    response = requests.get(general_stats_url).json()
    date = response['data']['last_update']
    cases = response['data']['total_cases']

    # Number of cumulative cases of coronavirus (COVID-19) worldwide from January 8 to April 3, 2020,
    return "Number of cumulative cases of coronavirus (COVID-19) worldwide from " + date + ": " + str(cases)


def get_pl_data() -> str:
    global poland_status_url

    print("Fetching data from " + poland_status_url)
    response = requests.get(poland_status_url).json()[-1]
    date = response['Date']
    cases = response['Confirmed']
    deaths = response['Deaths']
    return "Status in Poland on " + date + " cases: " + str(cases) + ", deaths: " + str(deaths)


def get_difference() -> str:
    global poland_daily_difference_url
    print("Fetching data from " + poland_daily_difference_url)

    response = requests.get(poland_status_url).json()[-2:]
    yesterday = response[0]
    yesterday_confirmed = yesterday['Confirmed']
    today = response[1]
    today_confirmed = today['Confirmed']
    cases_difference = str(abs(today_confirmed - yesterday_confirmed))

    cases_difference = str(abs(today_confirmed - yesterday_confirmed))
    state = "Compared to yesterday cases {} by {} new cases."
    if yesterday_confirmed < today_confirmed:
        state = state.format("increased", cases_difference)
    elif yesterday_confirmed > today_confirmed:
        state = state.format("decreased", cases_difference)
    else:
        state = "Compared to yesterday there are no new cases."

    return state


print(get_world_data())
print(get_pl_data())
print(get_difference())

import requests


url = 'https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats'

response = requests.get(url).json()
date = response['data']['last_update']
cases = response['data']['total_cases']

world_info = "World status on " + date + ": " + cases
print(world_info)

url = 'https://api.covid19api.com/live/country/poland/status/confirmed'
response = requests.get(url).json()[-1]
date = response['Date']
cases = response['Cases']
pl_info = "Status in Poland on " + date + ": " + str(cases)

print(pl_info)

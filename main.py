import requests

r = requests.get(url="https://apicovid2019.herokuapp.com/country=Malaysia")
#print(r.json())  to get all the data

print(f"Covid-19 stats for {r.json()['Country/other']}\n")
print(f"New cases: {r.json()['NewCases']}")
print(f"Total cases: {r.json()['TotalCases']}\n")

print(f"New recovered: {r.json()['NewRecovered']}")
print(f"Active cases: {r.json()['ActiveCases']}")
print(f"Total recoveries: {r.json()['TotalRecovered']}\n")

print(f"New deaths: {r.json()['NewDeaths']}")
print(f"Total deaths: {r.json()['TotalDeaths']}")
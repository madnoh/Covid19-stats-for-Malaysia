from requests import get

r = get(url="https://apicovid2019.herokuapp.com/country=Malaysia").json()
#print(r.json())  to get all the data

print(f"Covid-19 stats for {r['Country/other']}\n")
print(f"New cases: {r['NewCases']}")
print(f"Total cases: {r['TotalCases']}\n")

print(f"New recovered: {r['NewRecovered']}")
print(f"Active cases: {r['ActiveCases']}")
print(f"Total recoveries: {r['TotalRecovered']}\n")

print(f"New deaths: {r['NewDeaths']}")
print(f"Total deaths: {r['TotalDeaths']}")
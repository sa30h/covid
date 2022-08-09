import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

# print(response.json())

for i in range(0,20):


    print(response.json()['response'][i]['country'])
    print(response.json()['response'][i]['cases']['total'])
    print(response.json()['response'][i]['day'])
    print("\n")


# import requests

# url = "https://covid-193.p.rapidapi.com/statistics"

# querystring = {"country":"canada"}

# headers = {
# 	"X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
# 	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
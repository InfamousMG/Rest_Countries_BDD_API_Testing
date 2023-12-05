import requests

response = requests.get(url="https://restcountries.com/v3.1/all")
response_json = response.json()


def countries_list():
    list_of_countries = []
    number_of_country = 0
    for country in range(0, 250):
        list_of_countries.append(response_json[number_of_country]["name"]["common"])
        number_of_country += 1

    return list_of_countries

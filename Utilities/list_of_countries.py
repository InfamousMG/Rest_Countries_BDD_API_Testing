import requests

response = requests.get(url="https://restcountries.com/v3.1/all")
response_json = response.json()


def countries_count():
    number_of_countries = len(response_json)
    return number_of_countries


def countries_list():
    list_of_countries = []
    country_position = 0
    for country in range(0, countries_count()):
        list_of_countries.append(response_json[country_position]["name"]["common"])
        country_position += 1

    return list_of_countries

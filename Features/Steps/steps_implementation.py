import requests
import random
from behave import *
from Utilities.configuration import get_config
from Utilities.list_of_countries import countries_list, countries_count

config = get_config()


@given("the name of a country")
def step_given_country_name(context):
    """The name of a country is randomly picked from countries list"""
    context.random_country_name = random.choice(countries_list())


@when("I request information about the country via parametrized endpoint")
def step_when_request_country_info(context):
    context.url = f"{config['API']['base_url']}/name/{context.random_country_name}"
    context.response = requests.get(context.url)


@then("the response status code should be 200")
def step_then_response_status_code(context):
    assert context.response.status_code == 200, "status code is not 200"


@then("the response should contain the same name of the country as in the request")
def step_then_response_country_info(context):
    context.country_info = context.response.json()
    assert "name" in context.country_info[0], "name field is not present"
    assert context.country_info[0]["name"]["common"] == context.random_country_name, ("the name is not the same as in "
                                                                                      "the request")


@then("the response should include essential details like {currencies}, {capital}, {region}, {languages}, {area}, "
      "{population}, and {timezones}")
def step_then_response_details(context, currencies, capital, region, languages, area, population, timezones):
    assert "currencies" in context.country_info[0], "currencies field is not present"
    assert "capital" in context.country_info[0], "capital field is not present"
    assert "region" in context.country_info[0], "region field is not present"
    assert "languages" in context.country_info[0], "languages field is not present"
    assert "area" in context.country_info[0], "area field is not present"
    assert "population" in context.country_info[0], "population field is not present"
    assert "timezones" in context.country_info[0], "timezones field is not present"


@given("that the list of countries should contain a certain number of countries")
def step_given_countries_count(context):
    context.number_of_countries = countries_count()


@when("I call /all endpoint and create a list of countries based on their names")
def step_when_request_all_endpoint(context):
    context.countries_list = countries_list()


@then("the list of countries has a certain number of countries positions")
def step_then_x_positions(context):
    assert len(context.countries_list) == context.number_of_countries, ("number of countries on the list do not match "
                                                                        "with the number of countries returned by "
                                                                        "/all endpoint")


@given("the countries names on a parametrized list")
def step_given_specific_countries(context):
    context.specific_countries = ["Vatican City", "Israel", "Bulgaria"]


@when("I call /all endpoint to create a list of countries")
def step_when_calling_all_endpoint(context):
    context.countries_list = countries_list()


@then("the given countries are on the list of countries returned by /all endpoint")
def step_then_countries_are_on_list(context):
    assert all(country in context.countries_list for country in context.specific_countries), ("Some of these countries "
                                                                                              "are not on the list")


@given("the language")
def step_given_language(context):
    context.language = "Chinese"


@when("I request for a list of countries that use this language")
def step_when_request_list_of_countries_using_language(context):
    context.lang_url = f"{config['API']['base_url']}/lang/{context.language}"
    context.response_lang = requests.get(context.lang_url)
    context.response_lang_json = context.response_lang.json()


@then("a list of countries using that language is created")
def step_then_the_list_is_created(context):
    countries_with_language = []
    country_position = 0
    context.number_of_countries = len(context.response_lang_json)
    for country in range(0, context.number_of_countries):
        countries_with_language.append(context.response_lang_json[country_position]["name"]["common"])
        country_position += 1

    print(countries_with_language)


@then("the presence of the language is checked among those countries")
def step_then_language_check(context):
    countries_languages = []
    position = 0
    for each_country in range(0, context.number_of_countries):
        countries_languages.append(context.response_lang_json[position]["languages"])
        position += 1

    print(countries_languages)

    for each_dictionary in countries_languages:
        assert any(value == context.language for value in each_dictionary.values()), (f"{context.language} is not "
                                                                                      f"present on the list of "
                                                                                      f"languages")


@given("a name of an imaginary country")
def step_given_imaginary_country(context):
    context.imaginary_country = "Russlandia"


@when("I call a parametrized endpoint to retrieve information about the country")
def step_when_calling_parametrized_endpoint(context):
    context.url = f"{config['API']['base_url']}/name/{context.imaginary_country}"
    context.response = requests.get(context.url)


@then("the response status code should be 404 not found")
def step_then_status_404(context):
    assert context.response.status_code == 404, "status code is not 404 not found, the country shouldn't exist"

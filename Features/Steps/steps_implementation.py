import requests
from behave import *
from Utilities.configuration import get_config
from Utilities.list_of_countries import countries_list

config = get_config()


@given("the name of a {country}")
def step_given_country_name(context, country):
    context.country_name = "Poland"


@when("I request information about the country via parametrized endpoint")
def step_when_request_country_info(context):
    context.url = f"{config['API']['base_url']}/name/{context.country_name}"
    context.response = requests.get(context.url)


@then("the response status code should be 200")
def step_then_response_status_code(context):
    assert context.response.status_code == 200


@then("the response should contain the same name of the country as in the request")
def step_then_response_country_info(context):
    context.country_info = context.response.json()
    print(context.country_info)
    assert "name" in context.country_info[0]
    assert context.country_info[0]["name"]["common"] == context.country_name


@then("the response should include essential details like {currencies}, {capital}, {region}, {languages}, {area}, "
      "{population}, and {timezones}")
def step_then_response_details(context, currencies, capital, region, languages, area, population, timezones):
    assert "currencies" in context.country_info[0]
    assert "capital" in context.country_info[0]
    assert "region" in context.country_info[0]
    assert "languages" in context.country_info[0]
    assert "area" in context.country_info[0]
    assert "population" in context.country_info[0]
    assert "timezones" in context.country_info[0]


@given("that the list of countries should contain 250 countries")
def step_given_list_of_countries(context):
    context.complete_list = 250


@when("I call /all endpoint")
def step_when_request_all_endpoint(context):
    context.countries_list = countries_list()


@then("the list of countries has 250 positions")
def step_then_250_positions(context):
    assert len(context.countries_list) == context.complete_list


@given("the {country} name")
def step_given_specific_country(context, country):
    context.specific_country = "Vatican City"


@when("I call /all endpoint to create a list of countries")
def step_when_calling_all_endpoint(context):
    context.countries_list = countries_list()


@then("the <country> is on the list of countries returned by /all endpoint")
def step_then_country_on_list(context):
    assert context.specific_country in context.countries_list
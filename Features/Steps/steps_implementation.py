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
    assert context.response.status_code == 200, "status code is not 200"


@then("the response should contain the same name of the country as in the request")
def step_then_response_country_info(context):
    context.country_info = context.response.json()
    assert "name" in context.country_info[0], "name field is not present"
    assert context.country_info[0]["name"]["common"] == context.country_name, ("the name is not the same as in the "
                                                                               "request")


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


@given("that the list of countries should contain 250 countries")
def step_given_list_of_countries(context):
    context.complete_list = 250


@when("I call /all endpoint")
def step_when_request_all_endpoint(context):
    context.countries_list = countries_list()


@then("the list of countries has 250 positions")
def step_then_250_positions(context):
    assert len(context.countries_list) == context.complete_list


@given("the <countries> names in a list")
def step_given_specific_countries(context):
    context.specific_countries = ["Vatican City", "Israel", "Bulgaria"]


@when("I call /all endpoint to create a list of countries")
def step_when_calling_all_endpoint(context):
    context.countries_list = countries_list()


@then("the <countries> is on the list of countries returned by /all endpoint")
def step_then_countries_on_list(context):
    assert all(country in context.countries_list for country in context.specific_countries), ("Some of these countries "
                                                                                              "are not on the list")

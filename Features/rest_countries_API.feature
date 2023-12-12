Feature: Retrieving information about countries

  @country_details
  Scenario: Check whether a country is available through country-specific endpoint
    Given the name of a country
    When I request information about the country via parametrized endpoint
    Then the response status code should be 200
    And the response should contain the same name of the country as in the request
    And the response should include essential details like <currencies>, <capital>, <region>, <languages>, <area>, <population>, and <timezones>

  @list_of_countries
  Scenario: Check whether the list of countries is complete
    Given that the list of countries should contain a certain number of countries
    When I call /all endpoint and create a list of countries based on their names
    Then the list of countries has a certain number of countries positions

  @presence_of_countries
  Scenario: Check whether given countries on a list are available on the list of countries returned by /all endpoint
    Given the countries names on a parametrized list
    When I call /all endpoint to create a list of countries
    Then the given countries are on the list of countries returned by /all endpoint

  @language
  Scenario: Search for countries that use a specific language
    Given the language
    When I request for a list of countries that use this language
    Then a list of countries using that language is created
    And the presence of the language is checked among those countries

  @invalid_country_name
  Scenario: Seek countries that don't exist
    Given a name of an imaginary country
    When I call a parametrized endpoint to retrieve information about the country
    Then the response status code should be 404 not found

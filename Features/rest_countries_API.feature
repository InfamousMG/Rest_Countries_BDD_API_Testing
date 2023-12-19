Feature: Retrieving information about countries

  @country_details
  Scenario: Check whether a country is available through country-specific endpoint
    Given the name of a country
    When I request information about the country via parametrized endpoint
    Then the response status code should be 200
    And the response should contain the same name of the country as in the request
    And the response should include essential details like currencies, capital, region, languages, area, population, and timezones

  @list_of_countries
  Scenario: Check whether the list of countries is complete
    Given that the list of countries should contain a certain number of countries
    When I call /all endpoint and create a list of countries based on their names
    Then the list of countries has a certain number of countries positions

  @presence_of_countries
  Scenario Outline: Check whether given countries on a list are available on the list of countries returned by /all endpoint
    Given I have a list of countries with <countries>
    When I call /all endpoint to create a list of countries and compare it to the list above
    Then the given countries are on the list of countries returned by /all endpoint
      Examples:
      | countries |
      | Poland, China, Turkey |
      | Russia, Belarus, Argentina |
      | Bangladesh, Morocco, South Africa |

  @language
  Scenario: Search for countries that use a specific language
    Given a random language from a list of languages
    When I request for a list of countries that use this language
    Then a list of countries using that language is created
    And the presence of the language is checked among those countries

  @invalid_country_name
  Scenario: Seek countries that don't exist
    Given a name of a <fake_country>
    When I call a parametrized endpoint to retrieve information about the country
    Then the response status code should be 404 not found

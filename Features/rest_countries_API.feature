Feature: Retrieving information about countries

  Scenario: Check whether a country is available through country-specific endpoint
    Given the name of a <country>
    When I request information about the country via parametrized endpoint
    Then the response status code should be 200
    And the response should contain the same name of the country as in the request
    And the response should include essential details like <currencies>, <capital>, <region>, <languages>, <area>, <population>, and <timezone>

  Scenario: Check whether the list of countries is complete
    Given that the list of countries should contain 250 countries
    When I call /all endpoint
    Then the list of countries has 250 positions

  Scenario: Check whether countries in a list are available on the list of countries returned by /all endpoint
    Given the <countries> names in a list
    When I call /all endpoint to create a list of countries
    Then the <countries> is on the list of countries returned by /all endpoint

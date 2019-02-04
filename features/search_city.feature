Feature: Search validation of city for openweathermap website
  Scenario: Searching Invalid city
    Given I open url "https://openweathermap.org"
    When I enter "SomeCityWhichDoesNotExists"
    And Click Search button
    Then I should see result for invalid city "Not found"

  Scenario: Searching Valid city
    Given I open url "https://openweathermap.org"
    When I enter "Lucknow"
    And Click Search button
    Then I should see result for valid city "Lucknow"
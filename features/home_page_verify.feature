Feature: Acting in openweather home page. Checking if important label is there
    Scenario: Open website
      Given I visit url "https://openweathermap.org"
      Then title be "Сurrent weather and forecast - OpenWeatherMap"
      Then search button text should be "Search"
      Then tagline should be "We Deliver 2 Billion Forecasts Per Day"
      Then I should see navigation bar
      Then I should see footer

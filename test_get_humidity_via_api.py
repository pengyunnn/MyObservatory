import pytest
import requests


from datetime import datetime, timedelta


API_URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
PARAMS = {
    "dataType": "fnd",
    "lang": "tc"
}

@pytest.fixture(scope="module")
def api_response():
    """ Fixture to fetch the API response once for all tests """
    response = requests.get(API_URL, params=PARAMS)
    return response

def test_api_status(api_response):
    """ Test if the API response status is 200 (OK) """
    assert api_response.status_code == 200, f"API request failed with status code {api_response.status_code}"

def test_extract_relative_humidity(api_response):
    """ Extract the relative humidity for the day after tomorrow """
    data = api_response.json()
    
    assert "weatherForecast" in data, "No weather forecast data found in API response"
    
    day_after_tomorrow = (datetime.today() + timedelta(days=2)).strftime("%Y%m%d")
    
    for forecast in data["weatherForecast"]:
        if forecast["forecastDate"] == day_after_tomorrow:
            max_humidity = forecast["forecastMaxrh"]['value']
            min_humidity = forecast["forecastMinrh"]['value']
            print(f"Relative Humidity for {day_after_tomorrow}: {min_humidity}% ~ {max_humidity}%")
            assert max_humidity, "Relative humidity data missing"
            assert min_humidity, "Relative humidity data missing"
            return
    
    pytest.fail(f"No forecast found for {day_after_tomorrow}")
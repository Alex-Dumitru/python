# will use Weather Underground at www.wunderground.com
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'location, condition, temperature, scale')
def main():
    print_the_header()
    zip_code = input("What zip code do you want the wheater for? ")
    html = get_html_from_web(zip_code)
    report = get_weather_from_html(html)
    print("In {}, the weather is {}. Current temperature is: {}{}".format(
        report.location, 
        report.condition, 
        report.temperature, 
        report.scale))


def print_the_header():
    header_text = """
    ==================
    MY WHEATHER CLIENT
    ==================
    """
    print(header_text)

def get_html_from_web(zip_code):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zip_code)
    response = requests.get(url)
    # print(response.status_code)
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    location = soup.find(class_='region-content-header').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()
    temperature = soup.find(class_='condition-data').find(class_='wu-value wu-value-to').get_text().strip()
    scale = soup.find(class_='condition-data').find(class_='wu-label').get_text().strip()
    report = WeatherReport(location, condition, temperature, scale)

    return report


if __name__ == "__main__":
    main()
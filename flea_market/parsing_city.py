import requests
from bs4 import BeautifulSoup as bs

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36",
}

base_url = 'https://cars.av.by/search?region_id='


def get_dict_regions():
    session = requests.Session()
    dict_regions = {}
    for number_region in range(1, 7):
        request = session.get(base_url + str(number_region), headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'html.parser')
            region = soup.find("select", {'id': 'region_id_filter'}).find('option', {'selected': 'selected'}).text
            cities = soup.find("select", {'id': 'city_id_filter'}).find_all('option')
            cities_list = []
            cities_list.append(number_region)
            for city in cities[1:]:
                cities_list.append(city.text)
            dict_regions[region] = cities_list

    return dict_regions

get_dict_regions()

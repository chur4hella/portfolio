import requests
from bs4 import BeautifulSoup as bs
import json


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36",
}

base_url = "https://baraholka.onliner.by/"


def get_dict_categories(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        category_box = soup.find_all('div', attrs='cm-onecat')
        dict_categories = {}
        number_category = 1
        number_subcategory = 1

        for item in category_box:
            category = item.find('h3').text
            dict_categories[number_category] = {
                'name_category': category,
            }
            li_list = item.find('ul').find_all('li')
            for li in li_list:
                subcategory = li.find('a').text
                dict_categories[number_category][number_subcategory] = {
                    'name_subcategory': subcategory,
                }
                number_subcategory += 1
            number_category += 1
        return dict_categories


# dict_for_file = get_dict_categories(base_url, headers)

# category_file = open('json/categories.json', 'w', encoding='utf-8')
# category_file.write(json.dumps(dict_for_file, sort_keys=True, indent=4, ensure_ascii=False))
# category_file.close()

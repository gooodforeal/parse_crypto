import requests, lxml, json
from bs4 import BeautifulSoup
from savefiles import save_xlsx, save_json
from main import headers, url


def is_digit(char):
    chars = "0123456789"
    if char in chars:
        return True
    return False

def get_html(url):
    response = requests.get(url = url, headers = headers)
    with open("data.html", "w") as file:
        file.write(response.text)

def open_file():
    file = open("data.html", "r")
    return file

def parse():
    result = []
    file = open_file()
    soup = BeautifulSoup(file, "lxml")
    cards = soup.find(class_ = "cmc-table").find("tbody").find_all("tr")
    count = 0
    for card in cards:
        if (count == 10):
            break
        rows = card.find_all("td")
        for row in rows:
            result_dict = dict()
            try:
                name = card.find("div", class_ = "escjiH").text.strip()
                for char in name:
                    if (is_digit(char)):
                        name = name.split(char)[0]
                        break
                result_dict["Name"] = name
            except:
                pass
            try:
                result_dict["Price"] = card.find("div", class_ = "sc-131di3y-0").find("span").text.strip()
            except:
                pass
            try:
                result_dict["Market Cap"] = card.find("span", class_ = "sc-1ow4cwt-1").text.strip()
            except:
                pass
        result.append(result_dict)
        count +=1
    save_json(result) # Saving as json file
    save_xlsx(result) # Saving excel table
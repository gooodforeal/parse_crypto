import requests, lxml, json
from bs4 import BeautifulSoup
from openpyxl import Workbook


'''Saving as json file, params - python list'''
def save_json(list):  #dump - запись в файл, dumps - возвращает текст в переменную
    with open("result.json", "w") as file:
        json.dump(list, file, indent = 4, ensure_ascii = False) # indent - tab, ensure - encoding fix

'''Saving as excel file, params - python list'''
def save_xlsx(list):
    work_book = Workbook() # Creating excel workbook
    work_sheet = work_book.active   # Selecting worksheet
    header = []
    for key in list[0].keys(): # keys - returns all keys of dict
        header.append(key)
    work_sheet.append(header)
    for element in list:
        cols = []
        for col in element.values(): # values - returns all values of dict
            cols.append(col)
        work_sheet.append(cols)
    work_book.save("result.xlsx") # Saving as excel file

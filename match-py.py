import csv
import re

import pytils as pt
from fuzzywuzzy import fuzz


def is_rus_lang(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

def is_match_names(name_1, name_2):

    lng_1 = is_rus_lang(name_1)
    lng_2 = is_rus_lang(name_2)

    if lng_1 == lng_2:
        if (fuzz.token_sort_ratio(name_1, name_2) > 60) and (re.findall("\d+", name_1) == re.findall("\d+", name_2)):
            return True
        else:
            return False
    elif lng_1:
        if (fuzz.token_sort_ratio(pt.translit.translify(name_1), name_2) > 60) and (re.findall("\d+", name_1) == re.findall("\d+", name_2)):
            return True
        else:
            return False
    elif lng_2:
        if (fuzz.token_sort_ratio(name_1, pt.translit.translify(name_2)) > 60) and (re.findall("\d+", name_1) == re.findall("\d+", name_2)):
            return True
        else:
            return False

def is_match_sellers(seller_1, seller_2):

    lng_1 = is_rus_lang(seller_1)
    lng_2 = is_rus_lang(seller_2)

    if lng_1 == lng_2:
        if fuzz.token_sort_ratio(seller_1, seller_2) > 40:
            return True
        else:
            return False
    elif lng_1:
        if fuzz.token_sort_ratio(pt.translit.translify(seller_1), seller_2) > 40:
            return True
        else:
            return False
    elif lng_2:
        if fuzz.token_sort_ratio(pt.translit.translify(seller_1), seller_2) > 40:
            return True
        else:
            return False

apt_1 = "source/Eapteka.csv"
apt_2 = "source/Zdravcity.csv"
res_1 = "matchres.csv"  
res_2 = "nomatchres.csv"    

match_file = open(res_1, mode = "w", encoding = 'utf-8')
nomatch_file = open(res_2, mode = "w", encoding = 'utf-8')
names = ["Наименование товара1", "Цена товара1", "Производитель1", "Наименование товара2", "Цена товара2", "Производитель2"]

match_file_writer = csv.DictWriter(match_file, delimiter = ';', lineterminator = '\n', fieldnames = names)
nomatch_file_writer = csv.DictWriter(nomatch_file, delimiter = ';', lineterminator = '\n', fieldnames = names)

read_1_file = open(apt_1, encoding = 'utf-8')
read_2_file = open(apt_2, encoding = 'utf-8')
file_1_reader = csv.reader(read_1_file, delimiter = ";")
file_2_reader = csv.reader(read_2_file, delimiter = ";")

"""Заполнение таблицы совпавших записей ниже"""

for row_1 in file_1_reader:
    for row_2 in file_2_reader:
        if is_match_names(row_1[0], row_2[0]):

            if is_match_sellers(row_1[3], row_2[3]):

                match_file_writer.writerow({"Наименование товара1": row_1[0],
                                      "Цена товара1": row_1[1],
                                      "Производитель1": row_1[3],
                                      "Наименование товара2": row_2[0],
                                      "Цена товара2": row_2[1],
                                      "Производитель2": row_2[3]})
        else:
            continue
    read_2_file.seek(0)

read_1_file.seek(0)
match_file.close()

"""Заполнение таблицы НЕ совпавших записей ниже"""  

match_file = open(res_1, encoding = 'utf-8')                     
match_reader = csv.reader(match_file, delimiter = ";")           

for row_1 in file_1_reader:                                    
    for row in match_reader:
        if row_1[0] == row[0]:
            break
    else:
        nomatch_file_writer.writerow({"Наименование товара1": row_1[0],
                                  "Цена товара1": row_1[1],
                                  "Производитель1": row_1[3]})
    match_file.seek(0)

for row_2 in file_2_reader:                                    
    for row in match_reader:                               
        if row_2[0] == row[3]:
            break
    else:
        nomatch_file_writer.writerow({"Наименование товара2": row_2[0],
                                  "Цена товара2": row_2[1],
                                  "Производитель2": row_2[3]})
    match_file.seek(0)

"""Сколько в файле отмечено точечных объектов (node), являющихся заправкой.
В качестве ответа вам необходимо вывести количество АЗС каждой фирмы"""

import xmltodict

fin = open('map1.osm', 'r', encoding='utf-8')
dct = xmltodict.parse(fin.read())

k = 0

for node in dct['osm']['node']:
    if 'tag' in node and isinstance(node['tag'], list):
        for tag in node['tag']:
            if tag['@v'] == 'fuel':
                k += 1
    elif 'tag' in node and isinstance(node['tag'], dict):
        if node['tag']['@v'] == 'fuel':
            k+=1

print(k)
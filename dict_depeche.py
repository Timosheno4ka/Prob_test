# Есть словарь песен группы Depeche Mode
# violator
# songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
# 1. Выведите общее время звучания всех песен.
# 2. Создайте список песен, время звучаниях которых больше 5 минут
# 3. Создайте новый словарь тех песен, в название которых состоит из одного слова

songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
# print(len(songsdict))
# print(songsdict.values())
a = songsdict.values()#список значений (длительность песен)
print(f'Общее время звучания песен: {sum(a)} минут')

for key, value  in songsdict.items():
    if value>5:
        print(f'Песня, время звучания которой больше 5 минут: {key}, {value}')

songsdict_1 = dict(zip(['Halo', 'Clean'],[4.30,5.68]))
print(f'Словарь песен, название которых состотит из одного слова:  {songsdict_1}')
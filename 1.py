# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом: в качестве ключей
# возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку

a = 'An apple a day keeps the doctor away'

b = {i:a.count(i) for i in a}

print(b)
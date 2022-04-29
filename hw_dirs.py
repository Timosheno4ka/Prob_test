# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('Desktop') #переход в папку рабочего стола
# os.mkdir('Home_files') #создание новой папки на рабочем столе
os.chdir('Home_files') #переход в созданную папку
# f = open('test_1.txt','w')
# f = open('test_2.txt','w')
# f = open('test_3.txt','w')
# os.rename('test_1.txt','rename_1.txt') #переименование файлов
# os.rename('test_2.txt','rename_2.txt')
# os.rename('test_3.txt','rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('..')
os.rmdir('Home_files')
print(os.getcwd())
# В саду сорвали цветы garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# На лугу сорвали цветы meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Создайте множество цветов, произрастающих одновременно в саду и на лугу

garden = {'ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза'}
meadow = {'клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка'}
a = garden.intersection(meadow)
print(f'Цветы, произрастающие одновременно в саду и на лугу{a}')
b = garden&meadow
print(f'Цветы, произрастающие одновременно в саду и на лугу{b}')

arr = []

with open("db.txt") as file_handler:
    for line in file_handler:
        s = line.split(',')
        arr.append({'name': s[0],
                    'count': s[1],
                    'size': s[2],
                    'color': s[3],
                    'label': s[4],
                    'season': s[5]})

while True:
    print('1 - добавить товар')
    print('2 - вывод всех товаров')
    print('3 - вывод статистики')
    print('4 - выйти')
    print('Введите номер действия')
    x = input()

    if x == '1':
        print('Введите название товара')
        name = input()
        print('Введите количество')
        count = input()
        print('Введите размер')
        size = input()
        print('Введите цвет')
        color = input()
        print('Введите марку товара')
        label = input()
        print('Введите сезон')
        season = input()
        arr.append({'name': name,
                    'count': count,
                    'size': size,
                    'color': color,
                    'label': label,
                    'season': season})
    elif x == '2':
        for i in arr:
            print(f'Товар: {i["name"]}, \
                    Количество: {i["count"]}, \
                    Размер: {i["size"]}, \
                    Цвет: {i["color"]}, \
                    Марка: {i["label"]}, \
                    Сезон: {i["season"]}')
    elif x == '3':
        buf = {}
        for i in arr:
            count = i['count']
            if i['label'] in buf.keys():
                buf[i['label']] += int(count)
            else:
                buf[i['label']] = int(count)
        print(buf)
    else:
        break
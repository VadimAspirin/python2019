
arr = []

while True:
    print('1 - добавить товар')
    print('2 - вывод всех товаров')
    print('3 - выйти')
    print('Введите номер действия')
    x = input()

    if x == '1':
        print('Введите название товара')
        name = input()
        print('Введите количество товара')
        count = input()
        print(name, count)
        arr.append({'name': name, 'count': count})
    elif x == '2':
        #print(arr)
        for i in arr:
            print(f'Товар: {i["name"]}, Количество: {i["count"]}')
    else:
        break
def zad1():
    import json
    with open('p1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    products = data['products']
    for product in products:
        name = product['name']
        price = product['price']
        weight = product['weight']
        available = product['available']
        print(f"Название: {name}")
        print(f"Цена: {price}")
        print(f"Вес: {weight}")
        if available:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
def zad2():
    import json
    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = float(input("Введите вес продукта: "))
    available = input("Товар в наличии? (да/нет): ").lower() == 'да'
    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }

    with open('p1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    data['products'].append(new_product)

    with open('p1.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    with open('p1.json', 'r', encoding='utf-8') as file:
        updated_data = json.load(file)
        for product in updated_data['products']:
            available = "В наличии" if product['available'] else "Нет в наличии!"
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']}")
            print(f"Вес: {product['weight']}")
            print(available)
            print()
def zad3():
    redict = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                eng, rus = line.split(' - ')
                ruswords = [word.strip() for word in rus.split(',')]
                for rusword in ruswords:
                    if rusword in redict:
                        redict[rusword].append(eng)
                    else:
                        redict[rusword] = [eng]

    sorted_ru_en_dict = dict(sorted(redict.items()))

    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for russian_word, english_words in sorted_ru_en_dict.items():
            line = russian_word + ' – ' + ', '.join(english_words) + '\n'
            file.write(line)
    print("усе")
zad3()
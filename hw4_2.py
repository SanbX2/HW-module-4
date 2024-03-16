from pathlib import Path

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                values = line.strip().split(',')
                cats_dict = {"id": "", "name": "", "age": ""}
                for key, value in zip(cats_dict, values):
                    cats_dict[key] = value
                cats_list.append(cats_dict)
            return cats_list
            
    except Exception as error:
        print('Виникає помилка -', error)

cats_info = get_cats_info('cats_info.txt')
print(cats_info)
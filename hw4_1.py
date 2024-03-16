from pathlib import Path

# with open('salary_file.txt', 'w') as file:
#     file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

def total_salary(path):
    prepared_dict = {}
    salary_list = []
    try:
        with open(path, "r", encoding='utf-8') as file:
            lines = [el.strip() for el in file.readlines()]
            prepared_list = [el.split(',') for el in lines]
            prepared_dict.update(prepared_list)

    except Exception:
        print("Файл пошкоджено або файл відсутній")

    else:
        for val in prepared_dict.values():
            int_val = int(val)
            salary_list.append(int_val)
            salary_sum = sum(salary_list)
            salary_avg = int(salary_sum / len(salary_list))

        return f"Загальна сума заробітної плати: {salary_sum}$, Середня заробітна плата: {salary_avg}$"

print(total_salary('slary_file.txt'))
import random

# Список студентов
students = ["Султан","Eldar","Alikhan","Sasha","ern","dan","nurai","dimash","arlan","dias","ansar","nursult","alzhan","kuka","sanzhar","temerlan"]

# Генерация уникальных случайных чисел для каждого студента
unique_numbers = random.sample(range(1, 17), len(students))

# Соответствие студентов и уникальных чисел
students_with_unique_numbers = {student: number for student, number in zip(students, unique_numbers)}

# Вывод результата
for student, number in students_with_unique_numbers.items():
    print(f"{student}: {number}")
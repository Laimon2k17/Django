groupmates = [
    {
        "name": "Александр",
        "surname": "Блинов",
        "exams": ["Информатика", "ЭЭиС", "Ин.язык"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Косенок",
        "exams": ["История", "АиГ", "ТП"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Александра",
        "surname": "Кобелькова",
        "exams": ["Философия", "АИС", "ТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Сафонов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Никита",
        "surname": "Брагин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Арсений",
        "surname": "Кузин",
        "exams": ["История", "АиГ", "ТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Максим",
        "surname": "Жачек",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 5]
    }
 ]
 
def print_students(students):
    while True:
        try:
            threshold = float(input("Введите минимальный средний балл: ").replace(',', '.'))
            break
        except ValueError:
            print("Ошибка! Пожалуйста, введите число (можно с запятой или точкой).")
    
    # Шапка таблицы
    print(f"{'Имя':<15} {'Фамилия':<10} {'Экзамены':<40} {'Оценки':<20} {'Средняя оценка':<40}")
    
    # Фильтрация и вывод студентов
    for student in students:
        avg_score = sum(student["marks"]) / len(student["marks"])
        if avg_score >= threshold:
            print(
                f"{student['name']:<15} "
                f"{student['surname']:<10} "
                f"{str(student['exams']):<40} "
                f"{str(student['marks']):<20} "
                f"{avg_score:.1f}"
            )

print_students(groupmates)
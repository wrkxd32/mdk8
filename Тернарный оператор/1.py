def is_even(n):
    return "Четное" if n % 2 == 0 else "Нечетное"

def age_category(vozrast):
    return "Детский" if vozrast < 13 else "Подростковый" if vozrast < 18 else "Взрослый"

def check_sign(nmb):
    return "Положительное" if nmb > 0 else "Отрицательное" if nmb < 0 else "Ноль"

def score_evaluation(score):
    return "Ужасно" if score < 50 else "Нужно учиться" if score < 75 else "Хорошо" if score < 90 else "Отлично"

def greeting(vr):
    return "Доброе утро" if 5 <= vr < 12 else "Добрый день" if 12 <= vr < 18 else "Добрый вечер" if 18 <= vr < 22 else "Доброй ночи"

def average_score(a):
    sc = sum(a) / len(a)
    return "Низкий" if sc < 50 else "Средний" if sc < 75 else "Высокий"

def classify_number(number):
    return "Положительное четное" if number > 0 and number % 2 == 0 else "Положительное нечетное" if number > 0 else "Отрицательное четное" if number < 0 and number % 2 == 0 else "Отрицательное нечетное" if number < 0 else "Ноль"
from datetime import datetime, time, timedelta

pattern = "%d.%m.%Y %H:%M"

opening_hours = {
    0: (10, 18),  # вс
    1: (9, 21),  # пн
    2: (9, 21),  # вт
    3: (9, 21),  # ср
    4: (9, 21),  # чт
    5: (9, 21),  # пт
    6: (10, 18),  # сб
}

user_date = datetime.strptime(input(), pattern)

today_open = opening_hours[int(user_date.strftime("%w"))]

if time(today_open[0]) <= user_date.time() < time(today_open[1]):
    user_time = timedelta(hours=user_date.hour, minutes=user_date.minute)
    res = timedelta(hours=today_open[1]) - user_time
    print(int(res.total_seconds() // 60))

else:
    print("Магазин не работает")

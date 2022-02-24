duration = int(input('Enter duration  '))
if duration <= 60:
    print(duration, 'сек')

elif duration > 60 and duration <= 3600:
    min = duration // 60
    print(min, 'мин', duration % 60, 'сек')
elif duration > 3600 and duration <= 86400:
    hour = duration // 3600
    duration = duration % 3600
    min = duration // 60
    print(hour, 'час', min, 'мин', duration % 60, 'сек')
elif duration > 86400:
    day = duration // 86400
    duration = duration % 86400
    hour = duration // 3600
    duration = duration % 3600
    min = duration // 60
    print(day,'сут', hour,'час', min,'мин', duration % 60, 'сек')
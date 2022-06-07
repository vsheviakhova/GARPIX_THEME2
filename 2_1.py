temp_current = int(input('Актуальная температура в помещении: '))
temp_goal = int(input('Желаемая температура в помещении: '))
humidity = int(input('Актуальная влажность воздуха: '))

if temp_current > temp_goal and humidity <= 80:
    print('on')
else:
    print('off')

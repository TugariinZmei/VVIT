import requests

city="Moscow,RU"
appid="d3f2e56b94cffe406067fc47f764b379"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'], "М/С")
print("Видимость", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("Скорость ветра", i['wind']['speed'], "М/С")
    print("Видимость", i['visibility'])
    print("____________________________")

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
place = input('Введите ваш город: ')
country = input('Введите ваш страну: ')
country_and_place = place + ", " + country

owm = OWM('de7a21d8032bc1bf1e58bc4b59906cb2')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(country_and_place)
w = observation.weather

status = w.detailed_status
w.wind()
humidity = w.humidity 
temp = w.temperature('celsius')['temp']

def weather():
    print("В городе" + str(place) + "сейчас" + str(status) +
            "\nТемпература" +str(round(temp)) + "градусов по цельсию" + 
            "\nАлажность составляет" +str(humidity) + "%" +
            "\nскорость ветра " + str(w.wind()['speed']) + "Метров в секунду"
            )

weather()
# weather_forecast_in_your_city.py
def weather_report(city, temperature, humidity, weather_description, precipitation, windSpeed):
  return f"Погода в місті {city}:\nТемпература: {temperature}°C\nВологість: {humidity}%\nОпади: {precipitation}%\nШвидкість вітру:{windSpeed}км/год\n{weather_description}"

city = input("Введіть назву міста: ")
temperature = float(input("Введіть температуру по Цельсію: "))
humidity = int(input("Введіть вологість у відсотках: "))
precipitation = int(input("Введіть опади у відсотках: "))
weather_description = input("Введіть опис погоди: ")
windSpeed = input("Введіть швидкість вітру (кілометри за годину): ")

print(weather_report(city, temperature, humidity, weather_description, precipitation, windSpeed))
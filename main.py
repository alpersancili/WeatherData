import requests

def my_inputs():
    city = input("Enter City:")
    api_key = input("Enter Your API key: ")
    target_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    return target_url

def make_requests():
    new_url = my_inputs()
    response = requests.get(new_url)
    data = response.json()
    return data


def weather():
    link = make_requests()
    temp = link["main"]["temp"]
    wind = link["wind"]["speed"]
    pressure = link["main"]["pressure"]
    humidity = link["main"]["humidity"]
    description = link["weather"][0]["description"]

    print("Temperature: ", temp)
    print("Wind: ", wind)
    print("Pressure: ", pressure)
    print("Humidity: ", humidity)
    print("Description: ", description)

weather()
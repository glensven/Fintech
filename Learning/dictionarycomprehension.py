cities_in_f = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

cities_in_c = {key: round((value-32)*(5/9)) for (key,value) in cities_in_f.items()}
print(cities_in_c)

weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

cities_warm_cold = {key: ("Warm" if value >= 70 else "Cold") for (key,value) in cities.items()}
print(cities_warm_cold)

def check_temp(value):
    if value >=75:
        return "Hot"
    elif 75 > value >= 40:
        return "Warm"
    else:
        return "Cold"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
cities_warm_cold = {key: check_temp(value) for (key,value) in cities.items()}

print(cities_warm_cold)
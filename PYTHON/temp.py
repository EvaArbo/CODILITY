def hows_the_weather(temperature):
    if temperature <40:
        return("It's brisk out there!")
    elif 40 <= temperature < 65:
        return("It's a little chilly out there!")
    elif 60 <= temperature < 85:
        return("It's perfect out there!")
    elif 85 <= temperature < 100:
        return("It's a little too hot out there!")
    else:
        return("It's perfect out there!")
print(hows_the_weather(30))
print(hows_the_weather(50))
print(hows_the_weather(70))
print(hows_the_weather(90))
print(hows_the_weather(105))
    

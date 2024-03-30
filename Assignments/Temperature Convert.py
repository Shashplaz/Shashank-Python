# Temperature Converter (°F − 32) × 5/9 = °C ||| (°C × 9/5) + 32 = °F
def temperaturecoverter(temperature, conversion):
    if conversion == "FtC":
        converted = (temperature - 32) * (5 / 9)
        return (temperature, "Fareheight coverted to celcius is", converted)
    else:
        conversion == "CtF"
        convert = (temperature * 9 / 5) + 32
        return (temperature, "Celcius coverted to Fareheight is", convert, "°F")


# Final
conversion = input(
    "Type FtC if you want to convert Fareheight to Celsius or Type CtF to convert Celsius to Fareheight: "
)
temperature = int(input("What number do you want to convert? "))
print(temperaturecoverter(temperature, conversion))

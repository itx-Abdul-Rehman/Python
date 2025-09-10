# write a program using function to convert Celsius to Fahrenheit
# F = (°C × 9/5) + 32

def celsiusToFahrenheit(celsius):
    fahrenheit=(celsius*(9/5))+32
    return fahrenheit

celsius=float(input('Enter Celsius:'))

fahrenheit=celsiusToFahrenheit(celsius)
print(f'{celsius}C is equal to {fahrenheit}F')

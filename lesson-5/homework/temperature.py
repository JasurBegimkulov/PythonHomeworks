def convert_cel_to_far(celcius):
    return celcius * 9/5 + 32

temp_celcius = float(input(f"Enter a temperature in degrees C:"))
temp_fahrenheit = convert_cel_to_far(temp_celcius)
print(f"{temp_celcius} degrees C = {temp_fahrenheit} degrees F")

def convert_far_to_cel(fahrenheit1):
    return (fahrenheit1 - 32) * 5/9

temp_fahrenheit1 = float(input(f"Enter a temperature in degrees F:"))
temp_celcius1 = convert_far_to_cel(temp_fahrenheit1)
print(f"{temp_fahrenheit1} degrees F = {temp_celcius1} degrees C")



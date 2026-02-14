temperature = int(input("Enter temperature (F): "))

if temperature >= 80:
    print("It's hot! Wear shorts.")
elif 60 <= temperature <= 79:
    print("It's pleasant. A t-shirt is fine")
elif 40 <= temperature <= 59:
    print("It's cool. Bring a jacket")
elif temperature < 40:
    print("It's cold! Bundle up")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Convertidor de Temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Celsius a Kelvin")
    print("4. Kelvin a Celsius")
    print("5. Fahrenheit a Kelvin")
    print("6. Kelvin a Fahrenheit")
    
    choice = int(input("Elige una opción (1-6): "))
    
    if choice == 1:
        celsius = float(input("Introduce la temperatura en Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == 3:
        celsius = float(input("Introduce la temperatura en Celsius: "))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius):.2f}K")
    elif choice == 4:
        kelvin = float(input("Introduce la temperatura en Kelvin: "))
        print(f"{kelvin}K = {kelvin_to_celsius(kelvin):.2f}°C")
    elif choice == 5:
        fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit):.2f}K")
    elif choice == 6:
        kelvin = float(input("Introduce la temperatura en Kelvin: "))
        print(f"{kelvin}K = {kelvin_to_fahrenheit(kelvin):.2f}°F")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()

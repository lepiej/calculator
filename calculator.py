#!/usr/bin/env python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    while True:
        print("Enkel Kalkylator")
        print("Velg operasjon:")
        print("1. Addisjon")
        print("2. Subtraksjon")
        print("3. Multiplikasjon")
        print("4. Divisjon")

        choice = input("Skriv inn valg (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Skriv inn første tall: "))
            num2 = float(input("Skriv inn andre tall: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Ugyldig input")

        again = input("Gjør en annen beregning? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
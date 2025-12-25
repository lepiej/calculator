#!/usr/bin/env python3

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Feil: Divisjon med null"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Feil: Kvadratrot av negativt tall"
    return math.sqrt(x)

def calculator():
    while True:
        print("Avansert Kalkylator")
        print("Velg operasjon:")
        print("1. Addisjon")
        print("2. Subtraksjon")
        print("3. Multiplikasjon")
        print("4. Divisjon")
        print("5. Potens")
        print("6. Kvadratrot")
        print("7. Avslutt")

        choice = input("Skriv inn valg (1-7): ")

        if choice == '1':
            num1 = float(input("Skriv inn første tall: "))
            num2 = float(input("Skriv inn andre tall: "))
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            num1 = float(input("Skriv inn første tall: "))
            num2 = float(input("Skriv inn andre tall: "))
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            num1 = float(input("Skriv inn første tall: "))
            num2 = float(input("Skriv inn andre tall: "))
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            num1 = float(input("Skriv inn første tall: "))
            num2 = float(input("Skriv inn andre tall: "))
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            base = float(input("Skriv inn grunnverdi: "))
            exp = float(input("Skriv inn eksponent: "))
            print(f"{base} ^ {exp} = {power(base, exp)}")
        elif choice == '6':
            num = float(input("Skriv inn tall: "))
            print(f"Kvadratrot av {num} = {square_root(num)}")
        elif choice == '7':
            print("Takk for at du brukte kalkulatoren!")
        else:
            print("Ugyldig valg")

if __name__ == "__main__":
    calculator()


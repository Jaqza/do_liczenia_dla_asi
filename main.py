from random import randint


def dodawanie():
    num1 = randint(2, 25)
    num2 = randint(2, 25)
    wynik = num1 + num2
    print(f"Ile to jest {num1} + {num2}")
    odpowiedz = int(input())
    if wynik == odpowiedz:
        print("Swietnie !!!")
    else:
        print("Cos poszło nie tak")
    print(f"{num1} + {num2} = {wynik}")

def odejmowanie():
    num1 = randint(2, 25)
    num2 = randint(2, 25)
    wynik = num1 - num2
    print(f"Ile to jest {num1} - {num2}")
    odpowiedz = int(input())
    if wynik == odpowiedz:
        print("Swietnie !!!")
    else:
        print("Cos poszło nie tak")
    print(f"{num1} - {num2} = {wynik}")

is_program_on = True
while is_program_on:
    operations = randint(1,7)
    if operations <= 3:
        dodawanie()
    else:
        odejmowanie()
    print("\n")
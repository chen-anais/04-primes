from math import sqrt

#### Fonction secondaire


def isprime(p):
    premier = True
    n = int(input("entrer un nombre: "))
    max = int(sqrt(n)) + 1
    for i in range(2,max + 1):
        if n % i == 0:
            premier = False
            a= int(n/i)
            print(f'{n} = {i} x {a} : False')
            break

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()

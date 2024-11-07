""" 
contient une fonction isprime qui retourne si le nombre passé en paramètre est premier
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne True si p est premier et False si il ne l'est pas
    """
    if p in (0, 1) :
        return False
    for i in range(2,int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Teste si les nombres de 0 à 99 sont premiers

    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()

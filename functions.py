from math import sqrt

def find_N_Primes(N: int):
    primes = []
    number = 2
    while len(primes) != N:
        nbr_divisors = 0
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                nbr_divisors += 1
            if nbr_divisors > 2:
                break
        if nbr_divisors == 2:
            primes.append(number)
        number += 1
    return primes

def print_Line(line, spaces, offset):
    print(" " * (spaces // 2) * offset , end="")
    for i in line:
        print(f"{i :<{spaces}}", end="")
    print("")

def print_Triangle(ligneDepart):
    ligneA = ligneDepart
    spaces = len(str(max(ligneA))) + 1
    offset = 0
    print_Line(ligneA, spaces, offset)
    while (len(ligneA) > 1):
        offset += 1
        ligneB = []
        for i in range(len(ligneA) - 1):
            ligneB.append(abs(ligneA[i] - ligneA[i+1]))
        print_Line(ligneB, spaces, offset)
        ligneA = ligneB

def first_Of_Lines_Is_1(ligneDepart):
    ligneA = ligneDepart
    while (len(ligneA) > 1):
        ligneB = []
        for i in range(len(ligneA) - 1):
            ligneB.append(abs(ligneA[i] - ligneA[i+1]))
        if ligneB[0] != 1:
            return False
        ligneA = ligneB
    return True

def test_Remove_Values(ligneDepart):
    for valeur in ligneDepart:
        ligne = ligneDepart
        ligne.remove(valeur)
        if not(first_Of_Lines_Is_1(ligne)):
            print(valeur)
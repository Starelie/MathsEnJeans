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

def find_N_Odds(N: int):
    odds = [0] * N
    for i in range(len(odds)):
        odds[i] = i * 2 + 1
    return odds

def find_N_Squares(N: int):
    squares = []
    for i in range(N):
        squares.append(i*i)
    return squares

def find_N_Powers_Of_X(N: int, X: int):
    powers = []
    for i in range(N):
        powers.append(X**i)
    return powers

def find_N_Values_Fibonacci(N: int):
    fibonacci = [1, 1]
    for i in range(N):
        fibonacci.append(fibonacci[i] + fibonacci[i + 1])
    return fibonacci

def _print_Line_Spaces(line, spaces, offset):
    print(" " * (spaces // 2) * offset , end="")
    for i in line:
        print(f"{i :<{spaces}}", end="")
    print("")

def _simple_Print_Line(line):
    for i in line:
        print(i, end=" ")
    print("")

def print_Triangle_Spaces(ligneDepart):
    ligneA = ligneDepart.copy()
    spaces = len(str(max(ligneA))) + 1
    offset = 0
    _print_Line_Spaces(ligneA, spaces, offset)
    for i in range(len(ligneA) - 1):
        offset += 1
        ligneB = []
        for i in range(len(ligneA) - 1):
            ligneB.append(abs(ligneA[i] - ligneA[i+1]))
        _print_Line_Spaces(ligneB, spaces, offset)
        ligneA = ligneB

def simple_Print_Triangle(ligneDepart):
    ligneA = ligneDepart.copy()
    _simple_Print_Line(ligneA)
    for i in range(len(ligneA) - 1):
        ligneB = []
        for i in range(len(ligneA) - 1):
            ligneB.append(abs(ligneA[i] - ligneA[i+1]))
        _simple_Print_Line(ligneB)
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
    remove_Not_1 = []
    for valeur in ligneDepart:
        ligne = ligneDepart.copy()
        ligne.remove(valeur)
        if not(first_Of_Lines_Is_1(ligne)):
            remove_Not_1.append(valeur)
    return remove_Not_1
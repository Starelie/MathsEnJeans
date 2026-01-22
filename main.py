import functions as f
import matplotlib.pyplot as plot
import comparators as c

maxLineLength = 50
ligne = f.find_N_Primes(maxLineLength)
f.print_Triangle_Spaces(ligne)
f.simple_Print_Triangle(ligne)
f.print_Triangle_2_Categories(ligne, c.greater_or_equal, 2)
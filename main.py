import functions as f
import matplotlib.pyplot as plot

maxLineLength = 100
ligneB = f.find_N_Odds(maxLineLength)
ligneB.remove(101)
f.print_Triangle(ligneB)
# for lineLength in range(3, maxLineLength + 1):
#     ligneTest = []
#     for i in range(lineLength):
#         ligneTest.append(ligneA[i])
#     print(f.test_Remove_Values(ligneTest))
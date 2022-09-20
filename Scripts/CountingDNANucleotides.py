DNA = open(r'rosalind_dna (3).txt')
DNA1 = DNA.read()
A_Count = 0
C_Count = 0
G_Count = 0
T_Count = 0

for i in range(len(DNA1)):
    if DNA1[i] == "A":
        A_Count = A_Count + 1
    elif DNA1[i] == "C":
        C_Count = C_Count + 1
    elif DNA1[i] == "G":
        G_Count = G_Count + 1
    elif DNA1[i] == "T":
        T_Count = T_Count + 1

print(str(A_Count) + " " + str(C_Count) + " " + str(G_Count) + " " + str(T_Count))

input("Press enter to exit")
DNA = open(r'rosalind_dna (3).txt')
DNA1 = DNA.read()
A_Count = DNA1.count("A")
C_Count = DNA1.count("C")
G_Count = DNA1.count("G")
T_Count = DNA1.count("T")

print(str(A_Count)+ " " + str(C_Count) + " " + str(G_Count) + " " + str(T_Count))

input("Press enter to exit")
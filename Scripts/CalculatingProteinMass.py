AAMMFilePath = open(r"AminoAcidMonoisotopicMassTable.txt")

with AAMMFilePath:
    AAMMlist = AAMMFilePath.read().splitlines()

ProteinSeq = input("What is the protein sequence for the protein you would like the mass of?")

mass = 0
for AA in ProteinSeq:
    for aa in AAMMlist:
        if AA == aa[0]:
            mass += float(aa[4:])
print(round(mass,3))




DNApath = open(r'rosalind_rna (1).txt')
DNA = DNApath.read()

for i in range(len(DNA)):
    if DNA[i] == "T":
        DNA1 = DNA.replace("T", "U")

#open text file
DNAtoRNATranscribed = open(r"DNAtoRNATranscribed.txt", "w")
DNAtoRNATranscribed.write(DNA1)
DNAtoRNATranscribed.close()
print(DNA1)
print(DNA)

input("Press enter to exit")
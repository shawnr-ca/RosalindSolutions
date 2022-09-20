#Open text file with DNA sequence
DNApath = open(r'rosalind_revc (1).txt')
DNAOrig = DNApath.read()

#Create sequence complementary to original sequence
DNAcomp = ""

for i in range(len(DNAOrig)):
    if DNAOrig[i] == "A":
        DNAcomp = DNAcomp + "T"
    elif DNAOrig[i] == "T":
        DNAcomp = DNAcomp + "A"
    elif DNAOrig[i] == "C":
        DNAcomp = DNAcomp + "G"
    elif DNAOrig[i] == "G":
        DNAcomp = DNAcomp + "C"

#Create reverse sequence of complementary sequence
DNAcomprev = ""

for index, base in enumerate(DNAcomp):
    DNAcomprev += DNAcomp[(len(DNAcomp)-1)-index]

#Print and write to text file complete reverse compliment sequence
print("The Original Sequence is: " + DNAOrig)
print("The Reverse Compliment Sequence is: " + DNAcomprev)

revcompfile = open(r"ReverseComplimentSequence.txt", "w")
revcompfile.write(DNAcomprev)
revcompfile.close()

input("Press enter to exit")


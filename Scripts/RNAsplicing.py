#Open Fasta Sequences and Create list
FASTAFilePath = open(r"DNAFASTASampleData.txt")
ProteinSeqFilePath = open(r"ProteinSeqOutput.txt","w")

with FASTAFilePath:
    FASTArawList = FASTAFilePath.read().splitlines()

FASTAlist = []
SeqBool = False
for line in FASTArawList:
    if line[0] == ">":
        SeqBool = True
    else:
        if SeqBool == True:
            FASTAlist.append(line)
            SeqBool = False
        else:
            FASTAlist[-1] += line

#Remove introns from main sequence containing initial transcript. Convert from DNA to RNA (for ease with codon dict)
MainSeq = FASTAlist[0]
print("The initial DNA sequence is : " + MainSeq)

for intron in FASTAlist[1:]:
    MainSeq = MainSeq.replace(intron, "")
    

for base in MainSeq:
    if base == "T":
       MainSeq = MainSeq.replace(base,"U")

print("The mature mRNA sequence is : " + MainSeq)

#Convert RNA sequence to protein sequence
codons = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

FinalRNASeq = ""
Start = False
for base in range(len(MainSeq)):  #Ensure starting with Start codon
    if Start == False:
        if MainSeq[base:base + 3] == "AUG":
            FinalRNASeq += "A"
            Start = True
    else:
        FinalRNASeq += MainSeq[base]

RNACodon = []
for base in range(len(FinalRNASeq)):
    if base % 3 == 0:
        RNACodon.append(FinalRNASeq[base:base + 3])

ProteinSeq = ""
for i in RNACodon:
    if RNACodon[0] == "AUG":
        for codon in codons.keys():
            if i == codon:
                ProteinSeq += codons[codon]
                if i != "UGA" and i != "UAG" and i != "UAA":
                    ProteinSeq1 = ProteinSeq.replace("Stop","")
                    break
print("The protein sequence is : " + ProteinSeq1)

with ProteinSeqFilePath:
    ProteinSeqFilePath.write(ProteinSeq1)


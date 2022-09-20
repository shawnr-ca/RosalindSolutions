#Create string with sequence and translate to RNA
FASTAseqFilePath = open("FASTASampleData.txt")
with FASTAseqFilePath:
    FASTAseqRAW = FASTAseqFilePath.read().splitlines()

FASTAseq = []
FASTAIDBool = False
for line in FASTAseqRAW:
    if line[0] == ">":
        FASTAIDBool = True
    else:
        if FASTAIDBool:
            FASTAseq.append(line)
            FASTAIDBool = False
        else:
            FASTAseq[-1] += line

#Convert RNA sequence to protein sequence
Seq = FASTAseq[0]
for base in Seq:
    if base == "T":
        Seq = Seq.replace(base, "U")

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

def ProteinSeq(Seq):
    ProteinSeq = ""
    StartBool = False
    Done = False
    for i in range(len(Seq)):
        if Done == True:
            break
        if Seq[i:i + 3] == "AUG" and StartBool == False:
            StartBool = True
            Start = int(i)
        if StartBool:
            if (i - Start) % 3 == 0:
                for codon in codons.keys():
                    if Seq[i:i + 3] == codon:
                        ProteinSeq += codons[codon]
                        if Seq[i:i + 3] == "UGA" or Seq[i:i + 3] == "UAG" or Seq[i:i + 3] == "UAA":
                            ProteinSeq = ProteinSeq.replace("Stop", "")
                            Done = True
    return ProteinSeq
   # print(Seq)
   # print("ORF = " + str(Seq[Start:Start + len(ProteinSeq)*3]))
   # print("ORF Location =  " + str(Start) + ":" + str(Start + len(ProteinSeq)*3))

def ReverseCompliment(RNAOrig):
    # Create sequence complementary to original sequence
    DNAcomp = ""
    for base in range(len(RNAOrig)):
        if RNAOrig[base] == "A":
            DNAcomp += "U"
        elif RNAOrig[base] == "U":
            DNAcomp += "A"
        elif RNAOrig[base] == "C":
            DNAcomp += "G"
        elif RNAOrig[base] == "G":
            DNAcomp += "C"
    # Create reverse sequence of complementary sequence
    DNAcomprev = ""
    for base in DNAcomp:
        DNAcomprev = base + DNAcomprev
    return DNAcomprev

def ORFfinder(Sequence):
    ForSeq = Sequence
    BackSeq = ReverseCompliment(Sequence)
    ORFs = []
    for loc in range(len(ForSeq)):
        if len(ProteinSeq(ForSeq[loc:])) != 0:
            ORFs.append(ProteinSeq(ForSeq[loc:]))
    for loc in range(len(BackSeq)):
        if len(ProteinSeq(BackSeq[loc:])) != 0:
            ORFs.append(ProteinSeq(BackSeq[loc:]))
    ORFs1 = []
    for i in range(len(ORFs)):
        if ORFs[i] != ORFs[i-1]:
            if ORFs[i] not in ORFs1:
                ORFs1.append(ORFs[i])
    for ORF in ORFs1:
        print(ORF)



ORFfinder(Seq)

#Open RNA sequence from text file and convert string to list of codons
RNAseqFilePath = open(r"rosalind_prot.txt")

RNAseq = RNAseqFilePath.readline().strip()

#Use codon dictionary to create string of proteins
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

ProteinSeq = ""
StartBool = False
for i in range(len(RNAseq)):
    if RNAseq[i:i + 3] == "AUG" and StartBool == False:
        StartBool = True
        Start = int(i)
    if StartBool:
        if (i - Start) % 3 == 0:
            for codon in codons.keys():
                if RNAseq[i:i + 3] == codon:
                    ProteinSeq += codons[codon]
                    if RNAseq[i:i + 3] != "UGA" and RNAseq[i:i + 3] != "UAG" and RNAseq[i:i + 3] != "UAA":
                        ProteinSeq1 = ProteinSeq.replace("Stop", "")
                        break

#Print and write Protein Sequence to Text file
ProteinSequenceFilePath = open(r"ProteinSequence.txt", "w")
ProteinSequenceFilePath.write(ProteinSeq1)
print(ProteinSeq1)

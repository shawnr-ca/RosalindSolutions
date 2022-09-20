# This program accepts the Uniprot IDs of multiple proteins and checks if the N-glycosylation motif
# (N{P}[ST]{P}) is  present, while also returning its location in their respective protein FASTA
# sequences

from bioservices import UniProt
u = UniProt(verbose=True)
# Open text file with Uniprot IDs and create list of IDs
# IDs containing "_" return error so they are shortened

ProteinIDFilePath = open(r"rosalind_mprt.txt")

ProteinIDs0 = []
ProteinIDs = []
for line in ProteinIDFilePath.readlines():
    ProteinIDs0.append(line.strip())

for ID in ProteinIDs0:
    if ID.count("_") == 0:
        ProteinIDs.append(ID)
    elif ID.count("_") > 0:
        for char in range(len(ID)):
            if ID[0:char].count("_") == 0 and len(ID[0:char]) == ID.index("_"):
                    ProteinIDs.append(ID[0:char])

# Create list of Protein Fasta Sequences and remove first line containing Protein Info

FastaSeqs0 = []
FastaSeqs = []

for ID in ProteinIDs:
    FastaSeqs0.append(u.get_fasta(ID).splitlines())

for i in range(len(ProteinIDs)):
    FastaSeqs.append("")

for seq in FastaSeqs0:
    for line in seq:
        if line != seq[0]:
            FastaSeqs[FastaSeqs0.index(seq)] += line

# Create dictionary of Uniprot ID and Fasta Sequence
UniprotDict = {FastaSeqs[i]:ProteinIDs0[i] for i in range(len(ProteinIDs))}

# Search for N-glycosylation motif (N{P}[ST]{P}) in Protein sequences
# and return Protein ID followed by location in protein sequence
NglycoPos = []

for Fasta in FastaSeqs:
    for amino in range(0, len(Fasta) - 4):
        if Fasta[amino] == "N":
            if Fasta[amino+1] != "P":
                if Fasta[amino+2] == "S" or Fasta[amino+2] == "T":
                    if Fasta[amino+3] != "P":
                        NglycoPos.append((UniprotDict[Fasta],amino+1))

# Append to text file

MotifLocPathFile = open(r"Location of Motif.txt","w+")

NglycoPosList = []
for i in range(len(NglycoPos)):
    if NglycoPos[i][0] != NglycoPos[i-1][0]:
        NglycoPosList.append(NglycoPos[i][0])
        NglycoPosList.append(NglycoPos[i][1])
    else:
        NglycoPosList.append(NglycoPos[i][1])


print(NglycoPosList[0])
MotifLocPathFile.writelines(str(NglycoPosList[0]) + "\n")

for i in NglycoPosList:
        if str(i).isupper() or str(i).islower():
            if i != NglycoPosList[0]:
                MotifLocPathFile.writelines("\n" + str(i) + "\n")
                print("\n" + str(i))
        else:
            print(i, end=" ")
            MotifLocPathFile.writelines(str(i) + " ")



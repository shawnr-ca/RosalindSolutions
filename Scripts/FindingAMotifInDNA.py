#Create string variables for S string (DNA sequence) and and T substring (Motif)
SequenceMotif_FilePath = open(r"rosalind_subs.txt")
seq = SequenceMotif_FilePath.readline()
mot = SequenceMotif_FilePath.readline().strip()

#Find index locations of Motif
index = []

for i in range(len(seq)):
    if seq.startswith(mot,i):
        index.append(i)

for i in range(len(index)):
    index[i] += 1

index_clean = str(index).replace(",","").replace("[","").replace("]","")
print(index_clean)
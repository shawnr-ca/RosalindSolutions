SequenceFilePath = open(r"rosalind_hamm.txt")
Seq1 = SequenceFilePath.readline()
Seq2 = SequenceFilePath.readline()

HammingCount = 0

for i in range(len(Seq2)):
    if Seq1[i] != Seq2[i]:
        HammingCount = HammingCount + 1

print(HammingCount)


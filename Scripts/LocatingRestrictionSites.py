SampleDataFilePath = open(r"rosalind_revp.txt")
SampleDataTxt = SampleDataFilePath.readlines()
Seq = []

for line in SampleDataTxt:
    Seq.append(line.strip())

Seq0 = []
SeqIDBool0 = False
for i in range(len(Seq)):
    if Seq[i].count(">") > 0:
        Seq0.append(Seq[i])
        SeqIDBool0 = True

Seq1 = []
SeqIDBool = False
for i in range(len(Seq)):
    if Seq[i].count(">") > 0:
        SeqIDBool = True
    else:
        if SeqIDBool:
            Seq1.append(Seq[i])
            SeqIDBool = False
        else:
            Seq1[-1] += Seq[i]

def FindRestrictionList(SequencesList):
    for Sequences in SequencesList:
        print(Seq0[SequencesList.index(Sequences)])
        PossPals = []
        Pos = []
        PosLenPal = []
        for pos in range(len(Sequences) + 1):
            for length in range(4, 13):
                if len(Sequences[pos:pos + length]) >= 4:
                    PossPals.append(Sequences[pos:pos + length])
        for seq in PossPals:
            if len(seq) % 2 == 0:
                seq1 = seq[0:int(len(seq) / 2)]
                seq2 = seq[int(len(seq) / 2):]
                seq1pal = ""
                for base in range(len(seq1)):
                    if seq1[base] == "A":
                        seq1pal = "T" + seq1pal
                    if seq1[base] == "T":
                        seq1pal = "A" + seq1pal
                    if seq1[base] == "G":
                        seq1pal = "C" + seq1pal
                    if seq1[base] == "C":
                        seq1pal = "G" + seq1pal
                if seq1pal == seq2:
                    count = 0
                    while count < len(Sequences):
                        count = Sequences.find(seq, count)
                        if count == -1:
                            break
                        PosLenPal.append(((count + 1), len(seq)))
                        Pos.append(count + 1)
                        count += len(seq)
            PosLenPal.sort()
            PosLenPalFinal = []
        for i in PosLenPal:
            if i not in PosLenPalFinal:
                PosLenPalFinal.append(i)
        for i in range(len(PosLenPalFinal)):
            print(str(PosLenPalFinal[i][0]) + " " + str(PosLenPalFinal[i][1]))

def FindRestriction(Sequences):
    PossPals = []
    Pos = []
    PosLenPal = []
    for pos in range(len(Sequences) + 1):
        for length in range(4, 13):
            if len(Sequences[pos:pos + length]) >= 4:
                PossPals.append(Sequences[pos:pos + length])
    for seq in PossPals:
        if len(seq) % 2 == 0:
            seq1 = seq[0:int(len(seq) / 2)]
            seq2 = seq[int(len(seq) / 2):]
            seq1pal = ""
            for base in range(len(seq1)):
                if seq1[base] == "A":
                    seq1pal = "T" + seq1pal
                if seq1[base] == "T":
                    seq1pal = "A" + seq1pal
                if seq1[base] == "G":
                    seq1pal = "C" + seq1pal
                if seq1[base] == "C":
                    seq1pal = "G" + seq1pal
            if seq1pal == seq2:
                count = 0
                while count < len(Sequences):
                    count = Sequences.find(seq, count)
                    if count == -1:
                        break
                    PosLenPal.append(((count + 1), len(seq)))
                    Pos.append(count + 1)
                    count += len(seq) - 2
        PosLenPal.sort()
        PosLenPalFinal = []
    for i in PosLenPal:
        if i not in PosLenPalFinal:
            PosLenPalFinal.append(i)
    for i in range(len(PosLenPalFinal)):
        print(str(PosLenPalFinal[i][0]) + " " + str(PosLenPalFinal[i][1]))



FindRestriction(Seq1[0])


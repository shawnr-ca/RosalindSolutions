#Open Data Set from Rosalind
SampleDataSetPath = open(r"rosalind_gc (1).txt")
SampleDataSet = SampleDataSetPath.read()

#Create list with Fasta Rosalind Sequence IDs as key and DNA sequences and values ({seqID1:seq1,seqID2:seq2...)
FastaData = []
FastaIDlist = []
seqlinelist = []


for line in SampleDataSet.splitlines():
    if line.count(">Rosalind") > 0:
        FastaData.append(line)
    elif line.count(">Rosalind") == 0:
        FastaData.append(line)

Fasta1 = []
FastaBool = False
for string in FastaData:
    if string[0] == ">":
        Fasta1.append(string)
        FastaBool = True
    else:
        if FastaBool:
            Fasta1.append(string)
            FastaBool = False
        else:
            Fasta1[-1] += string

for i in Fasta1:
    if i[0] == ">":
        FastaIDlist.append(i)
    else:
        seqlinelist.append(i)

#Count GC percentage for each sequence and append to list. Combine list of GC content to list of ID's into dictionary
GCcountList = []
for i in seqlinelist:
    GCcountList.append((i.count("G") + i.count("C"))/len(i)*100)

GCcountDict1 ={GCcountList[i]: FastaIDlist[i] for i in range(len(FastaIDlist))}

#Return onlu highest GC content sequence (ID and GC %)
print(str(GCcountDict1[max(GCcountDict1)]).replace(">",""))
print(max(GCcountDict1))


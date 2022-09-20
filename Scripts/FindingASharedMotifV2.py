# This version initially checks for the length of the largest shared motif between three
# random sequences and then only creates possible motifs smaller than this value
# for all the sequences
import random
import time

start = time.time()
#Open file with Fasta ID's and sequences
seqsFilePath = open(r"rosalind_lcsm.txt")
seqsText = seqsFilePath.read()

#Create list with only test sequences
Testseqslist0 = []
Testseqslist = []


for line in seqsText.splitlines():
    if line.count(">Rosalind") > 0:
        Testseqslist0.append(line)
    elif line.count(">Rosalind") == 0:
        Testseqslist0.append(line)

for string in Testseqslist0:
    if string.count(">") == 1:
        FastaBool = True
    else:
        if FastaBool:
            Testseqslist.append(string)
            FastaBool = False
        else:
            Testseqslist[-1] += string

RandomSeqNums = random.sample(range(0,len(Testseqslist)), 4)
Testseqslist1 = [Testseqslist[RandomSeqNums[0]], Testseqslist[RandomSeqNums[1]], Testseqslist[RandomSeqNums[2]], Testseqslist[RandomSeqNums[3]]]

#Create lists of test substrings
TesttheorSubstringInitial = []
TesttheorSubstringComplete = []


for i in Testseqslist1:
    for j in range(len(i)):
        TesttheorSubstringInitial.append(i[0:j+1])

for i in TesttheorSubstringInitial:
    for j in range(len(i)):
            TesttheorSubstringComplete.append(i[j:])

#Search for substrings contained in test sequences and append to list of shared test substrings
TestsharedSubstrings = []

def CommonSubstring(str,list):
   for i in list:
      if str not in i:
         return False
   return True


for i in TesttheorSubstringComplete:
        if CommonSubstring(i,Testseqslist1):
            TestsharedSubstrings.append(i)

#Return longest shared substring amongst first three sequences
LongestPossibleSubstring = max(TestsharedSubstrings, key=len)
LongestPossibleSubstringLength = len(max(TestsharedSubstrings, key=len))
print("The largest common motif amongst the test sequences is " + str(LongestPossibleSubstring))
print("The length of the largest common motif amongst the test sequences is " + str(LongestPossibleSubstringLength) + " nucleotides long")

#Create list of all sequences
seqslist0 = []
seqslist = []


for line in seqsText.splitlines():
    if line.count(">Rosalind") > 0:
        seqslist0.append(line)
    elif line.count(">Rosalind") == 0:
        seqslist0.append(line)

for string in seqslist0:
    if string.count(">") == 1:
        FastaBool = True
    else:
        if FastaBool:
            seqslist.append(string)
            FastaBool = False
        else:
            seqslist[-1] += string


#Create lists of substrings. For final list containing all possible substrings, remove duplicate substrings
theorSubstringInitial = []
theorSubstringInitial1 = []
theorSubstringComplete = []


for i in seqslist:
    for j in range(len(i)):
        theorSubstringInitial.append(i[0:j+1])

for i in theorSubstringInitial:
    for j in range(len(i)):
        if len(i[j:]) <= LongestPossibleSubstringLength:
            theorSubstringComplete.append(i[j:])

#Search for substrings contained in all sequences and append to list of shared substrings
sharedSubstrings = []

for i in theorSubstringComplete:
        if CommonSubstring(i,seqslist):
            sharedSubstrings.append(i)

#Return longest shared substring amongst all sequences and its length
print("The largest common motif amongst all the sequences is " + str(max(sharedSubstrings, key=len)))
print("The length of the largest common motif amongst all the sequences is " + str(len(max(sharedSubstrings, key=len))) + " nucleotides long")

end = time.time()
TimeToExecute = str((end - start)/60)
print("It took " + TimeToExecute + " minutes to execute this search for the largest common motif")

#This version generates all possible substrings and searches for largest one present in all sequences.
import time

start = time.time()
#Open file with Fasta ID's and sequences
seqsFilePath = open(r"rosalind_lcsm.txt")
seqsText = seqsFilePath.read()

#Create list with only sequences
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
            theorSubstringComplete.append(i[j:])


#Search for substrings contained in all sequences and append to list of shared substrings
sharedSubstrings = []

def CommonSubstring(str,list):
   for i in list:
      if str not in i:
         return False
   return True


for i in theorSubstringComplete:
        if CommonSubstring(i,seqslist):
            sharedSubstrings.append(i)

#Return longest shared substring
print("The largest common motif amongst all the sequences is " + str(max(sharedSubstrings, key=len)))
print("The length of the largest common motif amongst all the sequences is " + str(len(max(sharedSubstrings, key=len))) + " nucleotides long")

end = time.time()
TimeToExecute = str((end - start)/60)
print("It took " + TimeToExecute + " minutes to execute this search for the largest common motif")






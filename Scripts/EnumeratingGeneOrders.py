import math
Numb = int(input("What positive non-negative integer do wish to find the possible combinations of?"))
PermCombResultFilePath = open(r"PermCombResult.txt", "w")


print(math.perm(Numb))

Perms = math.perm(Numb)

NumbList = []
for i in range(1,Numb + 1):
    NumbList.append(i)
PermCombResultFilePath.writelines(str(Perms) + "\n")
def HeapAlgo(List, Length):
    if Length == 1:
        PermCombResultFilePath.writelines(str(List).replace("[", "").replace("]", "").replace(",", "") + "\n")
        print(List)
        return


    for i in range(Length):
        HeapAlgo(List, Length - 1)
        if Length % 2 != 0:
            List[0], List[Length-1] = List[Length-1], List[0]
        else:
            List[i], List[Length - 1] = List[Length - 1], List[i]

HeapAlgo(NumbList,len(NumbList))


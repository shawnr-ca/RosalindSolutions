from math import comb
k = int(input("What is the number of Homozygous Dominant individuals?"))
m = int(input("What is the number of Heterozygous individuals?"))
n = int(input("What is the number of Homozygous Recessive individuals?"))
def CalcDomAlleleProb(k, m, n):
    #Calculate total number of individuals
    totInd = k + m + n
    #Calulate possible combinations of individuals
    totPossibComb = comb(totInd, 2)
    #Find combos that will produce offspring with at least 1 dominant allele (display dominant phenotype)
    DomComb = (4/4)*comb(k,2) + (4/4)*k*m + (4/4)*k*n + (2/4)*m*n + (3/4)*comb(m,2) + (0/4)*n*n
    probability = DomComb/totPossibComb
    print(totPossibComb)
    print(comb(k,2))
    return probability

# Example Call: 
print(CalcDomAlleleProb(k, m, n))



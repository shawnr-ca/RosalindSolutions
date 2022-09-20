n = int(input("How many months?"))
k = int(input("How many pairs per a litter?"))


def TotRabbitPairs(n, k):
   if n == 0:
    return 0
   elif n == 1:
    return 1
   else:
       return TotRabbitPairs(n-1,k) + k*TotRabbitPairs(n-2,k)



print(TotRabbitPairs(n,k))

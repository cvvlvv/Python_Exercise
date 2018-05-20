
# coding: utf-8

# Day 2:
# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

# In[ ]:

def PrimeFactors ():
    n = int(input("Please give a number."))
    PrimeFactors = []
    prime = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime.append(i)
    i = 0
    while i<len(prime):
        if n%prime[i] == 0:
            PrimeFactors.append(prime[i])
            n = n/prime[i]
        else:
            i = i+1
    for i in range(0,len(PrimeFactors)-1):
        print("%s *"%(PrimeFactors[i]), end=" ")
    print(PrimeFactors[-1])


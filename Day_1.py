
# coding: utf-8

# Day 1:
# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number

# In[ ]:

def FiboSeq ():
    FiboSeq = [0,1]
    Nth = int(input("Please give a number."))
    if Nth == 0 or Nth == 1:
        return FiboSeq[0:Nth+1]
    else:
        for i in range(2,Nth):
            FiboSeq.append(FiboSeq[i-1]+FiboSeq[i-2])
    return FiboSeq  


# In[ ]:

def FiboSeqtoNum ():
    N = int(input("Please give a number."))
    FiboSeqtoNum = [0,1]
    for i in range(0,100):
        a = FiboSeqtoNum[i]+FiboSeqtoNum[i+1]
        if a<=N:
            FiboSeqtoNum.append(a)
        else:
            break
    return FiboSeqtoNum


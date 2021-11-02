from math import factorial

def get_seq():
    file = open('rosalind_pmch.txt', 'r').read().split("\n")[1:-1]
    seq = ''
    for i in range(len(file)):
        seq += file[i]
    return seq

def count(char, seq):
    c = 0
    for i in range(len(seq)):
        if seq[i] == char:
               c += 1
    return c
 
if __name__=="__main__":
    seq = get_seq()
    countA, countC = count('A', seq), count('C', seq)
    print(factorial(countA)*factorial(countC))

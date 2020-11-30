alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}



def HammingDistance(p, q):
    count = 0
    for i, j in zip(p, q):
        if i != j:
            count += 1
    return count

def NumberToPattern(Number, k):
    Pattern = ""
    for i in range(k):
        indx = Number % 4
        Number = int(Number / 4)
        Pattern += alphabet[indx]
    return Pattern[::-1]

def DistanceBetweenPatternAndString(Pattern, DNA):
    k = len(Pattern)
    distance = 0
    for seq in DNA:
        hammingDistance = float("inf")
        for i in range(len(seq)-k+1):
            currDistace = HammingDistance(Pattern, seq[i:i+k])
            if hammingDistance > currDistace:
                hammingDistance = currDistace
        distance += hammingDistance
    return distance

def MedianString(DNA, k):
    distance = float("inf")
    for i in range(4**k):
        Pattern = NumberToPattern(i, k)
        currDist = DistanceBetweenPatternAndString(Pattern, DNA)
        if distance > currDist:
            distance = currDist
            Median = Pattern
    return Median

if __name__ == "__main__":
    file = open("./rosalind_ba2b.txt", "r").read().split("\n")
    k, DNA = int(file[0]), file[1:-1]
    print(MedianString(DNA, k))

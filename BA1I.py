
nucleotides = ["A", "T", "G", "C"]

def HammingDistance(p, q):
    count = 0
    for i, j in zip(p, q):
        if i != j:
            count += 1
    return count

def Neighbors(Pattern, d):
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ["A", "C", "G", "T"]
    Neighborhood = list()
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for n in nucleotides:
                    Neighborhood.append(n+Text)
        else:
            Neighborhood.append(Pattern[0]+Text)
    return Neighborhood

def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = list()
    Count = dict()
    for i in range(len(Text)-k+1):
        neighbor = Neighbors(Text[i:i+k], d)
        for n in neighbor:
            Count[n] = Count.get(n, 0) + 1

    maxCount = max(Count.values())

    for pattern, count in Count.items():
        if count == maxCount:
            FrequentPatterns.append(pattern)
    return FrequentPatterns

if __name__ == "__main__":
    Text, values, _ = open("./rosalind_ba1i.txt", "r").read().split("\n")
    k, d = values.split(" ")
    for i in FrequentWordsWithMismatches(Text, int(k), int(d)):
        print(i, end=" ")
    print()

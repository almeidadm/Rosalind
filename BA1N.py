
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


if __name__ == "__main__":
    Pattern, d, _ = open("./rosalind_ba1n.txt", "r").read().split("\n")
    for i in Neighbors(Pattern, int(d)):
        print(i)
    print()

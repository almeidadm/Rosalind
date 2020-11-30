def ApproximatePatternMatching(Text, Pattern, d):
    positions = list()
    k = len(Pattern)
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+k], Pattern) <= d:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    count = 0
    for i, j in zip(p, q):
        if i != j:
            count += 1
    return count

if __name__ == "__main__":
    Pattern, Text, d, _ = open("./rosalind_ba1h.txt", "r").read().split("\n")
    for i in ApproximatePatternMatching(Text, Pattern, int(d)):
        print(i, end=" ")
    print()


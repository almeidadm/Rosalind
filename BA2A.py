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

def MotifEnumaration(DNA_set, k, d):
    all_patterns = [list() for _ in range(len(DNA_set))]

    for pos, seq in enumerate(DNA_set):
        for j in range(len(seq) - k +1):
            for neighbor in Neighbors(seq[j:j+k], d):
                all_patterns[pos].append(neighbor)

    patterns = set(all_patterns[0])
    for p in all_patterns[1:]:
        patterns.intersection_update(p)
    return patterns

if __name__ == "__main__":
    file = open("./rosalind_ba2a.txt", "r").read().split("\n")
    k, d = file[0].split(" ")
    DNA_set = file[1:-1]
    for motif in MotifEnumaration(DNA_set, int(k), int(d)):
        print(motif, end=" ")

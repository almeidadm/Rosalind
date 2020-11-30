
skew_value = {'C': -1, 'G':1, 'A': 0, 'T': 0}

def MinimumSkew(Genome):
    skew = 0
    minimum = float("inf")
    indx = list()
    for i in range(len(Genome)):
        skew += skew_value[Genome[i]]
        if skew == minimum:
            indx.append(i+1)
        elif skew < minimum:
            minimum = skew
            indx = [i+1]

    return indx

if __name__ == "__main__":
    Genome = open("./rosalind_ba1f.txt", "r").read()[:-1]
    print(MinimumSkew(Genome))


alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}

def NumberToPattern(Number, k):
    Pattern = ""
    for i in range(k):
        indx = Number % 4
        Number = int(Number / 4)
        Pattern += alphabet[indx]
    return Pattern[::-1]


def PatternToNumber(Pattern):
    Number = 0
    for i in range(len(Pattern)):
        indx = list(alphabet.keys())[list(alphabet.values()).index(Pattern[i])]
        add = int(indx) * (4 ** (len(Pattern)-i-1))
        Number += add
    return Number

def ComputingFrequencies(Text, k):
    FrequencyArray = list()
    for i in range(4**k):
            FrequencyArray.append(0)
    for i in range(len(Text) - k + 1):
        Pattern = Text[i: i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
    return FrequencyArray

def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = list()
    Clump = dict()

    for i in range(4**k):
        Clump[str(i)] = 0
    Text = Genome[:L]
    FrequencyArray = ComputingFrequencies(Text, k)

    for i in range(4**k):
        if FrequencyArray[i] >= t:
            Clump[str(i)] = 1

    for i in range(1, len(Genome)-L+1):
        FirstPattern = Genome[i-1:i+k-1]
        indx = PatternToNumber(FirstPattern)
        FrequencyArray[indx] -= 1
        LastPattern = Genome[i+L-k:i+L]
        indx = PatternToNumber(LastPattern)
        FrequencyArray[indx] += 1

        if FrequencyArray[indx] >= t:
            Clump[str(indx)] = 1

    for i in range(4**k):
        if Clump[str(i)] == 1:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)

    return FrequentPatterns

if __name__ == "__main__":
    Genome, values, _ = open("rosalind_ba1e.txt","r").read().split("\n")
    values = values.split(" ")
    k, L, t = int(values[0]), int(values[1]), int(values[2])
    ClumpFinding(Genome, k, L, t)
    for i in ClumpFinding(Genome, int(k), int(L), int(t)):
        print(i, end=" ")
    print()

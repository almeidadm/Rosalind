alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}

def PatternToNumber(Pattern):
    Number = 0
    for i in range(len(Pattern)):
        indx = list(alphabet.keys())[list(alphabet.values()).index(Pattern[i])]
        add = int(indx) * (4 ** (len(Pattern)-i-1))
        Number += add
    return Number

if __name__ == "__main__":
    Pattern = open("./rosalind_ba1l.txt", "r").read()[:-1]
    print(PatternToNumber(Pattern))


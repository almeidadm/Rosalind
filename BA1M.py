alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}

def NumberToPattern(Number, k):
    Pattern = ""
    for i in range(k):
        indx = Number % 4
        Number = int(Number / 4)
        Pattern += alphabet[indx]
    return Pattern[::-1]

if __name__ == "__main__":
    file = open("./rosalind_ba1m.txt", "r").read().split("\n")
    Number, k = int(file[0]), int(file[1])
    print(NumberToPattern(Number, k))

inv_alphabet = {'A':0, "C":1, "G":2, "T":3}


def Profile_value(Text, profile):
    value = 1
    for i, nucl in enumerate(Text):
        value *= float(profile[inv_alphabet[nucl]][i])
    return value

def ProfileMostProbableKmer(Text, k, profile):
    min_prof = -1
    probable_mer = ""
    for i in range(len(Text)-k+1):
        mer = Text[i:i+k]
        prof = Profile_value(mer, profile)
        if min_prof < prof:
            min_prof = prof
            probable_mer = mer
    return probable_mer

if __name__ == "__main__":
    text = open("./rosalind_ba2c.txt", "r").read()[:-1].split("\n")
    seq, k, profile = text[0], int(text[1]), text[2:]
    for i, p in enumerate(profile):
        profile[i] = profile[i].split(" ")

    print(ProfileMostProbableKmer(seq, k, profile))

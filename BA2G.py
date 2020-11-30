inv_alphabet = {'A':0, "C":1, "G":2, "T":3}
import numpy as np
import random
alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}


def HammingDistance(p, q):
    count = 0
    for i, j in zip(p, q):
        if i != j:
            count += 1
    return count
    
def createProfile(Motifs, prob=True):
    motif_len = len(Motifs[0])

    profile = [[1,1,1,1] for _ in range(motif_len)]

    for i in range(motif_len):
        for motif in Motifs:
            profile[i][inv_alphabet[motif[i]]] += 1
    if prob == False:
        return profile

    for i in range(motif_len):
        for j in range(len(profile[i])):
            profile[i][j] = profile[i][j]/len(Motifs)

    return profile


def Profile_value(Text, profile):
    value = 1
    for i, nucl in enumerate(Text):
        value *= float(profile[i][inv_alphabet[nucl]])
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

def ConsensusString(profMatrix):
    seq = ""
    for row in profMatrix:
        seq += alphabet[np.argmax(row)]
    return seq

def Score(Motifs):
    profMatrix = createProfile(Motifs)
    consensus = ConsensusString(profMatrix)
    score = 0
    for motif in Motifs:
        score += HammingDistance(consensus, motif)
    return score
    
def GibbsSampler(DNA, k, t, N):
    Motifs = list()
    
    for i in range(len(DNA)):
            indx = random.randrange(len(DNA[0])-k+1)
            Motifs.append(DNA[i][indx:indx+k])

    bestMotifs = Motifs.copy()
    bestScore = Score(bestMotifs)
    
    for i in range(N):
        i = random.randrange(t)
        Profile = createProfile(Motifs[:i]+Motifs[i+1:])
        Motifs[i] = random.choices([DNA[i][j:j+k] for j in range(len(DNA[i])-k+1)], weights=[Profile_value(DNA[i][j:j+k], Profile) for j in range(len(DNA[i])-k+1)])[0]
    
        currScore = Score(Motifs)
        if currScore < bestScore:
            bestMotifs = Motifs
            bestScore = currScore
    print(bestScore)
    return bestMotifs
                       
if __name__ == "__main__":
    file = open("./rosalind_ba2g.txt").read().split("\n")
    k, t, N = file[0].split(" ")
    DNA = file[1:-1]
    for motif in GibbsSampler(DNA, int(k), int(t), int(N)):
        print(motif)

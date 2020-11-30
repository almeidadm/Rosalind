alphabet = {0:'A', 1:'C', 2:'G', 3:'T'}
inv_alphabet = {'A':0, "C":1, "G":2, "T":3}
import numpy as np

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

def GreedyMotifSearch(DNA, k, t):
    bestMotifs = [strand[:k] for strand in DNA]
    bestScore = Score(bestMotifs)
    for i in range(len(DNA[0])-k+1):
        motif = [DNA[0][i:i+k]]
        for j in range(1, len(DNA)):
            profileMatrix = createProfile(motif)
            j_motif = ProfileMostProbableKmer(profile=profileMatrix, k=k, Text=DNA[j])
            motif.append(j_motif)
        currScore = Score(motif)
        if currScore < bestScore:
            bestMotifs = motif
            bestScore = currScore
    return bestMotifs



if __name__ == "__main__":
    file = open("./rosalind_ba2e.txt").read().split("\n")
    k, t = file[0].split(" ")
    DNA = file[1:-1]
    for motif in GreedyMotifSearch(DNA, int(k), int(t)):
        print(motif)


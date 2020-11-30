def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


def FrequentWords(Text, k):
    FrequentPatterns = list()
    Count = dict()
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[str(i)] = PatternCount(Text, Pattern)
    
    maxCount = max(Count.values())
    
    for i in range(len(Text)-k+1):
        if Count[str(i)] == maxCount:
            FrequentPatterns.append(Text[i: i+k])
    FrequentPatterns = list(dict.fromkeys(FrequentPatterns))
    return FrequentPatterns
    
if __name__ == "__main__":
	file = open("rosalind_ba1b.txt", "r").read().split("\n")
	Text, k = file[0], int(file[1])    
	for i in FrequentWords(Text, k):
	    print(i, end=" ")


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

if __name__ == "__main__":
	file = open("/home/diego/Documentos/BCC/Algoritmos em Bioinformática/Rosalind/rosalind_ba1a.txt", "r").read().split("\n")
	Text, Pattern = file[0], file[1]
	print(PatternCount(Text, Pattern))

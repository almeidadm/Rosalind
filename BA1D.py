
def PatternMatching(Pattern, Genome):
	k = len(Pattern)
	Match_indx = list()
	for i in range(len(Genome)-k+1):
    	if Genome[i:i+k] == Pattern:
    		Match_indx.append(i)
	return Match_indx
    
if __name__ == "__main__":
	Pattern, Genome, _ = open("rosalind_ba1d.txt", "r").read().split("\n")
	for match in PatternMatching(Pattern, Genome):
    	print(match,end=" ")
   	

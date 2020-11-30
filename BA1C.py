complement = {"A":"T", "C":"G", "G":"C", "T":"A"}

def ReverseComplement(Pattern):
    rc = ""
    for nucleotide in Pattern:
        rc += complement[nucleotide]
    return rc[::-1]
    
if __name__ == "__main__":
	Text = open("rosalind_ba1c.txt", "r").read()[:-1]
	print(ReverseComplement(Text))


def LCS(A, B):
	
	dp = [[0 for i in range(len(A)+1)]for j in range(len(B)+1)]
	for i in range(len(B)+1):
		for j in range(len(A)+1):
			if i== 0 or j == 0:	dp[i][j] = 0
			elif B[i-1] == A[j-1]:	dp[i][j] = dp[i-1][j-1] + 1
			else:	dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	lcs = ''
	i = len(B)
	j = len(A)
	while i > 0 and j > 0:
		if B[i-1] == A[j-1]:
			lcs += B[i-1]
			i -= 1
			j -= 1
		elif dp[i-1][j] > dp[i][j-1]:	i -= 1
		else: j -= 1

	print(A+B-lcs[::-1])
	return print(lcs[::-1])

if __name__ == '__main__':
	arq = open('FindingaSharedSplicedMotif.txt', 'r')
	arq = arq.read()
	arq = arq[1:-1].split('>')
	for i in range(len(arq)):
		j = arq[i].find('\n')
		arq[i] = arq[i][j:].replace('\n', '')
	
	if len(arq[0]) > len(arq[1]):		
		LCS(arq[0], arq[1])
	else:	LCS(arq[1], arq[0])
		

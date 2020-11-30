
def SCS(A, B):
	dp = [[0 for i in range(len(B)+1)]for j in range(len(A)+1)]

	for i in range(len(A)+1):
		for j in range(len(B)+1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif A[i-1] == B[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
	
	i = len(A)
	j = len(B)
	scs = ''
	while i > 0 and j > 0:
		if A[i-1] == B[j-1]:
			scs += A[i-1]
			i -= 1
			j -= 1
		elif dp[i-1][j] > dp[i][j-1]:
			scs += B[j-1]
			j -= 1
		else:
			scs += A[i-1]
			i -= 1

	while i > 0:
		scs += A[i-1]
		i -= 1
	while j > 0:
		scs += B[j-1]
		j -= 1

	print(scs[::-1])
				

if __name__ == '__main__':
	arq = open('InterleavingTwoMotifs.txt', 'r')
	arq = arq.read()
	arq = arq[:-1].split('\n')
	SCS('ATTTTTG','GTTTTTA' )

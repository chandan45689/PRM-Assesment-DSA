# Given a string str, your task is to write a program which takes a string str as its only input and
# returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could
# be formed from the string str

def countPS(str):

	N = len(str)
	cps = [[0 for i in range(N + 2)] for j in range(N + 2)]
	for i in range(N):
		cps[i][i] = 1

	for L in range(2, N + 1):

		for i in range(N):
			k = L + i - 1
			if (k < N):
				if (str[i] == str[k]):
					cps[i][k] = (cps[i][k - 1] +
								cps[i + 1][k] + 1)
				else:
					cps[i][k] = (cps[i][k - 1] +
								cps[i + 1][k] -
								cps[i + 1][k - 1])

	return cps[0][N - 1]

str = 'abcdef'
print("Total palindromic subsequence are : ", countPS(str))


















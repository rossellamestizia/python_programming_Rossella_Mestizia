#NW
seq1 = "ACTGCATTACGT"
seq2 = "ATGCGCCAG"

def prettyMatrix(matrix):
	for i in matrix:
		print(i)

match = 2
mismatch =  -1
gap = -1

r = len(seq1) + 1
c = len(seq2) + 1

score_matrix =[[0 for col in range(c)] for row in range(r)]
traceback_matrix = [['0' for col in range(c)] for row in range(r)]

for i in range(0, c):
	score_matrix[0][i] = gap *i 
for j in range(0, r):
	score_matrix[j][0] = gap *j

max_score = 0
max_position = None
for j in range(1, c):
	for i in range(1, r):
		if seq1[i-1] == seq2[j-1]:
			diag_score = score_matrix[i-1][j-1] + match
		else:
			diag_score = score_matrix[i-1][j-1] + mismatch

		up_score = score_matrix[i-1][j] + gap		
		left_score = score_matrix[i][j-1] + gap
		
		
		scores = [diag_score, left_score, up_score]
		score_matrix[i][j] = max(scores)

	
		if max(scores) == diag_score:
			traceback_matrix[i][j] = 'D'
		elif max(scores) == left_score:
			traceback_matrix[i][j] = 'L'
		else:
			traceback_matrix[i][j] = 'U'

prettyMatrix(score_matrix)
prettyMatrix(traceback_matrix)

col = len(seq2)
row = len(seq1)

s1 = ''
s2 = ''

while col > 0 and row > 0:
	if traceback_matrix[row][col] =='D':
		s1 += seq1[row-1]
		s2 += seq2[col-1]
		row -= 1
		col -= 1
	elif traceback_matrix[row][col] == 'L':
		s1 += '-'
		s2 += seq2[col-1]
		col -=1
	else:
		s1 += seq1[row-1]
		s2 += '-'
		row -= 1
print(s1[::-1])
print(s2[::-1])


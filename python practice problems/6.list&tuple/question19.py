#WAP to transpose two matrices.
rows = int(input("Enter matrix rows: "))
cols = int(input("Enter matrix columns: "))
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter elements for row {i+1} (space separated): ").split()))
    matrix.append(row)

print("Original matrix:")
for row in matrix:
    print(row)

# Transpose the matrix
transpose = []
for i in range(cols):
    trans_row = []
    for j in range(rows):
        trans_row.append(matrix[j][i])
    transpose.append(trans_row)

print("Transpose matrix:")
for row in transpose:
    print(row)

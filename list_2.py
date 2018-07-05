##################################################
# list의 조금 어려운 로직
# 복잡한 로직을 python에서 쉽게 구현할 수 있는 list 
#
#
###################################################

# lambda 이용
squares = list(map(lambda x:x**2, range(10)))
print(squares)

new_squares = [x**2 for x in range(10)]
print(new_squares)


# col 부분으로 추출 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print([[row[i] for row in matrix]  for i in range(4)])

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)


#zip 함수 활용해서 쉽게 해결
print( list(zip(*matrix)) )
##################################################
# 2차원 리스트 사용하는 방법
# - 사용자로부터 리스트의 크기를 입력받는다.
# - 입력받은 리스트의 크기를 이용하여 2차원 리스트를 작성하고 0, 1 중 임의의 수를 세팅한다.
# - 2차원 리스트를 출력한다.
# - 변경할 matrix의 좌표와 값을 입력받고 값을 변경하고 출력한다.
###################################################


import random
import sys
import os
import pygame as pg 
from time import sleep
matrix = []


def display_matrix():
    for r in matrix:
        print(r)


rows = int( input("매트릭스의 크기를 입력하시오>>"))
print("랜덤한 매트릭스 {}X{}를 작성하고 있습니다.".format(rows, rows))
print()
sleep(1)

for i in range(rows):
    onerow = []
    for j in range(rows):
        onerow.append( random.choice([0,1]) )
    matrix.append(onerow)
    onerow = []     # 배열을 초기화해야 합니다. 

display_matrix()


running = True

while running:
    x, y = input("변경할 좌표를 입력하시오(x, y)>>").split(',')
    x = int(x)
    y = int(y)
    # x, y = map(int, input("").split()) #형변환과 입력값 분할을 동시에 할 경우 map() 사용함.
    val = input("값을 입력하시오>>")
    val = int(val)

    matrix[y][x] = val

    display_matrix()

    ans = input("계속할까요?(y/n)>>").lower()
    running = False if ans == 'n' else True


##################################################
# 2차원 리스트 사용하는 방법
# - 사용자로부터 리스트의 크기를 입력받는다.
# - 입력받은 리스트의 크기를 이용하여 2차원 리스트를 작성하고 0, 1 중 임의의 수를 세팅한다.
# - 2차원 리스트를 출력한다.
###################################################


import random
import sys
import os
import pygame as pg 
from time import sleep

matrix = []
#onerow = []

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


for r in matrix:
    print(r)


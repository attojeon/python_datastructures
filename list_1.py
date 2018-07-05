##################################################
# 2차원 배열 사용하는 방법
###################################################


import random
import sys
import os
import pygame as pg 

matrix = []
onerow = []
row = 10

for i in range(row):
    onerow.clear()
    for j in range(row):
        onerow.append( random.choice([0,1]) )
    matrix.append(onerow)
    onerow = []     # 배열을 초기화해야 합니다. 

for i in range(row):
    print(matrix[i])



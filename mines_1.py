##################################################
# 지뢰찾기 게임 작성 1
# - 랜덤하게 matrix에 지뢰 심기
# - 지뢰의 위치를 알려주는 힌트 연산하기
# matrix 출력하기
###################################################


import random
import sys
import os
import pygame as pg 
from time import sleep
matrix = []
mines = 20
rows = 0
cols = 0
mine_flag = 9


def display_matrix():
    for r in matrix:
        print(r)
    print()


def init_matrix():
    global rows, cols
    rows = int( input("매트릭스의 크기를 입력하시오>>"))
    cols = rows  # 임시로 같게 만듬.
    print("랜덤한 매트릭스 {}X{}를 작성하고 있습니다.".format(rows, cols))
    print()
    sleep(1)

    for i in range(rows):
        onerow = []
        for j in range(cols):
            onerow.append(0)
        matrix.append(onerow)


def place_mines():
    placed = 0
    # ...
    display_matrix()


def mine_pos(y, x):
    # matrix[y][x]에 지뢰가 있으면 1, 없으면 0을 리턴함.

def mines_near(y, x):
    m = 0
    # 8방향에 지뢰를 추적하여 지뢰의 갯수 m을 늘려간다.
    # 위 mine_pos(y, x)를 활용한다.
    return m

    

def calc_hints():
    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] != mine_flag :
                matrix[y][x] = mines_near(y, x)
    display_matrix()


def main():
    init_matrix()
    place_mines()
    print("Calculationg mines...")
    print("Wait for seconds...")
    calc_hints()


if __name__ == "__main__":
    main()

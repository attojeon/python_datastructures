##################################################
# 지뢰찾기 게임 작성 2
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
    while placed < mines:
        #x, y = map(int, input('지뢰를 설치할 좌표를 입력하시오>>').split(',')) #형변환과 입력값 분할을 동시에 할 경우 map() 사용함.
        rx = random.randint(0, cols-1)
        ry = random.randint(0, rows-1)
        if matrix[ry][rx] != mine_flag:
            matrix[ry][rx] = mine_flag
            placed += 1

    display_matrix()


def mine_pos(y, x):
    if y >= 0 and y < rows and x >= 0 and x < cols and matrix[y][x] == mine_flag :
        return 1
    return 0

def mines_near(y, x):
    m = 0
    m += mine_pos(y-1, x-1) #NW
    m += mine_pos(y-1, x)   #N
    m += mine_pos(y-1, x+1) #NE
    m += mine_pos(y, x-1)   #W
    m += mine_pos(y, x+1)   #E
    m += mine_pos(y+1, x-1) #SW
    m += mine_pos(y+1, x)   #S
    m += mine_pos(y+1, x+1) #SE

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

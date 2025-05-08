#!/usr/bin/python3

def create_board():
    return [["." for _ in range(8)] for _ in range(8)]

def print_board(board):
        for row in board:
            print("".join(row))
        print()

def mark_move(board, moves):
    for x, y in moves:
        if 0 <= x < 8 and 0<= y < 8:
            board[x][y]= 'z'
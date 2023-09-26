
# 업&다운 게임
from random import randint  # 랜덤 숫자

print("Welcome to python Casino")
pc_choice = randint(1, 100)  # 랜덤 숫자 범위

playing = True

while playing:
    user_choice = int(input("choose number(1-100):"))

    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Down!")
    elif user_choice < pc_choice:
        print("Up!")

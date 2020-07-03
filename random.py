print('             我等着你的挑战哦           ')
import random

while True:
    a = input("石头/布/剪刀:")
    b = ["剪刀", "石头", "布"]
    win_list = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    mac = random.choice(b)
    print("你出拳：", a)
    print("计算机出拳：", mac)

    if a == mac:
        print("平局")

    elif [a, mac] in win_list:
        print("恭喜，你赢了")
    else:
        print("很遗憾，你输了")
        break

print("游戏结束")

print('game over')


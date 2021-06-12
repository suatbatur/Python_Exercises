import random
import time
from threading import Thread

def coord_func(i, j, liste):
    if i < 10 and j < 10:
        liste.append("0" + str(i) + "0" + str(j))
    elif i < 10 and j >= 10:
        liste.append("0" + str(i) + str(j))
    elif i >= 10 and j < 10:
        liste.append(str(i) + "0" + str(j))
    elif i >= 10 and j >= 10:
        liste.append(str(i) + str(j))

coord_list = []  # random yem atamak için koordinat listesi
for i in range(15):
    for j in range(15):
        coord_func(i, j, coord_list)
index = None
def bait_assign():  # yem atama fonksiyonu
    global index
    a = 1
    while a == 1:
        index = random.choice(coord_list)
        if map_list[int(index[:2])][int(index[2:])] == None:
            map_list[int(index[:2])][int(index[2:])] = "o"
            a = 2
        elif map_list[int(index[:2])][int(index[2:])] == "█":
            pass

c = 2

def map_snake():  # harita display fonksiyonu
    global map_list
    map_list = []  # map in ilk database'i
    icliste = []
    for i in range(15):
        for j in range(15):
            icliste.append(None)
        map_list.append(icliste)
        icliste = []

    for i in snakelist:                         # snakein database'e işlenmesi
        map_list[int(i[:2])][int(i[2:])] = "█"

    if c == 1:                                  # yem yenildiyse yem ata yenmediyse eski yemi ata
        map_list[int(index[:2])][int(index[2:])] = "o"
    elif c == 2:
        bait_assign()

    # while t < 15:
    #     if "o" not in map_list[t]:
    #         if t == 14:
    #             bait_assign()
    #     elif "o" in map_list[t]:
    #         break
    #     t += 1
    print(32 * "═")
    for i in map_list:
        print("║", end="")
        for j in i:
            if j == None:
                print(" ", end=" ")
            elif j == "█":
                print("█", end="█")
            elif j == "o":
                print("o", end=" ")
        print("║")
    print(32 * "═")

snakelist = ["0000", "0001", "0002", "0003", "0004", "0005"]  # ilk snake assign
fault = 0

def check():
    global way
    while True:
        time.sleep(1)
        if way == None:
            break
        else:
            break
        time.sleep(1)

i = 0
j = 5
fault = 0
while fault == 0:
    way = None
    map_snake()
    Thread(target=check).start()
    way = input("Input something: ")
    if i == 15 or i == -1 or j == 15 or j == -1:
        print("patladın")
        break
    elif way == "6":
        if j == 14:
            fault = 1
            print("patladın")
        elif map_list[i][j + 1] == None:
            coord_func(i, j + 1, snakelist)
            snakelist.pop(0)
            j += 1
        elif map_list[i][j + 1] == "o":
            coord_func(i, j + 1, snakelist)
            j += 1
        elif map_list[i][j + 1] == "█":
            fault = 1
            print("patladın")
    elif way == "8":
        if i == 0:
            fault = 1
            print("patladın")
        elif map_list[i - 1][j] == None:
            coord_func(i - 1, j, snakelist)
            snakelist.pop(0)
            i -= 1
        elif map_list[i - 1][j] == "o":
            coord_func(i - 1, j, snakelist)
            i -= 1
        elif map_list[i - 1][j] == "█":
            fault = 1
            print("patladın")
    elif way == "4":
        if j == 0:
            fault = 1
            print("patladın")
        elif map_list[i][j - 1] == None:
            coord_func(i, j - 1, snakelist)
            snakelist.pop(0)
            j -= 1
        elif map_list[i][j - 1] == "o":
            coord_func(i, j - 1, snakelist)
            j -= 1
        elif map_list[i][j - 1] == "█":
            fault = 1
            print("patladın")
    elif way == "2":
        if i == 15:
            fault = 1
            print("patladın")
        elif map_list[i + 1][j] == None:
            coord_func(i + 1, j, snakelist)
            snakelist.pop(0)
            i += 1
        elif map_list[i + 1][j] == "o":
            coord_func(i + 1, j, snakelist)
            i += 1
        elif map_list[i + 1][j] == "█":
            fault = 1
            print("patladın")
    if snakelist[-1] == index:
        c = 2
    else:
        c = 1
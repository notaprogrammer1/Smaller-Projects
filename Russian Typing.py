# -*- coding: UTF-8 -*-
import time
import random

alphabetFull = ["Ёё" ,"Йй", "Цц", "Уу", "Кк", "Ее", "Нн", "Гг", "Шш", "Щщ", "Зз", "Хх", "Ъъ", "Фф", "Ыы", "Вв", "Аа", "Пп",
            "Рр","Оо","Лл","Дд","Жж","Ээ","Яя","Чч","Сс","Мм","Ии","Тт","Ьь","Бб","Юю"]

level1 = ["Аа","Кк","Мм","Тт","Оо"]
level2 = level1 + ["Ее","Нн","Вв","Рр"]
level3 = level2 + ["Сс","Уу","Хх","Яя","Ии"]
level4 = level3 + ["Ёё","Йй","Цц","Чч","Гг","Шш"]
level5 = level4 + ["Ъъ","Фф","Ыы","Пп","Лл","Дд"]
level6 = level5 + ["Ээ","Ьь","Бб","Юю","Жж","Зз","Щщ"]



level = ''
check = []
streak = False
streakD = ''
streakTlist = [4,5.4,6.7,8,9.4]

def rando(level):
  return random.choice(level)

def populate(length):
    while len(check) < length:
        x = rando(level)
        if x not in check:
            check.append(x)

while True:
    com = input("Select your difficulty level (1-6):\n")
    if com == "1":
        level = level1
    elif com == "2":
        level = level2
    elif com == "3":
        level = level3
    elif com == "4":
        level = level4
    elif com == "5":
        level = level5
    elif com == "6":
        level = level6
    else:
        print("Select 1, 2, 3, 4, 5 or 6.\n")
    while True:
        com = input("Select your word length: (3-7, or back)\n")
        if com == "back":
            break
        if com == "3" or com == "4" or com == "5" or com == "6" or com == "7":
            streakNumber = 0
            if com == "3":
                streakTimer = streakTlist[0]
            elif com == "4":
                streakTimer = streakTlist[1]
            elif com == "5":
                streakTimer = streakTlist[2]
            elif com == "6":
                streakTimer = streakTlist[3]
            elif com == "7":
                streakTimer = streakTlist[4]
            else:
                pass
            while True:

                populate(int(com))
                newCheck = "".join(check)
                ctime = time.time()
                checkInput = input("Type the letters shown or type back to exit: "+str(check)+"\n")
                ntime = time.time() - ctime
                print("-"*45,"{0:.2f}".format(ntime))

                if checkInput == "back":
                    break
                test = checkInput.split()
                score = 0
                for i in newCheck:
                    for j in test:
                        if i in j:
                            score += 1
                            break
                if ntime < streakTimer and str(score) == str(com):
                    streak = True
                    streakNumber += 1
                else:
                    streak = False
                    streakNumber = 0
                print("-"*45,str(score)+"/"+str(com))
                if streak:
                    print("-"*45,"Streak of",streakNumber,"!!!")
                check = []
        else:
            print("Your choices are 3, 4, 5, 6, 7 or back.")
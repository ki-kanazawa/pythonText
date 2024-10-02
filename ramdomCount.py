import random

def guess_number():
    number = random.randint(1,100)
    attemps = 0
    while True :
        guess = int(input("数字を入力してください："))
        attemps +=1
        if number < guess:
           print("大きいです。")
        elif number > guess:
            print("小さいです。")
        else :
            print(f"おめでとう。{attemps}回で当たりました。")
            break
guess_number()
        
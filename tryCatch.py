try:
    num1 = float(input("数字1を入力してください："))
    num2 = float(input("数字2を入力してください："))
    result = num1 / num2
    print(f"結果は：{result}")
except ZeroDivisionError:
    print("除数は0できません")
except ValueError:
    print("数字以外は入力できません。")
weight = float(input("体重を入力ください:"))
height = float(input("身長を入力してください："))
bmi = weight / (height ** 2)
print(f"BMIは{bmi:.2f}です")
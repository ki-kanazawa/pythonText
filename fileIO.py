with open("test/test.txt","w") as file:
    content = input("内容を入力してください：")
    file.write(content)


with open("test/test.txt" , "r") as file:
    print("ファイル内容は：")
    print(file.read())
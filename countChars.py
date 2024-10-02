def count_chars (s):
    letters,digits,others = 0, 0, 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else :
            others += 1
    return letters,digits,others

s = input("テキストを入力してください：")
letters,digits,others = count_chars(s)
print(f"アルファベット：{letters}、数字：{digits}、その他：{others}")
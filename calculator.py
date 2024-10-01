def calculator():
    try:
        num1 = float(input("输入第一个数字:　"))
        operetor = input("输入运算符: ")
        num2 = float(input("输入第二个数字·: "))

        if operetor == "+":
            result = num1 + num2
        elif operetor == "-":
            result = num1 - num2
        elif operetor == "*":
            result = num1 * num2
        elif operetor == "/":
            if num2 == 0:
                return "除数不能为0"
            result = num1 /num2
        else:
            return "无效运算符"
        
        return f"结果是：{result}"
    except ValueError:
        return "请输入正确数字"
    
if __name__ == "__main__":
    print(calculator())



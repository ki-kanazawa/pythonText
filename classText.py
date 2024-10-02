class Person:
    def __init__(self, name ,age) -> None:
        self.name = name
        self.age = age

    def introduce(self):
        print(f"私の名前は{self.name}です。今年は{self.age}歳です。")

person1 = Person("太郎", 20)
person1.introduce()
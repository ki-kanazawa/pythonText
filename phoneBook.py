class phone_book:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self,name , phone):
        self.contacts[name] = phone
        print(f'連絡先:{name},電話番号：{phone}')
    def remove_contact(self , name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'連絡先{name}は削除しました。')
        else :
            print('連絡先ありません。')

    def find_contact(self, name):
        return self.contacts.get(name , '連絡先が存在しません')
    
    def diplay_contacts(self ):
        if not self.contacts:
            print('電話番号存在しません。')
        else :
            for name,phone in self.contacts.items():
                print(f'{name}：{phone}')

phonebook = phone_book()
phonebook.add_contact('Alice' , '12345678')
phonebook.add_contact('Bob', '987654321')


phonebook.diplay_contacts()
phonebook.find_contact('Alice')

phonebook.remove_contact('Alice')
phonebook.add_contact('Mike','11223344')
phonebook.diplay_contacts()
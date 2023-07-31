class User:
    def __init__(self, username, mail, age, number):
        self.username=username
        self.mail=mail
        self.age=age
        self.number=number
    def change_username(self,new_username):
        self.username=new_username
    def change_number(self, new_number):
        self.number=new_number
    def change_mail(self, new_mail):
        self.mail=new_mail
user1=User(username='pavel', mail='pavel@.mail.ru', age=26, number='+998998001010')
while True:
    print('---------------------------------', '\n''1-изменит имя ползователя', '\n''2-изменит телефон номер ползователя',
          '\n''3-изменит почту ползователя', '\n''4-показат данные ползователя')
    operator=int(input('выбирайте: '))
    if operator==1:
        user1.change_username(input('новая имя ползователя: '))
    elif operator==2:
        user1.change_number(input('новый номер ползователя: '))
    elif operator==3:
        user1.change_mail(input('новый почта ползователя: '))
    elif operator==4:
        print(user1.__dict__)
    else:
        print('выбран не правилный команда')
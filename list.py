#первый пример

list_1=['pavel','jhon','richard','samanta']
first=[i.capitalize() for i in list_1 if 'a' in i]
print(first)

#второй пример

list_2=['pavel ','jhon ','richard ','samanta ']
second=[i*2 for i in list_2]
print(second)

#третий пример

list_3=['pavel','jhon','richard','samanta']
theerth=[]
a=[theerth.append(i) for i in list_3 if i[1]=='a']
print(theerth)

#четвертый пример

list_4= range(1,50)
fourth=[]
a=[fourth.append(i) for i in list_4 if i %2==0]
print(fourth)

#пятый пример

list_5= range(1,50)
fiveth=[i for i in list_5 if i %3==0]
print(fiveth)

#шестой пример

list_6=range(1,50)
sixth=[(i+i) for i in list_6 if i %3==0]
print(sixth)

#седмой пример

list_7=range(1,51)
seventh=[]
a=[seventh.append(i) for i in list_7]
print(seventh[::-1])
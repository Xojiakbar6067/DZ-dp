print('1-вичеслит обёма 0.25','\n''2-вичеслит обёма 0.50','\n''3-вичеслит обёма 1.00','\n''4-вичеслит обёма 1.50','\n''5-вичеслит обёма 2.00')
operator=int(input('выбирите: '))
price1=0.10
price2=0.25
allprice=[]
if operator==1:
    tara_025=int(input('количество 0.25л: '))
    allprice=tara_025*price1
    b='%.2f' % allprice
    print(f'${b}')
elif operator==2:
    tara_050=int(input('количество 0.50л: '))
    allprice=tara_050*price1
    b='%.2f' % allprice
    print(f'${b}')
elif operator==3:
    tara_100=int(input('количество 1.00л: '))
    allprice=tara_100*price1
    b='%.2f' % allprice
    print(f'${b}')
elif operator==4:
    tara_150=int(input('количество 1.50л: '))
    allprice=tara_150*price2
    b='%.2f' % allprice
    print(f'${b}')
elif operator==5:
    tara_200=int(input('количество 2.00л: '))
    allprice=tara_200*price2
    b='%.2f' % allprice
    print(f'${b}')
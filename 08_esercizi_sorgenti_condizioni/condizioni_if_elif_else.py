domanda1 = (input('Inserire S per procedere N per sospendere'))
if domanda1 ==' S':
    domanda2 = int(input('indicare età: '))
    if domanda2 >= 65:
        print('Sei anziano') 
    elif domanda2 >= 18 :
        print ('sei adulto')
    else:
        print ('Sei minorenne')
else:
    print('sessione terminata')
    
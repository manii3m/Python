name = input('Enter your name : ')

if (len(name) < 10 ):
    print('Yes less than 10 char')
elif ( ' ' in name ):
    print('Not Valid, Only Single word ')
else:
    print('Yes more than 10')
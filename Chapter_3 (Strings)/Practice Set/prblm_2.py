#write a program to fill in a letter template given below with name and date

# letter = input('Type of Letter = ')
# rname =  input('Enter Reciever Name = ')
# date = input('Enter Date (in format DD/MM/YYYY) = ')

# print(f'Letter :  {letter}')
# print('You\' are selected ! ')
# print(f'\tDear {rname}')
# print('\t',date)


print('')

leter = '''Dear <|Name|> ,
            You are selected !
            <|Date|>'''

print(leter.replace('<|Name|>','Mayank').replace('<|Date|>','14/4/26'))
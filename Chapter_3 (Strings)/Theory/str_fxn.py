name = 'Mayank'
print('checking last and first words')
print(len(name))
print(name.endswith('k')) #check the ending of the string
print(name.startswith('m')) #check the starting of string
print(name.capitalize()) #capital the first word

print('')
print('making upper or lower case')
print('')

print(name.lower())  # mayank  
print(name.upper())  # MAYANK

print('')
print('removing spaces , left , right')
print('')

name_s = '  MANI   '
print(name_s.strip())
print(name_s.lstrip())
print(name_s.rstrip())

print('')
print('replacing word')
print('')

text = 'I still love her'
print(text.replace('still','actually'))

print('')
print('Spliting each word')
print('')

print(text.split())
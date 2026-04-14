name = "Mani with 2 qoute"
name_a = 'Mani with 1 qoute'
name_b = '''Mani with 3 quote'''

print(name_a)
print(name)
print(name_b)

alphabets = 'abcdefghijklmnopqrstuvwxyz'
namelength = alphabets[0:10]
# include from index 0 to 10
# starts from index 0 and print upto 9 not 10th one
print(namelength)
character1 = alphabets[12]
print('Character No. 12 is ',character1)

alpha = 'vishwakarma'
print(alpha[-7:-1])

# [:] represent the [ 0 : length-1 ]
# [:7] represent the [ 0 : 7 ]
# [2:] represent the [ 2 : lenght-1 ]

queue = 'abcdefghijklmnopqrstuvwxyz'
ab = queue[1:5:3] # this means range of 1 to 5(upto 4) and then 3 between 1-4
print(ab)
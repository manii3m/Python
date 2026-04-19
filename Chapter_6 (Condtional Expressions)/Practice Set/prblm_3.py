c1 = 'Make a lot of Money'
c2 = 'Buy Now'
c3 = 'Subscribe this'
c4 = 'click this'

comment = input('Enter Your Comment :')

if ((c1 in comment) or (c2 in comment) or (c3 in comment) or (c4 in comment)):
    print('It is a spam comment')
else:
    print('Not a Spam')
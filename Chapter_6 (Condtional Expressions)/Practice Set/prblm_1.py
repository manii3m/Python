s1 = int(input('Enter Number 1: '))
s2 = int(input('Enter Number 2: '))
s3 = int(input('Enter Number 3: '))
s4 = int(input('Enter Number 4: '))

if (s1 > s2 and s1 > s3  and s1 > s4 ):
    print('S1 is greatest Number :', s1)
elif (s2 > s1 and s2 > s3  and s2 > s4 ):
    print('S2 is greatest Number :', s2)
elif (s3 > s2 and s3 > s1  and s3 > s4 ):
    print('S3 is greatest Number :', s3)
else:
    print('S4 is greatest Number :', s4)
print('End of Program')


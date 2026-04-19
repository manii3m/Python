english = int(input("Enter Marks of English : "))
math = int(input("Enter Marks of Math : "))
hindi = int(input("Enter Marks of Hindi : "))

total = (english+math+hindi) / 300
total_percentage = total * 100

if ( total_percentage >=40 and english >= 33 and hindi >= 33 and math >=33 ):
    print('Pass in this Year',total)
else:
    print('Try Next Year' ,'Total Percentage', total_percentage , 'here is your data given below')

if ( english >= 33 ):
    print("English : Pass")
else:
    print('English : Fail')
if ( math >= 33 ):
    print("Math : Pass")
else:
    print('Math : Fail')
if ( hindi >= 33 ):
    print("Hindi : Pass")
else:
    print('Hindi : Fail')

print('End of Program')
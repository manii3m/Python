friends = ['Apple', 'Orange', 5, 5.33, False, 'Akash']
print(friends)

friends.append('Mani')
print(friends)

sort = [1,3,4,2,44,12,8,6]
sort.sort() # sort in ascending order
print(sort)
sort.reverse() # sort in descending order
print(sort)
sort = [1,3,4,2,44,12,8,6]
sort.insert(3,42) #insert custom value at custom index (index, value)
sort.sort() # sort in ascending order

print(sort)
sort.pop(3) # remove the n'th index value
print(sort)
sort.remove(44)
print(sort)

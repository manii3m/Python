data = {
    'Name' : 'Mayank',
    'Age' : 29,
    'Sex' : 'Male',
    'Marks' : [13,12,22,25]
}
print(type(data))
print(data['Name'])
print(data)
print(data['Sex'])
print(data['Marks'])
print(data.items())
print(data.keys())
print(data.values())

data.update({'Name':'Mani'})
print(data)
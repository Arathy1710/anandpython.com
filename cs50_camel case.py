
x =input('enter a camel case string:')
result = ''
for char in x:
    if char is upper():
    result = result+'_'+char.lower()
else:
result =  result + char
print(result)


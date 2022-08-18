x =input('enter a camel case string:')
result = ''
for char in x:
    if char.upper():
        result = result+'_'+char.lower()
    else:
        result =  result + char
print(result)



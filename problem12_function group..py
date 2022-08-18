my_list = [1,2,3,4,5,6,7,8,9]
n = 4
final = [my_list[i:i+n]for i in range(0,len(my_list),n)]
print(final)

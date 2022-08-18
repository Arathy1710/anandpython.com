def sum(n):
    sm = 0
    cum_list =[]
    for i in n:
        sm =sm+i
        cum_list.append(sm)
    return cum_list
a = [10,20,30,40]
print(sum(a))


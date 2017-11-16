num = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}

def helper(x):
    print(x)
    if x in group:
        return (0,x)
    return (1,x)
num.sort(key=helper)
print(num)

#same as above
b = [(1,8),(0,3),(1,1),(0,2),(0,5),(1,4),(0,7),(1,6)]
b.sort()
b

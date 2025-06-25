def toggle(tup, val):
    if val != tup[0] and val not in tup:
        return tup[0]
    return tup[1]
    

x_val = (1,2)

x = 1

x = toggle(x_val, x)
print (x)


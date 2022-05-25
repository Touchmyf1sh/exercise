def yyds(a):
    for b in range(2,a):
        if a%b == 0:
            return False
    return True
list_new = []
for x in range(2,100):
    if yyds(x):
        list_new.append(x)
print(list_new)

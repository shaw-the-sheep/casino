def ty(par):
    if par == 1:
        return "only one"
    else:
        return "more than one", "this is the second"
    
def show(par):
    return list(ty(par))

print(show(1))
print(show(2))
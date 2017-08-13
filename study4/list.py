catNames = []
while True:
    print('please enter the name of cat. If you want to end, type enter')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('cat name is bellow')
for name in catNames:
    print(' '+ name)

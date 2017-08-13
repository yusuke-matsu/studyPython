## getfunc
items = {'apples':5 , 'books':2}
print(str(items.get('books',0)))
print(str(items.get('test',0)))

#setdefault

test = {'name':'alice','age':5}
# if 'color' not in test:
#     test['color'] = 'black'

test.setdefault('color','black')
print(test)

test.setdefault('color','white')
print(test)

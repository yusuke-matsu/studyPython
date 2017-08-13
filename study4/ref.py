import copy

def eggs(params):
    params.append('hello')

spam = [1,2,3]
eggs(spam)
print(spam)

strList = ['a','b','c','d']
copyList = copy.copy(strList)
copyList[1] = 42
print(strList)
print(copyList)

allGuests = {'alice': {'apple':5,'banana':6},
             'bob': {'lemon':10,'cup':5},
             'tom': {'test':5, 'hoge':10}
}

def totalBought(guests,items):
    num = 0
    for key, v in guests.items():
        print(key)
        print(v)
        num = num + v.get(items,0)
    return num

print('items number')
print('apple'+ str(totalBought(allGuests, 'apple')))
print('banana'+ str(totalBought(allGuests,'banana')))
print('lemon'+ str(totalBought(allGuests,'lemon')))
print('cup'+ str(totalBought(allGuests,'cup')))
print('test'+ str(totalBought(allGuests,'test')))
print('hoge'+ str(totalBought(allGuests,'hoge')))
print('ok'+ str(totalBought(allGuests,'ok')))

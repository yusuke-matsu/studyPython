birthdays = {'alice':'4/1','bob':'2/1', 'iva':'2/21'}

while True:
    print('please input the name. if you want to quite, please enter ')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + 'birthday is' + birthdays[name])
    else:
        print(name + 'birthday is not recorded')
        print('please input birthday')
        birthday = input()
        birthdays[name] = birthday
        print('update birthday!!!')

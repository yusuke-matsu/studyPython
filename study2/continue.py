while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('こんにちは')
    password = input()
    if password == 'test':
        break
print('OK')

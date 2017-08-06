def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1
#    else:
#        except  ZeroDivisionError:
#            print('no good')

print('please input number')
number = int(input())
if number == 0:
    print('elegal')
else:
    while number != 1:
        number = collatz(number)
        print(str(number))

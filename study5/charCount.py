import pprint

message = 'it was a bright cokd day in April , and the clocks were striking thirteen'

count={}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#print(count)
pprint.pprint(count)

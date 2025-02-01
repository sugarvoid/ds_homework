# David Durham
# Week 2
# Projects 4.1


from classes import Stack

stack = Stack(12)
#stack.pop()

for word in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']:
    stack.push(word)
print('After pushing', len(stack), 'words on the stack, it contains:\n', stack)
print('Is stack full?', stack.isFull())


stack.push("eleven")


print('Popping items off the stack:')
while not stack.isEmpty():
    print(stack.pop(), end=' ')
print()


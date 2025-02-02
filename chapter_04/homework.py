# David Durham
# Week 2
# Projects 4.1


from classes import Stack


# Pushing and popping within its index range
def test_1_pass() -> None:
    pass

# Popping from an empty stack
def test_2_fail() -> None:
    pass

# Pushing to a full stack
def test_3_fail() -> None:
    pass



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


if __name__ == "__main__":
    test_1_pass()
    # test_2_fail()
    # test_3_fail()

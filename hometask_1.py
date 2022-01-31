# import "random" module
import random

# declair the empty list
numbers = []
# for each of 100 item
for i in range(100):
    # append randomly generated item into the list - numbers; the range of random numbers is from 0-1000
    numbers.append(random.randint(0, 1000))
# print the new generated list on the screen
print(numbers)

# declair the empty list with sorted numbers
sorted_list = []
# when "numbers" list is empty, "while numbers:" will stop looping
while numbers:
    # let`s consider that min value in the list is the first item
    minimum = numbers[0]
    # for each item in "numbers"
    for x in numbers:
        # the check of each item if it is less than previously considered min
        if x < minimum:
            # new min value
            minimum = x
    # the first min from the whole list is appended; then second min...
    sorted_list.append(minimum)
    # remove the first min from the whole list; then second min...
    numbers.remove(minimum)

# print a sorted list on the screen
print(sorted_list)

# defining new variables and setting them to zero
evenSums = 0
oddSums = 0
evenCount = 0
oddCount = 0
# error handling block starts

# for each item in sorted_list
for x in sorted_list:
    # checking the item if it is odd or even
    if x % 2 == 0:
        # if even we increase respective variable
        evenSums += x
        evenCount += 1
    # if odd:
    else:
        # we increase variables (sum and count) for odd numbers
        oddSums += x
        oddCount += 1

try:
    # here we print out even average and odd average
    print("Even Average: " + str(evenSums / evenCount))
    print("Odd Average: " + str(oddSums / oddCount))
# the error handling block ends
except ZeroDivisionError as e:
    # if error handler will catch a mistake it will print it on the screen
    print(str(e))



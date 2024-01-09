numbers = [1, 2, 3, 4, 5]

print(numbers)
numbers.append(7)
print(numbers)
numbers.insert(5, 6)
print(numbers)

other_numbers = [8, 9, 10]
numbers.extend(other_numbers)
print(numbers)

numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]
other_list = numbers.copy()
print(other_list)
other_list.append(6)
print(other_list, numbers)

numbers.extend([2, 5, 9, 5])
print(numbers)
print(numbers.count(5))

print(numbers.index(5))
print(numbers.index(5, 5, 8))

print(numbers.pop(1))
print(numbers)

numbers.remove(5)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

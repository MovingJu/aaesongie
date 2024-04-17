'''
number = "1, 2, 3, 4"
number1 = number.split(',')
print(number1)

numbers = [5, 3, 8, 2, 9, 1]
max_number = max(numbers)
print("가장 큰 수는:", max_number)

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("중복을 제거한 숫자들:", unique_numbers)

number = [1, 2, 3, 4, 4, 3, 2, 1]
sortednumber = sorted(number)
number.sort()
print(sortednumber, '\n', number)

numbers = [1,2,3,4,5,6]
reversed = numbers[::-1]
print(reversed)

num1 = [1,2,3]
num2 = [4,5,6]
merged = num1 + num2
print(merged)
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)

print("----------------------------------------")

def is_pair(number:int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

pairs_filter = list(filter(is_pair, numbers))
print(pairs_filter)

filter(is_pair, numbers)
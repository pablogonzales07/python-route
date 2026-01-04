
def sum_with_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


result = sum_with_range(1, 10)
result_2 = sum_with_range(10, 30)
result_3 = sum_with_range(1, 100)

print(result, result_2, result_3)
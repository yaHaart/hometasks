numbers = [1, 2, 0, 2, 5, 0, 4, 2, 1, 0]
zero_count = numbers.count(0)
zip_numbers_with_0 = [x for x in numbers if x != 0]
for _ in range(zero_count):
    zip_numbers_with_0.append(0)
print(zip_numbers_with_0)
zip_numbers = zip_numbers_with_0[:len(zip_numbers_with_0) - zero_count]
print(zip_numbers)

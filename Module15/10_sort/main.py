base_list = [1, 4, -3, 0, 10, 12, 3, 4, 6, -4, 11, 5, 5]

sortList1 = sorted(base_list)
print('Встроенная сортировка ', sortList1)

# сортировка пузырьком

a = base_list
for j in range(1, len(a)):
    f = 0
    for i in range(len(a) - j):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            f = 1
    if f == 0:
        break
print('Сортировка пузырьком', a)

# сортировка перемешиванием
a = base_list

left = 0
right = len(a) - 1

while left <= right:
    for i in range(left, right, +1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    right -= 1

    for i in range(right, left, -1):
        if a[i - 1] > a[i]:
            a[i], a[i - 1] = a[i - 1], a[i]
    left += 1

print('Сортировка перемешиванием', a)

#  сортировка расческой
alist = base_list
alen = len(alist)
gap = (alen * 10 // 13) if alen > 1 else 0
while gap:
    if 8 < gap < 11:
        gap = 11
    swapped = False
    for i in range(alen - gap):
        if alist[i + gap] < alist[i]:
            alist[i], alist[i + gap] = alist[i + gap], alist[i]
            swapped = True
    gap = (gap * 10 // 13) or swapped

print('Сортировка расческой', alist)

# зачёт! 🚀

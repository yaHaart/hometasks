def q_sequence(n):
    q_list = []
    for j in range(n):
        if j < 2:
            q_list.append(1)
            yield 1
        else:
            q_list.append(q_list[j - q_list[j - 1]] + q_list[j - q_list[j - 2]])
            yield q_list[j - q_list[j - 1]] + q_list[j - q_list[j - 2]]


q = q_sequence(20)
for i in q:
    print(i, end=' ')

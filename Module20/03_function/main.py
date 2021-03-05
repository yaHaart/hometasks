
my_tuple = ('q', 'w', 'e', 'r', 't', 'a', 'c', 'e', 'c', 's')
char_to_count = 'e'
my_list = list(my_tuple)
# [f(x) if condition else g(x) for x in sequence]
new_list = [char if my_list.index(char_to_count) <= my_list.index(char) else
# new_list = [char for char in my_list
#             if my_list.index(char_to_count) <= my_list.index(char) <
#             my_list[my_list.index(char_to_count) + 1:].index(char_to_count) + 1 + my_list.index(char_to_count)]
print(new_list)

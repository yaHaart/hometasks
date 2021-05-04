
class Stack:

    def __init__(self):
        self.stack_list = list()

    def stack_add(self, new_element):
        self.stack_list.append(new_element)

    def stack_get(self):
        if len(self.stack_list) > 0:
            return self.stack_list.pop()
        else:
            raise IndexError('Очередь закончилась')


class TaskManager:
    def __init__(self):
        self.stack_list = list()

    def stack_add(self, task, priority):
        if str(priority).isdigit():
            self.stack_list.append([task, priority])
        else:
            raise ValueError('Приоритет всегда число!')

    def stack_get(self):
        if len(self.stack_list) > 0:
            return self.stack_list.pop()
        else:
            raise IndexError('Очередь закончилась')

    def manager(self):
        prioritized_task_dict = dict()
        for elem in self.stack_list:
            if elem[1] in prioritized_task_dict:
                prioritized_task_dict[elem[1]] += '; ' + elem[0]
            else:
                prioritized_task_dict[elem[1]] = elem[0]
        for i_key in sorted(prioritized_task_dict):
            print(i_key, prioritized_task_dict[i_key])


try:
    stack = Stack()
    stack.stack_add('a')
    stack.stack_add('b')
    stack.stack_add('c')
    print(stack.stack_get())
    print(stack.stack_get())
    print(stack.stack_get())

    task_manager = TaskManager()
    task_manager.stack_add("сделать уборку", 4)
    task_manager.stack_add("помыть посуду", 4)
    task_manager.stack_add("отдохнуть", 1)
    task_manager.stack_add("поесть", 2)
    task_manager.stack_add("сдать дз", 2)
    task_manager.manager()

except IndexError as ie:
    print(ie)
except ValueError as ve:
    print(ve)

# зачёт! 🚀

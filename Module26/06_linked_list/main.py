import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'LinkedList []'

    def append(self, x):
        self.length+=1
        if self.first is None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def delete(self, i):
        if self.first is None:
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr is not None:
            if count == i:
              if curr.next is None:
                self.last = curr
              old.next = curr.next
              break
            old = curr
            curr = curr.next
            count += 1

    def get(self, i):

        if 0 >= i or i > self.length:
            return None
        else:
            curr = self.first
            count = 0
            if i == 0:
                return self.first.value
            while curr is not None:
                if count == i:
                    return curr.value

                curr = curr.next
                count += 1
        return None


ranked_list=LinkedList()
for i in range(10):
    ranked_list.append(random.randint(0, 10))
ranked_list.append('a')
print(ranked_list)
print()

ranked_list.delete(0)
print(ranked_list)
print(ranked_list.get(3))

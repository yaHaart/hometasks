class MyDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


dict1 = dict()
dict2 = MyDict()

dict1[1] = 'a'
dict2[1] = 'a'

print(dict1.get(1))
print(dict2.get(1))

print(dict1.get(2))
print(dict2.get(2))

# зачёт! 🚀

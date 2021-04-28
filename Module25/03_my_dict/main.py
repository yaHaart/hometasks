class MyDict(dict):
    def setdefault(self, __key: _KT, __default: _VT = ...) -> _VT:

dict1 = MyDict()
dict2 = dict()

dict1[1] = 'мой словарь'
dict2[1] = 'обычный словарь'

print(dict2.get(1))
print(dict1.get(1))
print(dict2.get(2))
print(dict1.get(2))
print(dict1, dict2)
dict2.get()

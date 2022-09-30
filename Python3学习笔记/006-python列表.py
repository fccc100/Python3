'''
  列表 List
'''

import operator

list = ['Google', 'Apple', 1900, True]
print(list[1]) # Apple
print(list[-2]) # 1900

print(list[1:3]) # ['Apple', 1900]

# append(), 向列表末尾添加元素
list.append(100.2)
print(list) # ['Google', 'Apple', 1900, True, 100.2]

# del 删除列表元素
del list[2]
print(list) # ['Google', 'Apple', True, 100.2]

# + 连接列表
# * 重复列表
print(list + list) # ['Google', 'Apple', True, 100.2, 'Google', 'Apple', True, 100.2]
print(list * 3) # ['Google', 'Apple', True, 100.2, 'Google', 'Apple', True, 100.2, 'Google', 'Apple', True, 100.2]

# 列表比较
# import operator
l1 = [1, 2]
l2 = [2, 3]
l3 = [2, 3]
print(operator.__eq__(l1, l2)) # False
print(operator.__eq__(l2, l3)) # True

'''
  List Api
'''
list2 = [2, 3, 5, 23, 43, 12]
# len() 返回列表长度
print(len(list2)) # 6
# max() 返回列表最大值
print(max(list2)) # 43
# min 返回列表最小值
print(min(list2)) # 2

# list.append()
# list.count(obj) 返回某个元素在列表中出现的次数
print(list2.count(2)) # 1

# list.index(obj) 返回某个元素第一次出现的索引
print(list2.index(5)) # 2

# list.insert(index, obj) 在指定索引插入元素
list2.insert(2, 100)
print(list2) # [2, 3, 100, 5, 23, 43, 12]

# list.pop() 弹出最后一个元素

# list.remove() 删除列表中某个元素的第一个匹配项

# list.reverse() 反转列表元素

# list.sort() 排序

# list.clear() 清空列表

# list.copy() 复制列表
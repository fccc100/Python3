'''
  Python逻辑运算符
'''
a = True
b = False

# 与运算
if (a and b):
  print('True')
else:
  print('False')

# 或运算
if (a or b):
  print('True')
else :
  print('False')

# 非
if (not b):
  print('True')
else:
  print('False')

'''
  Python成员运算符
'''

# in
list = [1, 2, 3, 4]
print(1 in list) # True
print(5 in list) # False

# not in
print(5 not in list) # True
print(1 not in list) # False
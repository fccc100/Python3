from this import d

num = 100 # 整型变量
num1 = 1000.2 # 浮点型
name = 'mi' #字符串

# 同时赋值
a = b = c = 1

a, b, c = 3, 4, 'test'
print(a) # 3
print(b) # 4
print(c) # test

'''
  python3中有六个标准数据类型:
  Number      数字
  String      字符串
  List        列表
  Tuple       元组
  Set         集合
  Dictionary  字典

  其中不可变数据: Number String Tuple
  可变数据: List Dictionary Set
'''

'''
  1.Number
  支持int float bool complex
'''
# 内置type()函数查询变量类型
a, b, c, d = 20, 5.5, True, 'test'
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'bool'>
print(type(d)) # <class 'str'>

print(type(a) == int) # True
print(type(b) == float) # True
print(type(c) == bool) # True
print(type(d) == str) # True

# isinstance()判断类型
print(isinstance(a, int)) # True
print(isinstance(b, float)) # True
print(isinstance(c, bool)) # True
print(isinstance(d, str)) # True

# type() 和 isinstance() 的区别
# type() 不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型

'''
  bool 是 int 的子类, True == 1, false == 0, 但是可以通过 is 来判断类型
'''
print(issubclass(bool, int)) # True
print(True == 1) # True
print(False == 0) # True
print(0 is False) # False
print(1 is True) # False

# 运算符 除法
# / 得到浮点数
# // 得到整数
print(5 / 3) # 1.6666666666666667
print(5 // 3) # 1


'''
  String
  字符串的索引从前往后为0 1 2 3..., 从后往前为-1 -2 -3 -4...
'''
s = 'string'


'''
  List
'''

list = [1, '2']

'''
  Tuple
'''

tuple = (1, 2)

'''
  Set
'''

set = {'1', '2'}

'''
  Dictionary
'''

dict = {}
dict['one'] = 1
dict['two'] = 2
print(dict['two']) # 2

dict1 = {
  name: '1',
  id: 'id'
}
print(dict1[id]) # id
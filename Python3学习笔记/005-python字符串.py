'''
  python字符串
'''

s = 'hello world!'

# 字符串首字母大写
print(s.capitalize()) # Hello world!

# 返回指定字符串在原字符串中出现的次数
print(s.count('ll')) # 1

# 判断字符串是否以指定字符串结尾
print(s.endswith('d!')) # True

# 返回指定字符串在原字符串中第一次出现的索引
print(s.find('lo')) # 3

# 判断字符串是否只包含数字
print(s.isdigit()) # False

# islower() 是否全小写
# isupper() 是否全大写
# istitle() 是否每个单词首字母大写

# 返回字符串的长度
print(len(s))

# startswith()
# lower()
# upper()
# title()
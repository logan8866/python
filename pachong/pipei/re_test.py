import re

one = "abcdefg1234567nnnnngggg1234nnnn"
pattern = re.compile("g\d*n")
result = pattern.findall(one)
print(result)

two = """
maslhbkjfvhdsg12345nnn
ownqowuefqhroughg54321nniuhvia
qfbg123456
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
"""
pattern = re.compile("g(.*?)n",re.S|re.I)
result = pattern.findall(two)
print(result)

one = "abc123"
pattern = re.compile("\d")
result = pattern.match(one)
result_2 = pattern.search(two)
print(result_2.group())
result_3 = pattern.sub("#",one)
print(result_3)

one = "a1b2c4d5e"
pattern = re.compile("\d")
result = pattern.split(one)
print(result)

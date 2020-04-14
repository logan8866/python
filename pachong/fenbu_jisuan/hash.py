import hashlib
obj = hashlib.md5()
obj.update("hello hashlib".encode("utf8"))
result = obj.hexdigest()
print(result)

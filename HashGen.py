#Instance hash's size is like an 8
#00:1 00:2 00:3 00:4 | 00:5 00:6 00:7 00:8

from hashlib  import blake2b

def gethash(byte,size):
  hashgen = blake2b(byte,digest_size=size)
  return hashgen.hexdigest()
  
def string2hash(string,size):
  return gethash(string.encode(),size)

#example here
print("Example hash¥ngive me name")
gethas = input()
print(string2hash(gethas,8))

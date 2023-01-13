text = "nayeem@123"
sk="riyu"

b=''.join(str(ord(c)) for c in sk)
print(b)
a=''.join(str(ord(c)) for c in text)
print(a)
c=a+b
print(c)



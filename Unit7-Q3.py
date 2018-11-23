import re
QR="""
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""
q=re.compile("(\d{3}[-]\d{4})[-]\d{4}")

print(q.sub("\g<1>-####",QR))

s="""
kim,fail,fail
shin,pass,fail
"""
pat=re.compile("(\w{3,}[,]\w{4})[,](\w{4})")

print(pat.sub("\g<1>,pass",s))

pat.re.compile("fail$",re.MULTILINE)
print(pat.sub("pass",s))
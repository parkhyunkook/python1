import re
s="""
park 010-9999-9998
kim 010-9909-7789
lee 010-8789-7768
"""
q=re.compile("(\d{3}[-]\d{4})[-]\d{4}")

print(q.sub("\g<1>-####",s))


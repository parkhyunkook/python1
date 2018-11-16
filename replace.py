import sys

src=sys.argv[1]
obj=sys.argv[2]

f=open(src,'r')
txt=f.read()
a = txt.replace("\t","_"*4)
f.close()

f=open(obj,'w')
f.write(a)
f.close()

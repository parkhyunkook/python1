strinput = str(input("Input String"))

char=""
result = ([])
count = 0
for i in strinput:
    result.append(i)
for i in result:
    if char == i:
        count = count + 1
    else:  
        if count != 0:
            print(char,count)
            count = 1
        char = i
print(char, count) 
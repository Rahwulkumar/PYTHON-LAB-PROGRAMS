A = ['abc','xyz','aba',1221]

for index,item in enumerate(A):
    if isinstance(item,str):
        if item[0] == item[-1]:
            print(f"String: '{item}, Index:{index}")
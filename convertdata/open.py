import string
import os
original_files=os.listdir('./before')
for i in original_files:
    before='./before//'+i
    after='./afterdata//'+i
    with open(before,"r",encoding="utf-8") as f:
        with open(after,"w+",encoding="utf-8")as p:
            for line in f.readlines():
                k=line.split(" ")
                if len(k)>2:
                    print (k[2:])
                    p.write('/'.join(k[2:])+'\n')
            
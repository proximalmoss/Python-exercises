st=input("enter a sentence")
words=st.split(" ")
coding=True
if coding:
    nwords=[]
    for word in words:
        if len(word)>=3:
            r1="hnh"
            r2="nhk"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if len(word)>=3:
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
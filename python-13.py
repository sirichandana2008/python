word=input()
upper,lower,special=0,0,0
for ch in word:
    if ch.isalpha():
        if ch.isupper():
            upper+=1
        else:
            lower+=1
    else:
        special+=1
print("no of upper case letters",upper)
print("no of lower case letters",lower)
print("no of special cases",special)

word = input()
result = 0 
n = len(word)
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1 
 
print(result)

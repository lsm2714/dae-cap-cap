word = input()

word_list = []
for n in word :
    word_list.append(n)
kaka = word_list[-1::-1]
for i in kaka :
    print(i, end='')

# or 

jaja = input() 
print(jaja[::-1])


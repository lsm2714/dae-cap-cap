int_value = input()
int_list = int_value.split()
max_value = max(int_list)
print(max_value)

count = 0 
for i in int_list : 
    count += 1 
    if i == max_value :
        print(count - 1)
        break

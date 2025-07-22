int_value = int(input())

int_list = []

for val in range(1, int_value + 1) :
    print(val, end=' ')
    if val % 2 != 0 :
        int_list.append(val)
print() 
print(sum(int_list))
    
def max_number(num1, num2, num3, num4):
    max_num = -1
    for num in [num1, num2, num3, num4]:
        if num > max_num:
            max_num = num
            
    return max_num
    
def min_number(num1, num2, num3, num4):
    min_num = 10000000
    for num in [num1, num2, num3, num4]:
        if num < min_num:
            min_num = num

    return min_num

user_input1 = int(input())
user_input2 = int(input())
user_input3 = int(input())
user_input4 = int(input())

max_num = max_number(user_input1, user_input2, user_input3, user_input4)
min_num = min_number(user_input1, user_input2, user_input3, user_input4)

print(f"Maximum is {max_num}")
print(f"Minimum is {min_num}")

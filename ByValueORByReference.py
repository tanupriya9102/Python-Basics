# When you pass a list (a mutable object) to a function and modify its contents within the function, the changes will be reflected outside the function as well. This is known as passing by reference. On the other hand, when you pass an integer (an immutable object) to a function and modify it within the function, the changes won't be reflected outside the function. This is because integers are passed by value.


def modify_list(lst):
    lst[0] = 42

my_list = [0]
modify_list(my_list)
print(my_list)  # Output: [42]

def modify_integer(num):
    num = 42

my_num = 0
modify_integer(my_num)
print(my_num)  # Output: 0

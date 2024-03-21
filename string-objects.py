my_num = 5
my_str = "Hello"

f = ...
print(f)

# 1.
f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)

# 2.
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)

# 3.
f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)

# 4.
f = "my_num is {my_num}, and my_str is '{my_str}'.".format()

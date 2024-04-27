# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

#1 import make_sandwich
#2 from make_sandwich import make_sandwich
#3 from make_sandwich import make_sandwich as ms
#4 import make_sandwich as ms
from make_sandwich import *

#1 make_sandwich.make_sandwich('cheese', 'beef', 'egg')
#2 make_sandwich('cheese', 'beef')
#3 ms('cheese')
#4 ms.make_sandwich('cheese', 'beef', 'egg')
make_sandwich('cheese', 'beef')
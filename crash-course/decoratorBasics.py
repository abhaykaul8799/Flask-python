# def hello(name,greet=True):

#     print("Hello ",name)

#     def welcome():
#         return "Welcome to this page!"
    
#     def greetings():
#         return "Greetings"
    
#     if greet:
#         return greetings
#     else:
#         return welcome

# temp = hello("Abhay")
# print(temp())
# print("*"*100)
# temp = hello("Kaul",greet=False)
# print(temp())

####################################

# def hello():
#     return "Hi abhay"

# def other(func):
#     print("New function")
#     print(func())

# other(hello)

######################################

def new_decorator(func):

    def wrap_func():
        print("Some code before func")
    
        func()

        print("Some code after func")
    
    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!")

func_needs_decorator()

    
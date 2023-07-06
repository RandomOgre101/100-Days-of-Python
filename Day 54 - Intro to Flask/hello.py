# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == "__main__":
#     app.run()

## Python Decorator
import time
# def delay_decorator(function):
#     def wrapper_func():
#         time.sleep(2)
#         function()

#     return wrapper_func

# # @delay_decorator
# # def say_hello():
# #     print("Hello")

# # @delay_decorator
# # def say_bye():
# #     print("Bye")

# # def say_greeting():
# #     print("How are you?")

# # say_hello()
# # say_bye()
# # say_greeting()

import time

def speed_calc_decorator(function):
    def wrapper():
        t1 = time.time()
        function()
        t2 = time.time()
        print(f"{function.__name__} run speed: {t2-t1}")
    
    return wrapper
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
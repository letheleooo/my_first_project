# 计算器，实现一些基本的操作，加减乘除运算，以及打印结果操作
# result = 0
# 
# 
# def first_value(v):
#     global result
#     result = v
# 
# 
# def add(n):
#     global result
#     result += n
# 
# 
# def subtract(n):
#     global result
#     result -= n
# 
# 
# def multiply(n):
#     global result
#     result *= n
# 
# 
# first_value(2)
# add(6)
# subtract(5)
# print(multiply(3))

# ------------------------面向对象----------------------
#
#
# class Calculator:
#     __result = 0
#
#     @classmethod
#     def first_value(cls, v):
#         cls.__result = v
#
#     @classmethod
#     def add(cls, n):
#         cls.__result += n
#
#     @classmethod
#     def subtract(cls, n):
#         cls.__result -= n
#
#     @classmethod
#     def multiply(cls, n):
#         cls.__result *= n
#
#     @classmethod
#     def show(cls):
#         print("计算的结果是：%s" % cls.__result)
#
#
# Calculator.first_value(2)
# Calculator.add(5)
# Calculator.subtract(4)
# Calculator.multiply(5)
# Calculator.show()


# --------------------------对象属性--------------------------
# class Calculator:
#
#     def __init__(self, num):
#         self.__result = num
#
#     def first_value(self, v):
#         self.__result = v
#
#     def add(self, n):
#         self.__result += n
#
#     def subtract(self, n):
#         self.__result -= n
#
#     def multiply(self, n):
#         self.__result *= n
#
#     @classmethod
#     def show(cls):
#         print("计算的结果是：%s" % cls.__result)
#
#
# Calculator.first_value(2)
# Calculator.add(5)
# Calculator.subtract(4)
# Calculator.multiply(5)
# Calculator.show()

# --------------------------容错处理-----------------------------
# class Calculator:
#
#     def check_num(self, n):
#         if not isinstance(n, int):
#             raise TypeError("当前数据类型有问题，应该是一个整型数据。")
#
#     def __init__(self, n):
#         self.check_num(n)
#         self.__result = n
#
#     def add(self, n):
#         self.__result += n
#
#     def subtract(self, n):
#         self.check_num(n)
#         self.__result -= n
#
#     def multiply(self, n):
#         self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是：%s" % self.__result)
#
#
# c1 = Calculator(2)
# c1.add(6)
# c1.subtract(4)
# c1.multiply(5)
# c1.show()

# --------------------------容错处理+装饰器-----------------------------
import win32com.client


class Calculator:

    def __check_num_deco(func):

        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("当前这个数据的类型有问题，应该是一个整型数据")
            return func(self, n)
        return inner

    def __speak(self, word):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(word)

    def __create_speaker_deco(word=""):
        def __speaker_deco(func):
            def inner(self, n):
                self.__speak(word+str(n))
                return func(self, n)
            return inner
        return __speaker_deco

    @__check_num_deco
    @__create_speaker_deco()
    def __init__(self, n):
        self.__result = n

    @__check_num_deco
    @__create_speaker_deco("加")
    def add(self, n):
        self.__result += n
        return self

    @__check_num_deco
    @__create_speaker_deco("减")
    def subtract(self, n):
        self.__result -= n
        return self

    @__check_num_deco
    @__create_speaker_deco("乘")
    def multiply(self, n):
        self.__result *= n
        return self

    def show(self):
        output = "计算的结果是：%s" % self.__result
        self.__speak(output)
        print(output)
        return self

    @property
    def result(self):
        return self.__result

c1 = Calculator(2)
c1.add(6).subtract(4).multiply(5).show()
print(c1.result)
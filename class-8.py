# a = open('test1.txt','r')

# print(a.read())
# a.close()

# for i in a:
#     print(i)

# a = open('test1.txt','w')
# a.write("Amar Shonar Bangla")
# a.close()

# a = open('test1.txt','a')
# a.write(" Ami Tomay Valobashi")
# a.close()

# a = open('test1.txt','r')

# print(a.read())


# import os

# # # os.remove('test1.txt')
# # os.rmdir('test')

# os.rename('test1.txt','1.txt')

# try:
#     a = open('test1.txt','r')
#     print(a.read())
#     # for i in a:
#     #     print(i)
# except Exception as e:
#     print(e)
#     print('Vul Koreci')
# # import class7

# print(class7.b)
# class7.myfun(12,44)

# import datetime

# a = datetime.datetime.now()

# print(a.strftime("%I"))

# try:
#     a = open('test2.txt','r')
#     print(a.read())
#     # for i in a:
#     #     print(i)
# except Exception as e:
#     print(e)
# else:
#     print("Hello world")
# try:
#     a = open('test1.txt','r')
#     print(a.read())
#     # for i in a:
#     #     print(i)
# except Exception as e:
#     print(e)
# finally:
#     print("Hello world")


# a = 5

# for i in range(a):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\r")


# for i in range(a+1,0,-1):
#     for j in range(0,i-1):
#         print("*",end="")
#     print("\r")

# from py_package import class7

# x = class7.myfun(12,23)

# print(x)



class Student:
    p = 'Ajim'
    b = 3454

    def __init__(self,x,y):
        self.t = x
        self.z = y        
        print(self.t+self.z)
        # return self.t + self.z

    def __del__(self):
        print("Deleted")

daroan = Student(45,67)

# del daroan

# print(daroan)

# print(daroan.p)

# a.myfun(12,23)
# print(daroan.myfun(12,23))
# print(daroan.b)
# # print(len(daroan.p))
# print(daroan.p)

# class Father:
#     x = 123
#     y = 2323
#     def xy(self):
#         print('India')
#     class Mother:
#         def xy(self):
#             print('China')

# class son(Father):
#     def ab(self):
#         print('Bangladesh')

# # a = Father()
# # print(a.x)
# b = son()

# b.xy()
# b.Mother().xy()


# class A:
#     def math(self,x,y):
#         self.t = x
#         self.b = y
#         print(self.t + self.b)
# class B:
#     def math(self,x,y):
#         self.t = x
#         self.b = y
#         print(self.t - self.b)

# a = A()
# b = B()

# a.math(23,45)
# b.math(34,12)



# # # nums = [1, 2, 3]

# # # i_nums = iter(nums)

# # # # for num in nums:
# # # #     print(num)
# # # # print(i_nums)
# # # # print(dir(i_nums))

# # # print(next(i_nums))
# # # print(next(i_nums))
# # # print(next(i_nums))
# # # # print(next(i_nums))


# # # # LEGB
# # # # Local > Enclosing > Global >Built-in

# # # # local - variables in a function
# # # # build in

# # # x = 'global x'

# # # import builtins

# # # # print(dir(builtins))


# # # def my_min():
# # #     pass


# # # m = min([5, 1, 4, 2, 3])
# # # print(m)


# # # def test(z):
# # #     # global x
# # #     x = 'local x'
# # #     # print(y)
# # #     print(z)


# # # test('local z')
# # # # print(z)


# # # def outer():
# # #     # x = 'outer x'

# # #     def inner():
# # #         # nonlocal x
# # #         # x = 'inner x'
# # #         print(x)

# # #     inner()
# # #     print(x)


# # # outer()


# # # my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # # list(start:end:step)
# # # print(my_list[-9])

# # # print(my_list[:])

# # # print(my_list[-1:2:-2])

# # # print(my_list[::-1])

# # # sample_url = 'http://coreyns.com'
# # # print(sample_url)

# # # # ? reverse the sample_url

# # # print(sample_url[::-1])

# # # # get top level domain
# # # print(sample_url[-4:])

# # # # print url without Http
# # # print(sample_url[7:])

# # # # print url without the top level domain or http://

# # # print(sample_url[7:-4])

# # # # list comprehensions

# # # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # # I want 'n' for each 'n' in nums

# # # my_list = []
# # # for n in nums:
# # #     my_list.append(n)
# # # print(my_list)

# # # # I want 'n*n' for each 'n' in nums

# # # my_list = []
# # # for n in nums:
# # #     my_list.append(n * n)
# # # print(my_list)

# # # # my_list = [n * n for n in nums]
# # # # print(my_list)

# # # # using a map + lambda
# # # # my_list = map(lambda n: n * n, nums)
# # # # print(my_list)

# # # #  I want  'n' for each 'n' in nums if 'n' is even

# # # my_list = []
# # # for n in nums:
# # #     if n % 2 == 0:
# # #         my_list.append(n)
# # # print(my_list)


# # # my_list = []
# # # my_list = [n for n in nums if n % 2 == 0]

# # # my_list = []
# # # my_list = filter(lambda n: n % 2 == 0, nums)
# # # print(my_list)


# # # # I want a (letter, number) pair for each letter in 'abcd' and each number in '0123'

# # # my_list = []
# # # for letter in 'abcd':
# # #     for num in range(4):
# # #         my_list.append((letter, num))
# # # print(my_list)

# # # my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# # # print(my_list)

# # # # Dictionary comprehensions
# # # names = ['Bruce', 'Clark', 'Peter', 'logan', 'Wade']
# # # heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# # # print(zip(names, heros))


# # # # i want a dict{name: heros} for each name, hero in zip(names, heros)

# # # my_dict = {}

# # # for name, hero in zip(names, heros):
# # #     my_dict[name] = hero
# # # print(my_dict)


# # # my_dict = {}

# # # my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
# # # print(my_dict)

# # # # Set comprehensions

# # # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 3, 4, 5, 6, 2, 3, 4, 7, 8, 9, 9, 7, 6, 5, 4]

# # # my_set = set()
# # # for n in nums:
# # #     my_set.add(n)
# # # print(my_set)

# # # my_set = {n for n in nums}
# # # print(my_set)


# # # # Generator expressions
# # # # I want to Yeild n*n for each n
# # # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# # # def gen_func(nums):
# # #     for n in nums:
# # #         yield n * n


# # # my_gen = gen_func(nums)

# # # for i in my_gen:
# # #     print(i)


# # # my_gen = (n * n for n in nums)
# # # print(my_gen)

# # # # How to sort in python

# # # li = [1, 2, 3, 4, 5, 9, 8, 7, 6]
# # # s_li = sorted(li, reverse=True)
# # # print('print sorted Variable:\t', s_li)


# # # li.sort(reverse=True)

# # # print('Original Variable:\t', li)

# # # # Sorting for tuple

# # # tup = (9, 1, 3, 2, 4, 6, 0, 8, 7)

# # # print('Tuple\t:', tup)
# # # s_tup = sorted(tup)
# # # print('Sorted Tuple\t:', s_tup)


# # # # Dictionary Sorted

# # # di = {'Name': 'Vamsi', 'Jobs': 'Programming', 'Age': None, 'As': 'Mat'}
# # # s_di = sorted(di)
# # # print('Dict \t:', s_di)

# # # li = [-2, -3, -4, 1, 0, 2, 3]

# # # s_li = sorted(li, key=abs)
# # # print(s_li)


# # # class Employee():
# # #     def __init__(self, name, age, salary):
# # #         self.name = name
# # #         self.age = age
# # #         self.salary = salary

# # #     def __repr__(self):
# # #         return '({},{},${})'.format(self.name, self.age, self.salary)


# # # from operator import attrgetter
# # # e1 = Employee('Vamsi', 26, 60000)
# # # e2 = Employee('Clark', 23, 23423)
# # # e3 = Employee('John', 34, 6546434)

# # # employees = [e1, e2, e3]


# # # def e_sort(emp):
# # #     return emp.name


# # # s_employees = sorted(employees, key=e_sort, reverse=True)
# # # print(s_employees)


# # # s_employees = sorted(employees, key=lambda e: e.name, reverse=True)

# # # print(s_employees)

# # # s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
# # # print(s_employees)

# # # # String formatiing

# # # person = {'name': 'Jason', 'age': 33}
# # # sentence = 'My Name is ' + person['name'] + 'and iam' + str(person['age']) + 'Years old'
# # # print(sentence)

# # # sentence = 'My Name is {0} and I am {0} years old'.format(person['name'], person['age'])
# # # print(sentence)

# # # tag = 'Hi'
# # # text = 'This is a headline'

# # # sentence = '<{0}>{1}</{0}>'.format(tag, text)

# # # print(sentence)

# # # sentence = 'My Name is {0[name]} and I am {0[age]} years old'.format(person, person)
# # # print(sentence)


# # # sentence = 'My Name is {0[name]} and I am {0[age]} years old'.format(person)
# # # print(sentence)

# # # l = ['jenn', 23]

# # # sentence = 'My Name is {0[0]} and I am {0[1]} years old'.format(l)
# # # print(sentence)


# # # class person():
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age


# # # p1 = person('Jason', '23')

# # # sentence = 'My name is {0.name} and Iam {0.age} years old'.format(p1)
# # # print(sentence)

# # # person = {'name': 'Jenn', 'age': 23}

# # # sentence = 'My name is {name} and i am {age} years old.'.format(**person)
# # # print(sentence)

# # # for i in range(1, 11):
# # #     sentence = 'The value is {:03}'.format(i)
# # #     print(sentence)

# # # pi = 3.14235678

# # # sentence = 'Pi is equal to {:.3f}'.format(pi)
# # # print(sentence)

# # # sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# # # print(sentence)

# # # import datetime
# # # my_date = datetime.datetime(2018, 4, 20, 16, 4, 2)
# # # print(my_date)

# # # import keyword

# # # print(keyword.kwlist)

# # # print('Tortal no of kewword', len(keyword.kwlist))

# # # a = 1 + 2 + 3 + 4 +\
# # #     5 + 6 + 7 +\
# # #     8 + 9
# # # print(a)

# # # b = 10
# # # e = 10
# # # c = 4.4
# # # d = 'ML'
# # # # b.type()
# # # print(b)
# # # print(type(c))
# # # print(type(d))

# # # print(id(b))
# # # print(id(e))

# # # f = 1 + 2j
# # # print(type(f))
# # # print(isinstance(1 + 2j, (complex, bool, float)))

# # # help(isinstance)

# # # s = '''online AI
# # # course'''
# # # # print(s)
# # # print(s[4:-3])

# # # list_1 = [10, 20.4, 'str', True, ['Vamsi', 26, False]]

# # # print(list_1)
# # # print(list_1[-1][2])

# # # list_1[-1] = []

# # # print(list_1)

# # # # set_1 ={1,2,3,4,5,6,7,8,7,6,5,4,['Tuple',20,False],('Dictonary',True,20.9),{'Key':10,'Company':'Mckinsey' }}

# # # # print(set_1)

# # # # Set doesnot support indexing
# # # # print(set_1[1])


# # # li_1 = [1, 2, 3, 4]
# # # print(li_1)

# # # print(type(li_1))

# # # s = set(li_1)
# # # print(s)
# # # print(type(s))

# # # # d = dict(li_1)
# # # # print(d)
# # # # print(type(d))

# # # # import os
# # # # print(os.getcwd())
# # # # os.chdir('/Users/vsayarwar/Documents/')
# # # # print(os.getcwd())

# # # # print(os.listdir())
# # # # os.chdir('/Users/vsayarwar/Desktop')
# # # # print(os.getcwd())
# # # # print(os.listdir())

# # # # os.mkdir('NewFolder')
# # # # os.makedirs('NewFolder1/SubFolder2')

# # # # print(os.listdir())

# # # # Python OOPS


# # # class Employee:
# # #     num_of_emps = 0
# # #     raise_amount = 1.04

# # #     def __init__(self, first, last, pay):
# # #         self.first = first
# # #         self.last = last
# # #         self.pay = pay
# # #         self.email = first + '.' + last + '@gmail.com'
# # #         Employee.num_of_emps += 1

# # #     def fullname(self):
# # #         return('{} {}'.format(self.first, self.last))

# # #     def apply_raise(self):
# # #         self.pay = int(self.pay * self.raise_amount)

# # #     # Special methods called dunder methods meaning DoubleUNDERrscore for example __init__, __str__, __repr__ are few common types

# # #     # __repr__ is unabiguous representation of the object and should be used for debugging and for logs It is really meant to be seen by another developers
# # #     # __str__ is more of a readable representation of the object and is meant to be used as a display to the end user

# # #     def __repr__(self):
# # #         return"Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

# # #     def __str__(self):
# # #             return'{} - {}'.format(self.fullname(),self.email)
# # #     def __add__(self,other):
# # #         return self.pay + other.pay

# # #     def __len__(self):
# # #         return len(self.fullname())

# # #     @classmethod
# # #     def set_raise_amt(cls, amount):
# # #         cls.raise_amount = amount

# # #     @classmethod
# # #     def from_string(cls, emp_str):
# # #         first, last, pay = emp_str.split('-')
# # #         return cls(first, last, pay)
# # #     # @classmethod
# # #     # def fromtimestamp(cls,t):
# # #     #     y,m,d,hh,mm,ss,weekday,jday,dst =time.localtime(t)
# # #     #     return cls(y,m,d)

# # #     @staticmethod
# # #     def is_workday(day):
# # #         if day.weekday() == 5 or day.weekday() == 6:
# # #             return False
# # #         return True


# # # # print(Employee.num_of_emps)

# # # class Developer(Employee):
# # #     raise_amount = 1.10
# # #     def __init__(self, first, last, pay,Prog_lang):
# # #         super().__init__(first,last,pay)
# # #         # Employee.__init__(self,first,last,pay)
# # #         self.Prog_lang=Prog_lang

# # # class Manager(Employee):

# # #     def __init__(self,first,last,pay,employees=None):
# # #         super().__init__(first,last,pay)
# # #         if employees is None:
# # #             self.employees=[]
# # #         else:
# # #             self.employees=employees

# # #     def add_emp(self,emp):
# # #         if emp not in self.employees:
# # #             self.employees.append(emp)

# # #     def remove_emp(self,emp):
# # #         if emp in self.employees:
# # #             self.employees.remove(emp)

# # #     def print_emps(self):
# # #         for emp in self.employees:
# # #             print('---->',emp.fullname())


# # # dev_1 = Developer('Vamsi', 'Sayarwar', 60000,'Python')
# # # dev_2 = Developer('Poornima', 'Sayarwar', 6000000,'Swift')
# # # mgr_1=Manager('Poori','Mallu',10000000,['cathy','brent','carl','Dorthey','Liam'])
# # # mgr_2=Manager('Siva','Mallu',12223334,[dev_1,dev_2])
# # # dev_3=Developer('Hari','Krishna',90840923,'ML')

# # # mgr_2.add_emp(dev_3)

# # # print(mgr_1.email)
# # # print(mgr_2.email)


# # # # print(mgr_1.employees)
# # # # print(mgr_2.employees)
# # # # mgr_1.print_emps()
# # # mgr_2.print_emps()

# # # mgr_2.remove_emp(dev_1)

# # # print('''Removed one employee Dev1''')

# # # mgr_2.print_emps()

# # # # print(dev_1.email)
# # # # print(dev_1.Prog_lang)
# # # # print(dev_1.pay)
# # # # dev_1.apply_raise()
# # # # print(dev_1.pay)

# # # # print(help(Developer))

# # # # print(dir(Developer))

# # # # emp_str_1 = 'Vamsi-Krishna-828747'
# # # # emp_str_2 = 'Vamsi-Sayarwar-445577'
# # # # emp_str_3 = 'Poornima-Sayarwar-10000000'


# # # # new_emp_1 = Employee(first, last, pay)
# # # # new_emp_1 = Employee.from_string(emp_str_1)

# # # # print(new_emp_1.email)
# # # # print(new_emp_1.pay)


# # # # print(Employee.num_of_emps)

# # # # print(emp_1.pay)
# # # # print('raise percentage with existing will be', employee.raise_amount)
# # # # emp_1.apply_raise()
# # # # print(emp_1.pay)
# # # # print(Employee.raise_amount)
# # # # print(emp_1.raise_amount)
# # # # print(emp_2.raise_amount)

# # # # print(emp_1.__dict__)

# # # # print('''============== ==

# # # # ''')
# # # # # print(Employee.__dict__)

# # # # emp_1.raise_amount = 1.05

# # # # print(emp_1.__dict__)

# # # # print(Employee.raise_amount)
# # # # print(emp_1.raise_amount)
# # # # print(emp_2.raise_amount)


# # # # # print(emp_1.email)
# # # # # print(emp_2.email)

# # # # # print(emp_1.fullname())
# # # # # print(emp_2.fullname())
# # # # # emp_1.first = 'Vamsi'
# # # # # emp_1.last = 'Sayarwar'
# # # # # emp_1.email = 'vamshiahead@gmail.com'
# # # # # emp_1.pay = 60000

# # # # # emp_2.first = 'Poornima'
# # # # # emp_2.last = 'Sayarwar'
# # # # # emp_2.email = 'poornimas007@gmail.com'
# # # # # emp_2.pay = 600000

# # # # # print(emp_1.email)
# # # # # print(emp_2.email)
# # # # print(Employee.num_of_emps)

# # # # Regular   class and static methods

# # # # emp_1.set_raise_amt(1.05)


# # # # print(Employee.raise_amount)
# # # # print(emp_1.raise_amount)
# # # # print(emp_2.raise_amount)

# # # # import datetime
# # # # my_date = datetime.date(2016, 7, 11)

# # # # print(Employee.is_workday(my_date))

# # # print(issubclass(Manager,Developer))
# # # print(isinstance(mgr_1,Employee))


# # # emp_1 = Employee('Vamsi', 'Sayarwar', 60000)
# # # emp_2 = Employee('Poornima', 'Sayarwar', 6000000)

# # # # print(emp_1)
# # # # print(repr(emp_1))
# # # # print(str(emp_1))

# # # print(emp_1.__repr__())
# # # print(emp_1.__str__())

# # # print(emp_1+emp_2)

# # # print(len(emp_1))

# # # print(len(emp_2))

# # # # num=input('Enter a number: ')
# # # # print(num)
# # # # num_1=input('Enter a number 1: ')
# # # # print(num_1)

# # # # nested list comprehensions

# # # # matrix=[[1,2,3,4],
# # # # [5,6,7,8],
# # # # [9,10,11,12]]

# # # # Transpose=[]
# # # # for i in range(4):
# # # #     lst=[]
# # # #     for row in matrix:
# # # #         lst.append(row)

# # # # Transpose the matrix without the list comprehensions

# # # # dictionary methods

# # # squares={1:1,2:4,3:9,4:16,5:25}
# # # my_dict=squares.copy()
# # # print(my_dict)


# # # subjects={}.fromkeys(['Math','English','Hindi'],0)
# # # print(subjects)

# # # print(subjects.items())

# # # print(subjects.values())

# # # print(subjects.keys( ))

# # # # dir() will give all the methods and attributes of Dictonary or tuple otr list or set or datatype

# # # set_1={}
# # # print(dir(set_1))


# # # # For dictionaries
# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')
# # # print(dir(subjects))


# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')


# # # # For list


# # # li_1=[]
# # # print(dir(li_1))

# # # # For tuples


# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')

# # # tu_1=(1,2)

# # # print(dir(tu_1))
# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')
# # # # Dictionary comprehensions

# # # d ={1:1,2:4,3:9,4:16,5:25}

# # # for pair in d.items():
# # #     print(pair)

# # # # print(dir(d))
# # # new_dict={k:v for k,v in d.items() if v>3.1}
# # # print(new_dict)

# # # new_dict1={k+2:v*4 for k,v in d.items() if v>5}
# # # print(new_dict1)


# # # list_method_attribute=set(dir(li_1))
# # # set_method_attribute=set(dir(set_1))

# # # print(list_method_attribute & set_method_attribute)


# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')

# # # print(list_method_attribute ^ set_method_attribute)

# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')

# # # print(dir(set_method_attribute))

# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')
# # # print(set_method_attribute.difference(list_method_attribute))


# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')


# # # print(list_method_attribute.difference(set_method_attribute))

# # # print('''==============
# # #     ============
# # #     ==============
# # #     ==============
# # #     ============''')


# # # print(list_method_attribute.difference(list_method_attribute))


# # # # Stringd UNICODE and ASCII


# # # mystring = 'Hello'
# # # print(mystring[:-1])
# # # print(mystring[2:])
# # # print(mystring[4])

# # # # mystring[4]='V'

# # # del mystring
# # # # print(mystring)

# # # s1='Hello'
# # # s2='Vamsi'
# # # # print(s1+s2)


# # # # print(s1*s2 )

# # # # Python functions

# # # # LEGB

# # # # Local Enclosing global bulit-in(LEGB)

# # # def print_name(name):
# # #     '''
# # #     This function prints the name
# # #     '''
# # #     print('Hello ' + name)
# # #     print('Hello {}'.format(name))

# # # print_name('Vamsi')
# # # # Doc dstring will pr int the commets placed in docstring
# # # print(print_name.__doc__)

# # # def get_sum(lst):
# # #     '''It will get the sum of all the values in the list
# # #     '''
# # #     # Initiate sum
# # #     _sum=0
# # #     for num in lst:
# # #         _sum=num+_sum
# # #     return _sum


# # # s=get_sum([1,2,3,4,5,6,7,8,9,10])
# # # print(s)
# # # print(get_sum.__doc__)

# # # # Return statements are optional

# # # # Scope and lifetime of a variables

# # # global_var='This is a global variable'
# # # def test_life_time():
# # #     '''
# # #     This function test the lifetime of a variable'''

# # #     local_var='This is a local variable'
# # #     print(local_var)

# # #     print(global_var)

# # # test_life_time()

# # # print(global_var)
# # # # print(local_var)

# # # # LEGB

# # # def compute_HCF(a,b):
# # #     hcf=1
# # #     if a<b:
# # #         smaller=a
# # #     else:
# # #         smaller=b

# # #     for num in range(1, smaller+1):
# # #         if (a%num == 0) and (b % num ==0):
# # #             hcf=num
# # #     return hcf

# # # num1=98
# # # num2=78

# # # hcf=compute_HCF(num1,num2)
# # # print(hcf)


# # # def c(a):
# # #     b=1
# # #     for i in range(1,11):
# # #         b=a*i
# # #         print('{0}*{1}={2}'.format(a,i,b))
# # #     return b
# # # a=2
# # # c(a)

# # # # HCF of 3 no's

# # # def hcf_3_nos(a,b,c):
# # #     hcf=1
# # #     if a<b and a<c:
# # #         smaller=a
# # #     elif b<a and b<c:
# # #         smaller=b
# # #     else:
# # #         smaller=c
# # #     for num in range(1,smaller+1):
# # #         if(a%num==0) and (b%num==0) and (c%num==0):
# # #             hcf=num
# # #     return hcf
# # # seperator=','
# # # # a=int(seperator.join(['7','2']))
# # # # b=int(seperator.join(['9','8']))
# # # # c=int(seperator.join(['4','2']))
# # # # result=hcf_3_nos(a,b,c)
# # # # print(result)

# # # def greet(name, msg):
# # #     pass

# # # '''
# # # This function is used to greeet people'''


# # # # print('Hello {0} {1}'.format(name, msg))


# # # # recursion function
# # # # def factorial(num):
# # # #     '''
# # # #     This is a recvursive function to find factorial of a givrn number
# # # #     '''
# # # #     if (num ==1):
# # # #         return num
# # # #     else:
# # # #         num = (num * factorial(num-1))

# # # # num =5
# # # # print('Factorial of {0} is {1}'.format(num, factorial(num)))

# # # def factorial(num):
# # #     return 1 if num==1 else (num * factorial(num-1))
# # # num= 7
# # # print('factorial of {0} is {1}'.format(num, factorial(num)))

# # # # Fibonaci set_raise_amt

# # # def fibonacci(num):
# # #     return num if num <=1 else fibonacci(num-1) + fibonacci(num-2)

# # # nterms=10
# # # print('fibonacci sequence')

# # # for num in range(nterms):
# # #     print(fibonacci(num))


# # # # lamda functions

# # # # Anonymous or lamda functions
# # # '''
# # # Anonymous or lamda functions
# # # '''

# # # # print(__doc__)

# # # # They are used extensively in data science

# # # # filter(), map(), reduce()

# # # # syntax lambda arguments: expressions

# # # # def double(x):
# # # #     return x*2

# # # # print(double(5))

# # # double = lambda x: 2*x

# # # print(double(5))

# # # # filter function used with lambda
# # # lst = [1,2,3,4,5]

# # # even_list = list(filter(lambda x:x%2 ==0, lst))
# # # print(even_list)

# # # # MAp function used with lambda

# # # lst = [1,2,3,4,5,6,7,8,9,10]
# # # new_list= list(map(lambda x: x**2, lst))
# # # print(new_list)

# # # # Rduce with lamda function


# # # from functools import reduce

# # # lst = [1,2,3,4,5]
# # # product_lst=reduce(lambda x,y:x+y, lst)
# # # print(product_lst)


# # # # modules are very useful constructs in python

# # # # a file containing the python code eg: abc.py is called a module and its module name would be abc

# # # # we use modules to break down large programs into small manageable and organized files. further more, modules provide reusability of code.of


# # # # we can define our most used functions in module and import it, instead of copying their definitions into different programs

# # # # We use import keyword to do This


# # # # import CoreyShaufer

# # # # CoreyShaufer.add(10,20)

# # # import math
# # # print(math.pi)

# # # import datetime
# # # print(datetime.datetime.now())


# # # import math as m
# # # print(m.pi)

# # # from datetime import datetime
# # # datetime.now()

# # # # from CoreyShaufer import add
# # # # print(add(10,20))


# # # # gouping of all modules is called package with __init__ file

# # # # packages are a way of structuring pythons module namespace by using 'dotted module names'

# # # # A directory must contain a file named init.py in order for python to consider it as a package. This file can be left empty but we generallt place the initializarion code for that package in this file


# # # ''''File I/o , how to maipulate files and directories in python '''


# # # '''file operation

# # # 1)open a file
# # # 2)read or write ( perform operation)
# # # 3)close a file'''


# # # f = open('thinkstats.pdf')

# # # '''
# # # Python file modes

# # # 'r' reading a file
# # # 'w' writing a file
# # # 'x' opena file for exclusive creation. If file already exists it will fail

# # # 'a' open for appending at the end of the file without truncating it. Create a new file if it doesnot exists

# # # 't' open in text mode
# # # 'b' open in binary mode
# # # '+' open a file for updating ( reading and Writing)

# # # Binary mode is extensively used in scientific computation'''

# # # f.close()


# # # try:
# # #     f=open('thinkpython.pdf')

# # # finally:
# # #     f.close()


# # # f =open('test.txt','w')
# # # f.write('This is a first file\n')
# # # f.write('Contains two lines\n')
# # # f.close()

# # # f=open('test.txt','r')
# # # # f.read(10)

# # # # print(f.tell())


# # # # f.seek(0)

# # # # print(f.read(10))

# # # f.seek(0)
# # # for line in f:
# # #     print(line)


# # # f = open('test.txt','r')
# # # # f.readline()
# # # # print(f.readline())
# # # # print(f.readline())

# # # print(f.readlines())


# # # import os

# # # os.rename('test.txt','sample.txt')

# # # f = open('sample.txt','r')
# # # print(f.readline())

# # # # os.remove('sample.txt')

# # # # f = open('sample.txt','r')

# # # # Current working directory
# # # print(os.getcwd())
# # # # Change directory
# # # os.chdir('/Users/vsayarwar/Documents/Python_Learning')
# # # print(os.getcwd())


# # # print(os.listdir(os.getcwd()))

# # # # import shutil

# # # # os.chdir('./test')
# # # # f=open('testfile.txt','w')
# # # # f.write('Hello World')
# # # # os.chdir('../')
# # # # os.rmdir('test')

# # # # shutil.rmtree('test1')
# # # # os.mkdir('test1')
# # # # f.close()
# # # # f=open('testfile.txt','r')
# # # # print(f.read())
# # # # os.rmdir('test1')

# # # # shutil is a shell util

# # # # Python Errors and built-in exceptions

# # # if a< 3:
# # #     pass


# # # # 1/0

# # # # open('test.txt')

# # # print(dir(__builtins__))

# # # import sys

# # # lst = ['b',0,2]

# # # for entry in lst:
# # #     try:
# # #         print('The Entry is', entry)
# # #         r=1/int(entry)
# # #     except:
# # #         print('oops',sys.exc_info()[0],'occured')
# # #         print('next entry')
# # #         print('*******************')
# # # print('the reciprocal of entry is ',entry,'is',r)

# # # for entry in lst:
# # #     try:
# # #         print('******************')
# # #         print('The Entry is ', entry)
# # #         r=1/int(entry)
# # #     except(ValueError):
# # #         print('This is a value error')
# # #     except(ZeroDivisionError):
# # #         print('This si a Zero error')
# # #     except:
# # #         print('Some other Error',sys.exc_info[0])

# # # print('the reciprocal of ',entry, 'is',r)

# # # # try:
# # # # except:
# # # # raise:
# # # # finally:

# # # # finally always runs neverthelss of any exceptions


# # # # Debugging a code

# # # # Python-debugger(pdb) implements an interactive
# # # # debugging environment for python programs.pythonIt includes features to let you pause your program, look at the values of variables, and watch program execution step -by -step, so you can understand what your program actually does to find bugs in the logic
# # # # Python-de

# # # # bugger(pdb)
# # # import pdb

# # # def seq(n):
# # #     for i in range (n):
# # #         # pdb.set_trace()
# # #         print(i)
# # #     return

# # # seq(5)

# # # # c: continue
# # # # q: quit
# # # # h: help
# # # # list
# # # # p:print
# # # # p locals()
# # # # p globals

# # # import numpy as np

# # # a = np.arange(10)
# # # print(a)

# # # a[7]=100

# # # print(a)

# # # b=np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
# # # print(b)

# # # # 30.55

# # # print(b.shape)

# # # a[5:]=99
# # # print(a)
# # # c = np.arange(5)
# # # a[5:]=c[::-1]
# # # print(a)


# # # b=a[::2]
# # # print(b)
# # # print(np.shares_memory(a,b))


# # # b[0]= 10
# # # print(b)

# # # print(a)

# # # a=np.random.randint(0,20,15)
# # # print(a)

# # # mask = (a%2 ==0)

# # # extract_from_a = a[mask]
# # # print(extract_from_a)

# # # a[mask]=-1
# # # print(a)

# # # a=np.arange(0,100,10)
# # # print(a)

# # # print(a[[2,3,2,4,2]])

# # # a[[9,7]]=200
# # # print(a)

# # # a= np.array([1,2,3,4])

# # # print(a+1)

# # # print(a**2)
# # # b=np.ones(4)+1
# # # print(a)
# # # print(b)
# # # print(a-b)

# # # print(2*(a-b))

# # # print(a*b)

# # # c=np.diag([1,2,3,4])

# # # print(c*c)
# # # print('**************')
# # # print(c.dot(c))

# # # a = np.array([1,2,3,4])
# # # b=np.array([5,2,2,4])
# # # print(a==b)

# # # a=np.array([[1,1],[1,1]])
# # # b=np.array([[1,0],[0,1]])
# # # print(a)
# # # print(b)
# # # print('*****************')
# # # print(a*b)
# # # print('*****************')
# # # print(b.dot(a))

# # # a=np.array([1,2,3,4])
# # # b=np.array([5,2,2,4])
# # # c=np.array([1,2,3,4])
# # # print(np.array_equal(a,b))

# # # print('*****************')

# # # a=np.array([1,1,0,0], dtype=bool)
# # # b=np.array([1,0,1,0], dtype=bool)
# # # print(np.logical_not(np.logical_or(a,b)))


# # # a=np.arange(5)
# # # print(np.sin(a))
# # # print(np.log(a))
# # # print(np.exp(a))

# # # # a=np.arange(4)
# # # # a+np.array([1,2])

# # # x = np.array([10,2,1,4])
# # # print(np.sum(x))

# # # # x=np.array([[1,1],[3,3 ]])
# # # # print(x)

# # # # print(x.sum(axis=0))

# # # # print(x.sum(axis=1))

# # # print(x.min())
# # # print(x.max())
# # # print(x.argmin())
# # # print(x.argmax())

# # # print(np.all([True,True,False,False]))

# # # print(np.any([True,False,False]))

# # # a=np.zeros((50,50))
# # # print(np.any(a!=0))

# # # print(np.all(a==a))
# # # print('*****************************************')
# # # a=np.array([1,2,3,2])
# # # b=np.array([2,2,3,2])
# # # c=np.array([6,4,4,5])

# # # print(((a<=b) & (b<=c)).all())


# # # x=np.array([1,2,3])
# # # y=np.array([[1,2,3],[5,6,7]])
# # # print(x.mean())
# # # print(np.median(x))
# # # # print(x.mode())
# # # print(np.median(y, axis=1))

# # # print(x.std())
# # # print(1.4142135623730950488/1.73205080757)

# # # data=np.loadtxt('populations.txt')
# # # print(data)

# # # year, hares,lynxes,carrots=data.T
# # # print(year)

# # # populations = data[:,1:]
# # # print(populations)
# # # print('***************************************************************')
# # # print(populations.std(axis=0))
# # # print('***************************************************************')
# # # print(populations.mean(axis=0))
# # # print('***************************************************************')
# # # print(np.median(populations,axis=0))

# # # print('***************************************************************')
# # # print(np.argmax(populations,axis=1))
# # # print('************************************')
# # # a=np.tile(np.arange(0,40,10),(3,1))
# # # print(a)
# # # print('************************************')
# # # a=a.T
# # # print(a)
# # # print('************************************')
# # # b=np.array([0,1,2])

# # # print(b)

# # # print(a+b)

# # # a=np.arange(0,40,10)
# # # print(a.shape)
# # # a=a[:,np.newaxis]
# # # print(a.shape)
# # # print(a)
# # # print(a+b)
# # # print('************************************')
# # # a=np.array([[1,2,3],[4,5,6]])
# # # print(a.ravel())


# # # print('************************************')

# # # a=np.arange(4*3*2)
# # # print(a)
# # # print('************************************')
# # # a=a.reshape(4,3,2)
# # # print(a)
# # # print('************************************')
# # # print(a.shape)
# # # print('************************************')
# # # print(a)

# # # # Mathplotlib.pyplot is a collection of coomand line functions that make matplotlib work like matlab

# # # # Each Pyplot function makes some change to a figure e.g creates a figure, creates a plotting area in a figure, plots somelines in a plotting area, decorates the plot with labels etc..

# # # import matplotlib.pyplot as plt

# # # # plt.plot([2,4,6,4])
# # # # plt.ylabel('numbers')
# # # # plt.xlabel('Indices')
# # # # plt.title('Myplot')
# # # # plt.show()

# # # # If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of Y values, and automatically generates the x values for you. Since python ranges start with 0,the default x vector has same length as y but starts with 0. Hence the x data are [0,1,2,3]


# # # # plt.plot([1,2,3,4],[1,4,9,16])
# # # # plt.ylabel('squares')
# # # # plt.xlabel('numbers')
# # # # plt.title('shdfaskdl')
# # # # plt.grid()
# # # # plt.show()

# # # #'ro' represents: Red color points, 'o' shaped dots

# # # # plt.plot([1,2,3,4],[1,4,9,16],'ro')
# # # # plt.grid()
# # # # plt.show()


# # # # t=np.arange(0.,5.,.2)

# # # # plt.plot(t,t**2,'b--',label='^2')# 'rs','g')
# # # # plt.plot(t,t**2.2,'rs',label='^2.2')
# # # # plt.plot(t,t**2.5,'g^',label='^2.5')
# # # # plt.grid()
# # # # plt.legend()
# # # # plt.show()


# # # # x1=[1,2,3,4]
# # # # y1=[1,4,9,16]
# # # # x2=[1,2,3,4]
# # # # y2=[2,4,6,8]
# # # # lines=plt.plot(x1,y1,x2,y2)
# # # # plt.setp(lines[0],color='r',linewidth=2.0)
# # # # # plt.setp()
# # # # plt.grid()


# # # # import numpy as np

# # # # import matplotlib.pyplot as plt

# # # # def f(t):
# # # #     return np.exp(-t) * np.cos(2*np.pi*t)

# # # # t1=np.arange(0.0,5.0,0.1)
# # # # t2=np.arange(0.0,5.0,.02)

# # # # plt.figure(1)
# # # # plt.subplot(211)
# # # # plt.grid()
# # # # plt.plot(t1,f(t1),'b-')

# # # # plt.subplot(212)
# # # # plt.plot(t2,np.cos(2*np.pi*t2),'r--')
# # # # plt.show()

# # # # import numpy as np
# # # # import matplotlib.pyplot as plt

# # # # plt.figure(1)
# # # # plt.subplot(211)
# # # # plt.plot([1,2,3])
# # # # plt.subplot(212)
# # # # plt.plot([4,5,6])

# # # # plt.figure(2)
# # # # plt.plot([4,5,6])

# # # # plt.figure(1)
# # # # plt.subplot(211)
# # # # plt.title('Easy as 1,2,3')
# # # # plt.show()

# # # # GEtting started with pandas


# # # import pandas as pd
# # # df=pd.read_csv('/Users/vsayarwar/Documents/Python_Learning/IPython_Notebook/nyc_weather.csv')

# # # print(df)

# # # print(df['Temperature'].max())

# # # print(df.Temperature.max())

# # # # print(df[['EST','WindDirDegrees','Events'=='Rain']])

# # # print(df.WindDirDegrees.mean())

# # # # Creating a DataFrame Using list of tuples


# # # weather_data=[('1/1/2017',32,6,'Rain'),('1/2/2017',32,4,'Sunny'),('1/3/2017',32,2,'Snow'),('1/4/2017',32,9,'Sunny'),('1/5/2017',32,10,'Sunny'),('1/6/2017',32,100,'OverCast')]

# # # df=pd.DataFrame(weather_data,columns=['Day','Temperature','WindSpeed','Weather'])
# # # print(df)

# # # print(df.shape)

# # # print(df.head())
# # # print(df.tail())

# # # print(df[2:5])

# # # print(df.columns)

# # # print(df.Temperature[1])

# # # print(df[df.Day=='1/10/2017'])


# # # print(df[['Day','Temperature','WindSpeed']])

# # # df1=df[df.WindSpeed==6]

# # # print(df1[['Day','Temperature']])

# # # import xlrd as xls
# # # import openpyxl as oppyxl

# # # df=pd.read_excel('/Users/vsayarwar/Documents/Python_Learning/report.xls')

# # # print(df)

# # # df.to_csv('new.csv')
# # # df.to_excel('new.xlsx')

# # # dfn=pd.read_csv('new.csv')
# # # print(dfn)

# # # dfx=pd.read_excel('new.xlsx')
# # # print(dfx)

# # # dfn.to_csv('new.csv',index=False)

# # # dfn=pd.read_csv('new.csv')
# # # print(dfn)


# # # # group by operator in python.

# # # import pandas as pd
# # # cwd=os.getcwd()
# # # df=pd.read_csv('/Users/vsayarwar/Documents/Python_Learning/IPython_Notebook/weather_data_cities.csv')
# # # print(df)
# # # print('************************')
# # # g=df.groupby('city')
# # # print(g.temperature.max())

# # # for city, city_df in g:
# # #     print(city)
# # #     print(city_df)
# # # print('**************************')

# # # print(g.get_group('new york'))

# # # print('**************************')

# # # print(g.get_group('paris'))

# # # g1=df.groupby('event')
# # # print(g1.windspeed.max())
# # # print(g1.get_group('Sunny'))
# # # print('**************************')
# # # print(g1.describe())


# # # import pandas as pd
# # # india_weather=pd.DataFrame({
# # #     'city':['Mumbai','Delhi','Blore'],
# # #     'temp':[45,51,20],
# # #     'humid':[210,50,70]
# # # })

# # # print(india_weather)
# # # us_weather=pd.DataFrame({'city':['NewYork','Dallas','Mountain View'],
# # #     'temp':[-12,-3,-7],
# # #     'humid':[220,240,40]})
# # # print(us_weather)
# # # print('**************************')
# # # print(pd.concat([india_weather,us_weather]))
# # # print('**************************')
# # # con=pd.concat([india_weather,us_weather],ignore_index=True)
# # # print(con.city.sort_values())

# # # con1=pd.concat([india_weather,us_weather],ignore_index=True,axis=1)
# # # print(con1)

# # # print('*****************************************')

# # # import pandas as pd
# # # df=pd.read_csv('/Users/vsayarwar/Documents/Python_Learning/IPython_Notebook/employees.csv')
# # # # print(df)
# # # print('*****************************************')
# # # # print(dir(df))
# # # df.sort_values("First Name",inplace=True)

# # # df.drop_duplicates(subset="First Name",keep=False,inplace=True)

# # # print(df)


# # # # df1=df.drop_duplicates(subset=['First Name'], keep='first',inplace=True)

# # # print(df1)

# # #  # df.drop_duplicates(['First Name'], )

# # # # print(dir(con))


# # # # os.chdir('../')


# # # import random as rd

# # # print(rd.random())


# # # from sklearn import datasets
# # # iris=datasets.load_iris()
# # # d=iris.data
# # # print(d.shape)

# # # print('****************************')

# # # # If I want to sample 30 points randomly from 150 point datasets

# # # n=150
# # # m=30

# # # p=m/n

# # # sample_data=[]

# # # for i in range(0,n):
# # #     x=rd.random()
# # #     if x<=p:
# # #         sample_data.append(x)

# # # print(sample_data)
# # # print(len(sample_data))

# # # # Bernouli and binomial distribution, They are discrete distributions

# # # print('****************')
# # # lst=[1,2,3,4,5]
# # # print(len(lst))

# # # lst.append('vasmi')

# # # print(lst)

# # # lst.insert(4,'krish')
# # # print(lst)

# # # lst.remove('krish')

# # # print(lst)

# # # lst2=['vasmi','poo','bbb']
# # # lst.extend(lst2)
# # # # lst.append(lst2)
# # # print(lst)

# # # # lst.del[-1]
# # # print(lst)


# # # print(dir(lst))
# # # print('*******************************************************************')

# # # import numpy as np
# # # import pandas as pd
# # # import matplotlib.pyplot as plt


# # # df = pd.read_csv('train.csv')

# # # print(df.head(10))

# # # label = df['label']

# # # print('*****************************************************************')

# # # print(label)

# # # df1 = df.drop('label', axis=1)
# # # print('*****************************************************************')
# # # print(df1)
# # # print('*****************************************************************')

# # # print(df.shape)
# # # print(label.shape)
# # # print(df1.shape)


# # # print('*****************************************************************')

# # # # plt.figure(figsize=(7, 7))

# # # # idx = 120
# # # # grid_data = df1.iloc[idx].as_matrix().reshape(28, 28)
# # # # # imshow = image show, cmap= color map
# # # # plt.imshow(grid_data, interpolation='none', cmap='gray')

# # # # plt.show()
# # # # print(df1[idx])


# # # print('**************Visualize PCA***********')

# # # labels = label.head(42000)
# # # data = df1.head(42000)

# # # print('the shape of sample data is ', data.shape)


# # # from sklearn.preprocessing import StandardScaler


# # # standard_data = StandardScaler().fit_transform(data)
# # # print(standard_data.shape)


# # # # find covariance matrix

# # # sample_data = standard_data

# # # covar_matrix = np.matmul(sample_data.T, sample_data)

# # # covar_matrix=covar_matrix/42000

# # # print('shape of covar_matrix is ', covar_matrix.shape)

# # # # finding top eigen values and corresponding eigen vectors

# # # # from scipy linear algebra
# # # from scipy.linalg import eigh

# # # eigen_values, eigen_vectors=eigh(covar_matrix,eigvals=(782,783))

# # # print('shape of eigen vectors', eigen_vectors.shape)

# # # print(eigen_values.shape)

# # # eigen_vectors=eigen_vectors.T


# # # print('shape of eigen vectors', eigen_vectors.shape)


# # # import matplotlib.pyplot as plt

# # # new=np.matmul(eigen_vectors,sample_data.T)


# # # print('vector shape',eigen_vectors.shape,'sample data',sample_data.shape)
# # # print('*********************************')

# # # print('newdal',new.shape)

# # # import pandas as pd
# # # new=np.vstack((new,labels)).T

# # # print(new.shape)

# # # dataframe=pd.DataFrame(data=new, columns=('1st_princ','2nd_princ','labels'))

# # # print(dataframe.head())


# # # import seaborn as sn
# # # sn.FacetGrid(dataframe, hue='labels',size=6).map(plt.scatter,'1st_princ','2nd_princ').add_legend()

# # # plt.show()


# # # # PCA using scikit Python_Learning

# # # from sklearn import decomposition


# # # pca=decomposition.PCA()

# # # pca.n_components=2

# # # pca_data=pca.fit_transform(sample_data)

# # # print('shape of PCA data',pca_data.shape)


# # # pca_data=np.vstack((pca_data.T,labels))

# # # pca_df=pd.DataFrame(data=pca_data,columns=('1st_princ','2nd_princ','labels'))

# # # plt.show()


# # # import numpy as np

# # # data=np.genfromtxt('test.csv', delimiter=',')

# # # print(data)


# # # iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
# # # plt.show()

# # # sns.set_style("whitegrid")
# # # g = sns.FacetGrid(iris, hue="species", size=4)
# # # # plt.show(g)
# # # g = g.map(plt.scatter, "sepal_length", "sepal_width")
# # # # plt.show(g)
# # # g = g.add_legend()
# # # plt.show(g)


# # # # sns.set_style("whitegrid")
# # # # sns.pairplot(iris, hue="species", size=2)
# # # # plt.show()


# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns

# # # iris = pd.read_csv("IRIS_Data_Set.csv")

# # # print(iris.shape)

# # # print(iris.columns)

# # # print(iris['species'].value_counts())

# # # import numpy as np
# # # # import pandas as pd

# # # iris_setosa = iris.loc[iris['species'] == 'setosa']

# # # print(iris_setosa)

# # # print('*=' * 40)
# # # iris_versicolor = iris.loc[iris["species"] == "versicolor"]
# # # print(iris_versicolor)
# # # print('*=' * 40)
# # # iris_virginica = iris.loc[iris["species"] == "virginica"]
# # # print(iris_virginica)
# # # print('*=' * 40)

# # # plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_setosa["petal_length"]), "g*")
# # # plt.show()


# # # plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_versicolor["petal_length"]), "r+")
# # # plt.show()


# # # plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_virginica["petal_length"]), "bo")

# # # # sns.add_legend()

# # # plt.show()


# # # # plt.close(g)

# # # # plt.show()

# # # g=sns.FacetGrid(iris,hue='species',size=4)
# # # g=g.map(sns.distplot,'petal_length')
# # # g=g.add_legend()
# # # plt.show()


# # # g=sns.FacetGrid(iris,hue='species',size=2)
# # # g=g.map(sns.distplot,'petal_width')
# # # g=g.add_legend()
# # # plt.show()
# # # g=FacetGrid(iris, hue='species',size=2)
# # # g=g.map(sns.distplot,'sepal_length')
# # # g=g.add_legend()
# # # plt.show()
# # # # plt.show()

# # # g=FacetGrid(iris,hue='species',size=2)
# # # g=g.map(sns.distplot,'sepal_width')
# # # g=g.add_length()
# # # plt.show()

# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns
# # # import pandas as pd

# # # iris=pd.read_csv('IRIS_Data_Set.csv')

# # # iris_setosa=iris.loc[iris['species']=='setosa']


# # # counts, bins_edges=np.histogram(iris_setosa['petal_length'], bins=10, density=True)
# # # pdf=counts/sum(counts)
# # # print(pdf)

# # # print('=*'*40)
# # # print(bins_edges)
# # # # cdf=np.cumsum(pdf)
# # # # plt.plot(bin-edges[1:],pdf)
# # # print('=*'*40)
# # # print(counts)

# # # plt.plot(bins_edges[1:],pdf)
# # # plt.show()

# # # cdf=np.cumsum(pdf)
# # # plt.plot(bins_edges[1:],cdf)

# # # plt.show()


# # # counts,bins_edges=np.histogram(iris_setosa['petal_length'],bins=20,density=True)

# # # pdf=counts/sum(counts)
# # # plt.plot(bins_edges[1:],pdf)

# # # plt.show()

# # # cdf=np.cumsum(pdf)
# # # plt.plot(bins_edges[1:],cdf)
# # # plt.show()


# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns

# # # import numpy as np

# # # iris = pd.read_csv('IRIS_Data_Set.csv')

# # # # iris.plot(kind='scatter', x='petal_length', y='petal_width')

# # # g = sns.FacetGrid(iris, hue='species', height=4)
# # # g = g.map(plt.scatter, 'petal_length', 'petal_width')
# # # g = g.add_legend()
# # # plt.show()

# # # # Now check for the mean , median , mode , stddev, MAD

# # # iris_setosa = iris.loc[iris['species'] == 'setosa']
# # # iris_virginica = iris.loc[iris['species'] == 'virginica']
# # # iris_versicolor = iris.loc[iris['species'] == 'versicolor']

# # # print('Mean:')

# # # print(np.mean(iris_setosa['sepal_length']))
# # # print(np.mean(iris_virginica['sepal_length']))
# # # print(np.mean(iris_versicolor['sepal_length']))

# # # print('\n Median:')

# # # print(np.median(iris_setosa['sepal_length']))
# # # print(np.median(iris_virginica['sepal_length']))
# # # print(np.median(iris_versicolor['sepal_length']))

# # # print('\nstddev:')

# # # print(np.std(iris_setosa['sepal_length']))
# # # print(np.std(iris_virginica['sepal_length']))
# # # print(np.std(iris_versicolor['sepal_length']))

# # # print('\nMAD:')

# # # from statsmodels import robust as rb

# # # print(rb.mad(iris_setosa['sepal_length']))
# # # print(rb.mad(iris_virginica['sepal_length']))
# # # print(rb.mad(iris_versicolor['sepal_length']))

# # # print('\n 90 percentiles:')

# # # print(np.percentile(iris_setosa['sepal_length'], 90))
# # # print(np.percentile(iris_virginica['sepal_length'], 90))
# # # print(np.percentile(iris_versicolor['sepal_length'], 90))

# # # print('\n quantiles:')

# # # print(np.percentile(iris_setosa['sepal_length'], np.arange(0, 100, 25)))
# # # print(np.percentile(iris_virginica['sepal_length'], np.arange(0, 100, 25)))
# # # print(np.percentile(iris_versicolor['sepal_length'], np.arange(0, 100, 25)))


# # # # Box plots na whiskers

# # # sns.boxplot(data=iris, x='species', y='sepal_length')

# # # plt.show()

# # # sns.violinplot(data=iris, x='species', y='sepal_length')

# # # plt.show()

# # import os
# # z = os.getcwd()

# # # print(z)
# # # import zipfile

# # # zip_ref = zipfile.ZipFile('/Users/vsayarwar/Desktop/digit-recognizer.zip', 'r')

# # # zip_ref.extractall('/Users/vsayarwar/Desktop/')
# # # zip_ref.close()
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import seaborn as sns
# # # import numpy as np

# # # haberman = pd.read_csv('haberman.csv')

# # # haberman['Survival_status']=haberman[
# # # 'Survival_status'].map({1:'yes',2:'no'})

# # # # d = sns.FacetGrid(haberman, hue='Survival_status', height=4)
# # # # d = d.map(plt.hist, 'Age', bins=10)
# # # # d = d.add_legend()
# # # # plt.show()
# # # plt.xlabel('Age', fontsize=16)
# # # plt.hist(x=haberman['Age'], bins=10)
# # # plt.show()
# # # plt.xlabel('OperationYear', fontsize=16)
# # # plt.hist(x=haberman['OperationYear'], bins=10)
# # # plt.show()
# # # plt.xlabel('Axil_nodes', fontsize=16)
# # # plt.hist(x=haberman['Axil_nodes'], bins=10)
# # # plt.show()
# # # # plt.xlabel('Survival_status', fontsize=16)
# # # # plt.hist(x=haberman['Survival_status'], bins=10)
# # # # plt.show()

# # # print(haberman.describe())
# # # print(haberman['Survival_status'].value_counts())

# # # print('no of rows', str(haberman.shape[0]))
# # # print('no of columns', str(haberman.shape[1]))


# # # # Univariate Analysis

# # # for index, feature in enumerate(list(haberman.columns)[:-1]):
# # #     d=sns.FacetGrid(haberman,hue='Survival_status',height=4)
# # #     d=d.map(sns.distplot, feature)
# # #     d=d.add_legend()
# # #     plt.show()


# # # # Compute cdf

# # # for index, feature in enumerate(list(haberman.columns)[:-1]):
# # #     plt.subplot(1,3,index+1)
# # #     count,bin_edges=np.histogram(haberman[feature], bins=10, density=True)
# # #     pdf=count/sum(count)
# # #     cdf=np.cumsum(pdf)
# # #     plt.xlabel(feature,fontsize=16)
# # #     plt.plot(bin_edges[1:],pdf,bin_edges[1:],cdf)
# # #     plt.show()


# # # # Box plots

# # # for index, feature in enumerate(list(haberman.columns)[:-1]):
# # #     sns.boxplot(data=haberman,x='Survival_status',y=feature)
# # #     plt.show()


# # # for index, feature in enumerate(list(haberman.columns)[:-1]):
# # #     sns.violinplot(data=haberman,x='Survival_status',y=feature)
# # #     plt.show()

# # # # Multivariate Analysis

# # # sns.pairplot(haberman,hue='Survival_status',height=4)
# # # plt.show()

# # # # Bivariate anaysis using scatter plot

# # # for index,column in enumerate(list(haberman.columns)[:-1]):
# # #     for ind,clm in enumerate(list(haberman.columns)[:-1]):
# # #         d=sns.FacetGrid(haberman,hue='Survival_status',height=4)
# # #         d=d.map(plt.scatter,column,clm)
# # #         d=d.add_legend()
# # #         plt.show()


# # # # KS test

# # # # import numpy as np
# # # # import seaborn as sns
# # # # from scipy import stats
# # # # import matplotlib.pyplot as plt

# # # # x = stats.norm.rvs(size=1000)
# # # # sns.set_style('whitegrid')
# # # # sns.kdeplot(np.array(x), bw=2)
# # # # plt.show()


# # # # print(haberman.head())

# # # # print(haberman['Survival_status'].value_counts())

# # # # plt.plot(kind=hist, x=Age, )

# # # # Age,OperationYear,Axil_nodes,Survival_status

# # import os

# # z = os.getcwd()
# # print(z)

# # # import zipfile

# # # unzip_file=zipfile.ZipFile('/Users/vsayarwar/Desktop/digit-recognizer.zip'
# # # ,'r')

# # # unzip_file.extractall('/Users/vsayarwar/Documents/Python_Learning/AAIC
# # # ')

# # # unzip_file.close()


# # import pandas as pd

# # mnist_train = pd.read_csv('/Users/vsayarwar/Documents/Python_Learning/AAIC/MNISTDataSet/train.csv')

# # # print(mnist_train.head())

# # l = mnist_train['label']
# # d = mnist_train.drop('label', axis=1)

# # print(l.head())

# # print(l.shape)
# # print(l.value_counts())

# # print(d.shape)

# # # import matplotlib.pyplot as plt

# # # plt.figure(figsize=(7, 7))

# # # index = 1

# # # grid_data = d.iloc[index].as_matrix().reshape(28, 28)
# # # plt.imshow(grid_data, interpolation='none', cmap='gray')
# # # plt.show()


# # # Visualization using PCA

# # from sklearn.preprocessing import StandardScaler

# # standardized_data = StandardScaler().fit_transform(d)

# # print(standardized_data.shape)

# # sample_data = standardized_data
# # import numpy as np
# # covar_matrix = np.matmul(sample_data.T, sample_data)

# # print('the shape of covar matrix is ', covar_matrix.shape)

# # # fromscipy import linear algebra
# # from scipy.linalg import eigh

# # values, vectors=eigh(covar_matrix,eigvals=(782,783))

# # print('shape of eigen vectors = ', values.shape)

# # vectors =vectors.T

# # print('updated shape of vectors', vectors.shape)

# # import matplotlib.pyplot as plt

# # new_coordinates=np.matmul(vectors,sample_data.T)

# # print('resultant new data point shape',vectors.shape,'x',sample_data.T.shape,'=',new_coordinates.shape)



# # new_coordinates=np.vstack((new_coordinates,l)).T

# # print(new_coordinates.shape)

# # dataframe=pd.DataFrame(new_coordinates,columns=('1st_princ','2nd_princ','label'))

# # print(dataframe.head())


# # import seaborn as sns

# # sns.FacetGrid(dataframe,hue='label',size=4).map(plt.scatter,'1st_princ','2nd_princ').add_legend()

# # plt.show()


# # # PCA using sklearn

# # from sklearn import decomposition

# # pca=decomposition.PCA()

# # # now configure parameters

# # pca.n_components=2
# # pca_data=pca.fit_transform(sample_data)

# # print('shape of pca datra',pca_data.shape)

# # pca_data=np.vstack((pca_data.T,l)).T

# # pca_df=pd.DataFrame(pca_data,columns=('1st_princ','2nd_princ','label'))

# # sns.FacetGrid(pca_df,hue='label',size=4).map(plt.scatter,'1st_princ','2nd_princ').add_legend()

# # plt.show()



# # # PCA for dimensionality Reduction

# # pca.n_components=784

# # pca_data=pca.fit_transform(sample_data)
# # percentage_var_explained=pca.explained_variance_/np.sum(pca.explained_variance_)
# # cum_var_explained=np.cumsum(percentage_var_explained)


# # plt.figure(1,figsize=(6,4))



# # plt.clf()

# # plt.plot(cum_var_explained
# #     ,linewidth=2)


# # plt.axis('tight')

# # plt.grid()

# # plt.xlabel('n_components')
# # plt.ylabel('cum_var_explained')
# # plt.show()


# # # Tsne using sklearn
# # from sklearn.manifold import TSNE

# # model=TSNE(n_components=2,random_state=0)

# # tsne_data=model.fit_transform(sample_data)

# # tsne_data=np.vstack((tsne_data.T,l)).T

# # tsne_df=pd.DataFrame(tsne_data,columns=('Dim_1','Dim_2','Dim_class'))





# # sns.FacetGrid(tsne_df,hue='Dim_class',size=4).map(plt.scatter,'Dim_1','Dim_2').add_legend()

# # plt.show()


# import os

# print(os.getcwd())

# # import zipfile

# # zip_ref=zipfile.ZipFile('/Users/vsayarwar/Documents/Python_Learning/AAIC/database.sqlite.zip','r')

# # zip_ref.extractall('/Users/vsayarwar/Desktop')
# # zip_ref.close()


# import sqlite3
# import pandas as pd

# con=sqlite3.connect('database.sqlite')

# filtered_data=pd.read_sql_query(''' select * from Reviews Where Score !=3 LIMIT 5000''',con)

# # print(filtered_data.head())

# # print(filtered_data.columns)


# def partition(x):
#     if x<3:
#         return 0
#     return 1


# actual_score=filtered_data['Score']

# positive_negative=actual_score.map(partition)

# filtered_data['Score']=positive_negative

# print('no.of.data points in our data',filtered_data.shape)


# # print(filtered_data.head(3))


# display=pd.read_sql_query('''select userid, productid, profilename,time,score,text,count(*) from reviews
#     group by userid
#     having count(*)>1
#     ''',con)

# # print(display.head())

# print(display.columns)


# print(display[display['UserId']=='AZY10LLTJ71NX'])

# print(display['count(*)'].sum())


# soreted_data=filtered_data.sort_values('ProductId',axis=0,ascending=True, inplace=False,kind='quicksort',na_position='last')

# final=soreted_data.drop_duplicates(subset={'UserId','ProfileName','Time','Text'},keep='first',inplace=False)





# print(final.shape)


# # display=pd.read_sql_query('''select * from reviews where HelpfulnessNumerator >HelpfulnessDenominator''',con)

# # print(display.shape)
# print('@'*30)

# final=final[final.HelpfulnessNumerator<=final.HelpfulnessDenominator]

# # print('@'*30)
# print(final.shape)

# print(final['Score'].value_counts())



# print('@'*30)

# # EDA


# # Text preprocessing

# sent_0=final['Text'].values[0]

# print(sent_0)
# sent_1000=final['Text'].values[1000]

# print(sent_1000)
# print('@'*30)
# sent_1500=final['Text'].values[1500]
# print(sent_1500)

# print('@'*30)
# sent_4900=final['Text'].values[4900]
# print(sent_4900)

# # print('@'*30)


# # print('@'*30)

# print('@'*30)



# # Using regular expressions to remove Urls from text using python
# import re
# sent_0=re.sub(r"http\S+","",sent_0)
# # sent_0=re.sub(r"https?[a-zA-Z0-9./:;]+","",sent_0)
# sent_1000=re.sub(r'http\S+','',sent_1000)
# sent_1500=re.sub(r'http\S+','',sent_1500)
# sent_1000=re.sub(r'http\S+','',sent_4900)

# print(sent_0)


# from bs4 import BeautifulSoup

# print('&'*30)
# soup=BeautifulSoup(sent_0,'lxml')
# sent_0=soup.get_text()
# print(sent_0)
# print('&'*30)


# # print('&'*30)
# soup=BeautifulSoup(sent_1000,'lxml')
# sent_1000=soup.get_text()
# print(sent_1000)
# # print('&'*30)

# print('&'*30)
# soup=BeautifulSoup(sent_1500,'lxml')
# sent_1500=soup.get_text()
# print(sent_1500)
# # print('&'*30)

# print('&'*30)
# soup=BeautifulSoup(sent_4900,'lxml')
# sent_4900=soup.get_text()
# print(sent_4900)


# import re

# def decontracted(phrase):
#     phrase=re.sub(r"won't","will not",phrase)
#     phrase=re.sub(r"can't","can not",phrase)

#     phrase=re.sub(r"n't"," not",phrase)
#     phrase=re.sub(r"'re"," are",phrase)

#     phrase=re.sub(r"'s"," is",phrase)
#     phrase=re.sub(r"'d"," would",phrase)

#     phrase=re.sub(r"'ll"," will",phrase)
#     phrase=re.sub(r"'t"," not",phrase)

#     phrase=re.sub(r"'ve"," have",phrase)
#     phrase=re.sub(r"'m"," am",phrase)
#     return phrase

# print('$'*30)
# sent_1500=decontracted(sent_1500)
# print(sent_1500)
# print('$'*30)

# print('$'*30)
# sent_0=decontracted(sent_0)
# print(sent_0)

# print('$'*30)
# sent_1000=decontracted(sent_1000)
# print(sent_1000)

# print('$'*30)
# sent_4900=decontracted(sent_4900)
# print(sent_4900)


# sent_0=re.sub(r'\S*\d\S*','',sent_0).strip()

# print(sent_0)


# print('$'*30)


# sent_1000=re.sub(r'\S*\d\S*','',sent_1000).strip()

# print(sent_1000)


# print('$'*30)


# sent_1500=re.sub(r'\S*\d\S*','',sent_1500).strip()

# print(sent_1500)

# print('$'*30)


# sent_4900=re.sub(r'\S*\d\S*','',sent_4900).strip()

# print(sent_4900)


# print('#'*30)
# sent_0=re.sub(r'[^a-zA-Z0-9]+',' ',sent_0)
# print(sent_0)
# print('#'*30)

# # print('#'*30)
# sent_1000=re.sub(r'[^a-zA-Z0-9]+',' ',sent_1000)
# print(sent_1000)


# print('#'*30)
# sent_1500=re.sub(r'[^a-zA-Z0-9]+',' ',sent_1500)
# print(sent_1500)


# print('#'*30)
# sent_4900=re.sub(r'[^a-zA-Z0-9]+',' ',sent_4900)
# print(sent_4900)



# stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've","you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself','she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their','theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those','am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does','did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of','at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after','above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further','then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more','most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're','ve', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',"hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",'won', "won't", 'wouldn', "wouldn't"])


# from tqdm import tqdm
# preprocessed_reviews=[]

# for sentence in tqdm(final['Text'].values):
#     sentence=re.sub(r'http\S+','',sentence)
#     # sentence=re.sub()
#     sentence=BeautifulSoup(sentence,'lxml').get_text()
#     sentence=decontracted(sentence)
#     sentence=re.sub(r'\S*\d\S*','',sentence).strip()
#     sentence=re.sub(r'[^a-zA-Z0-9]+',' ',sentence)
#     sentence=' '.join(e.lower() for e in sentence.split() if e.lower() not in stopwords)
#     preprocessed_reviews.append(sentence.strip())

# # print(sentence)


# print(preprocessed_reviews[1500])


# # Featurization
# from sklearn.feature_extraction.text import  CountVectorizer

# print('---'*20)

# count_vect=CountVectorizer()
# count_vect.fit(preprocessed_reviews)
# print('some features names', count_vect.get_feature_names()[:10])

# print('---'*20)


# final_count=count_vect.transform(preprocessed_reviews)
# print('the type of count vectorizer',type(final_count))

# print('the shape of BOW vectorizer',final_count.get_shape())

# print('the no of unique words',final_count.get_shape()[1])
# print('%'*40)

# # Bi grams and N grams

# count_vect=CountVectorizer(ngram_range=(1,2),min_df=10,max_features=5000)


# # Bi grams and n-grams

# count_vect=CountVectorizer(ngram_range=(1,2))
# final_grams=count_vect.fit_transform(preprocessed_reviews)
# print('type',type(final_grams))
# print('unique word',final_grams.get_shape())


# # TF-IDF

# from sklearn.feature_extraction.text import TfidfVectorizer

# print('='*40)
# tf_idf_vect=TfidfVectorizer(ngram_range=(1,2),min_df=10)

# tf_idf_vect.fit(preprocessed_reviews)

# print('some sample reviews',tf_idf_vect.get_feature_names()[0:10])

# print('='*40)

# final_tf_idf=tf_idf_vect.transform(preprocessed_reviews)

# print('type',type(final_tf_idf))
# print('size',final_tf_idf.get_shape())
# print('no of uni words',final_tf_idf.get_shape()[1])



# # Word2 vectorizer


# from gensim.models import Word2Vec

# i=0
# list_of_sentence=[]
# for sentence in preprocessed_reviews:
#     list_of_sentence.append(sentence.split())
# print('#@$'*30)

# # print(list_of_sentence)





# is_your_ram_gt_16g=False
# want_to_use_google_w2v = False
# want_to_train_w2v = True

# if want_to_train_w2v:
#     w2v_model=Word2Vec(list_of_sentence,min_count=5,size=50,workers=4)
#     print(w2v_model.wv.most_similar('great'))
#     print('='*40)
#     print(w2v_model.wv.most_similar('worst'))
# elif want_to_use_google_w2v and is_your_ram_gt_16g:
#     if os.path.isfile('GoogleNews-vectors-negative300.bin'):
#         # w2v_model=Word2Vec(list_of_sentence,min_count=5,size=50,workers=4)
#         w2v_model=KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',binary=True)
#         print(w2v_model.wv.most_similar('great'))
#         print(w2v_model.wv.most_similar('worst'))
#     else:
#         print('yoflsflksaf')


# w2v_words=list(w2v_model.wv.vocab)
# print(len(w2v_words))

# print('*'*20)

# print('sample words',w2v_words[0:50])



# # # Avg w2v and Tfidfw2V

# import numpy as np

# sent_vectors=[]
# for sent in tqdm(list_of_sentence):
#     sent_vec=np.zeros(50)
#     cnt_words=0
#     # print(sent_vec)
#     for word in sent:
#         if word in w2v_words:
#             vec=w2v_model.wv[word]
#             # print(vec)
#             sent_vec+=vec
#             cnt_words+=1
#     if cnt_words != 0:
#         sent_vec/=cnt_words
#     sent_vectors.append(sent_vec)

# print(len(sent_vectors))
# print(len(sent_vectors[0]))



# # TFIDF w2v
# model=TfidfVectorizer()
# model.fit(preprocessed_reviews)
# dictionary=dict(zip(model.get_feature_names(),list(model.idf_)))


# tfidf_feat=model.get_feature_names()

# tfidf_sent_vectors=[]
# row=0
# for sent in tqdm(list_of_sentence):
#     sent_vec=np.zeros(50)
#     weight_sum=0
#     for word in sent:
#         if word in w2v_words and word in tfidf_feat:
#             vec=w2v_model.wv[word]
#             tf_idf=dictionary[word]*(sent.count(word)/len(sent))
#             sent_vec+=(vec * tf_idf)
#             weight_sum+=tf_idf
#     if weight_sum != 0:
#         sent_vec /= weight_sum
#     tfidf_sent_vectors.append(sent_vec)
#     row+=1





# # Now applyin TSNE


# import numpy as np
# from sklearn.manifold import TSNE
# from sklearn import datasets
# import pandas as pd
# import matplotlib.pyplot as plt

# iris=datasets.load_iris()
# x=iris['data']
# y=iris['target']

# tsne=TSNE(n_components=2,perplexity=30,learning_rate=200)

# x_embedding=tsne.fit_transform(x)
# print('^&^'*40)
# # print(x_embedding)






# for_tsne=np.hstack((x_embedding,y.reshape(-1,1)))
# # print(for_tsne)

# for_tsne_df=pd.DataFrame(data=for_tsne,columns=['Dimensions_x','Dimensions_Y','Score'])

# colors={0:'red',1:'blue',2:'green'}

# plt.scatter(for_tsne_df['Dimensions_x'],for_tsne_df['Dimensions_Y'],c=for_tsne_df['Score'].apply(lambda x: colors[x]))

# plt.show()






# Applying TSNE on Text BOW vectors






import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# connection variable

con=sqlite3.connect('database.sqlite')

# Fetching data from reviews other than score=3


filtered_data=pd.read_sql_query(''' select * from Reviews Where Score !=3 limit 4000''',con)


# Using function to make score 4,5 to 1(positive review) and score 1,2 to 0 (negative Review)

def partition(x):
    if x<3:
        return 0
    return 1

# Now storing  the label columns tpo the variable actual_score

actual_score=filtered_data['Score']

# Now mapping +ve(score =4 or 5) reviews to 1 and -ve (score < 3)

positive_negative=actual_score.map(partition)

filtered_data['Score']=positive_negative

print('no.of.data points in our data',filtered_data.shape)


# print(filtered_data.head(3))

soreted_data=filtered_data.sort_values('ProductId',axis=0,ascending=True, inplace=False,kind='quicksort',na_position='last')

final=soreted_data.drop_duplicates(subset={'UserId','ProfileName','Time','Text'},keep='first',inplace=False)


print(final.shape)


# display=pd.read_sql_query('''select * from reviews where HelpfulnessNumerator >HelpfulnessDenominator''',con)

# print(display.shape)
print('@'*30)

final=final[final.HelpfulnessNumerator<=final.HelpfulnessDenominator]

# print('@'*30)
print(final.shape)

print(final['Score'].value_counts())

# filtered_data=final['Score']



print('@'*30)


import re

def decontracted(phrase):
    phrase=re.sub(r"won't","will not",phrase)
    phrase=re.sub(r"can't","can not",phrase)

    phrase=re.sub(r"n't"," not",phrase)
    phrase=re.sub(r"'re"," are",phrase)

    phrase=re.sub(r"'s"," is",phrase)
    phrase=re.sub(r"'d"," would",phrase)

    phrase=re.sub(r"'ll"," will",phrase)
    phrase=re.sub(r"'t"," not",phrase)

    phrase=re.sub(r"'ve"," have",phrase)
    phrase=re.sub(r"'m"," am",phrase)
    return phrase

stopwords= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've","you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself','she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their','theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those','am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does','did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of','at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after','above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further','then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more','most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're','ve', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',"hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't",'won', "won't", 'wouldn', "wouldn't"])


from tqdm import tqdm
preprocessed_reviews=[]

for sentence in tqdm(final['Text'].values):
    sentence=re.sub(r'http\S+','',sentence)
    # sentence=re.sub()
    sentence=BeautifulSoup(sentence,'lxml').get_text()
    sentence=decontracted(sentence)
    sentence=re.sub(r'\S*\d\S*','',sentence).strip()
    sentence=re.sub(r'[^a-zA-Z0-9]+',' ',sentence)
    sentence=' '.join(e.lower() for e in sentence.split() if e.lower() not in stopwords)
    preprocessed_reviews.append(sentence.strip())


# Featurization
# from sklearn.feature_extraction.text import  CountVectorizer

# print('---'*20)

# count_vect=CountVectorizer()
# count_vect.fit(preprocessed_reviews)
# print('some features names', count_vect.get_feature_names()[:10])

# print('---'*20)


# final_count=count_vect.transform(preprocessed_reviews)
# print('the type of count vectorizer',type(final_count))

# print('the shape of BOW vectorizer',final_count.get_shape())

# print('the no of unique words',final_count.get_shape()[1])
# print('%'*40)

# import numpy as np

# tsne_data=final['Score']

# print(tsne_data.shape)

# from scipy import sparse



# print(type(tsne_data))
# # tsne_data=np.array(tsne_data)
# print('&^*%'*40)
# # print(type(tsne_data))

# print('&^*%'*40)
# print(type(final_count))
# print(final_count.shape)

# final_count=final_count.toarray()

# final_count_df=pd.DataFrame(data=final_count)
# # final_count=np.array(final_count)

# print('&^*%'*40)
# print(type(final_count))
# print(final_count.shape)

# # print(type(final_count_df))

# import numpy as np
# from sklearn.manifold import TSNE
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# tsne=TSNE(n_components=2,perplexity=20, learning_rate=200)


# final_count=tsne.fit_transform(final_count)

# print(final_count.shape)

# tsne_data_final=np.hstack((final_count,tsne_data.values.reshape(-1,1)))

# print(tsne_data_final.shape)

# for_tsne_df=pd.DataFrame(data=tsne_data_final,columns=['Dimension_x','Dimension_y','Score'])

# # 8008699008

# sns.FacetGrid(for_tsne_df, hue='Score', size=4).map(plt.scatter,'Dimension_x','Dimension_y' ).add_legend()

# plt.title('TSNE VISUALIZATION OF REVIEWS')

# plt.show()


# print('*&^%'*40)


# # colors={}





# # print(tsne_data.values.reshape(-1,1).shape)

# print(type(tsne_data_final))

# print(tsne_data_final.shape)

# # tsne_data_final=pd.concat([tsne_data,final_count_df],ignore_index=True)

# # # tsne_data_final = pd.concat([tsne_data, final_count_df], axis=1, join_axes=[tsne_data.index])


# # print('&*%$'*40)

# # print(type(tsne_data_final))

# # print(tsne_data_final.shape)

# # # tsne_data_final_df=DataFrame(data=tsne_data_final,columns=[])



# # # # tsne_final=np.hstack(())


# Applying TSNE on Text TFIDF


from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np

import scipy.sparse

import matplotlib.pyplot as plt

# tf_idf_vect=TfidfVectorizer(ngram_range=(1,2), min_df=10)

# tf_idf_vect=tf_idf_vect.fit(preprocessed_reviews)



# final_tf_idf=tf_idf_vect.transform(preprocessed_reviews)

# print(final_tf_idf.shape)

# final_score=final['Score']

# print(final_score.shape)

# from sklearn.manifold import TSNE

# tsne=TSNE(n_components=2, perplexity=20, learning_rate=20)

# tsne_final=tsne.fit_transform(final_tf_idf.toarray())

# final_tf_idf_hstack=np.hstack((tsne_final,final_score.values.reshape(-1,1)))

# print(final_tf_idf_hstack.shape)



# import seaborn as sns

# final_tf_idf_hstack_df=pd.DataFrame(data=final_tf_idf_hstack, columns=('1st_DIM','2nd_DIM','Class'))

# sns.FacetGrid(data=final_tf_idf_hstack_df,hue='Class',size=4).map(plt.scatter,'1st_DIM','2nd_DIM').add_legend()

# plt.title('TFIDF-TSNE')

# plt.show()



# Applying TSNE on Text Avg w2v


from gensim.models import Word2Vec
i=0

list_of_sentence=[]
for sentence in preprocessed_reviews:
    list_of_sentence.append(sentence.split())

if True:
    w2v_model=Word2Vec(list_of_sentence,min_count=5,size=50,workers=4)

print(w2v_model.vector_size)
w2v_words=list(w2v_model.wv.vocab)

















































































































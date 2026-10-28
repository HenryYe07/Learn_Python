class Person():
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speek(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Worker:
    def __init__(self,company):
        self.company = company
    def do_work(self):
        print(f"在{self.company}工作")

class Student(Person,Worker):
    def __init__(self,name,age,gender,company,stu_id,grade):
        # super() 拿到的是第一个超类
        # 这里调用超类的init就必须用类名写
        Person.__init__(self,name,age,gender)
        Worker.__init__(self,company)

        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f"我是{self.name},我学了一下")

s1 = Student("张三",18,"男","Mcd","0001","初二")

# 先照 Student自己 然后去找 Person 然后去找 Worker
print(Student.__mro__)
# 先找实例自身的属性，如果没有就按照类的__mro__的顺序去找
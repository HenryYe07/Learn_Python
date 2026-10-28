class Person():
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speek(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Student(Person):
    def __init__(self,name, age,gender,stu_id,grade):
        # 方式 1 (推荐)
        super().__init__(name,age,gender)
        # super()的作用是拿到父类的实例

        # 方式 2
        # Person.__init__(self,name,age,gender)
        # 这样弄self要自己传 因为 拿到的是父类本身

        self.stu_id = stu_id
        self.grade = grade

    # 方法重写： 子类中出现了一个和父类中相同名字的方法，就会被重写 不过在里面用super()还是可以拿到父类的
    def speek(self):
        super().speek()
        print("这是在Student类里面的")

    def study(self):
        print(f"学生{ self.name }学了一下")



s1 = Student("Aaa",20,"M",123,1)
print(s1.__dict__)
print(type(s1))
# def speek():
#     print("这是直接加在s1的speek")
# s1.speek = speek
s1.speek()
s1.study()

# 两个实用函数
f1 = isinstance(s1,Student) # 判断 s1是不是Student或者Student子类的实例
f2 = issubclass(Student,Person) # 判断 Student是不是Person的子类
print(f1,f2)
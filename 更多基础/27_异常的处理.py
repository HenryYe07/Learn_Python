# 错误 关键字写错 括号写错 这样的语法错误 没有办法通过错误处理机制处理掉

# 异常 语法没问题 但是执行有问题
# 常见的：
# 除0 某个实例没有某个字段
print("Hello")


# 捕获全部异常
try:
    a = int(input("请输入一个数字"))
    b = int(input("请输入另一个数字"))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("程序出现了异常")


# 捕获指定类型的异常

try:
    a = int(input("请输入一个数字"))
    b = int(input("请输入另一个数字"))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("程序出现了异常 0不能作为除数")
except ValueError:
    print("程序出现了异常 你输入的不是整数")
except Exception:
    # 从上往下匹配 如果上面的匹配成功了，下面的就不会匹配 （因为错误类存在继承关系）
    # 所以这个范围特别大的要放在最下面
    print("未知错误")

# 异常类型的继承关系
print(issubclass(ZeroDivisionError, ArithmeticError))

# 获取异常的具体信息
try:
    a = int(input("请输入一个数字"))
    b = int(input("请输入另一个数字"))
    result = a / b
    print(x)
except (ZeroDivisionError,ValueError):
    print("程序出现了异常 0不能作为除数")
except ValueError:
    print("程序出现了异常 你输入的不是整数")
except Exception as e:
    print(f"未知错误{e}") # 'x' is not defined
    print(type(e)) # <class 'NameError'>
    print(e.__traceback__.tb_frame.f_code.co_filename)



# 错误会一层一层往外，一直没有处理最终就是程序报错

# 手动抛出异常
try:
    raise ValueError("年龄应该为0～120的整数")
except ValueError:
    pass

# 自定义异常类
class DefinedError(Exception):
    pass
raise DefinedError()






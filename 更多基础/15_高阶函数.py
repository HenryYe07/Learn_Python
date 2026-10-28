# 传入的参数是函数或者返回值是函数

def info(msg):
    return '[提示]' + msg

def warn(msg):
    return '[警告]' + msg

def error(msg):
    return '[错误 ]' + msg

def log(func,text):
    print(func(text))

log(info,'文件保存成功')
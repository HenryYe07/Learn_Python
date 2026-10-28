更多基础.try_package.tools.test_tool()

import try_package.tools as tool
tool.test_tool()

# from 包名 import * 只能导进来__init__.py 里 import 过的内容

from collections import Counter
names = ["张三","李四","王五","李华","王五","王五","王五","王五","李华","李华","李华"]
result = Counter(names)
print(result)

import pyfiglet
res2 = pyfiglet.figlet_format("Hello")
print(res2)

from faker import Faker
f = Faker("zh_CN")
print(f.name())
print(f.address())
#存放被测试项目基本信息，如url地址等

# os 模块是 Python 标准库的一部分，提供了一些与操作系统交互的功能。
# 它允许你执行许多与文件系统和操作系统相关的操作，例如文件和目录的创建、删除、重命名，获取环境变量，执行系统命令等
import os

# 设置项目环境域名
BASE_URL = "http://kdtx-test.itheima.net"

# 获取项目根路径
BASE_PATH = os.path.dirname(__file__)
# log_path = os.path.join(profile_path)
print(BASE_PATH)
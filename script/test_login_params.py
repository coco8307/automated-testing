# 导包
import config
from api.login import LoginAPI
import pytest
import json

# # 测试数据
# test_data=[
#     ("admin","HM_2023_test",200,"成功",200),
#     ("","HM_2023_test",200,"错误",500),
#     ("admin4568891","HM_2023_test",200,"错误",500)
# ]

# 读取json文件
def build_data(json_file):
    # 定义空列表
    test_data = []
    # 打开json文件
    with open(json_file,"r",encoding='UTF-8') as f:
        # 加载json文件数据
        json_data = json.load(f)
        # 循环遍历测试数据
        for case_data in json_data:
            # 转换数据格式 [{},{}] --> [(),()]
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            code = case_data.get("code")
            test_data.append((username,password,status,message,code))
    # 返回处理之后测试数据
    return test_data

# 创建测试类
class TestLoginAPI:
    # 初始化
    uuid = None
    # 前置处理
    def setup_method(self):
        self.login_api = LoginAPI()
        # 获取验证码
        response = self.login_api.get_verify_code()
        print(response.json())
        # 提取验证码接口返回的uuid参数值
        TestLoginAPI.uuid = response.json().get("uuid")
        print(TestLoginAPI.uuid)

    # 后置处理
    def teardown(self):
        pass

    # 登录成功
    @pytest.mark.parametrize("username,password,status,message,code",build_data(json_file= config.BASE_PATH + "/data/login.json"))
    # @pytest.mark.parametrize("username,password,status,message,code",build_data(json_file="../data/login.json"))
    def test_success(self,username,password,status,message,code):
        login_data = {"username":username,"password":password,"code":"2","uuid":TestLoginAPI.uuid}
        response = self.login_api.login(test_data=login_data)
        # 断言响应状态码为200
        assert status == response.status_code
        # 断言响应数据包含'成功'
        assert message in response.text
        # 断言响应json数据中code值
        assert code == response.json().get("code")


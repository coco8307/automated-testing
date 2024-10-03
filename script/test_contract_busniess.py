# 导包
import config
from api.login import LoginAPI
from api.course import CourseAPI
from api.contract import ContractAPI

# 创建测试类
class TestContractBusniess:
    # 初始化
    # token保存成类属性，在下方使用时可以直接通过类调用
    token = None

    # 前置处理(每个测试方法前需要准备的操作)
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        self.contract_api = ContractAPI()

    # 后置处理(测试方法运行之后的操作)
    def teardown(self):
        pass

    # 1.登录成功
    def test_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        print(res_v.json().get("uuid"))
        # 登录
        test_data={"username":"admin","password":"HM_2023_test","code":"2","uuid":res_v.json().get("uuid")}
        res_l = self.login_api.login(test_data = test_data)
        print(res_l.status_code)
        print(res_l.json())
        # 提取登录成功之后的token数据并保存在类的属性中
        TestContractBusniess.token = res_l.json().get("token")
        print(TestContractBusniess.token)

    # 2.课程新增成功
    def test_add_course(self):
        add_data = {"name":"测试开发提升课01","subject":"6","price":899,
                    "applicablePerson":"2","info":"测试开发提升课01"}
        res_c = self.course_api.add_course(test_data = add_data,token = TestContractBusniess.token)
        print(res_c.json())

    # 3.合同上传成功
    def test_upload(self):
        # 读取文件数据
        # f = open("../data/ht.pdf","rb")
        f = open(config.BASE_PATH + "/data/ht.pdf","rb")
        # f = open("../data/合同文件.doc","rb")
        res_u = self.contract_api.upload_contract(test_data= f,token = TestContractBusniess.token)
        print(res_u.json())

    # 4.合同新增
    def test_add_contract(self):
        add_data = {"name":"测试888","phone":"18712345678","contractNo":"HT20240720181715649",
                        "subject":"6","courseId":"99","channel":"0","activityId":77,"fileName":"xxx"}
        response =self.contract_api.add_contract1(test_data=add_data,token = TestContractBusniess.token)
        print(response.json())
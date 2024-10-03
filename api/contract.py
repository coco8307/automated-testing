# 上传合同文件、新增合同文件

# 导包
import requests
import config
# 创建接口类
class ContractAPI:

    # 初始化
    def __init__(self):
        # self.url_upload = "http://kdtx-test.itheima.net/api/common/upload"
        self.url_upload = config.BASE_URL + "/api/common/upload"
        # self.add_contract = "http://kdtx-test.itheima.net/api/contract"
        self.add_contract = config.BASE_URL + "/api/contract"

    # 合同上传接口
    def upload_contract(self,test_data,token):
        # return requests.post(url = self.url_upload,files=test_data,headers={"Authorization":token})
        return requests.post(url=self.url_upload, files={"file":test_data}, headers={"Authorization": token})

    # 合同新增
    def add_contract1(self,test_data,token):
        return requests.post(url=self.add_contract, json=test_data, headers={"Authorization": token})

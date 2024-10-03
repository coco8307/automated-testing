# 课程模块接口封装:
# 核心在于依据接口文档实现接口信息封装、重点关注接口如何被调用

# 导包
import requests
import config
#创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        # self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"
        # self.url_select_course = "http://kdtx-test.itheima.net/api/clues/course/list"
        self.url_add_course = config.BASE_URL + "/api/clues/course"
        self.url_select_course = config.BASE_URL + "/api/clues/course/list"

    # 课程添加
    def add_course(self,test_data,token):
        return requests.post(url=self.url_add_course,json=test_data,headers={"Authorization":token})

    # 课程查询
    def select_course(self,test_data,token):
        return requests.get(url=self.url_select_course + f"/{test_data}",headers={"Authorization":token})
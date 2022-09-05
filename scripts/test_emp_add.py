# coding=utf-8
import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_resp
from config import TEL


class TestEmpAdd(unittest.TestCase):
    # 类属性
    header = None

    @classmethod
    def setUpClass(self) -> None:
        self.header = get_resp()

    # def setUp(self) -> None:
    #     # 删除手机号
    #     delete_sql = f"delete from bs_user where mobile = '{TEL}'"
    #     DBUtil.uid_db(delete_sql)
    #
    # def tearDown(self) -> None:
    #     # 删除手机号
    #     delete_sql = f"delete from bs_user where mobile = '{TEL}'"
    #     DBUtil.uid_db(delete_sql)

    # 必选参数
    def test01_add_emp(self):
        json_data = {
            "username": "女娲接4",
            "mobile": "13959938002",
            "formOfEmployment": 1,
            "workNumber": "251315",
            "departmentName": "总裁办",
            "timeOfEntry": "2022-08-20T16:00:00.000Z",
            "correctionTime": "2022-08-24T16:00:00.000Z"
        }
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加-必选：", resp.json())
        print(self.header)
        print(resp.status_code)
        print("success", resp.json().get("success"))
        print("code", resp.json().get("code"))
        print("message", resp.json().get("message"))
        # 断言
        assert_util(self, resp, 200, True, 10000, "员工新增成功")

    # 组合参数
    def test02_add_emp(self):
        # 准备数据
        json_data = {
            "username": "女娲接4",
            "mobile": "13959938002",
            "formOfEmployment": 1,
            "workNumber": "251315",
            "departmentName": "总裁办",
            "timeOfEntry": "2022-08-20T16:00:00.000Z",
            "correctionTime": "2022-08-24T16:00:00.000Z"
        }
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加-组合：", resp.json())
        print(self.header)
        print(resp.status_code)
        print("success", resp.json().get("success"))
        print("code", resp.json().get("code"))
        print("message", resp.json().get("message"))
        # 断言
        assert_util(self, resp, 200, True, 10000, "员工新增成功")

    # 全部参数
    def test03_add_emp(self):
        # 准备数据
        json_data = {
            "username": "女娲接4",
            "mobile": "13959938002",
            "formOfEmployment": 1,
            "workNumber": "251315",
            "departmentName": "总裁办",
            "timeOfEntry": "2022-08-20T16:00:00.000Z",
            "correctionTime": "2022-08-24T16:00:00.000Z"
        }
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print("添加 - 全部 =", resp.json())
        print(self.header)
        print(resp.status_code)
        print("success", resp.json().get("success"))
        print("code", resp.json().get("code"))
        print("message", resp.json().get("message"))
        # 断言
        assert_util(self, resp, 200, True, 10000, "员工新增成功")

# coding=utf-8
"""获取登录成功的令牌，拼接到请求头，返回"""

# 定义函数
import requests


def get_resp():
    url = "http://ihrm.itheima.net/prod-api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url, json=data)
    print(resp.json())

    # 从 响应体中，获取 data的值
    token = resp.json().get("data")
    print(token)
    header = {"Content-Type": "application/json;charset=UTF-8",
              "Authorization": "Bearer " + token}

    return resp


def get_header():
    url = "http://ihrm.itheima.net/prod-api/sys/login"
    data = {"mobile": "13800000002", "password": "123456"}
    resp = requests.post(url=url, json=data)
    print(resp.json())

    # 从 响应体中，获取 data的值
    token = resp.json().get("data")
    print(token)
    header = {"Content-Type": "application/json;charset=UTF-8",
              "Authorization": "Bearer " + token}

    return resp


if __name__ == '__main__':
    get_resp()

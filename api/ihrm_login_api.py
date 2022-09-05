import requests


class IhrmLoginApi(object):
    # µÇÂ¼·½·¨
    @classmethod
    def login(cls, json_data):
        url = "http://ihrm.itheima.net/prod-api/sys/login"
        header = {"Content-Type": "application/json;charset=UTF-8"}
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp


if __name__ == '__main__':
    data = {"mobile": "13800000002", "password": "123456"}
    resp = IhrmLoginApi.login(data)
    print(resp.json())

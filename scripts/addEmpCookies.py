import requests

url = "http://ihrm.itheima.net/prod-api/sys/login"
data = {"mobile": "13800000002", "password": "123456"}
resp = requests.post(url=url, json=data)

print(resp.json())
print("88", resp.cookies)

# 从 响应体中，获取 data的值
token = resp.json().get("data")
print(token)
header = {"Content-Type": "application/json",
          "Authorization": "Bearer " + token}
print("88", header)
json_data = {
    "username": "女娲接4",
    "mobile": "13959938002",
    "formOfEmployment": 1,
    "workNumber": "251315",
    "departmentName": "总裁办",
    "timeOfEntry": "2022-08-20T16:00:00.000Z",
    "correctionTime": "2022-08-24T16:00:00.000Z"
}

url = "http://ihrm.itheima.net/prod-api/sys/user"
# respo = requests.post(url=url, headers=header, json=json_data)   requests.post必须加cookies的值 session不用！
respo = requests.post(url=url, headers=header, json=json_data, cookies=resp.cookies)
print(respo.json())





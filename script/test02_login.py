# 需求：登录成功

# 导包
import requests

# 发送请求
url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": "7228e602ac1442ef8bd63970f313de5f"
}
response = requests.post(url=url, headers=header_data, json=login_data)

# 查看响应
print(response.status_code)
print(response.json())


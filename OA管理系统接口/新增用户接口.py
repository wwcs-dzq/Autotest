import requests

url = "http://192.168.113.130/prod-api/system/user"


hearder = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA",
    "Content-Type":"application/json;charset=UTF-8"
}

canshu = {"userName":"10086","nickName":"10087","password":"123456","sex":"0","status":"0","postIds":[],"roleIds":[]}

response = requests.post(url=url,json=canshu,headers=hearder)
print(response.json())
import requests


url = "http://192.168.113.130/prod-api/system/menu"

canshu = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA",
    "Content-Type":"application/json;charset=UTF-8"
}

data = {"parentId":0,"menuName":"菜单123","menuType":"M","orderNum":2,"isFrame":"1","isCache":"0","visible":"0","status":"0","path":"didi1234567"}

response = requests.post(url=url,json=data,headers=canshu)
print(response.json())
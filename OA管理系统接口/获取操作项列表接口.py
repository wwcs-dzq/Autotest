
import requests

baseUrl = "http://192.168.113.130/prod-api"
url = "/system/menu/treeselect"

canshu = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA"
}
response = requests.get(url=baseUrl+url,headers=canshu)
print(response.json())
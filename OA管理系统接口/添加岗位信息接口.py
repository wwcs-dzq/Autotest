import  requests


url = "http://192.168.113.130/prod-api/system/post"

canshu ={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA",
    "Content-Type":"application/json;charset=UTF-8"
}

data ={"postCode":"user02","postName":"普通员工02","postSort":5,"status":"0"}

response = requests.post(url=url,json=data,headers=canshu)
print(response.json())
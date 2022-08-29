import requests


url = "http://192.168.113.130/prod-api/monitor/online/list"

canshu = {
"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA",
    "Accept":"application/json, text/plain, */*",
    "Cookie":"username=admin; rememberMe=true; password=av+NbBO1n8fMDIzS1QH3rX5kskMx1lRDEXDt5ebWB4O29xfNdJjT2NNc2eZz1IU4W1uAAWBRUuLMSAAe/Ej3xw==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA"
}


response =requests.get(url=url,headers=canshu)
print(response.json())

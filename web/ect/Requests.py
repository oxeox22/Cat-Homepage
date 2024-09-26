import requests     

url='http://localhost:55644/index.php'
data={'usernae':'babo','password':'babo1234'}
response=requests.post(url, data=data, allow_redirects=False)

cookies=response.cookies
##print(response)
print(cookies)
for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")


import requests

def login():
    try:
        # 登录之后界面的url
        urllogin="http://www.cqooc.com/user/login?username=12608199000635&password=48C032612C2A6777D28A969307B52127E198D59AA78522943C1B283CF7B89E69&nonce=6BA36BBB1F623279&cnonce=8257070573EFE28F"
        s=requests.session()
        r=s.post(urllogin,data=Form,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return s
    except Exception as error:
        print(error)

def get_html(s,url):
    try:
        r=s.get(url,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except Exception as error:
        print(error)

if __name__=="__main__":
    # 登录之后的界面user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    }
    # 跟着自己的改变
    Form = {
        "username": "12608199000635",
        "password": "48C032612C2A6777D28A969307B52127E198D59AA78522943C1B283CF7B89E69",
        "nonce": "6BA36BBB1F623279",
        "cnonce": "8257070573EFE28F"
    }
    lin=login()
    # 个人中心的网址
    url="http://www.cqooc.com/my/learn"
    html=get_html(lin,url)
    print(html)
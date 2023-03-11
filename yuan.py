
import requests
def image(url,time=10):
    try:
        r = requests.get(url,timeout=time)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        return r.content
    except:
        return "产生异常"
def save(path,content):
    with open(path,"wb") as f:
        f.write(content)
if __name__=="__main__":#main函数，流程设计
    url_list = ["https://qq.yh31.com/tp/lg/202103012208111470.jpg",
                "https://qq.yh31.com/tp/lg/202103012212431276.jpg"] #多图片列表
    for url in url_list: #循环遍历
        imag_content=image(url)
        dir = "D:\python"
        file_name = url.split("/")[-1:][0]
        path = dir + file_name
        save(path,imag_content)

import requests
def download_pic(url):
    print(f"开始下载{url}")

    # 发请求获取图片
    response = requests.get(url)

    print("下载完毕")

    # 保存图片到本地
    with open(f"{url[-10:]}","wb") as f:
        f.write(response.content)
def main():
    url_list = [
        "http://www.jxufe.edu.cn/uploadfile/186/202610/93f0163a1b.jpg",
        "http://www.jxufe.edu.cn/uploadfile/186/202610/4af585d8b2.jpg",
        "http://www.jxufe.edu.cn/uploadfile/186/202610/8dd85768d1.jpg"
    ]

    for url in url_list:
        download_pic(url)
main()
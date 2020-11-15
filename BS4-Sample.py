from bs4 import BeautifulSoup
import requests

resp = requests.get("https://club.autohome.com.cn/bbs/thread/2d1cec98f0060804/91118718-1.html#pvareaid=102410",
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
print(resp)
bs=BeautifulSoup(resp.text,"html.parser")
divs = bs.find_all("div",attrs={"class":"tz-picture"})
for div in divs:
    imgs = div.find_all("img")
    for img in imgs:
        #print(img.get("data-src"))
        src=img.get("data-src")
        src="http:"+src
        with open(f"{n}.jpg",mode="wb") as f:
            f.write(requests.get(src).content)
        n+=1
        print("Done")
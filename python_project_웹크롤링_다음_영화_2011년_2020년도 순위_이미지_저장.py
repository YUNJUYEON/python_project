import requests
from bs4 import BeautifulSoup

year: int
for year in range(2011, 2021):    
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")
    imgages=soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(imgages):
        # print(image["src"])
        image_url=image["src"]
        if image_url.startswith("//"):
            image_url="https: "+image_url
        print(image_url)
        image_res=requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx>=30: 
            # 상위 31개 이미지까지만 다운로드
            break

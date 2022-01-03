"""from bs4 import BeautifulSoup
with open("index.html","r") as f:
    doc = BeautifulSoup(f, "html.parser")
    print(doc.prettify())
tag = doc.title
tag.string = "hello"  #modify title name
print(tag)"""

"""tags = doc.find_all("p")
print(tags)"""


from bs4 import BeautifulSoup
import requests
url = "https://www.flipkart.com/comfybean-xl-designer-bean-bag-filled-beans-barely-awake-teardrop-filling/p/itmeee4f25e9084f?pid=BEBFWE4YQ7Q92SGD&lid=LSTBEBFWE4YQ7Q92SGD2QEKH4&marketplace=FLIPKART&store=wwe&srno=b_1_1&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_5_4.dealCard.OMU_JOETTIUUM7A0_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_5"
result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
print(doc.prettify())

import requests
from bs4 import BeautifulSoup

url = 'https://www.ebay.com/itm/374984751956?hash=item574ed53b54%3Ag%3AcgkAAOSwYUdkNWH7&amdata=enc%3AAQAIAAAA4DwynUvV8lSlfiBheFbMsCqEcp6v4Z3J7niE%2FBn2bOTztayY%2Bd%2BC25L2sfjdlrqYlrBgMW92vhOR%2Fr7wf7bjmhebwEwGOH2FYtZh0RYVetd%2BmYnM63O8kPOhcFoTlW9RcE22Lw5uH1HWdBDhGgu2CDsinu3h4zKMzSAc0rbs%2FSVjaf6FAKz5Nb833wv6uFtKTYghXjH0pPer82btRU73pwgskhQjmO4MFj8h33affqyV%2BXVdRkU%2BC32YNJ5tVRmQYBB5qqvg8Rw5X23YapAxGAGIwiU5fYuJzByL7XmrLQqc%7Ctkp%3ABk9SR_Dk27DnYg&LH_BIN=1'

# url = 'https://www.ebay.com/itm/266456985161?hash=item3e0a12ee49%3Ag%3A8mUAAOSw2HhlLEW6&amdata=enc%3AAQAIAAAA4H66eeCKhgsxHURLkPYTXie7oywIkJh%2FtRk3h3lN8GPSSlVK9MIm4Ccaj1Q%2Bqcio088cx2hhC4dgGPNcrZKKxXDrpvINRcUwRkOpDppY4ww%2By32pXQ115WL0cHFi1SSesl7sDT%2Fl98BbSHywPRjvSp6u0WNI0AC5Ev4emWEljU2WqHPEvhEX3%2Bw3jLiYHQHGqT4AQtcxNswHbRxtDF2JiIzoCYNWzkE58%2BN%2B5sbtfm%2FSmdAGEWQuydtICrQtupmNLOD49Y06m53ZnnO1M4prsnDskfsI87WHUkIwArKPHGkX%7Ctkp%3ABk9SR9628q7nYg&LH_BO=1&LH_ItemCondition=3000%7C2500'




def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 
        'Accept-Language':'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    name = soup.select_one(selector='.x-item-title__mainTitle').getText()
    name = name.strip()

    price = soup.select_one(selector='.x-price-primary').getText()
    price = price[4:]

    return name, price

print(get_link_data(url))


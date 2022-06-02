
from turtle import title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


options = Options()

driver = webdriver.Chrome(options=options)


def scr(url):

    driver.get(url)

    time.sleep(2)

    item_name = []
    url_list = []
    stock_flg =[]

    items=driver.find_elements_by_class_name("searchresultitem")
    for item in items:
        title = item.find_element_by_class_name("title")
        item_name.append(title.text)

        url = item.find_element_by_tag_name('a').get_attribute("href")
        url_list.append(url)

        item = item.text
        item = item.split('\n')

        if "売り切れ" in item:
            stock_flg.append(1)
        else:
            stock_flg.append(0)

    df = pd.DataFrame([item_name,url_list,stock_flg]).T
    df.columns = ["item_name","url","stock_flg"]

    driver.quit()

    return df

def main():
    url = "https://search.rakuten.co.jp/search/mall/ANKER/?f=0"
    df = scr(url)
    print(df)
    df.to_csv("test.csv")

if __name__=="__main__":
    main()

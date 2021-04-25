import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

'''
HackerNews WebScrapper - A simple Web scrapper to fetch
 all the titles, their links for titles having scores
  above 100 from HackerNews
'''


def sort_by_votes(dict_data):
    return sorted(dict_data, key=lambda k: k["score"], reverse=True)


def custom_hn(page_number):
    news_list = list()
    print(f"Data fetching from Page - {page_number} Started...")
    res = requests.get(f"https://news.ycombinator.com/news?p={page_number}")
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.select(".athing")

    for d in data:
        dt = d.select(".storylink")[0]
        title = dt.get_text()
        link = dt.get("href")
        id_val = "score_" + d.get('id')

        score_dt = soup.select(f"#{id_val}")
        if score_dt:
            score = int(score_dt[0].get_text().split(" ")[0])
            if score > 100:
                news_list.append({"title": title, "link": link, "score": score})
    print(f"Data fetching from Page - {page_number} completed...")
    time.sleep(2)
    return sort_by_votes(news_list)


if __name__ == "__main__":
    print("---Welcome to HackerNews WebScrapper---")
    pages_to_be_fetched = input("Enter the number of pages you want to fetch: ")
    for page_number in range(1, int(pages_to_be_fetched) + 1):
        returned_list = custom_hn(page_number)
        df = pd.DataFrame(returned_list)
        file_name = f"Data_{datetime.now().strftime('%Y_%m_%d-%I_%p')}"
        df.to_csv(f"{file_name}.csv", mode='a', index=False)
    print(f"Data fetched from HackerNews has been stored into {file_name}.csv . Do check the file!!")

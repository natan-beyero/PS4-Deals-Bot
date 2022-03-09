import requests
from bs4 import BeautifulSoup
import RedditBot as reddit


post_id = 2330
url_to_scrape = 'https://platprices.com/en-us/news_reddit.php?news_id=' + str(post_id) + '&direct=1&hidediff=1&hideplat=1&hidetime=1'
html = requests.get(url_to_scrape).text

html_soup = BeautifulSoup(html, 'html.parser')

all_text = html_soup.find('pre').text

comments = all_text.split('(continued in comment replies...)')

reddit_object = reddit.authenticate()

url = "https://www.reddit.com/user/PS4Deals_Bot/comments/t98jdf/test_02/"

thing_id = url.split("/")[6]

global prev_comment
prev_comment = None

for comment in comments:

    if prev_comment == None:
        prev_comment = reddit.post_comment_by_id(''.join(comment), reddit_object, thing_id)
    else:
        prev_comment = reddit.post_comment(''.join(comment), prev_comment)



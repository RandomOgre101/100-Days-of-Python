from bs4 import BeautifulSoup
import requests

# with open('website.html', encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))


response = requests.get(url="https://news.ycombinator.com/")
yc = response.text

soup = BeautifulSoup(yc, 'html.parser')

articles = soup.find_all(name='a', rel='noreferrer')

article_upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name='span', class_='score')]

article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get('href'))

highest = max(article_upvotes)
index = article_upvotes.index(highest)

print(article_texts[index])


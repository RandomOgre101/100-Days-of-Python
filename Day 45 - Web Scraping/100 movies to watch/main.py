import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movie_response = response.text
soup = BeautifulSoup(movie_response, 'html.parser')

movies_text = soup.find_all(name='h3', class_='title')
movies = [movie.getText() for movie in movies_text]

movies.reverse()

with open('movies.txt', mode='w', encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

from django.conf.urls import url
from bs4 import BeautifulSoup
import requests

from app import views

# r = requests.get("https://abokifx.com/")

# data = r.text

# soup = BeautifulSoup(data)

# name_box = soup.find('table', attrs={'class': 'grid-table'})
# print(name_box)
# for link in soup.find_all('a'):
#     print(link.get('href'))

urlpatterns = [
    url(r'^$', views.indexer, name='index'),
]

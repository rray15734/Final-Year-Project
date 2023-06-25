# -*- coding: utf-8 -*-
"""web_scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xrg-fgQdRy-yziuuRboLDkHPNCoaQwC7
"""
import string
import random
import re
import numpy as np
import bs4 as bs
import urllib.request
import nltk
import lxml
import requests

url = 'https://www.knust.edu.gh/'
response = urllib.request.urlopen(url)
html_content = response.read()

#Taking the data out of the site using beautiful soup
data = bs.BeautifulSoup(html_content, 'lxml')
soup = bs.BeautifulSoup(html_content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Print the URLs of the links
for link in links:
    print(link.get('href'))

import requests
import time
from apscheduler.schedulers.background import BackgroundScheduler

def scrape_website():
  # Replace with your desired URL

  url = 'https://www.knust.edu.gh/'
  response = urllib.request.urlopen(url)
  html_content = response.read()

#Taking the data out of the site using beautiful soup
data = bs.BeautifulSoup(html_content, 'lxml')
data_paragraphs = data.find_all('p')
data_text = ''

for para in data_paragraphs:
  data_text += para.text

  filename = r'C:\Users\Hp\Desktop\KnowledgeBase\knust news.txt'
  with open(filename, 'w', encoding='utf-8') as file:
        file.write(data_text)

def job():
    print("Scraping the website...")
    scrape_website()

scheduler = BackgroundScheduler()

scheduler.add_job(job, "interval", seconds=5)
scheduler.start()

for i in range(20):
  print(i)
  time.sleep(1)
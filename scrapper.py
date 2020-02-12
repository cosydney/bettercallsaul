from bs4 import BeautifulSoup

import requests

url = "https://www.avocat-immo.fr/annuaire/?is_avocat_immo=1&orderBy=nom%20ASC,%20prenom%20ASC,%20id%20ASC&statut=0&return=id&page="
lawyers = []


def find_lawyers(url):
  print("called", url)
  r  = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data)
  for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
      if 'annuaire/avocat' in href:
        lawyers.append(href)
        getLawyerInfo(href)
        break

def getLawyerInfo(url):
  r  = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data)
  name = soup.find("h1", {"class": "name-title"}).text
  print('name', name)
  email = soup.find("li", {"class": "email"}).text.replace('[kukac]', '@')
  print('email', email)
  tel = soup.find("li", {"class": "tel"}).text
  print('tel', tel)
  site = soup.find("li", {"class": "site"}).a.get('href')
  print('site', site)



def main(): 
  i = 0
  while i < 1:
      i += 1
      find_lawyers(url+str(i))
  
  print(lawyers)
  print(len(lawyers))

main()
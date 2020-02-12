from bs4 import BeautifulSoup
import csv


import requests

url = "https://www.avocat-immo.fr/annuaire/?is_avocat_immo=1&orderBy=nom%20ASC,%20prenom%20ASC,%20id%20ASC&statut=0&return=id&page="
lawyers = []


def find_lawyers(url):
  print('url', url)
  r  = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data)
  for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
      if 'annuaire/avocat' in href:
        if href not in lawyers:
          lawyers.append(href)
          getLawyerInfo(href)

def getLawyerInfo(url):
  print("lawyer", url)
  r  = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data)
  try:
    name = soup.find("h1", {"class": "name-title"}).text.encode('utf-8')
  except:
    name = ''

  try:
    email = soup.find("li", {"class": "email"}).text.replace('[kukac]', '@').encode('utf-8')
  except:
    email = ""

  try:
    tel = soup.find("li", {"class": "tel"}).text.encode('utf-8')
  except:
    tel = ""
  
  try:
    site = soup.find("li", {"class": "site"}).a.get('href').encode('utf-8')
  except:
    site = ""
  
  print('Lawyer', name, email, tel, site)
  writeToCsv([name, email, tel, site])

def writeToCsv(info):
  with open('lawyer.csv', mode='a') as employee_file:
        lawyer_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        lawyer_writer.writerow(info)


def main(): 
  i = 1
  while i < 70:
      i += 1
      find_lawyers(url+str(i))
  

  print('len', len(lawyers))

main()

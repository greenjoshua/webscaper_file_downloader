from bs4 import BeautifulSoup
import csv
import requests
import download_files

searchin = {'player-name': 'Martini', 'season': '12'}
r = requests.post('http://ballchasing.com', params=searchin)
main = r.url

r2 = requests.get(main).text
soup = BeautifulSoup(r2,'html.parser')
match = soup.find('body')
match_h2 = match.find_all("h2")

tagList = [str(tag) for tag in match_h2]
trial_file_names = []
preLink = []
for x in range(len(tagList)):
  trial = tagList[x]
  trial1 = trial.split('href="/replay/')[1].split('">')[0]
  """ Josh did this line. See Josh for changes cuz he killed it."""
  trial_file_names.append(trial1)
  trial1 = "http://www.ballchasing.com/dl/stats/players/" + trial1 + "/" + trial1 + "-players.csv"
  preLink.append(trial1)
 
download_files.download_csv(preLink[0], trial_file_names[0])


#print(preLink)
#if any('href="/replay/' in )
#for x in range(len(tagList)):
#   print(tagList[x])
#   print('\n' + str(x) )

#def any(iterable):
#    for element in iterable:
 #       if element:
  #          return True
   # return False

#
#
#
#
#
# ready_links = []
# for link in preLink:
#     ready_links.append(link + "/" + link)
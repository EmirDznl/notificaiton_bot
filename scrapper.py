import requests
from bs4 import BeautifulSoup
import json
with open("sensitive_infos.json", "r") as data_json:
    infos = json.load(data_json)

user_agent= infos["User-Agent"]
website_link = infos["website"]
first_time = infos["first_time"]

URL = website_link

headers = {
"User-Agent": user_agent
}

response = requests.get(URL , headers =  headers)
soup = BeautifulSoup(response.content, "html.parser")
orta_içerik = soup.find('div', attrs = {'id':'orta-icerik'})
box_content = soup.find_all("div", class_=["col-md-6", "col-sm-6", "col-xs-12"])
outer_div = soup.find_all("div", class_=["panel", "panel-visible"])
inner_div = soup.find_all("div", class_ = "panel-ust-ic")
ep_name_html = soup.find_all("a", class_ = "baloon")
orta_içerik = soup.find('div', attrs = {'id':'orta-icerik'})
box_content = soup.find_all("div", class_=["col-md-6", "col-sm-6", "col-xs-12"])
outer_div = soup.find_all("div", class_=["panel", "panel-visible"])
inner_div = soup.find_all("div", class_ =["panel-ust-ic"])
html_content = "".join(str(item) for item in inner_div)
final_soup = BeautifulSoup(html_content, "html.parser")
new_anime_ep_dict = {}
links = final_soup.find_all("a")
for link in links:
    title = link.get("title")
    href = link.get("href")
    if title and href:
        new_anime_ep_dict[title] = href
        user_follow_list = []
while(first_time):
    name = input("anime ismini girin(cikmak icin 'Exit' yazin): ")
    if name.lower() == "exit":
        break
    user_follow_list.append(name)

import difflib
def benzerlik_orani(kelime1, kelime2):
    benzerlik = difflib.SequenceMatcher(None, kelime1, kelime2).ratio()
    return benzerlik * 100
    
new_episodes_matched = {}

for yeni_bolum in new_anime_ep_dict.keys():
    for user_selection in user_follow_list:
        if benzerlik_orani(yeni_bolum, user_selection) > 50:
            new_episodes_matched[yeni_bolum] =  new_anime_ep_dict[yeni_bolum]

if first_time:
    old_new_episodes = []
    first_time = False
    with open("sensitive_infos.json", "w") as data_json:
        infos["first_time"] = "False"
        infos = json.dump(infos, data_json)

for eps in new_anime_ep_dict.keys():
    if eps in old_new_episodes:
        new_anime_ep_dict[eps] = new_anime_ep_dict[eps] + "    ////////was occured in previous list/////////"
old_new_episodes = list(new_anime_ep_dict.keys())


with open("episodes_to_watch.txt", "w" ) as file:
    for ep in new_episodes_matched.keys():
        file.write(ep + ": " + new_episodes_matched[ep] + "\n")
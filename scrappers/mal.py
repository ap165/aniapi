from requests import get
from bs4 import BeautifulSoup
import json

class mal:
  def __init__(self):
    self.BaseUrl = "https://myanimelist.net"
  
  def getAnimeById(self,id): ## Anime info by ID ##
    data = get(self.BaseUrl + f"/anime/{id}")
    soup = BeautifulSoup(data.text, "html.parser")
    songsarr = []
    for x in soup.select(".di-tc table tr"):
      if len(x.select("td")) != 3:
        pass
      else:
        song = (x.select("td"))[1].select("input")
        songsarr.append(song)
    songs = []
    for x in songsarr:
       if len(x) != 0 and x[0]["value"] != "":
        songs.append(x[0]["value"].split("/track/")[1])
    jsonData = {
      "mal_id" : id,
      "title": soup.select(".title-name")[0].text,
      "title_eng": soup.select(".title-english")[0].text,
      "url" : f"{self.BaseUrl}/anime/{id}",
      "img" : soup.select(".borderClass img.ac")[0]["data-src"],
      "rank": soup.select(".stats-block .ranked strong")[0].text,
      "popularity": soup.select(".stats-block .popularity strong")[0].text,
      "score": soup.select(".stats-block .score")[0].text,
      "description": soup.findAll("p", {"itemprop" : "description"})[0].text, 
      "info": {x.select(".dark_text")[0].text.replace(":","").strip().lower() : x.text.replace(x.select('.dark_text')[0].text,"").strip() for x in soup.select(".borderClass .leftside .spaceit_pad")},
      "external_links": [{"name": x.text.strip().lower(), "data" : x["href"]} for x in soup.select(".external_links a")],
      "theme_songs": songs
    }
    return json.dumps(jsonData)
  
  def animeCharacters(self, malid): ## Anime Charactors & voice Actors ##
    data = get(f"{self.BaseUrl}/anime/{malid}/animeName/characters")
    soup = BeautifulSoup(data.text, "html.parser")
    charactersList = soup.select(".anime-character-container table tr")
    x = []
    for character in charactersList:
      cName = character.select(".js-chara-roll-and-name")
      if len(cName) != 0:
        voice_actors = character.select(".js-anime-character-va .js-anime-character-va-lang")
        cINfoJson ={
          "name" : cName[0].text.strip(" \n").split("_")[1],
          "img": str(character.select(".ac img")[0]["data-srcset"].split(" 1x, ")[1].replace(" 2x","")),
          "type" : "main" if cName[0].text.strip(" \n").split("_")[0] == "m" else "supporting",
          "voice_actors" : [{
            "name": x.select('td')[0].select(".spaceit_pad")[0].text.strip("\n"),
            "img": x.select('td')[1].select("img")[0]["data-srcset"].split(", ")[1].replace(" 2x",""),
            "lang" : x.select(".js-anime-character-language")[0].text.strip("\n ") 
                }for x in voice_actors]}
        x.append(cINfoJson)
    charactersInfo = {
      "mal_id": malid,
      "name": soup.select(".title-name")[0].text,
      "data": (x) }
    return json.dumps(charactersInfo)

    



print(mal().animeCharacters(52299))


from bs4 import BeautifulSoup
import  requests, json


class gogo:
  def __init__(self) -> None:
    self.BASE_AJAX_URL = "https://ajax.gogo-load.com"
    # self.BASE_URL = urls.gogo1
  
  def search(self,query):
    data = requests.get(f"{self.BASE_AJAX_URL}/site/loadAjaxSearch?keyword={query}")
    # soup = BeautifulSoup(json.loads(data.text)["content"],"html.parser")
    return data
    

  def anime(self, gogoid):
    data = requests.get(f"{self.BASE_URL}/category/{gogoid}")
    soup = BeautifulSoup(data.text, "html.parser")
    id = soup.select("#movie_id")[0]["value"]
    name = soup.select("#alias_anime")[0]["value"]
    episData = requests.get(f"{self.BASE_AJAX_URL}/ajax/load-list-episode?ep_start=0&ep_end=9999&id={id}&alias={name}")
    episSoup = BeautifulSoup(episData.content, 'html.parser')
    
  
  def episode(self,gogoEpId):
    data = requests.get(f"{self.BASE_URL}/{gogoEpId}")
    soup = BeautifulSoup(data.text,"html.parser")
    


if __name__ == "__main__":
    gogo().search("naruto")



"""

class gogoJsonGenerator:
  def __init__(self) -> None:
    pass
  def searchJson(soup): 
    titles = [x.text for x in soup.select(".ss-title")]
    thumbnail = [(x["style"])[17:-2] for x in soup.select(".ss-title div")]
    gogoId =[x["href"] for x in soup.select(".ss-title")]
    json_data = "["
    for i in range(len(titles)):
      json_data += '{"title":"'+titles[i]+'","thumbnail":"'+thumbnail[i]+'","id": "'+gogoId[i].replace("category/","")+'"},'
    return json.loads(json_data[:-1]+"]")
  
  def animeJson(html,epis):
    eparr = [x["href"].replace(" /","") for x in epis.select("a")][::-1]
    genre = html.select(".anime_info_body .type")[2].select("a")
    status = html.select(".anime_info_body .type")[4]
    info = {
      "title": html.select(".anime_info_body h1")[0].text,
      "thumbnail": html.select(".anime_info_body img")[0]["src"],
      "type": html.select(".anime_info_body .type")[0].text.split("\n")[1],
      "description": html.select(".anime_info_body .type")[1].text.replace("Plot Summary: ",""),
      "genre": [{"title":a["title"], "url": "genre/"+a["href"].split("/genre/")[1]} for a in genre],
      "released" : html.select(".anime_info_body .type")[3].text.replace("Released: ",""),
      "status" : {"title": status.select("a")[0]["title"],"url" : status.select("a")[0]["href"]},
      "other_name" : html.select(".anime_info_body .type")[5].text.replace("Other name: ",""),
      "episodes": eparr
    }
    return json.dumps(info)
  def episodeJson(soup):
    servers = [{"video": x["data-video"],"name": x.text.replace("Choose this server","").replace("\n","")} for x in soup.select(".anime_muti_link ul li a")]
    return json.dumps(servers, indent = 2)

## myanimelist.net ##
class malJsonGenerator:
  def __init__(self) -> None:
    pass

  def searchAnime(data,page):
    soup = BeautifulSoup(data.text, "html.parser")
    last_page = 20 # int(soup.select(".ac .spaceit .bgColor1 a")[-1].text)
    animes = soup.select("#content div.list table tr")
    del animes[0]
    dataDict = {
      "pagination":{
        "next_page": True if page < last_page else False,
        "prev_page": True if page > 1 else False,
        "page": page
      },
      "items": [
        {
          "title": anime.select(".title a")[0].text,
          "mal_id": int(anime.select(".picSurround a")[0]["href"].replace("https://myanimelist.net/anime/","").split("/")[0]),
          "type": anime.select(".ac")[0].text.strip(" \n"),
          "url": anime.select(".picSurround a")[0]["href"],
          "img": (anime.select(".picSurround img")[0]["data-srcset"].split(" 1x, ")[1].replace(" 2x","")),
          "score": (anime.select(".ac")[2].text.strip(" \n"))
        } for anime in animes
      ]
    }
    return json.dumps(dataDict)

"""

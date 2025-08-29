from bs4 import BeautifulSoup
import  requests, json
import time


class gogo:
  def __init__(self) -> None:
    """
    https://ajax.gogocdn.net/site/loadajaxsearch?keyword=naruto
    https://gogoanime.onl/api/anime/suggest?keyword=naruto
    https://gogoanime.quest/api/anime/suggest?keyword=naru

    """
    self.BASE_URL = "https://gogoanime.quest"
    self.BASE_AJAX_URL = "https://gogoanime.quest/api"
  
  def search(self,query): ###  get anime by name  ###
    data = requests.get(f"{self.BASE_AJAX_URL}/anime/suggest?keyword={query}")
    soup = BeautifulSoup(json.loads(data.text)["content"], "lxml")
    json_data = [
        {
            "title": title.text,
            "thumbnail": thumbnail["style"][17:-2],
            "id": gogoId["href"].replace("category/", ""),
        }for title, thumbnail, gogoId in zip(
            soup.select(".ss-title"),
            soup.select(".ss-title div"),
            soup.select(".ss-title"), )
    ]
    return json_data
    

  def get_anime_info(self, gogoid): ### get anime imfo from gogo id ###
    base_url = self.BASE_URL
    data = requests.get(f"{base_url}/anime/{gogoid}")
    html = BeautifulSoup(data.text, "lxml")

    anime_id = html.select("#movie_id")[0]["value"]
    # print(anime_id)
    # anime_name = html.select("#alias_anime")[0]["value"]
    # epis_data = requests.get(f"{self.BASE_AJAX_URL}/ajax/load-list-episode?ep_start=0&ep_end=9999&id={anime_id}&alias={anime_name}")
    epis_data = requests.get(f"{self.BASE_AJAX_URL}/ajax/load-list-episode?ep_start=0&ep_end=9999&id={anime_id}")
    epis = BeautifulSoup(epis_data.content, 'lxml')
    eparr = [x["href"].replace(" /", "") for x in epis.select("a")][::-1]

    # genre_links = html.select(".anime_info_body .type")[2].select("a")
    # genre = [{"title": a["title"], "url": f"genre/{a['href'].split('/genre/')[1]}"} for a in genre_links]
    # status_link = html.select(".anime_info_body .type")[4].select("a")[0]
    # status = {"title": status_link["title"], "url": status_link["href"]}

    info = {
        "title": html.select(".anime_info_body h1")[0].text,
        "thumbnail": html.select(".anime_info_body img")[0]["src"],
        "episodes": eparr
    }
    return info
  
  def get_episode_servers(self,gogoEpId):
    data = requests.get(f"{self.BASE_URL}/episode/{gogoEpId}")
    soup = BeautifulSoup(data.text,"lxml")
    # print(soup)
    servers = [{"video": x["data-video"],"name": x.text.replace("Choose this server","").replace("\n","")} for x in soup.select(".anime_muti_link ul li a")]
    return json.dumps(servers, indent = 2)
    


if __name__ == "__main__":
  print(gogo().get_episode_servers("naruto-shippuden-episode-1"))

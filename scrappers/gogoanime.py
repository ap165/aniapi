from bs4 import BeautifulSoup
import  requests, json
# import time
import re



class gogo:
  def __init__(self) -> None:

    self.BASE_URL = "https://gogoanimez.to"
    self.BASE_AJAX_URL = "https://gogoanimez.to/wp-admin/admin-ajax.php"
  
  def search(self,query): ###  get anime by name  ###
    data = requests.get(f"{self.BASE_URL}?s={query}")
    soup = BeautifulSoup(data.text, "lxml")
    json_data = [
        {
            "title": x["title"],
            "thumbnail": x.select_one("img")["src"],
            "id": x["href"].replace("https://gogoanimez.to/anime/", "").replace("/", ""),
        }for x in soup.select(".items li .img a")
    ]
    return json_data
    # return soup
    

  def get_anime_info(self, gogoid): ### get anime imfo from gogo id ###
    base_url = self.BASE_URL
    data = requests.get(f"{base_url}/anime/{gogoid}")
    html = BeautifulSoup(data.text, "lxml")

    anime_id = html.select("#movie_id")[0]["value"]
    script = html.select(".anime_video_body script")[0].text
    nonce = re.search(r'nonce:\s*["\']([a-zA-Z0-9]+)["\']', script).group(1)
    # anime_name = html.select("#alias_anime")[0]["value"]
    data = {
      'action': 'load_episode_range',
      'range_start': '1',
      'range_end': '219',
      'seri_id': f'{anime_id}',
      'nonce': f'{nonce}'
    }
    # print(nonce)
    # print(anime_id)
    epis_data = requests.post(f"{self.BASE_AJAX_URL}", data=data)
    epis = BeautifulSoup(epis_data.json()["data"], 'lxml')
    eparr = [x["href"].split("/")[-2] for x in epis.select("a")][::-1]

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
    data = requests.get(f"{self.BASE_URL}/{gogoEpId}")
    soup = BeautifulSoup(data.text,"lxml")
    link = soup.select(".anime_muti_link ul li a")
    servers = [{"video": re.search(r'<iframe[^>]+src="([^"]+)"', x["data-video"]).group(1),"name": "server 1"} for x in link]
    return json.dumps(servers)
    


if __name__ == "__main__":
  import time
    # print(gogo().search("naruto"))
  # t = time.time()
  print(gogo().get_episode_servers("naruto-episode-1"))
  # print(time.time()-t)

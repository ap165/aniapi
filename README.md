# AniApi
>AniApi is a powerful and open-source API designed specifically for anime enthusiasts. With AniApi, you can effortlessly retrieve detailed information about anime series, characters, genres, and more. Whether you’re building an anime-related app, website, or just exploring anime data, AniApi provides a seamless way to access accurate and up-to-date information. Dive into the world of anime with AniApi! 🌟🎬🔍

## Search Anime BY Name


url:-
    ``` /api/search ```

 params:- <br>
   ```q= [anime-name]``` <br>
   ```page= [page-no]```

```bash
http://localhost:5000/api/search?q=naruto&page=1
```

## AJAX Search
url:- <br>
   ``` /ajax/search```

params:- <br>
    ```q= [anime-name]```

```bash
http://localhost:5000/api/ajax/search?q=naruto
```

## Top Animes

url:- <br>
```/topAnimes```

params:- <br>
type - ```airing```, ```upcoming```, `tv`, `movie`, `ova`, `ona`, `special`, `bypopularity`, `favorite` <br>

`page= [page-no]`
```bash
http://localhost:5000/api/topAnimes?type=airing&page=1
```

## Anime
url:- <br>
   ``` /api/anime```

params:- <br>
   ```id= [anime-id]```

```bash
http://localhost:5000/api/anime?id=51836
```

## Character
url:- <br>
   ``` /api/characters```

params:- <br>
    ```id= [anime-id]```

```bash
http://localhost:5000/api/characters?id=51836
```

## Episodes Info
url:- <br>
   ``` /api/info/epis```

params:- <br>
    ```id= [anime-id]```
    ```offsset= ```

```bash
http://localhost:5000/api/info/epis?id=21&offset=0
```

## Search From gogoAnime
url:- <br>
   ``` /api/search/gogo```

params:- <br>
    ```q= [anime-name]```

```bash
http://localhost:5000/api/search/gogo?q=naruto
```

## Get episodes from GOGOAnime
url:- <br>
   ``` /api/anime/epis```

params:- <br>
    ```gogoid= [gogo-anime-id]```

```bash
http://localhost:5000/api/anime/epis?gogoid=naruto-shippuden
```


## Get episode servers
url:- <br>
   ```/api/anime/ep```

params:- <br>
    ```epid= [gogo-anime-epid]```

```bash
http://localhost:5000/api/anime/ep?epid=naruto-shippuden-episode-1
```

## Extract M3U8 from Vidstreaming url
url:- <br>
   ```/api/extractors/vidstreaming```

params:- <br>
    ```url= [vidstreaming-url]```

```bash
http://localhost:5000/api/extractors/vidstreaming?url=https://embtaku.pro/streaming.php?id=MjIwMQ==&title=Naruto+Shippuden+Episode+1
```


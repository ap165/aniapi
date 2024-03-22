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

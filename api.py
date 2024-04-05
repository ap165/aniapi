from flask import Blueprint, request, jsonify
from scrappers.myanimelist import mal
from scrappers.gogoanime import gogo
from extractors.vidstreaming import getM3U8url
from flask_cors import CORS
import json

api = Blueprint('api', __name__)
CORS(api)

@api.route('/')
def index():
    return "This is an example app"     


###################   MAL   ############################
@api.route("/search")
def search():
    q = request.args.get("q") ## anime name
    page = request.args.get("page")  ## page No.
    data = mal().search(q, int(page))
    return json.loads(data)

@api.route("/ajax/search")
def ajaxSearch():
    q = request.args.get("q") 
    json_data = mal().ajaxSearch(q)
    return json.loads(json_data)

##   type "",   
##  url  https://myanimelist.net/topanime.php
@api.route("/topAnimes")
def topAnimes():
    type = request.args.get("type")
    page = request.args.get("page")
    data = mal().topAnime(type, page)
    return json.loads(data)

@api.route("/anime")
def anime():
    id = (request.args.get("id"))
    data = mal().getAnimeById(id)
    return json.loads(data)

@api.route("/characters")
def character():
    id = request.args.get("id")
    data = mal().animeCharacters(id)
    return json.loads(data)

################# GOGO #####################
@api.route("/search/gogo") ## q = animeName
def gogoSearch():
    q = request.args.get("q")
    data = gogo().search(q)
    return (data)

@api.route("/anime/epis")
def epis():
    GogoAnimeId = request.args.get("gogoid")
    data = gogo().get_anime_info(GogoAnimeId)
    return (data)

@api.route("/anime/ep")
def episode_servers():
    GogoEpId = request.args.get("epid")
    data = gogo().get_episode_servers(GogoEpId)
    return json.loads(data)

@api.route("/extractors/vidstreaming")
def vidstreaming():
    serverAddress = request.args.get("url")
    return getM3U8url(serverAddress)

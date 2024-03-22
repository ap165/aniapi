from flask import Blueprint, request, jsonify
from scrappers.mal import mal

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "This is an example app"     

@api.route("/search")
def search():
    q = request.args.get("q") ## anime name
    page = request.args.get("page")  ## page No.
    data = mal().search(q, int(page))
    return jsonify(data)

@api.route("/ajax/search")
def ajaxSearch():
    q = request.args.get("q") 
    json_data = mal().ajaxSearch(q)
    return jsonify(json_data)

##   type "",   
##  url  https://myanimelist.net/topanime.php
@api.route("/topAnimes")
def topAnimes():
    type = request.args.get("type")
    page = request.args.get("page")
    data = mal().topAnime(type, page)
    return jsonify(data)

@api.route("/anime")
def anime():
    id = (request.args.get("id"))
    data = mal().getAnimeById(id)
    return jsonify(data)

@api.route("/characters")
def character():
    id = request.args.get("id")
    data = mal().animeCharacters(id)
    return jsonify(data)
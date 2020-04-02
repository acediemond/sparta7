import pymongo
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import flask


def load_all_movies():
    client = MongoClient('localhost',27017)
    db = client.dbsparta.movies
    all_mv= list(db.find({}, {'_id':0}))
    #for movie in all_mv:
        #print(movie)
    return all_mv

def find_title(t):
    if t == None:
        return load_all_movies()

    client = MongoClient('localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({'title': t},{'_id':0}))


def find_rank(r):
    if r == None:
        return load_all_movies()

    client = MongoClient('localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({'rank': int(r)},{'_id':0}))

def write_movie(movie):
    # {'rank': 1, 'title': '제목', 'score': '10.0'}
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.movies
    db.insert_one(movie)



# def _run_server():
#     server = Flask('무비서버')
#     @server.route('/')
#     def home():
#         return 'HOME'
#     @server.route('/movies')
#     def movies():
#
#         rank_receive = request.args.get('rank')
#         all_mv = find_rank(rank_receive)
#         return jsonify(all_mv)
#         return "rank"
#         print(movies)
#
#     server.run('0.0.0.0', port=5000, debug=True)

def run_server():
    server = Flask('무비서버')

    @server.route('/')
    def home():
        return render_template('movies.html')

    @server.route('/movies')
    def movies():

        title_found = []
        rank_found = []

        title = request.args.get('title')
        rank = request.args.get('rank')

        if title is None and rank is None:
            return jsonify(load_all_movies())

        if title is not None:
            title_found = find_title(title)

        if rank is not None:
            rank_found = find_rank(rank)

        found = title_found + rank_found
        return jsonify(found)

    @server.route('/add_movie', methods = ['POST'])
    def add_movie():
        title = request.form['title']
        rank = request.form['rank']
        score = request.form['score']

        if title is None or rank is None or score is None:
            result = {'message': 'parameter not filled!', 'result': 'error'}
            return 'parameter not filled!'


        movie = {'rank': int(rank), 'title': title, 'score': score}
        write_movie(movie)
        return 'OK!'

    server.run('0.0.0.0', port=5000, debug=True)


run_server()

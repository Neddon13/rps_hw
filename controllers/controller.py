from app import app
from flask import render_template
from models.game import *
from models.player import *

@app.route('/<player_1_move>/<player_2_move>')
def play(player_1_move, player_2_move):
    player_1= Player("player_1", player_1_move)
    player_2= Player("player_2", player_2_move)
    game = Game()

    winner = game.play(player_1, player_2)

    return render_template("index.html", player_1=player_1, player_2=player_2, winner=winner)

@app.route('/rules')
def rules():
    return render_template('rules.html')


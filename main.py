from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

sounds = {
    "intro_music": "/static/sounds/intro_music.mp3",
    "ship_ambiance": "/static/sounds/ship_ambiance.mp3",
    "door_open": "/static/sounds/door_open.mp3",
    "monster_roar": "/static/sounds/monster_roar.mp3",
    "sword_swing": "/static/sounds/sword_swing.mp3",
    "healing_spell": "/static/sounds/healing_spell.mp3",
    "monster_attack": "/static/sounds/monster_attack.mp3",
    "victory": "/static/sounds/victory.mp3",
    "game_over": "/static/sounds/game_over.mp3",
    "treasure_open": "/static/sounds/treasure_open.mp3",
    "cheering_crowd": "/static/sounds/cheering_crowd.mp3",
    "creepy_whispers": "/static/sounds/creepy_whispers.mp3",
    "footsteps": "/static/sounds/footsteps.mp3",
    "rock_fall": "/static/sounds/rock_fall.mp3",
    "exit_sound": "/static/sounds/exit_sound.mp3",
    "trap": "/static/sounds/trap.mp3"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_sound/<sound_name>')
def play_sound(sound_name):
    if sound_name in sounds:
        return jsonify({"url": sounds[sound_name]})
    return jsonify({"error": "Sound not found"}), 404

if __name__ == "__main__":
    app.run()

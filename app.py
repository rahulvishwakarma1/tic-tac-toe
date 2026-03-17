from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [" " for _ in range(9)]
current_player = "X"

@app.route("/")
def home():
    return render_template("index.html", board=board)

@app.route("/move", methods=["POST"])
def move():
    global current_player

    data = request.json
    i = data["index"]

    if board[i] == " ":
        board[i] = current_player
        current_player = "O" if current_player == "X" else "X"

    return jsonify(board=board, player=current_player)

@app.route("/reset", methods=["POST"])
def reset():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    return jsonify(board=board, player=current_player)

if __name__ == "__main__":
    app.run(debug=True)
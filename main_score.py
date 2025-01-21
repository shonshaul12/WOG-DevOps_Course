from flask import Flask, render_template_string
import os
from utils import SCORES_FILE_NAME

app = Flask(__name__)

def read_score():
    """
    Reads the current score from the Scores.txt file.
    If the file doesn't exist or is empty, returns 0.
    """
    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read().strip()
                return int(score) if score else 0
        except ValueError:
            return 0
    return 0

@app.route('/score')
def score_server():
    """
    Serves the score in an HTML format.
    """
    score = read_score()

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Score</title>
    </head>
    <body>
        <h1>User Score</h1>
        <p>Your current score is: <strong>{{ score }}</strong></p>
    </body>
    </html>
    """


    return render_template_string(html_template, score=score)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

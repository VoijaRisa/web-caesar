from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label><b>Rotate by</b>:
                <input name="rot" type="text" value="0"/>
            </label>

            <br>

            <label method="POST">
                <textarea name="text" /></textarea>
            </label>

            <br>

            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
       rot = int(request.form['rot'])
       text = request.form['text']

       encryptedtext = "<h1>" + rotate_string(text, rot) + "</h1>"

       return encryptedtext

app.run()
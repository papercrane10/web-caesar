from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>


<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <!---create your form here --->
        <form method="post">
        <label>Rotate by:</label>
            <input name="rot" type="text" value=0 />
            <textarea name="text"/>{0}</textarea>
            <button type-"button">Submit</button>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])

def encrypt():
    new = """
    <!doctype html>
    <html>
        <h1>{response}</h1>
    </html>    
    """
    rot_value = int(request.form.get('rot'))
    text_value = str(request.form.get('text'))
    rotated = rotate_string(text_value, rot_value)
    return form.format(rotated)
    

app.run()
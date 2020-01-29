from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Strong password, sick admins...</title>
</head>
<body>
<h1>Cyberthon Super Secure Panel</h1>
    <p>You need to enter token...</p>

    <form method="POST">
        <input type="text" name="token" size="50" placeholder="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"/>
        <input type="submit" value="CHECK">
    </form>
</body>
</html>
"""

@app.route('/', methods=['POST'])
def answer():
    if request.form.get('token', None) == "94177166-14cf-4034-9693-1236239404aa":
        return "FLAG"
    return "Access Denied!"

app.run(debug=False, port=3006)
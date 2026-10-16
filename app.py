from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Deployment Lab</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2ff;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: white;
                margin: auto;
                padding: 35px;
                max-width: 450px;
                border-radius: 15px;
                box-shadow: 0 4px 15px #ccd2e0;
            }
            h1 { color: #263b80; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Application!</h1>
            <h2>Harshit Bansal</h2>
            <p>Application Version: 1.0.0</p>
            <p>Deployed using Docker and AWS EC2</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
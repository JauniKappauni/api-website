from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
APIKEY = os.getenv("APIKEY")
CHANNELID = os.getenv("CHANNELID")

@app.route("/", methods=["POST", "GET"])
def hello():
    response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={CHANNELID}&key={APIKEY}")
    data = response.json()
    channel = data["items"][0]
    title = channel["snippet"]["title"]
    subscribers = channel["statistics"]["subscriberCount"]
    views = channel["statistics"]["viewCount"]
    return render_template("index.html",title=title,subscribers=subscribers,views=views)

if __name__ == "__main__":
    app.run(debug=True)
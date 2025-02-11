from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
APIKEY = os.getenv("APIKEY")
CHANNELIDS = os.getenv("CHANNELIDS").split(",")  # Splitte die Channel-IDs in eine Liste

@app.route("/", methods=["POST", "GET"])
def hello():
    channel_info = []
    for channel_id in CHANNELIDS:
        response = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={APIKEY}")
        data = response.json()
        channel = data["items"][0]
        title = channel["snippet"]["title"]
        subscribers = channel["statistics"]["subscriberCount"]
        views = channel["statistics"]["viewCount"]
        channel_info.append({"title": title, "subscribers": subscribers, "views": views})

    return render_template("index.html", channel_info=channel_info)

if __name__ == "__main__":
    app.run(debug=True)
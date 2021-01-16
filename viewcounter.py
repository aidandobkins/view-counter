from pyyoutube import Api
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import urllib.parse as p
import re
import os

api = Api(api_key='')
sum = 0

with open("videourls.txt", "r") as f:
    for url in f:
        purl = p.urlparse(url)
        ids = p.parse_qs(purl.query).get("v")
        print(ids[0])
        video = api.get_video_by_id(video_id=ids)
        sum = sum + int(video.items[0].statistics.viewCount)

print(sum)

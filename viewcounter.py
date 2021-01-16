from pyyoutube import Api
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from tkinter import *
import urllib.parse as p
import re
import os

sum = 0
api = Api(api_key='AIzaSyBP8vpiJAuc8GduKZoYhqcIJHqtQlcQUKg')

def countViews():
    global sum
    sum = 0

    with open("videourls.txt", "r") as f:
        for url in f:
            purl = p.urlparse(url)
            ids = p.parse_qs(purl.query).get("v")
            video = api.get_video_by_id(video_id=ids)
            sum = sum + int(video.items[0].statistics.viewCount)
    counted = Label(root, text = str(str(sum) + " views"), bg = '#e5edf5').pack()
    

root = Tk()
root.title("View Counter")
root.geometry("350x350")
root.configure(bg = '#e5edf5')

Label(root, text = "\n\n", bg = '#e5edf5').pack()
count = Button(root, text = "Count Views", command = countViews, bg = '#e5edf5', pady = 50, padx = 50).pack()
Label(root, text = "\n\n", bg = '#e5edf5').pack()
Label(root, text = "Please give it a moment, it is slow...", bg = '#e5edf5').pack()

root.mainloop()

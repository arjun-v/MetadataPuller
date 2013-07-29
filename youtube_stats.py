#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser

import sys
import requests
import json

DEVELOPER_KEY = "AIzaSyBsp2EaHuR2gQO34cJIU0ma2tsJJQ_ia6I"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/videos?&key=%s&part=statistics,status" % DEVELOPER_KEY + "&id=%s"


def fetch_statistics(url):
  response = requests.get(url)
  return json.loads(response.content)	

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=options.q,
    part="id",
    order="viewCount",
    type="video",
    maxResults=options.maxResults
  ).execute()


  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
	videoId = search_result["id"]["videoId"]
	stats =  fetch_statistics(YOUTUBE_API_URL % videoId)["items"][0]["statistics"]
	print stats["viewCount"],stats["likeCount"],stats["dislikeCount"]

if __name__ == "__main__":
  parser = OptionParser()
  if (sys.argv[2] is None) or (sys.argv[4] is None): sys.exit()
  parser.add_option("--q", dest="q", help="Search term")
  parser.add_option("--max-results", dest="maxResults", help="Max results", default=20)
  (options, args) = parser.parse_args()

  youtube_search(options)





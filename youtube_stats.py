from apiclient.discovery import build

import sys
import requests
import json

class YoutubeUtil(object):
	DEVELOPER_KEY = "AIzaSyBsp2EaHuR2gQO34cJIU0ma2tsJJQ_ia6I"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"
	YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/videos?&key=%s&part=statistics,status" % DEVELOPER_KEY + "&id=%s"
	req_no = 20

	@staticmethod
	def fetch_statistics(url):
		response = requests.get(url)
		return json.loads(response.content)	

	@staticmethod
	def fetch_youtube_stats(query_string):
		youtube = build(YoutubeUtil.YOUTUBE_API_SERVICE_NAME, YoutubeUtil.YOUTUBE_API_VERSION,
		developerKey=YoutubeUtil.DEVELOPER_KEY)

  		search_response = youtube.search().list(
    			q=(query_string + " videos"),
	    		part="id",
    			order="viewCount",
	    		type="video",
	    		maxResults=YoutubeUtil.req_no
  		).execute()

		items = search_response.get("items", [])
  		viewcount_total = 0
  		count = 0
  		like_count = 0
  		dislike_count = 0
  		params = {}
  
		for search_result in search_response.get("items", []):
    			if search_result["id"]["kind"] == "youtube#video":
				count+=1
				videoId = search_result["id"]["videoId"]
				stats =  YoutubeUtil.fetch_statistics(YoutubeUtil.YOUTUBE_API_URL % videoId)["items"][0]["statistics"]
				like_count+=int(stats["likeCount"])
				dislike_count+=int(stats["dislikeCount"])
				viewcount_total+=int(stats["viewCount"])
  
  		params["y_popularity_index"] = len(str(viewcount_total))
  		params["y_rating"] = (float(like_count - dislike_count)/like_count)*10
  		params["y_normalized_rating"] = float(like_count - dislike_count)/viewcount_total
  		params["y_like_count"] = like_count
		params["y_dislike_count"] = dislike_count
  		params["y_view_count"] = viewcount_total
  		params["y_count"] = count
  		return params






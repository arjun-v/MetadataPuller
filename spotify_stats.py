import requests
import json

class SpotifyUtil(object):

	BASE_URL = "http://ws.spotify.com/search/1/artist.json?q=%s"	

	@staticmethod
	def get_spotify_stat(artist):
		response = requests.get(SpotifyUtil.BASE_URL % artist)
                json_object = json.loads(response.content)
		params = {}
		for i in json_object["artists"]:
			if artist.lower() in i["name"].lower():
				params["sp_popularity"] = i["popularity"]
				return params
		
		return None
	



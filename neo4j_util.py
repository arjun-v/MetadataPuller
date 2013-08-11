from py2neo import neo4j
from youtube_stats import YoutubeUtil
from facebook_stats import FacebookUtil
from twitter_stats import TwitterUtil

class Neo4jUtil(object):

	graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
	artist_key = "name"

	@staticmethod
	def create_or_update_artist_node(artist):
		artists = Neo4jUtil.graph_db.get_or_create_index(neo4j.Node, "Artists")
		params = {Neo4jUtil.artist_key : artist}
		params.update(YoutubeUtil.fetch_youtube_stats(artist))
		params.update(FacebookUtil.fetch_fb_pages(artist))
		params.update(TwitterUtil.get_twitter_user(artist))
		params.update(SpotifyUtil.get_spotify_stat(artist))
		node = artists.create_if_none(Neo4jUtil.artist_key, params[Neo4jUtil.artist_key], params)
		if node is None:
			node, = artists.get(Neo4jUtil.artist_key, params[Neo4jUtil.artist_key])
			node.update_properties(params)
		

		
	
	
         






from py2neo import neo4j

class Neo4jUtil(object):

	graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
	artist_key = "name"

	@staticmethod
	def create_artist_node(params):
		artists = Neo4jUtil.graph_db.get_or_create_index(neo4j.Node, "Artists")
		node = artists.create_if_none(Neo4jUtil.artist_key, params[Neo4jUtil.artist_key], params)
		if node is None:
			node, = artists.get(Neo4jUtil.artist_key, params[Neo4jUtil.artist_key])
			node.update_properties(params)
		

		
	
	
         






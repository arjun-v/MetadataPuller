import tweepy

class TwitterUtil(object):

	oauth_consumer_key = "42sOxsJO5cUtGiogqWLzcQ"
	oauth_consumer_secret = "y6RMuUkuEA7YPkoU7bgR1EB9ouxNvooeRCZEGeXR8"
	oauth_token = "1065036932-lT4q8UPkIraQSEzxFgIROMoQZ7EgF0RWsVXRyIM"
	oauth_token_secret = "azIoPlbm0y5mzkxpmRZYy0tW6s1uWA90oRY95WG8"

	
	@staticmethod
	def get_twitter_user(artist):
		auth = tweepy.OAuthHandler(TwitterUtil.oauth_consumer_key, TwitterUtil.oauth_consumer_secret)
	        auth.set_access_token(TwitterUtil.oauth_token, TwitterUtil.oauth_token_secret)
	        api = tweepy.API(auth)
	        api.retry_count = 2
		list = []
		for user in api.search_users(artist):
			if artist.lower() in user.name.lower():
				list.append(user)

		final_list =  sorted(list, key=lambda k: k.followers_count,reverse=True)

		if final_list is None or len(final_list) == 0:
			return None
		params = {}
		params["t_followers"] = final_list[0].followers_count
		params["t_listed_count"] = final_list[0].listed_count
		params["t_statuses_count"] = final_list[0].statuses_count
		return params





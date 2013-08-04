import facebook

class FacebookUtil(object):

	ACCESS_TOKEN = "543169595736560|x04p-MXsZbSWm8jxl_I0ffc_-R8"
        limit = 500
	req_no = 20

	@staticmethod
	def fetch_fb_pages(query_string):
  		graph = facebook.GraphAPI(FacebookUtil.ACCESS_TOKEN)
		args = {"type" : "page"}
		args["q"] = query_string
		args["fields"] = "id,name,likes,talking_about_count,checkins,category"
		args["limit"] = FacebookUtil.limit
		count = 0
		list = []
		while True:
			args["offset"] = count
			response =  graph.request('search', args)
			if len(response["data"]) == 0: 
				break
			for data in response["data"]:
				count+=1
				if data["category"] == "Musician/band" or data["category"] == "Artist" or data["category"] == "Public figure":
					if not "likes" in data:
						data["likes"] = 0
					if not "talking_about_count" in data:
						data["talking_about_count"] = 0
					list.append(data)
		
		final_list =  sorted(list, key=lambda k: k["likes"],reverse=True)[:FacebookUtil.req_no]
		params = {}
		talking_about_count = 0
		like_count = 0		

		for data in final_list:
			talking_about_count+=int(data["talking_about_count"])
			like_count+=int(data["likes"])

		params["fb_likes"] = like_count
		params["fb_talking_about"] = talking_about_count
		params["fb_count"] = FacebookUtil.req_no
		return params


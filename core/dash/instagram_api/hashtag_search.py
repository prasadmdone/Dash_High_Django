from credentials import getCredentials
import sys
from loguru import logger
import requests
import json

def getHashtagInfo( credentials ) -> dict :

	"""
		THIS MODULE INFO ABOUT HASTAG

	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}


	INPUT:
	--------
	ARG1: CREDENTIALS

	OUTPUT:
	--------
	INFO OF HASTAG 


	"""

	endPointCredentials  = dict() 
	endPointCredentials['user_id'] = credentials['instagram_account_id'] 
	endPointCredentials['q'] = credentials['hashtag_name'] 
	endPointCredentials['fields'] = 'id,name' 
	endPointCredentials['access_token'] = credentials['access_token'] 

	URL = credentials['endpoint_base'] + 'ig_hashtag_search' 

	response = requests.get(URL,endPointCredentials)

	return response.json()

def getHashtagMedia( credentials ) -> dict:

	"""
		THIS MODULE GIVED TOP AND LATEST HASHTAG POST
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}

	INPUT:
	--------
	ARG1: CREDENTIALS

	OUTPUT:
	--------
	DATA ABOUT HASHTAG


	"""

	endPointCredentials = dict() 
	endPointCredentials['user_id'] = credentials['instagram_account_id'] 
	endPointCredentials['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' 
	endPointCredentials['access_token'] = credentials['access_token'] 

	URL = credentials['endpoint_base'] + credentials['hashtag_id'] + '/' + credentials['type'] 

	response = requests.get(URL,endPointCredentials)

	return response

def getRecentlySearchedHashtags( credentials ) -> dict:

	"""
		THIS MODULE GIVEs THE RECECENT HASHTAG 
	
	API ENDPOINTS (GET):
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/recently_searched_hashtags?fields={fields}

	
	INPUT:
	--------
	ARG1: CREDENTIALS

	OUTPUT:
	--------
	DATA ABOUT HASHTAG


	"""

	endPointCredentials = dict() 
	endPointCredentials['fields'] = 'id,name' 
	endPointCredentials['access_token'] = credentials['access_token'] 

	URL =credentials['endpoint_base'] + credentials['instagram_account_id'] + '/' + 'recently_searched_hashtags'

	response = requests.get(URL,endPointCredentials)

	return response.json()

if __name__ == "__main__":

	try:

		credentials = getCredentials()
		credentials['hashtag_name'] = "coding" 
		response = getHashtagInfo( credentials )
		print(response) 
		credentials['hashtag_id'] = response['data'][0]['id']; 

		# logger.info("#################### HASHTAG INFO #########################") 
		
		# logger.info(f"Hashtag:  {hashtag}") 
		# logger.info(f"Hashtag ID:  {credentials['hashtag_id']}")

		# logger.info("###################### HASHTAG TOP MEDIA #######################") 
		
		# credentials['type'] = 'top_media' 
		# hashtagTopMediaResponse = getHashtagMedia( credentials ) 
		#print(json.dumps(hashtagTopMediaResponse))
		# for post in hashtagTopMediaResponse['data'] : 
		# 	logger.info(f"---------- POST ---------") 
		# 	logger.info(f"Link to post: {post['permalink']}") 
		# 	logger.info(f"Post caption: {post['caption']}") 
		# 	logger.info(f"Media type: {post['media_type']}")
		# 	logger.debug(f"Like counter: {post['like_count']}")

		# logger.info("##########################$$$ HASHTAG RECENT MEDIA $$$####################") 
		# params['type'] = 'recent_media' # set call to get recent media for hashtag
		# hashtagRecentMediaResponse = getHashtagMedia( params ) # hit the api for some data!

		# for post in hashtagRecentMediaResponse['json_data']['data'] : # loop over posts
		# 	logger.info(f"---------- POST ---------") # post heading
		# 	logger.info(f"Link to post: {post['permalink']}") # link to post
		# 	logger.info(f"\nPost caption: {post['caption']}") # post caption
		# 	logger.info(f"Media type: {post['media_type']}") # type of media

		# logger.info("##################### USERS RECENTLY SEARCHED HASHTAGS $$$#################") 
		# getRecentSearchResponse = getRecentlySearchedHashtags( credentials ) 

		# print(getRecentSearchResponse)
		# for hashtag in getRecentSearchResponse['data'] : # looop over hashtags
		# 	logger.info("---------- SEARCHED HASHTAG ----------") # searched heading
		# 	logger.info(f"Hashtag:  {hashtag['name']}") # display hashtag
		# 	logger.info(f"Hashtag ID:  {hashtag['id']}") # display hashtag id




	except Exception as e:
		logger.error(f"There is some error in the hashtag {e}")
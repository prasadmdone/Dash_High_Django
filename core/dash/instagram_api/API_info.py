from .credentials import getCredentials
import requests 
import json
import datetime 
from loguru import logger


def applicationInfo( credentials ) -> dict:

	"""
		GET INFO OF THE ACCES TOKEN


	API Endpoint:(GET)
		https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}


	INPUT:
	--------
	ARG1: 	CREDENTIALS 

	OUTPUT:
	--------
	
	RESPONSE OF THE APPLICATION 


	"""


	endPointCredentials = dict()
	endPointCredentials['input_token'] = credentials['access_token']
	endPointCredentials['access_token'] = credentials['access_token'] 

	URL = credentials["graph_domain"] + '/debug_token'

	response = requests.get(URL,endPointCredentials)

	response = response.json()
	logger.info(f"Data Access Expires at:{ datetime.datetime.fromtimestamp( response['data']['data_access_expires_at'] )}") 

	return response


def getLongAccessToken( credentials ) -> dict:

	"""
		GET  THE LONG ACCES TOKEN

	API Endpoint:(GET)
		https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}

	

	INPUT:
	--------
	ARG1: 	CREDENTIALS 

	OUTPUT:
	--------
	
	RESPONSE LONG AUTHENTICATION TOKEN (brear)

	"""
	endPointCredentials = dict() 
	endPointCredentials['grant_type'] = 'fb_exchange_token' 
	endPointCredentials['client_id'] = credentials['client_id'] 
	endPointCredentials['client_secret'] = credentials['client_secret']
	endPointCredentials['fb_exchange_token'] = credentials['access_token'] 


	URL = credentials['endpoint_base'] + 'oauth/access_token' # endpoint url
	
	response = requests.get(URL,endPointCredentials)

	return response



def getInstagramAccountNumber( credentials ) -> dict: 

	"""
		GET INSTAGRAM ACCOUNT ID


	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account


	INPUT:
	--------
	ARG1: 	CREDENTIALS 

	OUTPUT:
	--------
	
	RESPONSE OF THE INSTAGRAM ACCOUNT ID


	"""
	endPointCredentials = dict() 
	endPointCredentials['access_token'] = credentials['access_token'] 
	endPointCredentials['fields'] = 'instagram_business_account' 
	
	URL = credentials['endpoint_base'] + credentials['page_id'] 


	response = requests.get(URL,endPointCredentials)

	return response


def getFacebookPages( credentials ) -> dict:
	"""
		GET INSTAGRAM ACCOUNT ID

	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}


	INPUT:
	--------
	ARG1: 	CREDENTIALS 

	OUTPUT:
	--------
	
	RESPONSE OF THE FACEBOOK PAGE ID


	"""

	endPointCredentials = dict() 
	endPointCredentials['access_token'] = credentials['access_token'] 


	URL = credentials['endpoint_base'] +'me/accounts' 

	response = requests.get(URL,endPointCredentials)

	return response
	

if __name__ == '__main__':

	credentials = getCredentials()
	#--------------info-----------------------#
	# response = applicationInfo(credentials)
	# print(response)

	# THIS FOR THE LONGLIVED ACCESS TOKEN do only once you got 
	# change in the dotenv file 

	#--------------long response token-----------------#
	# response_token = getLongAccessToken(credentials)
	# print(json.dumps(response_token.json()))

	#--------to get instagram account id-------------#
	# response = getInstagramAccountNumber(credentials)
	# print(response.json())


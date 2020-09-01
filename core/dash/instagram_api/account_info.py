from .credentials import getCredentials
from loguru import logger 
import requests
import json

class AccountInfo:

	def __init__(self,credentials):
		self.credentials = credentials


	def activateAccount(self):
		"""
		API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}

		"""

		endpointCredentials = dict() 
		endpointCredentials['fields'] = 'business_discovery.username(' + self.credentials['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' 
		endpointCredentials['access_token'] = self.credentials['access_token'] 

		url = self.credentials['endpoint_base'] + self.credentials['instagram_account_id'] 

		data = requests.get( url, endpointCredentials)

		self.data = data.json()



	def getAccountInfo(self):

		final_list = []
		final_list.append(self.data['business_discovery']['follows_count'])
		final_list.append(self.data['business_discovery']['followers_count'])
		final_list.append(self.data['business_discovery']['media_count'])
		return final_list






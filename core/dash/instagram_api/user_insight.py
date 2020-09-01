from loguru import logger
import requests
from .credentials import getCredentials
import json

class userInsight:


	def __init__(self,credentials):

		self.credentials = credentials


	def activateUserInsights(self,flag) -> dict :

		"""
			THIS MODULE WILL HELP TO FIND THE USER INSIGHT


		API Endpoint:
			https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}



		INPUT:
		--------
		ARG1: CREDENTIALS
		ARG1: FLAG --> ENABLES THE DATA ANALYTICS OF USER READ FACEBOOK DOCUMENTATION

		OUTPUT:
		--------
		
		IF (DAY):

		[IMPRESSION,GET_DIRECTION_CLICKS,PHONE_CALL_CLICKS]
		
		ELSE (LIFETIME):

		[AUDIENCE_CITY , AUDIENCE_COUNTRY , AUDIENCE_GENDER_AGE}

		"""
		try:

			endPointCredentials = dict()
			if flag:
				endPointCredentials['metric'] = 'audience_city,audience_country,audience_gender_age,audience_locale,online_followers,' 
				endPointCredentials['period'] = 'lifetime'
			else:
				endPointCredentials['metric'] = 'email_contacts,follower_count,get_directions_clicks,phone_call_clicks,profile_views,text_message_clicks,website_clicks' 
				endPointCredentials['period'] = 'day'

			endPointCredentials['access_token'] = self.credentials['access_token'] 

			URL = self.credentials['endpoint_base'] + self.credentials['instagram_account_id'] + '/insights' 

			data = requests.get( URL, endPointCredentials )

			self.userInsights = data 

		except Exception as e:

			logger.error(f"Error in the insight{e}")


	def getAudienceCity(self) -> list:
		
		"""
			THIS MODULE WILL HELP TO FIND THE USER TARGET CITYS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER CITY LIST AND COUNT  
		
		"""
		data = self.userInsights.json()

		data_list  = [[],[]]

		for city,count in data['data'][0]['values'][0]['value'].items():
			data_list[0].append(city.split(',')[0])
			data_list[1].append(count)

		return data_list

	def getAudienceCountry(self) -> list:
		
		"""
			THIS MODULE WILL HELP TO FIND THE USER TARGET CITYS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER CITY LIST AND COUNT  
		
		"""
		data = self.userInsights.json()

	
		return data['data'][1]['values'][0]['value']


	def getAudienceGenderAge(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER TARGET CITYS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER CITY LIST AND COUNT  
		
		"""

		data = self.userInsights.json()

		final_list = [[],[]]

		out_put = data['data'][2]['values'][0]['value']
		

		for gender,age in out_put.items():
			final_list[0].append(gender)
			final_list[1].append(age)
	
		return final_list 

	def getOnlineFollowers(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER  ONLINE FOLLOWER COUNT


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER ONLINE FOLLOWER COUNT
		
		"""

		data =self.userInsights.json()


		return data['data'][4]['values'][0]['value']

	def getEmailContacts(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER EMIAL CONTACTS 


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER EMIAL CONTACTS 
		
		"""

		data = self.userInsights.json()

		return data['data'][0]['values']


	def getFollowerCount(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER  FOLLOWER COUNT


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER FOLLOWER COUNT
		
		"""

		data = self.userInsights.json()


		return data['data'][1]['values']


	def getDirectionsClicks(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER  DIRECTION CLICKS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER DIRECTION CLICKS
		
		"""

		data = self.userInsights.json()


		return data['data'][2]['values']

	def getPhoneCallClicks(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER PHONE CALL CLICKS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER PHONE CALL CLICKS
		
		"""

		data = self.userInsights.json()


		return data['data'][3]['values']

	def getProfileViews(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER USER PROFILE VIEWS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		USER PROFILE VIEWS
		
		"""

		data = self.userInsights.json()


		return data['data'][4]['values']

	def getTextMessageClicks(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER TEXT MESSAGE CLICKS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		TEXT MESSAGE CLICKS
		
		"""

		data = self.userInsights.json()


		return data['data'][5]['values']

	def getWebsiteClicks(self) -> dict:

		"""
			THIS MODULE WILL HELP TO FIND THE USER TARGET CITYS


		INPUT:
		--------
		ARG1: USERINSIGHT (JSON FORMAT)

		OUTPUT:
		--------
		WEBSITE CLICKS
		
		"""

		data = self.userInsights.json()


		return data['data'][6]['values']
	



if __name__ == '__main__':

	credentials = getCredentials()

	data = userInsight(credentials)
	data.activateUserInsights(False)

	print(data.getWebsiteClicks())



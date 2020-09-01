from dotenv import load_dotenv
import os 
from loguru import logger
load_dotenv()


def getCredentials() -> dict:

	"""
		THIS MODULE WILL RETURN CREDENTIALS

	INPUT:
	--------
	ARG1: NONE

	OUTPUT:
	--------
	CREDENTIALS 


	"""
	try:


		credentials = dict()
		credentials['access_token'] = os.getenv("ACCESS_TOKEN")
		credentials['client_id'] = os.getenv('FB-APP-CLIENT-ID') 
		credentials['client_secret'] = os.getenv('FB-APP-CLIENT-SECRET') 
		credentials['graph_domain'] = 'https://graph.facebook.com/'
		credentials['graph_version'] = os.getenv("VERSION") 
		credentials['endpoint_base'] = credentials['graph_domain'] + credentials['graph_version'] + '/' 
		credentials['page_id'] =os.getenv('FB-PAGE-ID') 
		credentials['instagram_account_id'] = os.getenv('INSTAGRAM-BUSINESS-ACCOUNT-ID') 
		credentials['ig_username'] = os.getenv("IG-USERNAME")
		
		return credentials

	except Exception as e:
		logger.error("Please check your Dotenv file",e)
		raise


if __name__ == '__main__':
	print(getCredentials())

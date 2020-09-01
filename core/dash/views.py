from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View 
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required 
from loguru import logger

# Importing the instagram api.
from .instagram_api import credentials 
from .instagram_api import user_insight
from .instagram_api import account_info

# i dont know this is the right way but doing this way
credentials = credentials.getCredentials()
data_lifetime = user_insight.userInsight(credentials)
data_lifetime.activateUserInsights(True)
data_day = user_insight.userInsight(credentials)
data_day.activateUserInsights(False)
account_data = account_info.AccountInfo(credentials)
account_data.activateAccount()
account_data = account_data.getAccountInfo()


@login_required
def mainPage(request):
    return render(request,"index.html",{"inst":account_data})


class CityData(APIView):
    
    final_data = data_lifetime.getAudienceCity()

    def get(self, request, format = None): 
        labels = self.final_data[0]
        chartLabel = "my data"
        chartdata = self.final_data[1] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        logger.debug(f"data has been send {labels} \n {chartLabel} \n {chartdata}")
        return Response(data) 


class GenderAge(APIView):
    
    final_data = data_lifetime.getAudienceGenderAge()
    
    def get(self, request, format = None): 
        labels = self.final_data[0]
        chartLabel = "my data"
        chartdata = self.final_data[1] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        logger.debug(f"data has been send {labels} \n {chartLabel} \n {chartdata}")
        return Response(data) 
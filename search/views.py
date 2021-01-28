from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.throttling import UserRateThrottle
import requests 
import json
from .models import Questions
from rest_framework.throttling import AnonRateThrottle

@api_view(['POST'])
def index(request):
    q=request.data.get("q")


    URL = "https://api.stackexchange.com/2.2/search/advanced"
    
    # location given here 
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'q':q, 'site':'stackoverflow'
    } 
    try:
        chachedResult=Questions.objects.get(searchTerm=json.dumps(PARAMS))
    except Exception as e:
        print(e)
        chachedResult=None
    if chachedResult==None:
        print('1')
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()    
        q=Questions(searchResult=data,searchTerm=json.dumps(PARAMS))
        print(q.id)
        q.save()
    else:
        print('2')
        data=chachedResult.searchResult
    print(data)
    return Response({'data': data})

@api_view(['POST'])
def complexQuery(request):
    q=request.data.get("q")
    title=request.data.get('title')
    body=request.data.get('body')
    url=request.data.get('url')
    tagged=request.data.get('tagged')
    nottagged=request.data.get('nottagged')
    views=request.data.get('views')
    answers=request.data.get('answers')
    closed=request.data.get('closed')
    accepted=request.data.get('accepted')
    migrated=request.data.get('migrated')
    notice=request.data.get('notice')
    wiki=request.data.get('wiki')




    URL = "https://api.stackexchange.com/2.2/search/advanced"
    
    # location given here 
    
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {'q':q, 'title':title, 'body':body,'url':url,"tagged":tagged,'nottagged':nottagged,'views':views,'answers':answers,'closed':closed,'accepted':accepted,'migrated':migrated,'notice':notice,'wiki':wiki, 'site':'stackoverflow'
    } 
    try:
        chachedResult=Questions.objects.get(searchTerm=json.dumps(PARAMS))
    except Exception as e:
        print(e)
        chachedResult=None
    if chachedResult==None:
        print('1')
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()    
        q=Questions(searchResult=data,searchTerm=json.dumps(PARAMS))
        print(q.id)
        q.save()
    else:
        print('2')
        data=chachedResult.searchResult
    print(data)
    return Response({'data': data})
import requests

def get_user_insights(access_token = '',api_url = '',ig_user_id = '',period = '',metric ='',since = '',until=''):
    url = api_url + ig_user_id + '/insights'
    param = dict()
    param['metric'] = metric
    param['period'] = period
    param['since'] = since
    param['until'] = until
    param['access_token'] = access_token
    response = requests.get(url=url,params=param)
    print("\n response",response)
    response = response.json()
    print("\n response",response)
    return response

def get_post_insights(access_token = '',api_url = '',instagram_account_id = ''):
    url = api_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    response = requests.get(url=url, params=param)
    response = response.json()
    media_insights = []
    for i in response['data']:
        url = api_url + i + '/insights'
        param = dict()
        param['access_token'] = access_token
        param['metric'] = 'engagement,impression,reach,saved,video_views'
        response = requests.get(url=url,params=param)
        print("\n response",response)
        response = response.json()
        media_insights.append(response)
        print("\n response",response)
    return response
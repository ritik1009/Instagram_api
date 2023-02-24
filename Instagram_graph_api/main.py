import requests
from insights import get_user_insights,get_post_insights

client_id = ''
client_secret = ''
redirect_url = 'https://ritik1009.github.io'
access_url = 'https://www.facebook.com/v13.0/dialog/oauth?response_type=token&display=popup&client_id=1&redirect_uri=https://ritik1009.github.io&auth_type=rerequest&scope=user_location%2Cuser_photos%2Cuser_friends%2Cuser_gender%2Cpages_show_list%2Cinstagram_basic%2Cinstagram_manage_comments%2Cinstagram_manage_insights%2Cpages_read_engagement%2Cpublic_profile'
graph_url = 'https://graph.facebook.com/v15.0/'

def func_get_url():
    print('\n access code url',access_url)
    code = input("\n enter the url")
    code = code.rsplit('access_token=')[1]
    code = code.rsplit('&data_access_expiration')[0]
    return code

def get_access_token(access_code = ''):
    url = graph_url + 'oauth/access_token'
    param = dict()
    param['client_id'] = client_id
    param['redirect_uri'] = redirect_url
    param['client_secret'] = client_secret
    param['code'] = access_code
    response = requests.get(url =url,params=param)
    print("\n response",response)
    response = response.json()
    print("\n response", response)
    access_tokken = response
    return access_tokken
    
def func_get_page_id(access_token = ''):
    url = graph_url + 'me/accounts'
    param = dict()
    param['access_token'] = access_token
    response = requests.get(url = url,params=param)
    print("\n response", response)
    response = response.json()
    print("\n response", response)
    page_id = response['data'][0]['id']
    print("\n page_id",page_id)
    return page_id

def func_get_instagram_business_account(page_id = '',access_token = ''):
    url = graph_url + page_id
    param = dict()
    param['fields'] = 'instagram_business_account'
    param['access_token'] = access_token
    response = requests.get(url = url,params=param)
    print("\n response",response)
    response = response.json()
    print("\n response", response)
    try:
        instagram_account_id = response['instagram_business_account']['id']
    except:
        return {'error':'Instagram account not linked'}
    return instagram_account_id


def get_post_data(media_id='', access_token=''):
    url = graph_url + media_id
    param = dict()
    param['fields'] = 'caption,like_count,media_url,owner,permalink'
    param['access_token'] = access_token
    response = requests.get(url=url, params=param)
    response = response.json()
    return response


def func_get_media_id(instagram_account_id = '',access_token = ''):
    url = graph_url + instagram_account_id +'/media'
    param = dict()
    param['access_token'] = access_token
    response = requests.get(url =url,params = param)
    response = response.json()
    media = []
    for i in response['data']:
        media_data = get_post_data(media_id =i['id'],access_token=access_token)
        media.append(media_data)
    return media

def get_post_data(media_id='',access_token=''):
    url = graph_url + media_id
    param = dict()
    param['fields'] = 'caption,like_count,media_url,owner,permalink'
    param['access_token'] = access_token
    response = requests.get(url = url,params =param)
    response =response.json()
    return response

def func_get_long_lived_access_token(access_token = ''):
    url = graph_url + 'oauth/access_token'
    param = dict()
    param['grant_type'] = 'fb_exchange_token'
    param['client_id'] = client_id
    param['client_secret'] = client_secret
    param['fb_exchange_token'] = access_token
    response = requests.get(url = url,params=param)
    print("\n response",response)
    response =response.json()
    print("\n response",response)
    long_lived_access_tokken = response['access_token']
    return long_lived_access_tokken

access_code = func_get_url()
#print(get_access_token(access_code=access_code))
long_lived_access_token = func_get_long_lived_access_token(access_token=access_code)

page_id =func_get_page_id(access_token=long_lived_access_token)
insta_id = func_get_instagram_business_account(page_id=page_id,access_token=long_lived_access_token)
post_data = func_get_media_id(instagram_account_id= insta_id,access_token=long_lived_access_token)


user_insights = get_user_insights(access_token=long_lived_access_token, api_url=graph_url,
                                  ig_user_id=insta_id, period='day', metric='follower_count', since='', until='')

post_insights = get_post_insights(access_token=long_lived_access_token, api_url=graph_url, instagram_account_id=insta_id)

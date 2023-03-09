import requests
from insights import get_user_insights,get_post_insights

client_id = ''
client_secret = ''
redirect_url = 'https://ritik1009.github.io'
access_url = ''
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
    #for i in response['data']:
    #    media_data = get_post_data(media_id =i['id'],access_token=access_token)
    #    media.append(media_data)
    #print("\n medeia_data",media)
    return response

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


from main import *
import requests
import config

page_id = func_get_page_id(config.access_token)
print("\n page_id", page_id)
instagram_account_id = func_get_instagram_business_account(
    page_id=page_id, access_token=config.access_token)
print("\n instagram account id", instagram_account_id)

################ Getting Hashtag_id ####################
def get_hashtag_id(hashtag = ''):
    url = config.graph_url + 'ig_hashtag_search'
    param = dict()
    param['user_id'] = instagram_account_id
    param['q'] = hashtag
    param['access_token'] = config.access_token
    response = requests.get(url,param)
    response = response.json()
    hashtag_id = response['data'][0]['id']
    return hashtag_id
#########################################################

################# Getting the data regarding a hashtag ##############
def get_data_of_hashtag(hashtag_id = ''):
    url = config.graph_url + hashtag_id
    param =dict()
    param['access_token'] = config.access_token
    param['fields'] = 'id,name'
    response = requests.get(url,param)
    response = response.json()
    print(response)
    return response
###################################################################

################## getting the top Media ###########################
def get_top_media(hashtag_id=''):
    url = config.graph_url + hashtag_id + '/top_media'
    param = dict()
    param['access_token'] = config.access_token
    param['user_id'] = instagram_account_id
    param['fields'] = 'caption,like_count,permalink'
    response = requests.get(url, param)
    response = response.json()
    print(response)
    return response
######################################################################

################# getting recent media ################################
def get_recent_media(hashtag_id=''):
    url = config.graph_url + hashtag_id + '/recent_media'
    param = dict()
    param['access_token'] = config.access_token
    param['user_id'] = instagram_account_id
    param['fields'] = 'caption,like_count,permalink'
    response = requests.get(url, param)
    response = response.json()
    print(response)
    return response
#########################################################################

################## Recently searched Hashtags ###########################


def get_recent_searched_hashtag():
    url = config.graph_url + instagram_account_id + '/recently_searched_hashtags'
    param = dict()
    param['access_token'] = config.access_token
    #param['user_id'] = instagram_account_id
    #param['fields'] = 'caption,like_count,permalink'
    response = requests.get(url, param)
    response = response.json()
    print(response)
    return response
#########################################################################

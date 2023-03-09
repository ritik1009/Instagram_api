from main import *
import requests
import config

page_id = func_get_page_id(config.access_token)
print("\n page_id",page_id)
instagram_account_id = func_get_instagram_business_account(page_id=page_id,access_token=config.access_token)
print("\n instagram account id",instagram_account_id)
media_data = func_get_media_id(instagram_account_id=instagram_account_id,access_token=config.access_token)
print("\n media_id",media_data)

############################ posting a comment on a picture ###################################
def post_comment(message = ''):
    media_id = media_data['data'][-1]['id']
    print("\n media_data",media_id)
    url = config.graph_url + media_id +'/comments'
    param = dict()
    param['message'] = message
    param['access_token'] = config.access_token
    print("\n URL",url)
    response = requests.post(url,params=param)
    print("\n response content",response.content)
    response = response.json()
    return response
###############################################################################################

################################## Getting the Comment #################################
def get_comment(ig_media_id=''):
    url = config.graph_url + ig_media_id + '/comments'
    param = dict()
    param['access_token'] = config.access_token
    response = requests.get(url,param)
    response = response.json()
    print(response)
    return response
#########################################################################################

################################## Getting the Comments Replies #############################
def get_comment_replies(ig_comment_id=''):
    url = config.graph_url + ig_comment_id + '/replies'
    param = dict()
    param['access_token'] = config.access_token
    response = requests.get(url, param)
    response = response.json()
    print(response)
    return
#############################################################################################

################################## Posting the reply to the comment #########################
def post_comment_reply(ig_comment_id='',message = ''):
    url = config.graph_url + ig_comment_id + '/replies'
    param = dict()
    param['message'] = message
    param['access_token'] = config.access_token
    print("\n URL", url)
    response = requests.post(url, params=param)
    print("\n response content", response.content)
    response = response.json()
    return response
#############################################################################################

################################## Hide/Unhide Comment ####################################
def hide_unhide_comment(ig_comment_id = ''):
    url = config.graph_url + ig_comment_id
    param = dict()
    param['hide'] = True
    param['access_token'] = config.access_token
    #print("\n URL", url)
    response = requests.post(url, params=param)
    response = response.json()
    print("\n response",response)
    return response
##########################################################################################

################################### enable/disable comment ##############################
def enable_disbale_comment(ig_media_id = ''):
    url = config.graph_url + ig_media_id
    param = dict()
    param['comment_enabled'] = True
    param['access_token'] = config.access_token
    #print("\n URL", url)
    response = requests.post(url, params=param)
    response = response.json()
    print("\n response", response)
    return response
#########################################################################################

################################## Deleting Ig comment #################################
def delete_comment(ig_comment_id = ''):
    url = config.graph_url + ig_comment_id
    param = dict()
    param['access_token'] = config.access_token
    #print("\n URL", url)
    response = requests.delete(url, params=param)
    response = response.json()
    print("\n response", response)
    return response

message = 'hello this is a comment using the graph api'
reply_message = "This is a reply using the Instagram Graph API"

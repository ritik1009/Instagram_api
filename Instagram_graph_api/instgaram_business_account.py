from main import *
import requests
import config

page_id = func_get_page_id(config.access_token)
print("\n page_id",page_id)
instagram_account_id = func_get_instagram_business_account(page_id=page_id,access_token=config.access_token)
print("\n instagram account id",instagram_account_id)

def func_get_business_account_deatils(search_id=''):
    url =config.graph_url + instagram_account_id 
    param = dict()
    param['fields'] = 'business_discovery.username('+search_id + \
        '){followers_count,follows_count,name,biography,username,profile_picture_url,id, media_count,media{comments_count,like_count,media_url,permalink,user_name,caption,timestamp,media_type,media_product_type}}'
    param['access_token'] = config.access_token
    response = requests.get(url,params=param)
    response =response.json()
    return response

account_name = 'selenagomez'

print(func_get_business_account_deatils(search_id=account_name))
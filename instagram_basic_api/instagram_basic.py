import requests
import urllib.parse
client_id = '512891473882043' # instagram APP ID
client_secret = 'edaa6d4914b8f9dacacec73939f9cd9f' # instagarm App Secret
redirect_uri = 'https://ritik1009.github.io/'
auth_url = 'https://api.instagram.com/'
graph_url = 'https://graph.instagram.com/'

def get_the_authorization_window():
    url = auth_url + 'oauth/authorize'
    param = dict()
    param['client_id'] = client_id
    param['redirect_uri'] = redirect_uri
    param['scope'] = 'user_profile,user_media,instagram_graph_user_profile,instagram_graph_user_media '
    param['response_type'] = 'code'
    parameters = urllib.parse.urlencode(param)
    url = url +'?'+ parameters
    print('\n parameters',url)
    code = input('\n Enter the url :-')
    code = code.rsplit('code=')[1]
    code = code.replace('#_','')
    return code
    

def get_short_lived_access_token(code = ''):
    url = auth_url + 'oauth/access_token'
    param = dict()
    param['client_id'] = client_id
    param['client_secret'] = client_secret
    param['code'] = code
    param['grant_type'] = 'authorization_code'
    param['redirect_uri'] = redirect_uri
    print("\n param",param)
    response = requests.post(url=url,data=param)
    response = response.json()
    print("\n short lived access token response :-",response)
    try:
        access_token = response['access_token']
        user_id = response['user_id']
        return access_token
    except:
        print("\n error",response)
        
def get_long_lived_access_token(access_token = ''):
    url = graph_url + 'access_token'
    param = dict()
    param['grant_type'] = 'ig_exchange_token'
    param['client_secret'] = client_secret
    param['access_token'] = access_token
    response = requests.get(url=url,params=param)
    response = response.json()
    print("\n long_lived_token_response :-",response)
    long_lived_access_token = response['access_token']
    expires_in = response['expires_in']
    return long_lived_access_token

def get_refresh_token(access_token = ''):
    url = graph_url + 'refresh_access_token'
    param = dict()
    param['grant_type'] = 'ig_refresh_token'
    param['access_token'] = access_token
    response = requests.get(url=url,params= param)
    response = response.json()
    access_token = response['access_token']
    expires_in = response['expires_in']
    return access_token

def get_all_the_media(access_token = ''):
    url = graph_url + 'me/media'
    param = dict()
    param['fields'] = 'id,username,caption,media_type,media_url,permalink,timestamp'
    param['access_token'] = access_token
    response = requests.get(url=url,params = param)
    response = response.json()
    return response
        
        
#code = get_the_authorization_window()
#short_lived_access_token = get_short_lived_access_token(code=code)
#long_lived_access_token =get_long_lived_access_token(access_token = short_lived_access_token) 
print(get_all_the_media(access_token='IGQVJVM0h0eEpLY3E0SzVzTDRPLVc0bjlTZAGdxeHE5dUNIWmJDRC0yT1M1V0lqSmdWaFI3U2tjUnR2SnUyb1ZAEb3hzaU14VFRYMnd4YzRrOVZASdHdmSGhXUEljbWNaZAG84SGZAacnNR'))

    

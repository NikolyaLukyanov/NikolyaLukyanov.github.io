import requests
import json


def take_1000_posts():
    tocken='cd6ad61ccd6ad61ccd6ad61c63cd056944ccd6acd6ad61c9323af835d1afa79027bd29e'
    version=5.103
    domain='bmstu1830'
    offset=0
    count=100
    all_posts=[]

    while offset < 1000:
        response=requests.get ( 'https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': tocken,
                                    'v': version,
                                    'domain': domain
                                } )
        data = response.json()['response'] ['items']
        offset += 100
        all_posts.extend(data)
    return all_posts

all_posts = take_1000_posts()
with open ( 'vk.json',"w", encoding='utf-8') as file:
        json.dump (take_1000_posts(), file)




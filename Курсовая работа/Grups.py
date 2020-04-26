import requests
import json


token='9960201fe990557f6ae56e2c7b041dd81abe0b4a6aff07979a0f8baddfc583bae18dd8cc1d6f19d186689'
version=5.103
extended=1

class People(object):
    group=[]
    def __init__(self, id, ids):
        self.id= id
        self.ids=ids

    def groups(self):
        response2=requests.get ( 'https://api.vk.com/method/groups.get',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'user_id': self.ids,
                                     'extended': extended,
                                 } )
        data=response2.json ()['response']['items']
        self.group.extend ( data )
        return self.group


if __name__ == "__main__":
    vlad_samoylenko=People('id155384397','155384397')
vlad_samoylenko.groups ()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_samoylenko.groups (), file )
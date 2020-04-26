import requests
import json

token='9960201fe990557f6ae56e2c7b041dd81abe0b4a6aff07979a0f8baddfc583bae18dd8cc1d6f19d186689'
version=5.103
extended=1

class People(object):
    user=[]
    fields='bdate, city, mobile_phone,home_phone,friends,music,about'
    def __init__(self, id, ids):
        self.id= id
        self.ids=ids

    def users(self):
       response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': self.id,
                                        'fields': self.fields

                                    } )
       data=response.json ()['response']
       self.user.extend ( data )
       return self.user

if __name__ == "__main__":
    vlad_samoylenko=People('id155384397','155384397')
vlad_samoylenko.users()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_samoylenko.users(), file )
import SQL
import requests
import json
import pymysql.cursors

token='cd6ad61ccd6ad61ccd6ad61c63cd056944ccd6acd6ad61c9323af835d1afa79027bd29e'
version=5.103
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class vlad_samoylenko:
    id='id155384397'
    all_posts=[]
    offset=0
    fields='about,bdate,city,contacts,counters,music'


    def take_1_posts(self):
        while self.offset == 0:
            response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': self.id,
                                        'offset': self.offset,
                                        'fields': self.fields

                                    } )
            data=response.json ()['response']
            self.offset+=1
            self.all_posts.extend ( data )

        while self.offset == 1:
            response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'domain': self.id,
                                        'offset': self.offset,


                                    })
            data=response1.json ()['response']['items']
            self.offset+=1
            self.all_posts.extend ( data )
        while self.offset == 1:
            response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'domain': self.id,
                                        'offset': self.offset
                                    })
            data=response1.json ()['response']
            self.offset+=1
            self.all_posts.extend ( data )

        return self.all_posts

vlad_s=vlad_samoylenko()
vlad_s.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_s.take_1_posts(), file )




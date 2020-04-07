import requests
import json
import pymysql.cursors

token='84122802c8f32e0b9f9fe4d518c9ad2335246592a61fa23aeb76e028f1e99ca03a1050941f219c333c765'
version=5.103
extended=1



class vlad_samoylenko:
    id='id155384397'
    ids='155384397'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'


    def take_1_posts(self):

            response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': self.id,
                                        'fields': self.fields

                                    } )
            data=response.json ()['response']
            self.all_posts.extend ( data )
            return self.all_posts
    def take_1_walls (self):
            response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'domain': self.id,
                                    })
            data=response1.json ()['response']['items']
            self.all_walls.extend ( data )
            return self.all_walls

    def take_1_groups(self):

              response2=requests.get ( 'https://api.vk.com/method/groups.get',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'user_id': self.ids,
                                     'extended': extended,
                                 } )
              data=response2.json ()['response']['items']
              self.all_groups.extend ( data )
              return self.all_groups

vlad_s=vlad_samoylenko()
vlad_s.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_s.take_1_posts(), file )
vlad_s=vlad_samoylenko()
vlad_s.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_s.take_1_walls(), file )
vlad_s=vlad_samoylenko()
vlad_s.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_s.take_1_groups(), file )


with open ('vk.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vk.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
connection.close ()
with open ('vkq.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkq.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`post_type`,`text`,`likes`) VALUES (%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'post_type' ), item.get ( 'text' ),item.get('likes').get('count')))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
connection.close ()


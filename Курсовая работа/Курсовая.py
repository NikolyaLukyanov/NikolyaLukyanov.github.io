import requests
import json
import pymysql.cursors

token='5f0571d294195b8bcdbd9597c247fc1f75845c3bdd2a8d5de0b65c16e01d99667845fd92b30598fe7adf0'
version=5.103
extended=1



class vlad_samoylenko:
    id='id155384397'
    ids='155384397'
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


        while self.offset == 2:
              response2=requests.get ( 'https://api.vk.com/method/groups.get',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'user_id': self.ids,
                                     'extended': extended,
                                     'offset': self.offset
                                 } )
              data=response2.json ()['response']
              self.offset+=1
              self.all_posts.extend ( data )

        return self.all_posts

vlad_s=vlad_samoylenko()
vlad_s.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_s.take_1_posts(), file )



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
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`post_type`,`text`,`photo`,`likes`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s  )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get ( 'post_type' ), item.get ( 'text' ),
                item.get('url'),item.get('likes').get('count')) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()


    connection.close ()
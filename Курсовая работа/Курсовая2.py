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
                sql="INSERT INTO `json` (`post_type`,`text`,`likes`) VALUES (%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'post_type' ), item.get ( 'text' ),item.get('likes').get('count')))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
            for attachment in post:
                for photo in post:
                   for size in post:
                     with connection.cursor () as cursor:
                      sql="INSERT INTO `json` (`photo`) VALUES (%s )"
                      cursor.execute (sql, (
                      size.get ( 'url' )))
                      # connection is not autocommit by default. So you must commit to save
                      # your changes.
                      connection.commit ()








connection.close ()
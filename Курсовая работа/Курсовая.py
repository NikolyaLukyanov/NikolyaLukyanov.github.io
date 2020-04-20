import requests
import json
import pymysql.cursors

token='ca516c97f990d1b1b29ae0fc6f476a79fa52b81ae217fc14f4421881c6cf401c98c5f9ae4e1b3e8d7af37'
version=5.103
extended=1



class vlad_samoylenko:
    id='id155384397'
    ids='155384397'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['1'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['1'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['1'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['1'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class misha_chemodanov:
    id='id122123897'
    ids='122123897'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

misha_ch=misha_chemodanov()
misha_ch.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (misha_ch.take_1_posts(), file )
misha_ch=misha_chemodanov()
misha_ch.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (misha_ch.take_1_walls(), file )
misha_ch=misha_chemodanov()
misha_ch.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (misha_ch.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['2'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                    item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                    item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                    item.get ( 'music' ), item.get ( 'about' ), item.get ( 'ID_p', ['2'] )) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['2'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['2'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class svatoslav_strelnikov:
    id='id226165635'
    ids='226165635'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

svatoslav_str=svatoslav_strelnikov()
svatoslav_str.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (svatoslav_str.take_1_posts(), file )
svatoslav_str=svatoslav_strelnikov()
svatoslav_str.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (svatoslav_str.take_1_walls(), file )
svatoslav_str=svatoslav_strelnikov()
svatoslav_str.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (svatoslav_str.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['3'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ), item.get ( 'ID_p', ['3'] )) )

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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['3'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['3'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class andrey_strelnikov:
    id='id204756182'
    ids='204756182'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

andrey_str=andrey_strelnikov()
andrey_str.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (andrey_str.take_1_posts(), file )
andrey_str=andrey_strelnikov()
andrey_str.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (svatoslav_str.take_1_walls(), file )
andrey_str=andrey_strelnikov()
andrey_str.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (andrey_str.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['4'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['4'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['4'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['4'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class alexsandr_chyfistov:
    id='id169916098'
    ids='169916098'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

alexsandr_ch=alexsandr_chyfistov()
alexsandr_ch.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_ch.take_1_posts(), file )
alexsandr_ch=alexsandr_chyfistov()
alexsandr_ch.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_ch.take_1_walls(), file )
alexsandr_ch=alexsandr_chyfistov()
alexsandr_ch.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_ch.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['5'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['5'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['5'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['5'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class lukyanov_nikolya:
    id='id287961694'
    ids='287961694'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

lukyanov_n=lukyanov_nikolya()
lukyanov_n.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (lukyanov_n.take_1_posts(), file )
lukyanov_n=lukyanov_nikolya()
lukyanov_n.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (lukyanov_n.take_1_walls(), file )
lukyanov_n=lukyanov_nikolya()
lukyanov_n.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (lukyanov_n.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['6'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['6'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['6'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['6'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class borodin_ivan:
    id='id226159703'
    ids='226159703'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

borodin_i=borodin_ivan()
borodin_i.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (borodin_i.take_1_posts(), file )
borodin_i=borodin_ivan()
borodin_i.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (borodin_i.take_1_walls(), file )
borodin_i=borodin_ivan()
borodin_i.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (borodin_i.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['7'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['7'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['7'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['7'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class alexsandr_ermolin:
    id='id207484334'
    ids='207484334'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

alexsandr_erm=alexsandr_ermolin()
alexsandr_erm.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_erm.take_1_posts(), file )
alexsandr_erm=alexsandr_ermolin()
alexsandr_erm.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_erm.take_1_walls(), file )
alexsandr_erm=alexsandr_ermolin()
alexsandr_erm.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (alexsandr_erm.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['8'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['8'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['8'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['8'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class dany_epifanov:
    id='id160504052'
    ids='160504052'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

dany_e=dany_epifanov()
dany_e.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_posts(), file )
dany_e=dany_epifanov()
dany_e.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_walls(), file )
dany_e=dany_epifanov()
dany_e.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['8'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['8'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['8'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['8'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()
class dany_epifanov:
    id='id160504052'
    ids='160504052'
    all_posts=[]
    all_walls=[]
    all_groups=[]
    fields='about,bdate,city,contacts,counters,music'
    offset=0

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

dany_e=dany_epifanov()
dany_e.take_1_posts()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_posts(), file )
dany_e=dany_epifanov()
dany_e.take_1_walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_walls(), file )
dany_e=dany_epifanov()
dany_e.take_1_groups()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (dany_e.take_1_groups(), file )


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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['9'])) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`ID_p`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql,(
                item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get ( 'is_closed' ),
                item.get ( 'can_access_closed' ), item.get ( 'bdate' ), item.get ( 'city',['null'] ),
                item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                item.get ( 'music' ), item.get ( 'about' ),item.get('ID_p',['9'])) )
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
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`ID_p`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute (sql,(
                item.get ( 'text' ),item.get('likes').get('count'),item.get('comments').get('count'),
                item.get('reposts').get('count'),item.get('ID_p',['9'])))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print("Error")
connection.close ()
with open ('vkw.json') as json_file:
    post = json.load(json_file)
    print(post)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
                with connection.cursor () as cursor:
                    # Create a new record
                    sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`ID_p`) VALUES (%s,%s,%s,%s )"
                    cursor.execute ( sql, (
                        item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),item.get('ID_p',['9'])) )
                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                connection.commit ()
        except Exception:
            print("Error")
connection.close ()





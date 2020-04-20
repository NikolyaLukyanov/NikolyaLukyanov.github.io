import requests
import json
import pymysql.cursors

token='081bb4e0995fbf2b149454b7e7fa944c22e41d1c1f14de0267036cb99b30f0b7c7862b90c607b6cba1787'
version=5.103
extended=1

class People(object):
    group=[]
    user=[]
    wall=[]

    def __init__(self, id, ids):
        self.id= id
        self.ids=ids

    def users(self):
        offset=0
        while offset<1:
            response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': self.id,
                                        'offset': offset

                                    } )
            data=response.json ()['response']
            offset+=1
            self.user.extend ( data )
            return self.user

    def walls(self):
        response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'domain': self.id,
                                 } )
        data=response1.json ()['response']['items']
        self.wall.extend ( data )
        return self.wall


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
Peopl=People()
Peopl.users()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (Peopl.users(), file )
Peopl=People()
Peopl.walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump ( Peopl.walls(), file )
Peopl=People()
Peopl.groups ()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump ( Peopl.groups (), file )

with open ( 'vk.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vk.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `people` (`first_name`,`last_name`) VALUES (%s ,%s)"
                cursor.execute ( sql, (
                    item.get ( 'first_name' ), item.get ( 'last_name' ),) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
connection.close ()
with open ( 'vk.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vk.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`json_has_wall_idjson_has_wall) VALUES (%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ),
                    item.get ( 'bdate' ), item.get ( 'city' ).get ( 'title' ),
                    item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                    item.get ( 'music' ), item.get ( 'about' ), item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`home_phone`,`friends`,`music`,`about`,`json_has_wall_idjson_has_wall`) VALUES (%s ,%s ,%s ,%s ,%s,%s,%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ),
                    item.get ( 'bdate' ), item.get ( 'city', ['null'] ),
                    item.get ( 'mobile_phone' ), item.get ( 'home_phone' ), item.get ( 'counters' ).get ( 'friends' ),
                    item.get ( 'music' ), item.get ( 'about' ), item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                connection.commit ()
connection.close ()
with open ( 'vkq.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vkq.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`json_has_wall_idjson_has_wall`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'text' ), item.get ( 'likes' ).get ( 'count' ), item.get ( 'comments' ).get ( 'count' ),
                    item.get ( 'reposts' ).get ( 'count' ), item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print ( "Error" )
connection.close ()
with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`json_has_wall_idjson_has_wall`) VALUES (%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ), item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print ( "Error" )
connection.close ()


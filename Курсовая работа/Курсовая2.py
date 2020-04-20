import requests
import json
import pymysql.cursors

token='ea3f5522a5f1ebc388e13887dad0a5a84dbcd8cf0cac1cfbfb137850b689094517c1e071557a13586a8c7'
version=5.103
extended=1

class People(object):
    group=[]
    user=[]
    wall=[]
    friend=[]
    user_friend=[]
    offset=0

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
                                        'offset': self.offset

                                    } )
            data=response.json ()['response']
            self.offset+=1
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
    def friends(self):
        response3=requests.get ( 'с',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'user_id': self.id,
                                     'extended': extended,
                                 } )
        data=response3.json ()['response']['items']
        self.friend.extend ( data )
        return self.friend
    def users_friend(self):
        while self.offset<1000:
            response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_id': self.friend,
                                        'offset': self.offset
                                    } )
            data=response.json ()['response']
            self.offset+=1
            self.user_friend.extend ( data )
            return self.user_friend

if __name__ == "__main__":
    vlad_samoylenko=People('id155384397','155384397')
vlad_samoylenko.users()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_samoylenko.users(), file )
vlad_samoylenko.walls()
with open ( 'vkq.json', "w", encoding='utf-8' ) as file:
    json.dump ( vlad_samoylenko.walls(), file )
vlad_samoylenko.groups ()
with open ( 'vkw.json', "w", encoding='utf-8' ) as file:
    json.dump (vlad_samoylenko.groups (), file )
vlad_samoylenko.users_friend()
with open ( 'vke.json', "r", encoding='utf-8' ) as file:
    json.dump (vlad_samoylenko.users_friend(), file )
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



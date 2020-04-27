import json

import pymysql.cursors
import requests

token='cb5a76303377bb8850962443835d335fedae3537b57449adb974329490bbd989738d5816a80aa9a223d86'
version=5.103
extended=1

class People(object):
    fields='bdate, mobile_phone,home_phone,friends,music,about'
    def __init__(self, id, ids,offset):
        self.id= id
        self.ids=ids
        self.offset=offset

    def users(self):
       user=[]
       response=requests.get ( 'https://api.vk.com/method/users.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_ids': self.id,
                                        'fields': self.fields

                                    } )
       data=response.json ()['response']
       user.extend ( data )
       return user

    def sql(self):
        with open ( 'vk.json' ) as json_file:
            post=json.load ( json_file )
            print ( post )
        connection=pymysql.connect ( host='127.0.0.1',
                                     user='root',
                                     password='Basketboll2002',
                                     db='mydb' )

        with open ( 'vk.json' ) as json_file:
            post=json.load ( json_file )
            for item in post:
                try:
                    with connection.cursor () as cursor:
                        # Create a new record
                        sql="INSERT INTO `json` (`№`,`id` , `first_name`,`last_name`,`bdate`,`mobile_phone`,`home_phone`,`music`,`about`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s )"
                        cursor.execute ( sql, (
                            item.get ( '№', [self.offset] ), item.get ( 'id' ), item.get ( 'first_name' ),
                            item.get ( 'last_name' ), item.get ( 'bdate' ),
                            item.get ( 'mobile_phone' ), item.get ( 'home_phone' ),
                            item.get ( 'music' ), item.get ( 'about' )) )
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                    connection.commit ()
                except Exception:
                  print ( "Error" )
        connection.close ()

if __name__ == "__main__":
    People21=People ( 'id72511618', '72511618', '21' )
    People21.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People21.users (), file )
    People21.sql ()

    People22=People ( 'id192260451', '192260451', '22' )
    People22.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People22.users (), file )
    People22.sql ()

    People23=People ( 'id132033643', '132033643', '23' )
    People23.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People23.users (), file )
    People23.sql ()
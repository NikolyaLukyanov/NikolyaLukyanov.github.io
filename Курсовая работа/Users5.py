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
    People17=People ( 'id487119415', '487119415', '17' )
    People17.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People17.users (), file )
    People17.sql ()

    People18=People ( 'id18864498', '18864498', '18' )
    People18.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People18.users (), file )
    People18.sql ()

    People19=People ( 'id444545086', '18864498', '19' )
    People19.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People19.users (), file )
    People19.sql ()

    People20=People ( 'id547652798', '547652798', '20' )
    People20.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People20.users (), file )
    People20.sql ()



import json

import pymysql.cursors
import requests

token='be3c5cb82a36174e2462c32d454cc4fd5e38eb5bdb9e268a87e41bdd6803de3c9ae701a1e0aa6b7b05cb8'
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
    People1=People('id155384397','155384397','1')
    People1.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People1.users(), file )
    People1.sql ()

    People2=People('id122123897','122123897','2')
    People2.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People2.users(), file )
    People2.sql ()

    People3=People('id226165635','226165635','3')
    People3.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People3.users(), file )
    People3.sql ()

    People4=People('id204756182','204756182','4')
    People4.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People4.users(), file )
    People4.sql ()







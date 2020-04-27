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
    People5=People('id169916098','169916098','5')
    People5.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People5.users(), file )
    People5.sql ()

    People6=People('id287961694','287961694','6')
    People6.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People6.users(), file )
    People6.sql ()

    People7=People('id226159703','226159703','7')
    People7.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People7.users(), file )
    People7.sql ()

    People8=People('id207484334','207484334','8')
    People8.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People8.users(), file )
    People8.sql ()


    People13=People('id164519173','164519173','13')
    People13.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People13.users(), file )
    People13.sql ()

    People14=People('id253456309','253456309','14')
    People14.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People14.users(), file )
    People14.sql ()

    People15=People('id203884671','203884671','15')
    People15.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People15.users(), file )
    People15.sql ()

    People16=People('id205840517','205840517','16')
    People16.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
      json.dump (People16.users(), file )
    People16.sql ()

    People17=People('id487119415','487119415','17')
    People17.users()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
     json.dump (People17.users(), file )
    People17.sql ()



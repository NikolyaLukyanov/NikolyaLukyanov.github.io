import pymysql.cursors
import requests

token='e04fb00c2d8a47d28dbbb4561467a308cbc362af802cc185c53ddb943891f6a2f4829eb1a23f14ecf385c'
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

       def users2():
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
       user=users2()

       connection=pymysql.connect ( host='127.0.0.1',
                                         user='root',
                                         password='Basketboll2002',
                                         db='mydb' )

       for item in user:
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
import os
os.startfile(r'C:/Users/nikol/OneDrive/Рабочий стол/Курсовая/Likes.py')

import pymysql.cursors
import requests

token='f906ab30c793e12b04822edd83a439d5f68cd6a9f151bc86693b5e99ad13216d4ac92ad37623fca3db7e9'
version=5.103
extended=1
class People(object):
    fields='bdate, mobile_phone,home_phone,friends,music,about'
    def __init__(self, id, ids,offset):
        self.id= id
        self.ids=ids
        self.offset=offset

    def users(self):
       global id_wall
       user=[]
       group=[]
       wall=[]
       friend=[]
       like=[]
       def users():
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
       user=users()

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
       def grups():

           response2=requests.get ( 'https://api.vk.com/method/groups.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_id': self.ids,
                                        'extended': extended,
                                    } )
           data=response2.json ()['response']['items']
           group.extend ( data )
           return group
       group=grups()


       connection=pymysql.connect ( host='127.0.0.1',
                                        user='root',
                                        password='Basketboll2002',
                                        db='mydb',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor )

       for item in group:
                   try:
                       with connection.cursor () as cursor:
                           # Create a new record
                           sql="INSERT INTO `grups` (`№`,`id_grup`,`name_grup`,`screen_name_grup`) VALUES (%s,%s,%s,%s )"
                           cursor.execute ( sql, (
                               item.get ( '№', [self.offset] ), item.get ( 'id' ), item.get ( 'name' ),
                               item.get ( 'screen_name' )) )
                           # connection is not autocommit by default. So you must commit to save
                           # your changes.
                       connection.commit ()
                   except Exception:
                       print ( "Error" )
       connection.close ()
       def walls():
           response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'domain': self.id,
                                    } )
           data=response1.json ()['response']['items']
           wall.extend ( data )
           return wall
       wall=walls()

       connection=pymysql.connect ( host='127.0.0.1',
                                     user='root',
                                     password='Basketboll2002',
                                     db='mydb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor )


       for item in wall:
                try:

                    with connection.cursor () as cursor:
                        # Create a new record
                        sql="INSERT INTO `wall` (`№`,`id`,`text`,`likes`,`comments`,`reposts`) VALUES (%s,%s,%s,%s,%s,%s )"
                        cursor.execute ( sql, (
                            item.get ( '№', [self.offset] ), item.get ( 'id' ), item.get ( 'text' ),
                            item.get ( 'likes' ).get ( 'count' ),
                            item.get ( 'comments' ).get ( 'count' ),
                            item.get ( 'reposts' ).get ( 'count' )) )
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                    connection.commit ()
                except Exception:
                    print ( "Error" )
       connection.close ()

       def friends():
           response1=requests.get ( 'https://api.vk.com/method/friends.get',
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'user_id': self.ids,
                                        'fields': self.fields
                                    } )
           data=response1.json ()['response']['items']
           friend.extend ( data )
           return friend
       friend=friends()

       connection=pymysql.connect ( host='127.0.0.1',
                                        user='root',
                                        password='Basketboll2002',
                                        db='mydb',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor )


       for item in friend:
                   try:

                       with connection.cursor () as cursor:
                           # Create a new record
                           sql="INSERT INTO `friends` (`№`,`id`,`first_name`,`last_name`) VALUES (%s,%s,%s,%s )"
                           cursor.execute ( sql, (
                               item.get ( '№', [self.offset] ), item.get ( 'id' ), item.get ( 'first_name' ),
                               item.get ( 'last_name' )) )
                           # connection is not autocommit by default. So you must commit to save
                           # your changes.
                       connection.commit ()
                   except Exception:
                       print ( "Error" )
       connection.close ()

       for item in wall:
        id_wall=item.get ( 'id' )

       def likes():
           try:
               type='post'
               response1=requests.get ( 'https://api.vk.com/method/likes.getList',
                                        params={
                                            'access_token': token,
                                            'v': version,
                                            'owner_id': self.ids,
                                            'type': type,
                                            'item_id': id_wall
                                        } )
               data=response1.json ()['response']['items']
               like.extend ( data )
               return like
           except Exception:
               print('error')

       like=likes()

       connection=pymysql.connect ( host='127.0.0.1',
                                     user='root',
                                     password='Basketboll2002',
                                     db='mydb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor )

       try:
           for item in like:
               try:
                   with connection.cursor () as cursor:
                       # Create a new record
                       sql="INSERT INTO `likes` (`№`,`id_wall`,`id_friends`) VALUES (%s,%s ,%s)"
                       cursor.execute ( sql, (
                           item.get ( '№', [self.offset] ), item.get ( 'id_wall', [id_wall] ), item) )
                       # connection is not autocommit by default. So you must commit to save
                       # your changes.
                   connection.commit ()
               except Exception as e:
                   print ( e )
           connection.close ()
       except Exception:
           print('ww')



if __name__ == "__main__":
    People19=People ( 'id444545086', '18864498', '19' )
    People19.users ()

    People20=People ( 'id547652798', '547652798', '20' )
    People20.users ()

#    People21=People ( 'id72511618', '72511618', '21' )
#    People21.users ()

    People22=People ( 'id192260451', '192260451', '22' )
    People22.users ()

    People23=People ( 'id132033643', '132033643', '23' )
    People23.users ()



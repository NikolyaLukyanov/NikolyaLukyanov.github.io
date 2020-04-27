import requests
import json
import pymysql.cursors

token='cb5a76303377bb8850962443835d335fedae3537b57449adb974329490bbd989738d5816a80aa9a223d86'
version=5.103
extended=1

class People(object):

    def __init__(self, id, ids,offset,id_wall):
        self.id= id
        self.ids=ids
        self.offset=offset
        self.id_wall=id_wall

    def users(self):
        id_friend=[]
        type= 'post'
        response1=requests.get ( 'https://api.vk.com/method/likes.getList',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'owner_id': self.ids,
                                     'type':type,
                                     'item_id':self.id_wall
                                 } )
        data=response1.json ()['response']['items']
        id_friend.extend ( data )
        return id_friend

    def sql(self):
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
            for post in post:
                try:
                    with connection.cursor () as cursor:
                        # Create a new record
                        sql="INSERT INTO `likes` (`№`,`id_wall`,`id_friend`) VALUES (%s,%s,%s)"
                        cursor.execute ( sql, (
                            post.get ( '№', [self.offset] ),post.get ( 'id',[self.id_wall] ), post.get ('id_friend',[post])) )
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                    connection.commit ()
                except Exception:
                    print ( "Error" )
        connection.close ()
if __name__ == "__main__":
    People1=People ( 'id155384397', '155384397', '1','714' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '705' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '686' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '685' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '684' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '676' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '671' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '669' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '668' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '666' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '664' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '661' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '660' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '659' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '654' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '653' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '650' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '648' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '643' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People1=People ( 'id155384397', '155384397', '1', '636' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()
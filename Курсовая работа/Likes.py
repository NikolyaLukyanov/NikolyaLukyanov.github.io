import requests
import json
import pymysql.cursors

token='78814dcb6c1a9d89d9f6eda7ab9cd440379e10319320d433a35ea0258703713e2c6d2346974fdb3a6b406'
version=5.103
extended=1

class People(object):

    def __init__(self, id, ids, offset, id_wall):
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
            for item in post:
                try:
                    with connection.cursor () as cursor:
                        # Create a new record
                        sql="INSERT INTO `likes` (`№`,`id_wall`,`id_friends`) VALUES (%s,%s ,%s)"
                        cursor.execute ( sql, (
                            item.get ( '№', [self.offset] ), item.get ( 'id_wall',[self.id_wall] ), item.get ( 'id_friends',[post] )) )
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

    People2=People ( 'id155384397', '155384397', '1', '705' )
    People2.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People2.users (), file )
    People2.sql ()

    People3=People ( 'id155384397', '155384397', '1', '686' )
    People3.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People3.users (), file )
    People3.sql ()

    People4=People ( 'id155384397', '155384397', '1', '685' )
    People4.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People4.users (), file )
    People4.sql ()

    People5=People ( 'id155384397', '155384397', '1', '684' )
    People5.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People5.users (), file )
    People5.sql ()

    People6=People ( 'id155384397', '155384397', '1', '676' )
    People6.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People6.users (), file )
    People6.sql ()

    People7=People ( 'id155384397', '155384397', '1', '671' )
    People7.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People7.users (), file )
    People7.sql ()

    People8=People ( 'id155384397', '155384397', '1', '669' )
    People8.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People8.users (), file )
    People8.sql ()

    People9=People ( 'id155384397', '155384397', '1', '668' )
    People9.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People9.users (), file )
    People9.sql ()

    People10=People ( 'id155384397', '155384397', '1', '666' )
    People10.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People10.users (), file )
    People10.sql ()

    People11=People ( 'id155384397', '155384397', '1', '664' )
    People11.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People11.users (), file )
    People11.sql ()

    People12=People ( 'id155384397', '155384397', '1', '661' )
    People12.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People12.users (), file )
    People12.sql ()

    People13=People ( 'id155384397', '155384397', '1', '660' )
    People13.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People13.users (), file )
    People13.sql ()

    People14=People ( 'id155384397', '155384397', '1', '659')
    People14.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People14.users (), file )
    People14.sql ()

    People15=People ( 'id155384397', '155384397', '1', '654')
    People15.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People15.users (), file )
    People15.sql ()

    People16=People ( 'id155384397', '155384397', '1', '653' )
    People16.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People16.users (), file )
    People16.sql ()

    People17=People ( 'id155384397', '155384397', '1', '650' )
    People17.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People17.users (), file )
    People17.sql ()

    People18=People ( 'id155384397', '155384397', '1', '648' )
    People18.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People18.users (), file )
    People18.sql ()

    People19=People ( 'id155384397', '155384397', '1', '643' )
    People19.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People19.users (), file )
    People19.sql ()

    People20=People ( 'id155384397', '155384397', '1', '636' )
    People20.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People20.users (), file )
    People20.sql ()
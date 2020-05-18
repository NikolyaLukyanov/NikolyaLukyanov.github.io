import pymysql.cursors
import requests
import time

token='fbe039e0f062f04ed948134fe7e041f6356b8bd50de9e627976231ac3c956425de785b6186dc66083b9bf'
version=5.103
extended=1

class People(object):
    fields='bdate, mobile_phone,home_phone,friends,music,about'

    def __init__(self, id, ids, offset):
        self.id=id
        self.ids=ids
        self.offset=offset
    def users(self):
        user=[]
        def users2():
            time.sleep(0.5)
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

        user=users2 ()

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

class Grups(People):
    def group(self):
        group=[]
        def grups2():
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

        group=grups2()

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

class Friends(Grups):
    def friends(self):
        friend=[]
        def friends2():
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

        friend=friends2 ()

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

class Wall(Friends):
    def wall(self):
        wall=[]
        def walls2():
            response1=requests.get ( 'https://api.vk.com/method/wall.get',
                                     params={
                                         'access_token': token,
                                         'v': version,
                                         'domain': self.id,
                                     } )
            data=response1.json ()['response']['items']
            wall.extend ( data )
            return wall

        wall=walls2()

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
        for item in wall:
              likes(item)



class likes():
    def __init__(self, item):
        self.ids=item.get('owner_id')
        self.id_wall=item.get('id')
    def likes(self):
        like=[]
        def likes2():
            try:
                type='post'
                response1=requests.get ( 'https://api.vk.com/method/likes.getList',
                                         params={
                                             'access_token': token,
                                             'v': version,
                                             'owner_id': self.ids,
                                             'type': type,
                                             'item_id': self.id_wall
                                         } )
                data=response1.json ()['response']['items']
                like.extend ( data )
                return like
            except Exception as e:
                print ( e )

        like=likes2 ()
        print ( like )
        try:
            like=str ( like )
            like=like.split ( "," )
            like=" ".join ( like )
        except Exception  as e:
            print ( e )
        dict={}
        id_friends=[]
        id_friends.append ( {
            "id_friends": like} )
        dict["id_friends"]=id_friends

        connection=pymysql.connect ( host='127.0.0.1',
                                     user='root',
                                     password='Basketboll2002',
                                     db='mydb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor )

        try:
            for item in id_friends:
                try:
                    with connection.cursor () as cursor:
                        # Create a new record
                        sql="INSERT INTO `likes` (`id_wall`,`id_friends`) VALUES (%s ,%s)"
                        cursor.execute ( sql, (
                            item.get ( 'id_wall', [self.id_wall] ),
                            item.get ( 'id_friends', [like] )) )
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                    connection.commit ()
                except Exception as e:
                    print ( e )
            connection.close ()
        except Exception:
            print ( 'ww' )

if __name__ == "__main__":
    People1=Wall ( 'id155384397', '155384397', '1' )

    People1.wall ()



    People2=Wall('id122123897','122123897','2')
    People2.users()
    People2.wall()
    People2.friends()
    People2.group()


    People3=Wall('id226165635','226165635','3')
    People3.users()
    People3.wall()
    People3.friends()
    People3.group()


    People4=Wall('id204756182','204756182','4')
    People4.users()
    People4.wall()
    People4.friends()
    People4.group()


    People5=Wall ( 'id169916098', '169916098', '5' )
    People5.users ()
    People5.wall()
    People5.friends()
    People5.group()



    People6=Wall ( 'id287961694', '287961694', '6' )
    People6.users ()
    People6.wall()
    People6.friends()
    People6.group()



    People7=Wall ( 'id226159703', '226159703', '7' )
    People7.users ()
    People7.wall()
    People7.friends()
    People7.group()


    People8=Wall ( 'id207484334', '207484334', '8' )
    People8.users ()
    People8.wall()
    People8.friends()
    People8.group()


    People9=Wall( 'id160504052', '160504052', '9' )
    People9.users ()
    People9.wall()
    People9.friends()
    People9.group()


    People10=Wall ( 'id156930209', '156930209', '10' )
    People10.users ()
    People10.wall()
    People10.friends()
    People10.group()


    People11=Wall ( 'id62022070', '62022070', '11' )
    People11.users ()
    People11.wall()
    People11.friends()
    People11.group()


    People12=Wall ( 'id364803419', '364803419', '12' )
    People12.users ()
    People12.wall()
    People12.friends()
    People12.group()


    People13=Wall ( 'id164519173', '164519173', '13' )
    People13.users ()
    People13.wall()
    People13.friends()
    People13.group()


    People14=Wall ( 'id253456309', '253456309', '14' )
    People14.users ()
    People14.wall()
    People14.friends()
    People14.group()


    People15=Wall( 'id203884671', '203884671', '15' )
    People15.users ()
    People15.wall()
    People15.friends()
    People15.group()


    People16=Wall( 'id205840517', '205840517', '16' )
    People16.users ()
    People16.wall()
    People16.friends()
    People16.group()

    People17=Wall ( 'id487119415', '487119415', '17' )
    People17.users ()
    People17.wall()
    People17.friends()
    People17.group()


    People18=Wall( 'id18864498', '18864498', '18' )
    People18.users ()
    People18.wall()
    People18.friends()
    People18.group()

    People19=Wall ( 'id444545086', '18864498', '19' )
    People19.users ()
    People19.wall()
    People19.friends()
    People19.group()

    People20=Wall ( 'id547652798', '547652798', '20' )
    People20.users ()
    People20.wall()
    People20.friends()
    People20.group()

    People21=Wall ( 'id72511618', '72511618', '21' )
    People21.users ()

    People22=Wall( 'id192260451', '192260451', '22' )
    People22.users ()
    People22.wall()
    People22.friends()
    People22.group()

    People23=Wall ( 'id132033643', '132033643', '23' )
    People23.users ()
    People23.wall()
    People23.friends()
    People23.group()

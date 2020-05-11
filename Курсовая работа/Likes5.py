import requests

import pymysql.cursors

token='e04fb00c2d8a47d28dbbb4561467a308cbc362af802cc185c53ddb943891f6a2f4829eb1a23f14ecf385c'
version=5.103
extended=1


class People ( object ):

    def __init__(self, id, ids, offset, id_wall):
        self.id=id
        self.ids=ids
        self.offset=offset
        self.id_wall=id_wall

    def users(self):
        like=[]

        def likes():
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

        like=likes ()
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
                        sql="INSERT INTO `likes` (`№`,`id_wall`,`id_friends`) VALUES (%s,%s ,%s)"
                        cursor.execute ( sql, (
                            item.get ( '№', [self.offset] ), item.get ( 'id_wall', [self.id_wall] ),
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


    People181=People ( 'id487119415', '487119415', '17', '14' )
    People181.users ()

    People182=People ( 'id487119415', '487119415', '17', '13' )
    People182.users ()

    People183=People ( 'id487119415', '487119415', '17', '10' )
    People183.users ()

    People184=People ( 'id487119415', '487119415', '17', '9' )
    People184.users ()

    People185=People ( 'id487119415', '487119415', '17', '7' )
    People185.users ()

    People186=People ( 'id487119415', '487119415', '17', '6' )
    People186.users ()

    People187=People ( 'id487119415', '487119415', '17', '2' )
    People187.users ()

    People189=People ( 'id487119415', '487119415', '17', '1' )
    People189.users ()

    People190=People ( 'id18864498', '18864498', '18', '3028' )
    People190.users ()

    People191=People ( 'id18864498', '18864498', '18', '3038' )
    People191.users ()

    People192=People ( 'id18864498', '18864498', '18', '3038' )
    People192.users ()

    People193=People ( 'id547652798', '547652798', '20', '40' )
    People193.users ()

    People194=People ( 'id547652798', '547652798', '20', '34' )
    People194.users ()

    People195=People ( 'id547652798', '547652798', '20', '32' )
    People195.users ()

    People196=People ( 'id547652798', '547652798', '20', '30' )
    People196.users ()

    People197=People ( 'id547652798', '547652798', '20', '29' )
    People197.users ()

    People198=People ( 'id547652798', '547652798', '20', '21' )
    People198.users ()

    People199=People ( 'id547652798', '547652798', '20', '4' )
    People199.users ()

    People200=People ( 'id547652798', '547652798', '20', '1' )
    People200.users ()

    People201=People ( 'id192260451', '192260451', '22', '643' )
    People201.users ()

    People202=People ( 'id192260451', '192260451', '22', '642' )
    People202.users ()

    People203=People ( 'id192260451', '192260451', '22', '635' )
    People203.users ()

    People204=People ( 'id132033643', '132033643', '23', '1309' )
    People204.users ()

    People205=People ( 'id132033643', '132033643', '23', '1308' )
    People205.users ()

    People206=People ( 'id132033643', '132033643', '23', '1306' )
    People206.users ()

    People207=People ( 'id132033643', '132033643', '23', '1305' )
    People207.users ()

    People208=People ( 'id132033643', '132033643', '23', '1304' )
    People208.users ()

    People209=People ( 'id132033643', '132033643', '23', '1303' )
    People209.users ()

    People210=People ( 'id132033643', '132033643', '23', '1302' )
    People210.users ()

    People211=People ( 'id132033643', '132033643', '23', '1301' )
    People211.users ()

    People212=People ( 'id132033643', '132033643', '23', '1300' )
    People212.users ()

    People213=People ( 'id132033643', '132033643', '23', '1299' )
    People213.users ()

    People214=People ( 'id132033643', '132033643', '23', '1298' )
    People214.users ()

    People215=People ( 'id132033643', '132033643', '23', '1297' )
    People215.users ()

    People216=People ( 'id132033643', '132033643', '23', '1296' )
    People216.users ()

    People217=People ( 'id132033643', '132033643', '23', '1295' )
    People217.users ()

    People218=People ( 'id132033643', '132033643', '23', '1294' )
    People218.users ()

    People219=People ( 'id132033643', '132033643', '23', '1293' )
    People219.users ()

    People220=People ( 'id132033643', '132033643', '23', '1290' )
    People204.users ()

    People221=People ( 'id132033643', '132033643', '23', '1289' )
    People221.users ()

    People222=People ( 'id132033643', '132033643', '23', '1388' )
    People222.users ()







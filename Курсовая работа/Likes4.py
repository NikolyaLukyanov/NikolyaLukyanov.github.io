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


    People136=People ( 'id164519173', '164519173', '13', '2759' )
    People136.users ()

    People137=People ( 'id164519173', '164519173', '13', '2756' )
    People137.users ()

    People138=People ( 'id164519173', '164519173', '13', '2755' )
    People138.users ()

    People139=People ( 'id253456309', '253456309', '14', '427' )
    People139.users ()

    People140=People ( 'id253456309', '253456309', '14', '401' )
    People140.users ()

    People141=People ( 'id253456309', '253456309', '14', '393' )
    People141.users ()

    People142=People ( 'id253456309', '253456309', '14', '390' )
    People142.users ()

    People143=People ( 'id253456309', '253456309', '14', '389' )
    People143.users ()

    People144=People ( 'id253456309', '253456309', '14', '373' )
    People144.users ()

    People145=People ( 'id253456309', '253456309', '14', '371' )
    People145.users ()

    People146=People ( 'id253456309', '253456309', '14', '370' )
    People146.users ()

    People147=People ( 'id253456309', '253456309', '14', '369' )
    People147.users ()

    People148=People ( 'id253456309', '253456309', '14', '367' )
    People148.users ()

    People149=People ( 'id253456309', '253456309', '14', '366' )
    People149.users ()

    People150=People ( 'id253456309', '253456309', '14', '365' )
    People150.users ()

    People151=People ( 'id253456309', '253456309', '14', '361' )
    People151.users ()

    People152=People ( 'id253456309', '253456309', '14', '360' )
    People152.users ()

    People153=People ( 'id253456309', '253456309', '14', '347' )
    People153.users ()

    People154=People ( 'id253456309', '253456309', '14', '346' )
    People154.users ()

    People155=People ( 'id253456309', '253456309', '14', '345' )
    People155.users ()

    People156=People ( 'id253456309', '253456309', '14', '344' )
    People156.users ()

    People157=People ( 'id253456309', '253456309', '14', '338' )
    People157.users ()

    People158=People ( 'id253456309', '253456309', '14', '334' )
    People158.users ()

    People159=People ( 'id203884671', '203884671', '15', '353' )
    People159.users ()

    People160=People ( 'id203884671', '203884671', '15', '352' )
    People160.users ()

    People161=People ( 'id203884671', '203884671', '15', '336' )
    People161.users ()

    People162=People ( 'id203884671', '203884671', '15', '327' )
    People162.users ()

    People163=People ( 'id205840517', '205840517', '16', '484' )
    People163.users ()

    People164=People ( 'id205840517', '205840517', '16', '479' )
    People164.users ()

    People165=People ( 'id205840517', '205840517', '16', '474' )
    People165.users ()

    People166=People ( 'id205840517', '205840517', '16', '446' )
    People166.users ()

    People167=People ( 'id205840517', '205840517', '16', '431' )
    People167.users ()

    People168=People ( 'id205840517', '205840517', '16', '404' )
    People168.users ()

    People169=People ( 'id205840517', '205840517', '16', '403' )
    People169.users ()

    People170=People ( 'id205840517', '205840517', '16', '379' )
    People170.users ()

    People171=People ( 'id205840517', '205840517', '16', '372' )
    People171.users ()

    People172=People ( 'id205840517', '205840517', '16', '369' )
    People172.users ()

    People173=People ( 'id205840517', '205840517', '16', '368' )
    People173.users ()

    People174=People ( 'id205840517', '205840517', '16', '336' )
    People174.users ()

    People175=People ( 'id205840517', '205840517', '16', '225' )
    People175.users ()

    People176=People ( 'id205840517', '205840517', '16', '222' )
    People176.users ()

    People177=People ( 'id205840517', '205840517', '16', '139' )
    People177.users ()

    People178=People ( 'id487119415', '487119415', '17', '17' )
    People178.users ()

    People179=People ( 'id487119415', '487119415', '17', '16' )
    People179.users ()

    People180=People ( 'id487119415', '487119415', '17', '15' )
    People180.users ()

import os
os.startfile(r'C:/Users/nikol/OneDrive/Рабочий стол/Курсовая/Likes5.py')
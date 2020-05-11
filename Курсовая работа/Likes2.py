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

    People45=People ( 'id226159703', '226159703', '7', '323' )
    People45.users ()

    People46=People ( 'id226159703', '226159703', '7', '304' )
    People46.users ()

    People47=People ( 'id226159703', '226159703', '7', '303' )
    People47.users ()

    People48=People ( 'id226159703', '226159703', '7', '301' )
    People48.users ()

    People49=People ( 'id226159703', '226159703', '7', '213' )
    People49.users ()

    People50=People ( 'id226159703', '226159703', '7', '207' )
    People50.users ()

    People51=People ( 'id207484334', '207484334', '8', '1227' )
    People51.users ()

    People52=People ( 'id207484334', '207484334', '8', '1228' )
    People52.users ()

    People53=People ( 'id207484334', '207484334', '8', '1219' )
    People53.users ()

    People54=People ( 'id207484334', '207484334', '8', '1211' )
    People54.users ()

    People55=People ( 'id207484334', '207484334', '8', '1200' )
    People55.users ()

    People56=People ( 'id207484334', '207484334', '8', '1199' )
    People56.users ()

    People57=People ( 'id160504052', '160504052', '9', '361' )
    People57.users ()

    People58=People ( 'id160504052', '160504052', '9', '360' )
    People58.users ()

    People59=People ( 'id160504052', '160504052', '9', '359' )
    People59.users ()

    People60=People ( 'id160504052', '160504052', '9', '349' )
    People60.users ()

    People61=People ( 'id160504052', '160504052', '9', '348' )
    People61.users ()

    People62=People ( 'id160504052', '160504052', '9', '346' )
    People62.users ()

    People63=People ( 'id160504052', '160504052', '9', '343' )
    People63.users ()

    People64=People ( 'id160504052', '160504052', '9', '342' )
    People64.users ()

    People65=People ( 'id160504052', '160504052', '9', '341' )
    People65.users ()

    People66=People ( 'id160504052', '160504052', '9', '340' )
    People66.users ()

    People67=People ( 'id160504052', '160504052', '9', '339' )
    People67.users ()

    People68=People ( 'id160504052', '160504052', '9', '338' )
    People68.users ()

    People69=People ( 'id160504052', '160504052', '9', '336' )
    People69.users ()

    People70=People ( 'id160504052', '160504052', '9', '335' )
    People70.users ()

    People71=People ( 'id160504052', '160504052', '9', '334' )
    People71.users ()

    People72=People ( 'id160504052', '160504052', '9', '333' )
    People72.users ()

    People73=People ( 'id160504052', '160504052', '9', '332' )
    People73.users ()

    People74=People ( 'id160504052', '160504052', '9', '331' )
    People74.users ()

    People75=People ( 'id156930209', '156930209', '10', '948' )
    People75.users ()

    People76=People ( 'id156930209', '156930209', '10', '942' )
    People76.users ()

    People77=People ( 'id156930209', '156930209', '10', '925' )
    People77.users ()

    People78=People ( 'id156930209', '156930209', '10', '918' )
    People78.users ()

    People79=People ( 'id156930209', '156930209', '10', '902' )
    People79.users ()

    People80=People ( 'id156930209', '156930209', '10', '895' )
    People80.users ()

    People81=People ( 'id156930209', '156930209', '10', '890' )
    People81.users ()

    People82=People ( 'id156930209', '156930209', '10', '889' )
    People82.users ()

    People83=People ( 'id156930209', '156930209', '10', '830' )
    People83.users ()

    People84=People ( 'id156930209', '156930209', '10', '792' )
    People84.users ()

    People85=People ( 'id156930209', '156930209', '10', '762' )
    People85.users ()

    People86=People ( 'id156930209', '156930209', '10', '741' )
    People86.users ()

    People87=People ( 'id156930209', '156930209', '10', '740' )
    People87.users ()

    People88=People ( 'id156930209', '156930209', '10', '571' )
    People88.users ()

    People89=People ( 'id156930209', '156930209', '10', '539' )
    People89.users ()

    People90=People ( 'id156930209', '156930209', '10', '496' )
    People90.users ()

import os
os.startfile(r'C:/Users/nikol/OneDrive/Рабочий стол/Курсовая/Likes3.py')
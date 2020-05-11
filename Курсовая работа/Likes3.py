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

    People91=People ( 'id156930209', '156930209', '10', '475' )
    People91.users ()

    People92=People ( 'id156930209', '156930209', '10', '460' )
    People92.users ()

    People93=People ( 'id156930209', '156930209', '10', '459' )
    People93.users ()

    People94=People ( 'id156930209', '156930209', '10', '458' )
    People94.users ()

    People95=People ( 'id62022070', '62022070', '11', '4254' )
    People95.users ()

    People96=People ( 'id62022070', '62022070', '11', '4253' )
    People96.users ()

    People97=People ( 'id62022070', '62022070', '11', '4248' )
    People97.users ()

    People98=People ( 'id62022070', '62022070', '11', '4247' )
    People98.users ()

    People99=People ( 'id62022070', '62022070', '11', '4240' )
    People99.users ()

    People100=People ( 'id62022070', '62022070', '11', '4239' )
    People100.users ()

    People101=People ( 'id62022070', '62022070', '11', '4237' )
    People101.users ()

    People102=People ( 'id62022070', '62022070', '11', '4236' )
    People102.users ()

    People103=People ( 'id62022070', '62022070', '11', '4235' )
    People103.users ()

    People104=People ( 'id62022070', '62022070', '11', '4234' )
    People104.users ()

    People105=People ( 'id62022070', '62022070', '11', '4229' )
    People105.users ()

    People106=People ( 'id62022070', '62022070', '11', '4228' )
    People106.users ()

    People107=People ( 'id62022070', '62022070', '11', '4227' )
    People107.users ()

    People108=People ( 'id62022070', '62022070', '11', '4188' )
    People108.users ()

    People109=People ( 'id62022070', '62022070', '11', '2646' )
    People109.users ()

    People110=People ( 'id62022070', '62022070', '11', '2630' )
    People110.users ()

    People111=People ( 'id62022070', '62022070', '11', '2629' )
    People111.users ()

    People112=People ( 'id62022070', '62022070', '11', '2628' )
    People112.users ()

    People113=People ( 'id62022070', '62022070', '11', '2627' )
    People113.users ()

    People114=People ( 'id364803419', '364803419', '12', '216' )
    People114.users ()

    People115=People ( 'id364803419', '364803419', '12', '215' )
    People115.users ()

    People116=People ( 'id364803419', '364803419', '12', '213' )
    People116.users ()

    People117=People ( 'id364803419', '364803419', '12', '207' )
    People117.users ()

    People118=People ( 'id364803419', '364803419', '12', '198' )
    People118.users ()

    People119=People ( 'id364803419', '364803419', '12', '196' )
    People119.users ()

    People120=People ( 'id164519173', '164519173', '13', '2778' )
    People120.users ()

    People121=People ( 'id164519173', '164519173', '13', '2777' )
    People121.users ()

    People122=People ( 'id164519173', '164519173', '13', '2776' )
    People122.users ()

    People123=People ( 'id164519173', '164519173', '13', '2774' )
    People123.users ()

    People124=People ( 'id164519173', '164519173', '13', '2772' )
    People124.users ()

    People125=People ( 'id164519173', '164519173', '13', '2771' )
    People125.users ()

    People126=People ( 'id164519173', '164519173', '13', '2770' )
    People126.users ()

    People127=People ( 'id164519173', '164519173', '13', '2769' )
    People127.users ()

    People128=People ( 'id164519173', '164519173', '13', '2768' )
    People128.users ()

    People129=People ( 'id164519173', '164519173', '13', '2767' )
    People129.users ()

    People130=People ( 'id164519173', '164519173', '13', '2766' )
    People130.users ()

    People131=People ( 'id164519173', '164519173', '13', '2765' )
    People131.users ()

    People132=People ( 'id164519173', '164519173', '13', '2764' )
    People132.users ()

    People133=People ( 'id164519173', '164519173', '13', '2762' )
    People133.users ()

    People134=People ( 'id164519173', '164519173', '13', '2761' )
    People134.users ()

    People135=People ( 'id164519173', '164519173', '13', '2760' )
    People135.users ()

import os
os.startfile(r'C:/Users/nikol/OneDrive/Рабочий стол/Курсовая/Likes4.py')
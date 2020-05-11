import requests

import pymysql.cursors

token='e04fb00c2d8a47d28dbbb4561467a308cbc362af802cc185c53ddb943891f6a2f4829eb1a23f14ecf385c'
version=5.103
extended=1

class People(object):

    def __init__(self, id, ids, offset, id_wall):
        self.id= id
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
    People1=People ( 'id155384397', '155384397', '1','714' )
    People1.users ()


    People2=People ( 'id155384397', '155384397', '1', '705' )
    People2.users ()


    People3=People ( 'id155384397', '155384397', '1', '686' )
    People3.users ()


    People4=People ( 'id155384397', '155384397', '1', '685' )
    People4.users ()


    People5=People ( 'id155384397', '155384397', '1', '684' )
    People5.users ()

    People6=People ( 'id155384397', '155384397', '1', '676' )
    People6.users ()


    People7=People ( 'id155384397', '155384397', '1', '671' )
    People7.users ()



    People8=People ( 'id155384397', '155384397', '1', '669' )
    People8.users ()

    People9=People ( 'id155384397', '155384397', '1', '668' )
    People9.users ()


    People10=People ( 'id155384397', '155384397', '1', '666' )
    People10.users ()


    People11=People ( 'id155384397', '155384397', '1', '664' )
    People11.users ()

    People12=People ( 'id155384397', '155384397', '1', '661' )
    People12.users ()


    People13=People ( 'id155384397', '155384397', '1', '660' )
    People13.users ()


    People14=People ( 'id155384397', '155384397', '1', '659')
    People14.users ()


    People15=People ( 'id155384397', '155384397', '1', '654')
    People15.users ()


    People16=People ( 'id155384397', '155384397', '1', '653' )
    People16.users ()


    People17=People ( 'id155384397', '155384397', '1', '650' )
    People17.users ()


    People18=People ( 'id155384397', '155384397', '1', '648' )
    People18.users ()

    People19=People ( 'id155384397', '155384397', '1', '643' )
    People19.users ()


    People20=People ( 'id155384397', '155384397', '1', '636' )
    People20.users ()

    People21=People ( 'id122123897', '122123897', '2', '859' )
    People21.users ()

    People22=People ( 'id122123897', '122123897', '2', '847' )
    People22.users ()

    People23=People ( 'id122123897', '122123897', '2', '841' )
    People23.users ()

    People24=People ( 'id226165635', '226165635', '3', '540' )
    People24.users ()

    People25=People ( 'id226165635', '226165635', '3', '539' )
    People25.users ()

    People26=People ( 'id226165635', '226165635', '3', '538' )
    People26.users ()

    People27=People ( 'id226165635', '226165635', '3', '537' )
    People27.users ()

    People28=People ( 'id226165635', '226165635', '3', '536' )
    People28.users ()

    People29=People ( 'id226165635', '226165635', '3', '535' )
    People29.users ()

    People30=People ( 'id226165635', '226165635', '3', '522' )
    People30.users ()

    People31=People ( 'id226165635', '226165635', '3', '520' )
    People31.users ()

    People32=People ( 'id226165635', '226165635', '3', '505' )
    People32.users ()

    People33=People ( 'id226165635', '226165635', '3', '493' )
    People33.users ()

    People34=People ( 'id226165635', '226165635', '3', '492' )
    People34.users ()

    People35=People ( 'id226165635', '226165635', '3', '491' )
    People35.users ()

    People36=People ( 'id226165635', '226165635', '3', '490' )
    People36.users ()

    People37=People ( 'id226165635', '226165635', '3', '489' )
    People37.users ()

    People38=People ( 'id226165635', '226165635', '3', '488' )
    People38.users ()

    People39=People ( 'id226165635', '226165635', '3', '487' )
    People39.users ()

    People40=People ( 'id226165635', '226165635', '3', '486' )
    People40.users ()

    People41=People ( 'id226165635', '226165635', '3', '485' )
    People41.users ()

    People42=People ( 'id226165635', '226165635', '3', '484' )
    People42.users ()

    People43=People ( 'id204756182', '204756182', '4', '364' )
    People43.users ()

    People44=People ( 'id204756182', '204756182', '4', '363' )
    People44.users ()

import os
os.startfile(r'C:/Users/nikol/OneDrive/Рабочий стол/Курсовая/Likes2.py')
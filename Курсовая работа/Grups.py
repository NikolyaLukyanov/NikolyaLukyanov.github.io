import requests
import json
import pymysql.cursors

token='9960201fe990557f6ae56e2c7b041dd81abe0b4a6aff07979a0f8baddfc583bae18dd8cc1d6f19d186689'
version=5.103
extended=1

class People(object):
    group=[]
    def __init__(self, id, ids,offset):
        self.id= id
        self.ids=ids
        self.offset=offset

    def users(self):
        response2=requests.get ( 'https://api.vk.com/method/groups.get',
                                 params={
                                     'access_token': token,
                                     'v': version,
                                     'user_id': self.ids,
                                     'extended': extended,
                                 } )
        data=response2.json ()['response']['items']
        self.group.extend ( data )
        return self.group
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
                        sql="INSERT INTO `grup` (`№`,`id_grup`,`name_grup`,`screen_name_grup`,`json_has_wall_idjson_has_wall`) VALUES (%s,%s,%s,%s )"
                        cursor.execute ( sql, (
                            item.get ( '№', [self.offset] ), item.get ( 'id' ), item.get ( 'name' ),
                            item.get ( 'screen_name' )) )
                        # connection is not autocommit by default. So you must commit to save
                        # your changes.
                    connection.commit ()
                except Exception:
                    print ( "Error" )
        connection.close ()


if __name__ == "__main__":
    People1=People ( 'id155384397', '155384397', '1' )
    People1.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People1.users (), file )
    People1.sql ()

    People2=People ( 'id122123897', '122123897', '2' )
    People2.users ()
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People2.users (), file )
    People2.sql ()

    People3=People ( 'id226165635', '226165635', '3' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People3.users (), file )
    People3.sql ()

    People4=People ( 'id204756182', '204756182', '4' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People4.users (), file )
    People4.sql ()

    People5=People ( 'id169916098', '169916098', '5' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People5.users (), file )
    People5.sql ()

    People6=People ( 'id287961694', '287961694', '6' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People6.users (), file )
    People6.sql ()

    People7=People ( 'id226159703', '226159703', '7' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People7.users (), file )
    People7.sql ()

    People8=People ( 'id207484334', '207484334', '8' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People8.users (), file )
    People8.sql ()

    People9=People ( 'id160504052', '160504052', '9' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People9.users (), file )
    People9.sql ()

    People10=People ( 'id156930209', '156930209', '10' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People10.users (), file )
    People10.sql ()

    People11=People ( 'id62022070', '62022070', '11' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People11.users (), file )
    People11.sql ()

    People12=People ( 'id364803419', '364803419', '12' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People12.users (), file )
    People12.sql ()

    People13=People ( 'id164519173', '164519173', '13' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People13.users (), file )
    People13.sql ()

    People14=People ( 'id253456309', '253456309', '14' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People14.users (), file )
    People14.sql ()

    People15=People ( 'id203884671', '203884671', '15' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People15.users (), file )
    People15.sql ()

    People16=People ( 'id205840517', '205840517', '16' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People16.users (), file )
    People16.sql ()

    People17=People ( 'id487119415', '487119415', '17' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People17.users (), file )
    People17.sql ()

    People18=People ( 'id18864498', '18864498', '18' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People18.users (), file )
    People18.sql ()

    People19=People ( 'id444545086', '18864498', '19' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People19.users (), file )
    People19.sql ()

    People20=People ( 'id547652798', '547652798', '20' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People20.users (), file )
    People20.sql ()

    People21=People ( 'id72511618', '72511618', '21' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People21.users (), file )
    People21.sql ()

    People22=People ( 'id192260451', '192260451', '22' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People22.users (), file )
    People22.sql ()

    People23=People ( 'id132033643', '132033643', '23' )
    with open ( 'vk.json', "w", encoding='utf-8' ) as file:
        json.dump ( People23.users (), file )
    People23.sql ()
import Wall
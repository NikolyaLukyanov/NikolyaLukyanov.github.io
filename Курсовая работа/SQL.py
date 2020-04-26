import json
import pymysql.cursors

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
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`bdate`, `city`,`mobile_phone`,`home_phone`,`music`,`about`) VALUES (%s ,%s ,%s ,%s ,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ),
                    item.get ( 'bdate' ),item.get ( 'city' ).get ( 'title' ),
                    item.get ( 'mobile_phone' ), item.get ( 'home_phone' ),
                    item.get ( 'music' ), item.get ( 'about' )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`bdate`, `city`,`mobile_phone`,`home_phone`,`music`,`about`) VALUES (%s ,%s ,%s ,%s ,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ),
                    item.get ( 'bdate' ), item.get ( 'city', ['null'] ),
                    item.get ( 'mobile_phone' ), item.get ( 'home_phone' ),
                    item.get ( 'music' ), item.get ( 'about' )) )
                connection.commit ()
connection.close ()
with open ( 'vkq.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vkq.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:

            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `wall` (`text`,`likes`,`comments`,`reposts`,`json_has_wall_idjson_has_wall`) VALUES (%s,%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'text' ), item.get ( 'likes' ).get ( 'count' ),
                    item.get ( 'comments' ).get ( 'count' ),
                    item.get ( 'reposts' ).get ( 'count' ),
                    item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print ( "Error" )
connection.close ()
with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    print ( post )
connection=pymysql.connect ( host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor )

with open ( 'vkw.json' ) as json_file:
    post=json.load ( json_file )
    for item in post:
        try:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `grup` (`id_grup`,`name_grup`,`screen_name_grup`,`json_has_wall_idjson_has_wall`) VALUES (%s,%s,%s,%s )"
                cursor.execute ( sql, (
                    item.get ( 'id' ), item.get ( 'name' ), item.get ( 'screen_name' ),
                    item.get ( 'json_has_wall_idjson_has_wall', ['1'] )) )
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print ( "Error" )
connection.close ()
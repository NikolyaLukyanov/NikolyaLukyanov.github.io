import requests
import json
import pymysql.cursors


def take_1000_posts():
    token='cd6ad61ccd6ad61ccd6ad61c63cd056944ccd6acd6ad61c9323af835d1afa79027bd29e'
    version=5.103
    user_ids='id155384397,mybestid,id226165635,andreymuskat,chufstv,id287961694,b0rod1n,sladenkiykot,id160504052,id1234qw,id62022070,id364803419,official_page_lkik,petr_chernysh,mtboy,mark__magic,id487119415,moosemarti,m_miroslavka,aleks_dev,paradox_sd,tyapkindima,id132033643'
    fields='about,bdate,city,contacts,counters,music'
    all_posts=[]
    offset=0

    while offset < 1000:
        response=requests.get ( 'https://api.vk.com/method/users.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'user_ids': user_ids,
                                    'offset':offset,
                                    'fields':fields

                                } )
        data= response.json ()['response']
        offset+=1000
        all_posts.extend ( data )
    return all_posts


all_posts=take_1000_posts ()
with open ( 'vk.json', "w", encoding='utf-8' ) as file:
    json.dump ( take_1000_posts (), file )


with open ('vk.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(data)
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Basketboll2002',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with open ( 'vk.json', encoding='utf-8' ) as json_file:
    data=json.load ( json_file )
    for item in data:
        try:
            with connection.cursor () as cursor:
                # Create a new record
                sql="INSERT INTO `json` (`id` , `first_name`,`last_name`,`is_closed`,`can_access_closed`,`bdate`, `city`,`mobile_phone`,`music`) VALUES (%s,%s ,%s ,%s ,%s ,%s ,%s,%s,%s )"
                cursor.execute ( sql, (item.get ( 'id' ), item.get ( 'first_name' ), item.get ( 'last_name' ), item.get('is_closed'), item.get('can_access_closed'),item.get('bdate'), item.get('title'),item.get('mobile_phone'),item.get('music') ) )

                # connection is not autocommit by default. So you must commit to save
                # your changes.
            connection.commit ()
        except Exception:
            print ( "Error" )

    connection.close ()

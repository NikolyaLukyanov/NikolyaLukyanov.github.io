import mysql.connector
import requests
import time
import csv


def take_1000_posts():
    tocken = 'cd6ad61ccd6ad61ccd6ad61c63cd056944ccd6acd6ad61c9323af835d1afa79027bd29e'
    version = 5.103
    domain = 'bmstu1830'
    offset = 0
    count = 100
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': tocken,
                                    'v': version,
                                    'domain': domain
                                })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='vk',
                                       user='root',
                                       password='Basketboll2002')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()
print(1)
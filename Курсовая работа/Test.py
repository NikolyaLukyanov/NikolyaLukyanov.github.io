import requests


tocken = 'cd6ad61ccd6ad61ccd6ad61c63cd056944ccd6acd6ad61c9323af835d1afa79027bd29e'
version = 5.103
domain='bmstu1830'


response= requests.get('https://api.vk.com/method/wall.get',
                       params={
                           'access_token': tocken,
                           'v': version,
                           'domain':domain
                       })
data = response.json()
print(1)

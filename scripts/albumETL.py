import requests


def get_id(dt):
    return dt['id']


total = []
bik = []
access_token = 'BQBX4ue_zJki1LOwteINCxmdG24EbCw1vo_nR-QsHr6stJh7YZjWuK4JVmzx01BJvDdJuFLRqph515xB-gEfJ1ZnSE2xhAYcgqSGZ7QKWx3rf06r2F3as-QZAOEZ1vQqxtzz8NbdOfpDNfRr4HltAlU7tcVQIb1jyGFTVzxuQdWSYX6YrpZ46CoLF4blJHQ'
with open("artists_id.txt", 'r') as my_file:
    total.extend(eval(my_file.read()))
# print(total)
url = ''
for i in total:
    url = 'https://api.spotify.com/v1/artists/{0}/albums?limit=50'.format(i)
# url = 'https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/albums'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(access_token)
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    try:
        data = response.json()
        ans = list(map(get_id, data['items']))
        print(ans)
        with open("album_id.txt", "w") as my_file:
            bik.extend(ans)
            my_file.write(str(bik))
    except:
        pass


import requests


def get_id(dt):
    return dt['id']


total = []
bik = []
access_token = 'BQCvQoN1my9Rft8QT8znntS3u36ZWKSrTk1WQ8m1jcOIajavOq6Qf6i-u8fwcjkdRsZUYKcObNOgVXnDIrmHWRoYoIRrIV-xsJyIUCd2bMD8If5hmn4hY30oXud4iU5nf0BBkEWbwJ5NwRnGm1hl18rec6P9CStfe2nx0iaWatITZo7c63x5DJTd1K2mOsQ'
with open("artists.txt", 'r') as my_file:
    total.extend(eval(my_file.read()))
# print(total)
url = ''
for i in total:
    url = 'https://api.spotify.com/v1/search?q={0}&type=artist&limit=1'.format(
        i)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(access_token)
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    data = response.json()
    ans = data['artists']['items'][0]['id']
    print(ans)
    with open("artists_id.txt", "w") as my_file:
        bik.append(ans)
        my_file.write(str(bik))

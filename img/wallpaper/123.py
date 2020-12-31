import requests



for i in range(1,460):
    k = str(i)
    k = k.rjust(4,'0')
    url = '    - https://cdn.jsdelivr.net/gh/mambainveins/ImageHosting/img/wallpaper/{}.png'.format(k)
    print(url)
 
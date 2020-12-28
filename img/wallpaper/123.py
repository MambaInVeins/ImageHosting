import requests



for i in range(0,465):
    k = str(i)
    k = k.rjust(4,'0')
    url = 'https://cdn.jsdelivr.net/gh/Yafine/cdn@3.3.4/images/{}.png'.format(k)
    print(url)
    r = requests.get(url=url)

    with open('{}.png'.format(k), 'wb') as f:
        f.write(r.content)
        print(url,'OK')
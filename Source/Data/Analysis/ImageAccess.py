import requests

url = 'https://tpc.googlesyndication.com/simgad/3605728719349916052'
filename = url.split('/')[-1] + '.jpg'
r = requests.get(url, allow_redirects=True)
open(filename, 'wb').write(r.content)

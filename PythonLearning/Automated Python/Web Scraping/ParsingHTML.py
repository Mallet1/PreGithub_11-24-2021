import bs4, requests

res = requests.get('https://www.amazon.com/LULEX-Moccasin-Slippers-Memory-Anti-Slip/dp/B083BM2QWH/ref=sr_1_1_sspa?dchild=1&keywords=sperry+slippers&qid=1616707934&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMVFGWDE0NzRSTlROJmVuY3J5cHRlZElkPUEwNjUzODkzM01CR1FDVVNHOFVYTiZlbmNyeXB0ZWRBZElkPUEwNjA3NTAwMUlMVFcyV0dPNTlaWSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=')

print(res.raise_for_status())

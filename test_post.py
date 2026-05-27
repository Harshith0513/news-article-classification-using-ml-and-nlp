import urllib.parse
import urllib.request

samples = [
    'Stock market soars as tech earnings beat expectations',
    'Local team wins championship after dramatic overtime',
    'Government passes new education reform bill affecting millions',
    'New movie breaks box office records worldwide',
    'Scientists discover new method for renewable energy storage'
]

url = 'http://localhost:8000/classify'
for s in samples:
    data = urllib.parse.urlencode({'news_article': s}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(s[:60], '->', resp.read().decode('utf-8'))

import urllib2
import json

long_url = "http://timesofindia.indiatimes.com/international-home" #put the url to be shortened here

post_url = 'https://www.googleapis.com/urlshortener/v1/url'
postdata = {'longUrl':long_url}
headers = {'Content-Type':'application/json'}
request = urllib2.Request(post_url,json.dumps(postdata),headers)
short_url = urllib2.urlopen(request).read()
print json.loads(short_url)['id']

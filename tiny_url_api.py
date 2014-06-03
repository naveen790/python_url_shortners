import urllib2
import urllib

api_base_url = "http://tinyurl.com/api-create.php?"
long_url = "http://timesofindia.indiatimes.com/international-home" #put the url to be shortened here

enc_url = urllib.urlencode({'url':long_url})
api_url = api_base_url + enc_url
short_url = urllib2.urlopen(urllib2.Request(api_url))
print short_url.read()

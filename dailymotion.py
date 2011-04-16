#!/usr/bin/env python

BASE='https://api.dailymotion.com/json'
KEY='13fe53372252ffbcf7fc'
SECRET='1312afbc7a53a2f3c01fcf951878a05babd8bf4d'
USER='feroztest'
PASS='pitivitest'
OAUTH='https://api.dailymotion.com/oauth/token'


from httplib2 import Http
from urllib import urlencode
import json
import urllib2


#OAuth2 to fetch access_token and refresh_token 
values = {'grant_type' : 'password',
          'client_id' : KEY,
          'client_secret' : SECRET,
          'username' : USER,
          'password' : PASS,
          'scope':'write'
          }

data = urlencode(values)
req = urllib2.Request(OAUTH, data)
response = urllib2.urlopen(req)


result=json.load(response)
access_token=result['access_token']
refresh_token=result['refresh_token']

#print access_token, refresh_token

UURL='?access_token='+access_token





#advanced api
job=json.dumps({"call":"file.upload","args":None})

data = urlencode(values)
req = urllib2.Request(BASE+UURL, job, {'content-type': 'application/json'})
response = urllib2.urlopen(req)

result=json.load(response)
temp= result['result']

upload_url= temp['upload_url']






#Post using multipart form data using module poster (sudo easy_install install poster)
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

# Register the streaming http handlers with urllib2
register_openers()

# headers contains the necessary Content-Type and Content-Length
# datagen is a generator object that yields the encoded parameters
datagen, headers = multipart_encode({"file": open("sample.3gp")})

request = urllib2.Request(upload_url, datagen, headers)
result=json.load(urllib2.urlopen(request))
v_url = result['url'] #video URL returned




job=json.dumps({"call":"video.create","args":{"url":v_url}})

data = urlencode(values)
req = urllib2.Request(BASE+UURL, job, {'content-type': 'application/json'})
response = urllib2.urlopen(req)


result=json.load(response)
temp=result['result']
id=temp['id']

print id

#publish video

job=json.dumps({"call":"video.edit","args":{"id":id,"title":"samples","tags":"pitivi","channel":"comedy"}})

data = urlencode(values)
req = urllib2.Request(BASE+UURL, job, {'content-type': 'application/json'})
response = urllib2.urlopen(req)


print "Upload successful - http://dailymotion.com/video/"+id
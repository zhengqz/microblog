"""
>>>import base64,uuid
>>>base64.b64encode(uuid.uuid4().bytes+uuid.uuid4()
'3sVOCIXHRBuMGyCaSqwD+PartS9RU0sIgWY/fIL/FGg='
"""
WTF_CSRF_ENABLED = True
SECRET_KEY = '3sVOCIXHRBuMGyCaSqwD+PartS9RU0sIgWY/fIL/FGg='

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
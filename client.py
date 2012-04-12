import requests

class Content(object):
    def where(self, params={}):
        return Query(self).where(params)

    def all(self):
        return Query(self).all()

class Query(object):
    def __init__(self, klass):
        self._klass = klass
        self._client = Client()
        self._criteria = None
        self._request = None

    def criteria(self):
        if not self._criteria:
            self._criteria = {}
        return self._criteria

    def where(self, params={}):
        self.criteria().update(params)
        return self

    def all(self):
        return self.execute()

    def request(self):
        if not self._request:
            self._request = self._client.all(self.criteria())
        return self._request

    def execute(self):
        return self.request().perform()

class Client(object):
    def __init__(self):
        self._domain = "http://www.fcc.gov/api"
        self._params = None
        self._url = None

    def get(self, id):
        self._url = "%(domain)s/content/%(id)s.json" % {'id':id, 'domain':self._domain}
        return self
                
    def all(self, params={}):
        self._params = params
        self._url = "%(domain)s/content.json?" % {'domain':self._domain}
        return self
        
    def perform(self):
        return requests.get(self._url, params=self._params)

# example:
# print Content().where({"search_string":"broadband"}).where({"limit":1}).all().text
import webapp2
import sys
import logging
import os

app = webapp2.WSGIApplication([
    (r'/', 'views.Index'),
    (r'/html/(\w+)/', 'views.Html'),
    (r'/html', 'views.Html'),

    webapp2.Route(r'/.*', webapp2.RedirectHandler, defaults={'_uri': 'http://www.tagtoo.com.tw/'}),
], debug=False)
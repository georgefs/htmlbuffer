import webapp2
import sys
import logging
import os

app = webapp2.WSGIApplication([
    (r'/list$', 'views.Index'),
    (r'/list/([^\\]+)/?', 'views.Index'),
    (r'/html/([^\\]+)/?', 'views.Html'),
    (r'/html', 'views.Html'),

    webapp2.Route(r'/.*', webapp2.RedirectHandler, defaults={'_uri': 'http://www.tagtoo.com.tw/'}),
], debug=False)

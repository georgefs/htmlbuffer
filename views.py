import webapp2
from models import TempFile
import jinja2
import os
from jinja2 import Template, Environment
from google.appengine.datastore.datastore_query import Cursor
import urlparse
import urllib


loader_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
template_loader = Environment(loader=jinja2.FileSystemLoader(loader_path))
    

class Index(webapp2.RequestHandler):
    def get(self, group=None):
        cursor = self.request.get('cursor')

        template = template_loader.get_template('index.html')
        query = {}
        if cursor:
            query['start_cursor'] = Cursor.urlsafe(cursor)

        if group:
            temp_query = TempFile.query(TempFile.group==group)
        else:
            temp_query = TempFile.query()

        
        items, cursor, more = temp_query.order(-TempFile.updated).fetch_page(100, **query)
        cursor = cursor and cursor.urlsafe()

        self.response.write(template.render({"items":items, "cursor":cursor, "more":more}))


class Html(webapp2.RequestHandler):
    def get(self, name):
        no_fix = self.request.get('no_fix', False)

        temp = TempFile.get_by_id(name) or TempFile.get_by_id(urllib.quote_plus(name)) or TempFile.get_by_id(int(name))
                
        if no_fix:
            html = temp.html
        else:
            from funcs import fix_url
            html = fix_url(temp.html, temp.url)

        self.response.write(html)

    def post(self):
        if 'appspot.com' in self.request.headers.get('referer'):
            return

        name = self.request.params.get('name')
        html = self.request.params.get('html')
        url = self.request.params.get('url') or self.request.headers.get('referer')
        group = self.request.params.get('group')

        tempfile = TempFile(id=name, url=url, html=html, group=group)
        tempfile.put()

        self.response.write('success')

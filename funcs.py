import re
from functools import partial
import urlparse
 
def __update(matcher, base):
    def update_base(matcher, base):
        key, value = matcher.groups()
        return u'{}="{}"'.format(key, urlparse.urljoin(base, value))
 
    update_base = partial(update_base, base=base)
    data = matcher.group()
    return re.sub("(src|href)\s*=\s*[\"']([^\"']+)['\"]", update_base, data)
 

def fix_url(html, url):
    update_url = partial(__update, base=url)
    return re.sub("<script [^>]*>|<link [^>]+>|<a [^>]+>", update_url, html)

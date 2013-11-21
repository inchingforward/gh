import requests
from lxml import html


SITE_LINKS = (
    ('St. Louis Business Journal', 'http://www.bizjournals.com/stlouis/news', 'li.object_subtype_blog_post h4 a', True),
    ('Reddit', 'http://www.reddit.com/r/stlouis+programming', 'div.thing div.entry a.title', False),
)

if __name__ == '__main__':
    for (name, url, selector, include_base) in SITE_LINKS:
        print('\n\n%s\n%s' % (name, '-' * len(name)))
        res = requests.get(url)
        doc = html.fromstring(res.text)
        links = doc.cssselect(selector)
        base_url = doc.base[:-1] if include_base else ''
        
        for link in links:
            print '%s:\n  %s%s\n' % (link.text, base_url, link.get('href'))

# TODO:
#http://www.stltoday.com/search/?l=25&skin=/branding/stltoday/news&sd=desc&s=start_time&f=html&q=technology
#https://www.stlbeacon.org/#!/list/AND[CATEGORY[innovation_stl]]
#http://techli.com/news/
#https://news.ycombinator.com/newest
#http://monocle.io
#http://www.techmeme.com/river
#http://www.altdevblogaday.com

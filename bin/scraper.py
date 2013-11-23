import requests
from lxml import html


SITE_LINKS = (
    ('St. Louis Business Journal', 'http://www.bizjournals.com/stlouis/news', 'li.object_subtype_blog_post h4 a', True),
    ('Reddit', 'http://www.reddit.com/r/stlouis+programming', 'div.thing div.entry a.title', False),
    ('Hacker News', 'http://news.ycombinator.com', 'td.title a', False),
    ('Techli', 'http://techli.com/news', 'h2.post-title a', False),
    ('TechMeme', 'http://www.techmeme.com', 'div.ii strong a', False),
)

def print_site_links():
    for (name, url, selector, include_base) in SITE_LINKS:
        print('\n\n%s\n%s' % (name, '-' * len(name)))
        res = requests.get(url)
        doc = html.fromstring(res.text)
        links = doc.cssselect(selector)
        base_url = doc.base[:-1] if include_base else ''
        
        for link in links[0:20]:
            print '%s:\n  %s%s\n' % (link.text, base_url, link.get('href'))
    
if __name__ == '__main__':
    print_site_links()

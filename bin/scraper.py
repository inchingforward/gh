import requests
from lxml import html


def print_links(links, base_url=''):
    for link in links:
        print '%s:\n  %s%s\n' % (link.text, base_url, link.get('href')[1:])
        
def print_biz_journal_links():
    print("\n\nSt. Louis Business Journal\n--------------------------")
    res = requests.get('http://www.bizjournals.com/stlouis/news')
    doc = html.fromstring(res.text)
    links = doc.cssselect('li.object_subtype_blog_post h4 a')
    print_links(links, doc.base)

def print_reddit_links():
    print("\n\nReddit Stl+Programming\n----------------------")
    res = requests.get('http://www.reddit.com/r/stlouis+programming')
    doc = html.fromstring(res.text)
    links = doc.cssselect('div.thing div.entry a.title')
    print_links(links)

if __name__ == '__main__':
    print_biz_journal_links()
    print_reddit_links()

# TODO:
#http://www.stltoday.com/search/?l=25&skin=/branding/stltoday/news&sd=desc&s=start_time&f=html&q=technology
#https://www.stlbeacon.org/#!/list/AND[CATEGORY[innovation_stl]]
#http://techli.com/news/
#https://news.ycombinator.com/newest
#http://monocle.io
#http://www.techmeme.com/river
#http://www.altdevblogaday.com

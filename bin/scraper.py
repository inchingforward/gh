"""
scraper
-------

The scraper module scrapes pre-defined sites containing potential 
Gateway Hackers news links.  The pre-defined sites in the 
SITES list of maps contain the following keys:

    name       : The name of the site, used for display purposes.
    url        : The url of the site to scrape from.
    selector   : The css selector that indentifies a list of links within
                 the url result to scrape.
    transformer: A lambda that takes the base url of the site 
                 as well as the link to transform.  This is useful for sites that 
                 use relative urls or modify a link's url in some way.
"""

import re
import requests
from lxml import html


SITES = [{
        'name': 'St. Louis Business Journal', 
        'url': 'http://www.bizjournals.com/stlouis/news', 
        'selector': 'li.object_subtype_blog_post h4 a', 
        'transformer': lambda base, url: base + url[1:],
    }, {
        'name': 'Reddit', 
        'url': 'http://www.reddit.com/r/stlouis+programming', 
        'selector': 'div.thing div.entry a.title', 
        'transformer': lambda base, url: re.sub(r'^/r/', 'http://reddit.com/r/', url)
    }, {
        'name': 'Hacker News', 
        'url': 'http://news.ycombinator.com', 
        'selector': 'td.title a', 
        'transformer': lambda base, url: re.sub(r'^item?id', base + '/item?id', url)
    }, {
        'name': 'Techli', 
        'url': 'http://techli.com/news', 
        'selector': 'h2.post-title a', 
    }, {
        'name': 'TechMeme', 
        'url': 'http://www.techmeme.com', 
        'selector': 'div.ii strong a',
        'transformer': lambda base, url: re.sub(r'^/goto/', 'http://', url)
    }, {
        'name': 'St. Louis Beacon', 
        'url': 'https://www.stlbeacon.org/#!/list/AND[CATEGORY[innovation_stl]]',
        'selector': 'section#innovation_stl_panel h1 a',
        'transformer': lambda base, url: 'https://www.stlbeacon.org' + url
    },
]

def get_site_links():
    """Iterates through SITES and creates a list of maps with the following
    corresponding keys:
    
        name : The name of the site
        links: A list of news links from the site
    
    Each link in the links list contains a 'text' key for the link's
    text, and an 'href' which contains a fully-qualified url.
    """
    
    site_links = []
    
    for site in SITES:
        site_map = {'name': site['name'], 'links': []}
        
        res = requests.get(site['url'])
        doc = html.fromstring(res.text)
        links = doc.cssselect(site['selector'])
        transformer = site.get('transformer', None)
        base_url = doc.base or site['url']
        
        for link in links[0:20]:
            href = link.get('href')
            
            if link.text and href:
                if transformer:
                    href = transformer(base_url, href)
                
                site_map['links'].append({'text': link.text, 'href': href})
        
        site_links.append(site_map)
    
    return site_links

def print_site_links(site_links):
    """Prints a list of site_links maps."""
    
    for site in site_links:
        print('\n\n%s\n%s' % (site['name'], '-' * len(site['name'])))
        for link in site['links']:
            print '%s:\n  %s\n' % (link['text'], link.get('href'))

if __name__ == '__main__':
    site_links = get_site_links()
    print_site_links(site_links)


import requests
from lxml import html


SITES = [{
        'name': 'St. Louis Business Journal', 
        'url': 'http://www.bizjournals.com/stlouis/news', 
        'selector': 'li.object_subtype_blog_post h4 a', 
        'include_base': True
    }, {
        'name': 'Reddit', 
        'url': 'http://www.reddit.com/r/stlouis+programming', 
        'selector': 'div.thing div.entry a.title', 
        'include_base': False
    }, {
        'name': 'Hacker News', 
        'url': 'http://news.ycombinator.com', 
        'selector': 'td.title a', 
        'include_base': False
    }, {
        'name': 'Techli', 
        'url': 'http://techli.com/news', 
        'selector': 'h2.post-title a', 
        'include_base': False
    }, {
        'name': 'TechMeme', 
        'url': 'http://www.techmeme.com', 
        'selector': 'div.ii strong a', 
        'include_base': False
    },
]

def get_site_links():
    site_links = []
    
    for site in SITES:
        site_map = {'name': site['name'], 'links': []}
        res = requests.get(site['url'])
        doc = html.fromstring(res.text)
        links = doc.cssselect(site['selector'])
        base_url = doc.base[:-1] if site['include_base'] else ''
        
        for link in links[0:20]:
            href = base_url + link.get('href')
            site_map['links'].append({'text': link.text, 'href': href})
        
        site_links.append(site_map)
    
    return site_links

def print_site_links(site_links):
    for site in site_links:
        print('\n\n%s\n%s' % (site['name'], '-' * len(site['name'])))
        for link in site['links']:
            print '%s:\n  %s\n' % (link['text'], link.get('href'))

if __name__ == '__main__':
    site_links = get_site_links()
    print_site_links(site_links)


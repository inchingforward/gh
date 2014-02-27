from multiprocessing import Pool
import requests
from lxml import html
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from .models import WebPage


@user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
def get_pages(request):
    pages = WebPage.objects.all()
    
    page_links = {}
    if pages:
        pool = Pool(10)
        page_links = pool.map(get_links, pages)
        pool.close()
        pool.join()
    
    return render(request, "sources/pages.html", {'page_links': page_links})

def get_links(page):
    page_map = {'page': page, 'links': []}
    res = requests.get(page.url)
    doc = html.fromstring(res.text)
    links = doc.cssselect(page.selector)
    prefix = page.prefix
    
    for link in links[0:20]:
        href = link.get('href')
        
        if link.text and href:
            link_text = link.text.strip()
            print href
            if href.startswith("/"):
                href = page.prefix + href
            
            page_map['links'].append({'text': link_text, 'href': href})
    
    return page_map


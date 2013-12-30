import requests
from lxml import html
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render
from .models import WebPage


@user_passes_test(lambda u: u.is_staff, login_url='/accounts/login/')
def get_pages(request):
    pages = WebPage.objects.all()
    page_links = []
    
    for page in pages:
        page_map = {'page': page, 'links': []}
        get_links(page, page_map)
        page_links.append(page_map)
        
    return render(request, "sources/pages.html", {'page_links': page_links})

def get_links(page, page_map):
    res = requests.get(page.url)
    doc = html.fromstring(res.text)
    links = doc.cssselect(page.selector)
    prefix = page.prefix
    
    for link in links[0:20]:
        href = link.get('href')
        
        if link.text and href:
            link_text = link.text.strip()
            if href.startswith("/"):
                href = page.url + href
            
            page_map['links'].append({'text': link_text, 'href': href})

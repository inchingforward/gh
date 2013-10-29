import requests
from BeautifulSoup import BeautifulSoup
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import PostForm
from .models import Post


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    fields = ['url', 'title', 'details']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

def fetch_url_title(request):
    title = ''
    try:
        url = request.GET.get('url', '')
        if url:
            result = requests.get(url)
            if result and result.status_code == 200:
                soup = BeautifulSoup(result.content)
                if soup.title:
                    title = soup.title.string
    except Exception as e:
        print 'unexpected fetch_url_title error: %s' % e
    
    return HttpResponse(title)


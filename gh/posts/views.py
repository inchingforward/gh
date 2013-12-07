import requests
from BeautifulSoup import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from braces.views import LoginRequiredMixin
from .forms import PostForm
from .models import Post


class PostDetailView(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    fields = ['url', 'title', 'details']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        posts = Post.objects.filter(url__iexact=form.instance.url)
        
        if posts:
            url = posts.reverse()[0].get_absolute_url()
            messages.add_message(self.request, messages.INFO, 'This link has already been submitted:')
            return HttpResponseRedirect(url)
        
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)
    

class PostListView(ListView):
    model = Post
    paginate_by = 20

def fetch_url_title(request):
    title = ''
    try:
        url = request.GET.get('url', '')
        if url:
            result = requests.get(url)
            if result:
                if result.status_code == 200:
                    soup = BeautifulSoup(result.content)
                    if soup.title:
                        title = soup.title.string
            else:
                title = "Error: server returned status %s" % result.status_code
    except Exception as e:
        title = "Unexpected error"
    
    return HttpResponse(title)


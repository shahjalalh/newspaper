from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'newspaper/blog/post/post_list.html'
    queryset = Post.published.get_queryset()


class PostDetailView(DetailView):
    model = Post
    template_name = 'newspaper/blog/post/post_detail.html'

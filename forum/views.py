from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy, reverse
from .models import Thread, Post
from .forms import ThreadForm, PostForm

class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/index.html'
    context_object_name = 'threads'
    ordering = ['-created_at']
    paginate_by = 10

class ThreadDetailView(FormMixin, DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'
    context_object_name = 'thread'
    form_class = PostForm

    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(thread=self.object)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.thread = self.object
            post.save()
            return self.form_valid(form)
        return self.form_invalid(form)

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/create_thread.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
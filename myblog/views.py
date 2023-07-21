from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'myblog/post_create.html'
    fields = ['title', 'content', 'category', 'tags']
    success_url = reverse_lazy('myblog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'myblog/post_update.html'
    fields = ['title', 'content', 'category', 'tags']
    success_url = reverse_lazy('myblog:home')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'myblog/post_delete.html'
    success_url = reverse_lazy('myblog:home')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('full_name')
            email = request.POST.get('email')
            message = request.POST.get('message')

        # Send email
        send_mail(
            'New Contact Form Submission',
            f'Full Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.EMAIL_HOST_USER,  # Your email address as the sender
            ['augustinekyei16@gmail.com'],  # Replace with your specific email address as the recipient
        )

        return render(request, 'contact_form.html', {'success': True})

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})




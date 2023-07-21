from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.conf import settings
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm

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

def success_view(request):
    return render(request, 'success.html')

class MyContactFormView(FormView):
    template_name = 'contact_form.html'  # Replace this with the path to your template
    form_class = ContactForm
    success_url = '/success/'
    
    def form_valid(self, form):
        # Process the form data and send the email
        sender_name = form.cleaned_data['sender_name']
        sender_email = form.cleaned_data['sender_email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

    # Compose the email content
        email_content = f"Name: {sender_name}\nEmail: {sender_email}\n\n{message}"

        send_mail(
            subject=subject,
            message=email_content,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Use the default sender specified in settings.py
            recipient_list=['augustinekyei16@gmail.com'],  # Replace with the recipient email(s) you want to send the email to
        )
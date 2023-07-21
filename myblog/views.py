from email.message import EmailMessage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myblog.forms import ContactForm

from myblog.settings import EMAIL_HOST_USER
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .settings import EMAIL_HOST_USER

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

def send_email(sender_name, sender_email, subject, message):
    # Prepare the email
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=sender_email,
        to=['test@gmail.com'],  # Replace with your recipient's email address
        reply_to=[sender_email],
    )

    # Send the email
    email.send()

def contact_form_view(request):
    confirmation_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            confirmation_message = _extracted_from_contact_form_view_7(form)
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form, 'confirmation_message': confirmation_message})


# TODO Rename this here and in `contact_form_view`
def _extracted_from_contact_form_view_7(form):
    sender_name = form.cleaned_data['sender_name']
    sender_email = form.cleaned_data['sender_email']
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']

    # Call the function to send the email
    send_email(sender_name, sender_email, subject, message)

    return "Email sent successfully."
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/pages/home.html'

class AboutView(TemplateView):
    template_name = 'core/pages/about.html'

class GalleryView(TemplateView):
    template_name = 'core/pages/gallery.html'

class FAQView(TemplateView):
    template_name = 'core/pages/faq.html'
from django.views.generic import TemplateView
from .models import AssetCategory, FixedAsset, AssetOperation


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = AssetCategory.objects.all()
        context['assets'] = FixedAsset.objects.all()
        context['operations'] = AssetOperation.objects.all()[:5]
        return context
from django.views.generic import TemplateView

from .models import Service, JobTitle, Employee, FeaturedItem


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['job_titles'] = JobTitle.objects.order_by('?').all()
        context['featured_items'] = FeaturedItem.objects.order_by('?').all()
        return context


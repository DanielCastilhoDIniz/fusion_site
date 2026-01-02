from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, JobTitle, Employee, FeaturedItem
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['job_titles'] = JobTitle.objects.order_by('?').all()
        context['featured_items'] = FeaturedItem.objects.order_by('?').all()
        return context

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar a mensagem. Verifique os dados preenchidos.')
        return super().form_invalid(form)

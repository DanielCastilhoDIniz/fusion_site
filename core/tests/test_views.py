from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from django.contrib.messages import get_messages


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'user1',
            'email': 'user1@exemple.com',
            'subject': 'Subject Test',
            'message': 'This is a test message.'
        }
        self.cliente = Client()

    def test_form_valid(self):
        """Test ContactForm with valid data"""
        request = self.cliente.post(reverse_lazy('index'), data=self.data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        """Test ContactForm with invalid data"""
        data_invalid = {
            'name': 'user1',
            'email': 'user1@exemple.com'
        }
        request = self.cliente.post(reverse_lazy('index'), data=data_invalid)
        self.assertEqual(request.status_code, 200)

    def test_form_valid_message(self):
        
        response = self.cliente.post(
            reverse_lazy('index'),
            data=self.data, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Mensagem enviada com sucesso!')

    def test_form_invalid_message(self):
        response = self.cliente.post(
            reverse_lazy('index'),
            data={}, follow=True)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Erro ao enviar a mensagem.'
                         ' Verifique os dados preenchidos.')


from django.test import TestCase
from core.forms import ContactForm
from django.core import mail


class ContactFormTest(TestCase):
    """Tests for the ContactForm in core/forms.py
    """

    def setUp(self):
        self.name = 'user1'
        self.email = 'user1@example.com'
        self.subject = 'Subject Test'
        self.message = 'This is a test message.'

        self.valid_data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
        }

    def test_contact_form_valid_data(self):
        """Test ContactForm with valid data"""

        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

        form.send_email()
        self.assertEqual(len(mail.outbox), 1)

        email = mail.outbox[0]

        # Conteúdo do e-mail
        self.assertEqual(email.subject, self.valid_data['subject'])
        self.assertIn(self.valid_data['name'], email.body)
        self.assertIn(self.valid_data['email'], email.body)
        self.assertIn(self.valid_data['message'], email.body)

        # Destinatário
        self.assertEqual(email.to, ['contato@fusion.com.br'])

    def test_contact_form_missing_fields(self):
        """Test ContactForm with missing required fields"""

        invalid_data = self.valid_data.copy()
        del invalid_data['subject']

        form = ContactForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors)

    def test_contact_form_empty_message(self):
        """Test ContactForm with empty message field"""

        invalid_data = self.valid_data.copy()
        invalid_data['message'] = ''

        form = ContactForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)





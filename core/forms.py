from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=150)
    message = forms.CharField(label='Mensagem',
                              widget=forms.Textarea,
                              max_length=2000,
                              error_messages={
                                  'invalid': 'E-mail inválido.'
                                  })

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if '\n' in email or '\r' in email:
    #         raise forms.ValidationError('E-mail inválido.')
    #     return email

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        message_body = f'Nome: {name}\nE-mail: {email}\n\n{message}'

        email_message = EmailMessage(
            subject=subject,
            body=message_body,
            from_email='contato@fusion.com',
            to=['contato@fusion.com.br'],
            headers={'Reply-To': email}
        )

        email_message.send()

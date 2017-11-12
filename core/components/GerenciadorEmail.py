from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import engines
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Email(object):
    """
    A wrapper around Django's EmailMultiAlternatives
    that renders txt and html templates.
    Example Usage:
    >>> email = Email(to='oz@example.com', subject='A great non-spammy email!')
    >>> ctx = {'username': 'Oz Katz'}
    >>> email.text('templates/email.txt', ctx)
    >>> email.html('templates/email.html', ctx)  # Optional
    >>> email.send()
    >>>
    """
    def __init__(self, remetente, assunto):
        self.remetente = remetente
        self.assunto = assunto
        self._html = None
        self._texto = None
        self._configurar()
        
    def _configurar(self):
        try:
            config = dict(line.replace(' ','').strip().split('=') for line in open('mail.pwd') if not line.startswith('#') and not line.startswith('\n')) 
            self.EMAIL_HOST_USER = config['EMAIL_HOST_USER']
            self.EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
        except Exception as err:
            print(err)
            self.EMAIL_HOST_USER = ""
            self.EMAIL_HOST_PASSWORD = ""
        

    def _renderizar(self, template, conteudo):
        return render_to_string(template,conteudo)

    def html(self, template, conteudo):
        self._html = self._renderizar(template, conteudo)

    def texto(self, texto, conteudo):
        django_engine = engines['django']
        template = django_engine.from_string(texto)
        self._texto = self._renderizar(template, conteudo)

    def enviar(self, destinatario):

        email = MIMEMultipart()

        email['From'] = self.remetente
        email['To'] = destinatario
        email['Subject'] = self.assunto

        if self._texto:
            email.attach(MIMEText(self._texto, 'plain'))
        if self._html:
            email.attach(MIMEText(self._html, 'html'))

        server = smtplib.SMTP('br362.hostgator.com.br', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        try:
            server.login(self.EMAIL_HOST_USER, self.EMAIL_HOST_PASSWORD)
            server.sendmail(self.remetente, destinatario, email.as_string())
        except Exception as err:
            print(err)
        finally:
            server.quit()


    def enviar2(self, remetente=None, fail_silently=False):
        if isinstance(self.destinatario, str):
            self.destinatario = [self.destinatario]
        if not remetente:
            remetente = getattr(settings, 'EMAIL_FROM_ADDR')
        msg = EmailMultiAlternatives(
            self.assunto,
            self._text,
            remetente,
            self.destinatario
        )
        if self._html:
            msg.attach_alternative(self._html, 'text/html')
        msg.send(fail_silently)
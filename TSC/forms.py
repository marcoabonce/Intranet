from django import forms
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailForm(forms.Form):
    nombre = forms.CharField(required=True,
                                min_length=3, max_length=20,
                                widget=forms.TextInput(attrs={
                                    'id':'nombre'
                                }))
    apellido = forms.CharField(required=True,
                                min_length=3, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'id':'apellido'
                                }))
    email = forms.EmailField(required=True,
                                    widget=forms.TextInput(attrs={
                                    'id':'email'
                                }))
    telefono = forms.DecimalField(required=True,
                                    max_digits=10,
                                    widget=forms.TextInput(attrs={
                                    'id':'telefono'
                                }))
    mensaje = forms.CharField(required=True,
                                    widget=forms.Textarea(attrs={
                                    'id':'mensaje'
                                }))
    
    def send_email(self):
        nombre = self.cleaned_data.get('nombre')
        apellido = self.cleaned_data.get('apellido')
        email = self.cleaned_data.get('email')
        telefono = self.cleaned_data.get('telefono')
        mensaje = self.cleaned_data.get('mensaje')

        sender_address = 'stedeelte@gmail.com'
        sender_pass = '1234Lolo'

        session = smtplib.SMTP(host="smtp.gmail.com",port=587)
        context = ssl.create_default_context()
        session.starttls(context=context)
        session.login(sender_address,sender_pass)

        messasage = MIMEMultipart()
        messasage['From']=sender_address
        messasage['Subject'] = 'Correo de pagina'
        mail_content = 'De: '+nombre+' '+apellido+'\n'+'Numero: '+str(telefono) +'\n'+mensaje
        messasage.attach(MIMEText(mail_content, 'plain'))
        text = messasage.as_string()

        session.sendmail(sender_address, email,text)
        session.quit()
        

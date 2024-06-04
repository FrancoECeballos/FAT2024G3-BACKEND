import random
from mailer import Mailer

import os

def get_codigoVerificacion(pk):
    ran= random.randrange(1000,9999)
    print(ran)
    codigo = pk*10000 + ran
    
    return codigo

##para probar:
##print(get_codigoVerificacion(65))

def send_pass_mail(email_usuario,nombre):
    dirname = os.path.dirname(__file__)
    p = os.path.join(dirname, 'email_template.txt')

    with open(p, 'r') as file:
        file_contents = file.read()
    
    file_contents = file_contents.replace('<U>',nombre)

    file_contents = file_contents.replace('<C>',str(get_codigoVerificacion(65)))

    mail = Mailer(email='prontaentregaappoficial@hotmail.com',
                password='pedrito1234')

    mail.settings(repeat=1,
                sleep=0,
                provider=mail.MICROSOFT,
                multi=False)

    mail.send(receiver=email_usuario,  # Email From Any service Provider
            no_reply='noreplay@example.com', # Redirect receiver to another email when try to reply.
            subject='TEST',
            message=file_contents)
    
send_pass_mail('davidandradag@gmail.com','pedrito')
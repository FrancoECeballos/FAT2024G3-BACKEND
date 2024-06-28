import random
from mailer import Mailer

import os

mail = Mailer(email='prontaentregaappoficial@hotmail.com',password='pedrito1234')
mail.settings(repeat=1,
            sleep=0,
            provider=mail.MICROSOFT,
            multi=False)

dirname = os.path.dirname(__file__)

def get_codigoVerificacion(pk):
    ran= random.randrange(1000,9999)
    print(ran)
    codigo = pk*10000 + ran
    
    return codigo

##para probar:
##print(get_codigoVerificacion(65))

def cambiar_contra(email_usuario,nombre,codigo):
    
    p = os.path.join(dirname, 'email_cambiar_contra.txt')

    with open(p, 'r') as file:
        file_contents = file.read()
    
    file_contents = file_contents.replace('[nombre]',nombre)

    file_contents = file_contents.replace('[codigo]',str(codigo))

    send(email_usuario,file_contents)

def verificar_register(email_usuario,nombre,link):
    
    p = os.path.join(dirname, 'email_verificar_register.txt')

    with open(p, 'r') as file:
        file_contents = file.read()

    file_contents = file_contents.replace('[nombre]',nombre)
    file_contents = file_contents.replace('[link]',link) ## ESTO HAY QUE REMPLAZARLO MAS ADELANTE, tiene que dar a una pagina

    send(email_usuario,file_contents)
    
def send(email_usuario,file_contents):
    mail.send(receiver=email_usuario,  # Email From Any service Provider
            no_reply='noreplay@example.com', # Redirect receiver to another email when try to reply.
            subject='verificar cuenta',
            message=file_contents)

##cambiar_contra('davidandradag@gmail.com','pedrito')

#verificar_register('davidandradag@gmail.com','pedrito')
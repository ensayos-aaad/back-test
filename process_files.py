import pandas as pd
from sendmail import MailSender
import json

"""
Estructuras globales
"""
studens_df = pd.read_csv('encuestados.csv', 
                         index_col='id', 
                         dtype = {'id': 'string', 'est_name': 'string', 'cel': 'string', 'email': 'string'},
                         sep=';')

encuesta_df = pd.read_csv('preguntas.csv', 
                         index_col='num',                          
                         sep=';')


respuestas_df = pd.read_csv('respuestas.csv', 
                         index_col='id_estudiante',
                         dtype = {'id_estudiante': 'string', 'repuestas': 'string'},
                         sep=';')



""" Variables de test del correo
Gmail/GoogleApps:

Using SSL: smtp.gmail.com, port 465
Using TLS: smtp.gmail.com, port 587
Note: These connections may be blocked if 'Access for less secure apps' is disabled in your Google Account settings

Outlook.com/Live/Hotmail

Using TLS: smtp.live.com, port 587
"""

"""
Funciones de la aplicacion
"""

# TODO: Validar cuando el dato no se encuentra
def getStudentData(id):
    return studens_df.loc[id][['est_name', 'cel', 'email']].values.tolist()

def getQuestion(num):
    return encuesta_df.loc[num].values.tolist()  

def getAnswers(id):
    str_answers = respuestas_df.loc[id].values.tolist()[0]    
    #print(type(str_answers))
    #print(str_answers)
    answers = json.loads(str_answers)
    #print(answers)
    return answers



"""
Funciones de test
"""

def test3():
    ans_estudiante_0 = getAnswers("0000")
    print(type(ans_estudiante_0))
    print(ans_estudiante_0)
    print("---- Respuesta de cada pregunda ----")
    print(ans_estudiante_0['1'])
    print(ans_estudiante_0['2'])
    print(ans_estudiante_0['3'])
        
def test2():
    email_password = "Uff2021..*"
    sender_email_address = "agudelojairo@hotmail.com"


    mess_text = "Buenas tardes, \n" \
                "Este es un correo para informarle que nos debe plata.\n" \
                "Atte: El gobierno"


    ourmailsender = MailSender(sender_email_address, email_password, ('smtp.office365.com', 587))
    ourmailsender.set_message(mess_text, "Esto es un ensayo")
    ourmailsender.set_recipients(["helpu1409@gmail.com","henry.arcila@udea.edu.co"])
    ourmailsender.connect()
    ourmailsender.send_all()



def test1():
    print("--- Todo el CVS de los estudiantes ---")    
    print(studens_df)
    print("--- Todo el CVS de la encuesta ---")  
    print(encuesta_df)
    print("--- Informacion estudiante ID: 0000 ---")  
    print(getStudentData('0000'))
    print()
    print("--- Informacion preguntas ---")  
    print(getQuestion(1))
    print(getQuestion(2))
    print(getQuestion(3))
    print()

if __name__ == '__main__':
    # test1()
    # test2()
    test3()
    print("Test listos")
    

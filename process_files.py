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
                         dtype = {'num': int, 'enunciado':'string' ,'p_min':'int', 'p_max':'int'},                         
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
    """
    Retorna la lista de items asociados a la pregunta

    Parameters:
        num (int): Numero de la pregunta

    Returns:
       list: Lista con el contenido del enunciado, el puntaje minimo y el puntaje maximo de la pregunta num

    Requeriments:
       Que el numero de la pregunta exista (pendiente validacion)   
    """
    return encuesta_df.loc[num].values.tolist()  

def getAnswers(id):
    str_answers = respuestas_df.loc[id].values.tolist()[0]    
    #print(type(str_answers))
    #print(str_answers)
    answers = json.loads(str_answers)
    #print(answers)
    return answers

def modificarPregunta(num, enunciado, p_min = None, p_max = None):
    """
    Modifica la lista de preguntas

    Parameters:
        num (int): Numero de la pregunta a modificar
        enunciado (str): Enunciado de la pregunta a modificar
        p_min (int): Puntaje minimo asociado a la pregunta
        p_max (int): Puntaje maximo asociado a la pregunta
    Returns:
       None.
    Requeriments:
       Que el numero de la pregunta exista (pendiente validacion)   
    '''
    """
    # Actualizacion del enunciado
    encuesta_df.at[num,'enunciado']= enunciado
    # Actualizacion del puntaje minimo de la pregunta
    if p_min == None:
        encuesta_df.at[num,'p_min'] = 0
    else:
        encuesta_df.at[num,'p_min'] = p_min
    # Actualizacion del puntaje maximo de la pregunta
    if p_max == None:
        encuesta_df.at[num,'p_min'] = 0
    else:
        encuesta_df.at[num,'p_max'] = p_max

def agregarPregunta(enunciado, p_min = None, p_max = None):    
    encuesta_df.loc[len(encuesta_df) + 1] = [enunciado, p_min, p_max]
    """
    new_question = {
        'enunciado': enunciado,
        'p_min': p_min,
        'p_max': p_max,
        }
    df_question = pd.DataFrame(new_question)
    encuesta_df = df_question.append(new_question, ignore_index=True)
    """

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

def test4():
    print("Test 4 - Modificar preguntas")
    print("Encuesta antes de ser modificada")
    print(encuesta_df)
    print("Test modificar")
    print(modificarPregunta(1,"ensayo"))
    print(modificarPregunta(2,"ensayo2",1,5))
    print("Encuesta despues de ser modificada")
    print(encuesta_df)
    print("Items de la pregunta 1:", end = ' ')
    print(getQuestion(1))
    

def test5():
    print("Test 5 - Agregar preguntas")
    print("Encuesta antes de ser modificada")
    print(encuesta_df)
    agregarPregunta("Enunciado agregado 1")
    print("---> Encuesta despues agregar la primera pregunta")
    print("Numero de preguntas:", len(encuesta_df))
    print(encuesta_df)
    print("---> Encuesta despues agregar la segunda pregunta")
    agregarPregunta("Enunciado agregado 2",1,5)
    print("Numero de preguntas:", len(encuesta_df))
    print(encuesta_df)
    
if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
    print("Test listos")
    

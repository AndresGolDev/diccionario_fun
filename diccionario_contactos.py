"""
Agenda de Contactos (Diccionarios y Funciones)
Requerimiento:
Crea una función agregar_contacto que reciba un diccionario de
contactos y un nuevo contacto
con su número.
"""
def contactos(diccionario, nombre, numero):
    if nombre in diccionario:
        print(f"El contacto {nombre} ya existe.")
    else:
        diccionario[nombre] = numero

diccionario_contactos = {
    "Brenda": "0414155444",
    "Juan": "04124336574",
    "Carlos": "04126885598"
}

contactos(diccionario_contactos, "Brenda", "4141552975",)
print(diccionario_contactos)

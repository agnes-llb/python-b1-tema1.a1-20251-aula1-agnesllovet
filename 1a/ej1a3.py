'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

Enunciat:
Implementa una funció anomenada "invert_text(text_chain)" que rebi com
paràmetre una cadena de text de tipus string anomenada 'text_chain' i torni
el text invertit.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain:str):
    # Write here your code
    # verificacio que el parametre d'entrada es una string
    if not isinstance (text_chain,str):
        raise ValueError ("El parametre d'entrada ha de ser un string")
    # reseguir cadena en sentit invertit.
    text_chain_invert=""
    for iChar in range (len(text_chain)-1,-1,-1):
        text_chain_invert += text_chain[iChar]
    print (text_chain_invert)
    return text_chain_invert    

    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(invert_text("Hello world!"))
#print(invert_text(3546735))

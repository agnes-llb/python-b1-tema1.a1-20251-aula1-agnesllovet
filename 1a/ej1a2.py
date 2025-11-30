'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.
Considereu que 'list_numbers' ha de contenir valors numèrics enters majors
o iguals a '0', en cas contrari cal mostrar un error tipus 'ValueError'.

L'error el pots mostrar amb la següent instrucció:
raise ValueError("MISSATGE D'ERROR")

Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    # Write here your code
    # recorrerem la llista
    sum_odd_numbers=0
    for iNumber in list_numbers:
        if not isinstance(iNumber,int): 
            raise ValueError ("Los parametros entrados no coinciden con los valores requeridos")
        elif (iNumber <0):
                   raise ValueError ("Los parametros entrados no coinciden con los valores requeridos")
        #mirem si es un numero parell
        elif (iNumber %2)!=0:
            sum_odd_numbers+=iNumber
        # seguim seguent numero     
    return(sum_odd_numbers)

    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))

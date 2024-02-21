import numpy as np

variables_sistema = []
ecuaciones_sistema = []

def eliminar_espacios(cadena):
    return cadena.replace(" ", "")

def analizar_t_independiente(t_independiente):##Verifica que la ecuación tenga un termino independiente válido
    if not t_independiente:
        print("Error: La ecuación debe estar igualada a algún valor númerico")
        return False
    try:
        valor=eval(t_independiente) ## Si el termino independiente se puede evaluar como un número entonces es un termino válido
        float(valor)
    except ValueError:
        print("Error: El resultado de la ecuación debe ser un valor numérico.")
        return False
    return True

def analizar_ecuacion(ecuacion):##Función que retorna los coeficientes y variables de la ecuación en dos listas separadas
    coeficientes = []
    variables = []
    coeficiente_actual = 0
    denominador_actual = 1
    variable_actual = ""
    caracter_actual = ""
    caracter_anterior = ""
    definiendo = "c"  # c - definiendo coeficiente; d - definiendo denominador; v - definiendo variable

    for i in range(len(ecuacion)):
        if i == 0:
            caracter = ecuacion[0]
            if caracter.isalpha():
                coeficiente_actual = 1
                coeficientes.append(coeficiente_actual)
                definiendo = "v"
                variable_actual = caracter
            elif caracter.isdigit():
                coeficiente_actual = int(caracter)
            elif caracter == "+":
                coeficiente_actual = 1
            elif caracter == "-":
                coeficiente_actual = -1
            else:
                print("Ecuación inválida")
                return [], []
        else:
            caracter_anterior = ecuacion[i - 1]
            caracter_actual = ecuacion[i]
            if caracter_actual.isalpha():
                if caracter_anterior == "/":
                    print("Ecuación inválida")
                    return [], []
                elif caracter_anterior in "+-":
                    coeficientes.append(coeficiente_actual)
                    definiendo = "v"
                    variable_actual = caracter_actual
                elif caracter_anterior.isalpha():
                    variable_actual += caracter_actual
                elif caracter_anterior.isdigit():
                    if definiendo == "c":
                        coeficientes.append(coeficiente_actual)
                        definiendo = "v"
                        variable_actual = caracter_actual
                    elif definiendo == "d":
                        coeficiente_actual /= denominador_actual
                        coeficientes.append(coeficiente_actual)
                        definiendo = "v"
                        variable_actual = caracter_actual
                    elif definiendo == "v":
                        variable_actual += caracter_actual
                else:
                    print("Ecuación inválida")
                    return [], []

            elif caracter_actual.isdigit():
                if caracter_anterior in "+-":
                    coeficiente_actual *= int(caracter_actual)
                elif caracter_anterior == "/":
                    definiendo = "d"
                    denominador_actual = int(caracter_actual)
                elif caracter_anterior.isalpha():
                    variable_actual += caracter_actual
                elif caracter_anterior.isdigit():
                    if definiendo == "c":
                        if coeficiente_actual > 0:
                            coeficiente_actual = coeficiente_actual * 10 + int(caracter_actual)
                        elif coeficiente_actual < 0:
                            coeficiente_actual = coeficiente_actual * 10 - int(caracter_actual)
                    elif definiendo == "d":
                        denominador_actual = denominador_actual * 10 + int(caracter_actual)
                    elif definiendo == "v":
                        variable_actual += caracter_actual
                else:
                    print("Ecuación inválida")
                    return [], []

            elif caracter_actual in "+-":
                if caracter_anterior in "+-/":
                    print("Ecuación inválida")
                    return [], []
                elif definiendo == "c":
                    print("Ecuación inválida")
                    return [], []
                elif definiendo == "d":
                    print("Ecuación inválida")
                    return [], []
                elif definiendo == "v":
                    variables.append(variable_actual)
                    definiendo = "c"
                    coeficiente_actual = 1 if caracter_actual == "+" else -1

            elif caracter_actual == "/":
                if caracter_anterior in "+-/" or definiendo == "d" or definiendo == "v":
                    print("Ecuación inválida")
                    return [], []

            else:
                print("Ecuación inválida")
                return [], []

    if definiendo == "c":
        print("Ecuación inválida")
        return [], []
    elif definiendo == "d":
        print("Ecuación inválida")
        return [], []
    elif definiendo == "v":
        variables.append(variable_actual)

    return coeficientes, variables

def crear_ecuacion(coeficientes, variables, termino_independiente):##Crea un diccionario de datos para la ecuación
    coeficientes_retorno = []
    variables_retorno = []

    for variable in variables_sistema:
        variables_retorno.append(variable)
        coeficientes_retorno.append(coeficientes[variables.index(variable)] if variable in variables else 0)
    for variable in variables:
        if variable not in variables_sistema:
            variables_sistema.append(variable)
            variables_retorno.append(variable)
            coeficientes_retorno.append(coeficientes[variables.index(variable)])
    return {
        "coeficientes": coeficientes_retorno,
        "variables": variables_retorno,
        "termino_independiente": termino_independiente,
    }

def ajustar_sistema():##Verifica que todas las variables tengan un coeficiente en cada ecuación
    for ecuacion in ecuaciones_sistema:
        if ecuacion['variables'] != variables_sistema:
            for variable in variables_sistema:
                if variable not in ecuacion['variables']:
                    ecuacion['variables'].append(variable)
                    ecuacion['coeficientes'].append(0)

def determinante_sistema():
    coeficientes = []
    for ecuacion in ecuaciones_sistema:
        coeficientes.append(ecuacion['coeficientes'])
    matriz = np.array(coeficientes)
    print(matriz)
    return np.linalg.det(matriz)

def print_fila_actual(i,matriz,vector):
    for j in range(len(ecuaciones_sistema)):
        if i==j:
            print(f"--> {matriz[j]}  = {vector[j]}")
        else:
            print(f"    {matriz[j]}  = {vector[j]}")

def solucionar_sistema():
    matriz_A = []##Matriz de coeficientes
    vector_x = []##Vector de incognitas
    vector_b = []##Vector de terminos independientes

    for ecuacion in ecuaciones_sistema:
        matriz_A.append(ecuacion['coeficientes'])
        vector_b.append(float(ecuacion['termino_independiente']))
        vector_x.append(0.0)
    
    tam_sistema = len(ecuaciones_sistema) ##El tamaño del sistema

    

    for i in range(tam_sistema):##Pivoteo
        print(f"\nIteración {i+1}\n")
        pivote = matriz_A[i][i]
        print(f"Pivote = {pivote} en iteración {i+1}\n")
        if pivote == 0:
            for fila in matriz_A:
                print(fila)

            # Intercambiar fila i con una fila en la cual matriz_A[j][i] sea distinto de 0            
            for j in range(i + 1, tam_sistema):
                if matriz_A[j][i] != 0:
                    print(f"cambiando fila{i+1} por fila{j+1}\n")
                    matriz_A[i], matriz_A[j] = matriz_A[j], matriz_A[i]
                    vector_b[i], vector_b[j] = vector_b[j], vector_b[i]
                    pivote = matriz_A[i][i]
                    break  # Salir del bucle una vez que se ha realizado el intercambio
        print_fila_actual(i,matriz_A,vector_b)
        for j in range(i+1,tam_sistema):
            aji = matriz_A[j][i]
            print(f"aji= {aji} / pivote = {pivote}")
            factor = aji/pivote
            for k in range (i,tam_sistema):
                matriz_A[j][k] -= factor*matriz_A[i][k]
            vector_b[j] -= factor*vector_b[i]
    
    for i in range(tam_sistema - 1, - 1, -1):
        resto = 0 ##Cx+resto=b => x = (b-resto)/C
        for j in range(tam_sistema-1,i,-1):
            resto += matriz_A[i][j] * vector_x[j]
        xi = (vector_b[i]-resto)/matriz_A[i][i] ##x = (b-resto)/C
        vector_x[i]=xi

    print("Solución: ")
    for i in range(tam_sistema):
        print(f"{variables_sistema[i]}  =  {vector_x[i]}")





if __name__ == '__main__':

    continuar = "s"
    coeficientes_actuales = []
    variables_actuales = []
    termino_ind_actual = 0

    print("Algunos ejemplos de ecuaciones que el sistema acepta:")
    print("3x+y-4z=10")
    print("-4x1-3x2+4x3+5x5=15")
    print("a+2b+4c-5d=12")    
    print("Ecuaciones que el sistema no acepta:")
    print("x/2+y/3=5")
    print("C1X1+C2X2+C3X3=b1")
    print("x+y=")
    print("En caso de no ingresar termino independiente el sistema toma 1 como el valor")
    input("presione enter para continuar")

    while continuar == "s":

        ecuacion_ingresada = eliminar_espacios(input("Ingrese una ecuación lineal: "))
        partes = ecuacion_ingresada.split("=")##Separa las variables y el termino independiente

        termino_independiente = "1" if len(partes)==1 else partes[1] ##Si no se especifica termino independiente se toma 1 como el valor del termino independiente
        
        if analizar_t_independiente(termino_independiente) and len(partes)<3: ##Verifica que el termino independiente sea válido y que la ecuación solo tenga un "="
            coeficientes_actuales, variables_actuales = analizar_ecuacion(partes[0])##Obtiene los coeficientes y variables en 2 listas independientes
            ecuaciones_sistema.append(crear_ecuacion(coeficientes_actuales,variables_actuales,termino_independiente))##Agrega la ecuación a la lista de ecuaciones del sistema
            print(ecuaciones_sistema[len(ecuaciones_sistema)-1])
            continuar = input("Quiere ingresar otra ecuación? (s/n): ")
        else:
            print("Ecuación Invalida")

    for ecuacion in ecuaciones_sistema:##Verifica que todas las variables tengan un coeficiente en cada ecuación
        if ecuacion['variables'] != variables_sistema:
            ajustar_sistema()

    print(variables_sistema)
    for ecuacion in ecuaciones_sistema:
        print(f"{ecuacion['coeficientes']}"," = ",f"{ecuacion['termino_independiente']}")
        print()

    if len(ecuaciones_sistema) == len(variables_sistema):##Verificar que el número de ecuaciones y variables sea el mismo
        print("Hay igual cantidad de ecuaciones y variables")
        determinante = determinante_sistema()
        print("la determinante del sistema es: ",determinante)
        if determinante != 0:
            solucionar_sistema()
        else:
            print("El sistema no tiene solución")

    else:
        print("Sistema Invalido: Distinto número de ecuaciones y variables")

    finalizar = input("FIN")
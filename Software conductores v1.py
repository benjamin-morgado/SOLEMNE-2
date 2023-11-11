opcion = ['OPERARIO', 'SUPERVISOR'] #opciones a elegir
operarios = [1, 2, 3, 4, 5] #operarios disponibles
supervisores = ['profe'] #usuario supervisor
claves_operarios = ['agua', 'benja', 'juan', 'jorge', 'arlette'] #contraseñas operarios
clave_supervisores = '123456claveSegura' #contraseña para supervisor
intento = 1 #variable para contar los intentos de error en la contraseña
kms_base_datos = [0, 0, 0, 0, 0] #aquí se almacenarán los valores dados por los operarios
petroleo_base_datos = [0, 0, 0, 0, 0] #aquí se almacenarán los valores dados por los operarios
hr_inicio = [0, 0, 0, 0, 0]
min_inicio = [0, 0, 0, 0, 0]
hr_final = [0, 0, 0, 0, 0]
min_final = [0, 0, 0, 0, 0]
detener = 0 #variable para detener el bucle

while detener != 1: #mientras detener sea distinto a 1
    pregunta = input('Es usted operario o supervisor: ')
    pregunta = pregunta.upper() #pasa la respuesta a mayusculas
    if pregunta in opcion[0]: #evalua si la respuesta está en el elemento 0 de la lista opcion
        print('''
        ************************************************
        * Bienvenido a nuestro Sistema de Conductores. *
        ************************************************
        ''')
        ingreso_operarios = int(input('Por favor, Ingresa un N° de Operario: '))
        indice = ingreso_operarios - 1 #declaramos indice para hacer mas rapida la escritura
        if ingreso_operarios in operarios: #evaluamos si la repuesta está dentro de la lista operarios "evaluamos si es operario"
            clave_real = claves_operarios[indice] #buscamos la clave que le corresponde al operario
            clave_ingresada = input(f'Por favor operario {ingreso_operarios}, ingresa tu clave: ')
            while clave_ingresada != clave_real: #si la clave no coincide
                print(f'Error en el ingreso de la clave. Intenta nuevamente') #muestra error por pantalla
                print(f'Intento n°{intento}') #muesta el n° de intentos
                clave_ingresada = input(f'Por favor operario {ingreso_operarios}, ingresa tu clave: ') #vuelve a preguntar la clave
                intento += 1 #suma 1 intento
                if intento == 4: #si se llega al cuarto intento
                    raise Exception('Se registraron 4 intentos fallidos. Por tu seguridad se bloqueó el programa.') #provocaremos un error con ayuda de raise
            if clave_ingresada == clave_real: #si la clave coincide
                print(f'Bienvenido operario {ingreso_operarios}.') #saluda
                while True:
                    orden = int(input('Ingresa el número de Orden: ')) #pide n° de orden
                    orden_copia = orden #se hace una copia para no perder el valor original dado por el usuario
                    c = 0 #variable contador
                    while orden > 0: #mientras orden sea mayor a 0
                        orden = orden // 10 #se dividirá el número entre 10
                        c += 1 #se sumará 1 a contador cada vez que sea posible dividir orden entre 10
                    if c == 8:
                        # si contador llega exactamente a 8 imprime el numero en pantalla y termina el bucle
                        print(f'Se registró correctamente el número de orden: {orden_copia}')
                        break
                    else:
                        print('El número ingresado debe tener una longitud de 8 digitos.')
                while True:
                    mes = int(input('Ingresa el mes: '))
                    if mes > 0 and mes < 13:
                        print('Mes registrado correctamente.')
                        break
                    else:
                        print('Debe ingresar un valor entre 1 y 13.')
                while True:
                    dia = int(input('Ingresa el dia: '))
                    if mes == 2:
                        print('Mes de febrero tiene menos dias')
                        if dia > 0 and dia < 29:
                            print('Dia registrado correctamente.')
                            break
                        else:
                            print('Debe ingresar un valor entre 1 y 28.')
                    else:
                        if dia > 0 and dia < 32:
                            print('Dia registrado correctamente.')
                            break
                        else:
                            print('Debe ingresar un valor entre 1 y 31.')
                while True:
                    año = int(input('Ingresa el año: '))
                    if año > 2022 and año < 2025:
                        print('Año registrado correctamente.')
                        break
                    else:
                        print('Debe ingresar un valor entre 2023 y 2024.')
                print(f'{dia}-{mes}-{año}')
                while True:
                    kms = int(input('Ingrese los kilometros que recorrerá en la ruta: '))
                    if kms > 0:
                        kms_base_datos[indice] = kms
                        print('Kilometros registrados correctamente.')
                        break
                    else:
                        print('Ingresar valor mayor a 0.')
                while True:
                    petroleo = int(input('Ingrese los litros de petroleo que gastará en la ruta: '))
                    if petroleo > 0:
                        petroleo_base_datos[indice] = petroleo
                        print('Litros registrados correctamente.')
                        break
                    else:
                        print('Ingresar valor mayor a 0.')
                while True:
                    hr_usuario = int(input('Ingresar la hora de inicio: '))
                    if hr_usuario >= 0 and hr_usuario <= 24:
                        hr_inicio[indice] = hr_usuario
                        break
                while True:
                    min_usuario = int(input('Ingresar los minutos de la hora de inicio: '))
                    if min_usuario >= 0 and min_usuario <= 60:
                        min_inicio[indice] = min_usuario
                        break
                print(f'{hr_inicio[indice]}:{min_inicio[indice]}')
                while True:
                    hr_usuario = int(input('Ingresar la hora de termino: '))
                    if hr_usuario >= 0 and hr_usuario <= 24:
                        hr_final[indice] = hr_usuario
                        break
                while True:
                    min_usuario = int(input('Ingresar los minutos de la hora de termino: '))
                    if min_usuario >= 0 and min_usuario <= 60:
                        min_final[indice] = min_usuario
                        break
                print(f'{hr_final[indice]}:{min_final[indice]}')
                print('''
                **************************************************
                * Datos confirmados. Volviendo al menú principal *
                **************************************************
                ''')
    elif pregunta in opcion[1]:
        print('''
                ************************************************
                * Bienvenido a nuestro Sistema de Conductores. *
                ************************************************
                ''')
        n_supervisor = input('Ingresa tu nombre de supervisor:')
        if n_supervisor in supervisores:
            clave_ingresada = input(f'Por favor {n_supervisor} ingresa tu contraseña: ')
            while clave_ingresada != clave_supervisores:
                print(f'Error en el ingreso de la clave. Intenta nuevamente')
                print(f'Intento n°{intento}')
                clave_ingresada = input(f'Por favor {n_supervisor} ingresa tu contraseña: ')
                intento += 1
                if intento == 4:
                    raise Exception('Se registraron 4 intentos fallidos. Por tu seguridad se bloqueó el programa.')
            if clave_ingresada == clave_supervisores:
                while 0 in kms_base_datos:
                    kms_base_datos.remove(0)
                total_kms = sum(kms_base_datos)
                while 0 in petroleo_base_datos:
                    petroleo_base_datos.remove(0)
                total_p = sum(petroleo_base_datos)
                hr_inicio_ceros = hr_inicio
                while 0 in hr_inicio_ceros:
                    hr_inicio_ceros.remove(0)
                c = sum(hr_inicio_ceros)
                d = len(hr_inicio_ceros)
                hr_i_p = round(c/d)
                hr_final_ceros = hr_final
                while 0 in hr_final_ceros:
                    hr_final_ceros.remove(0)
                c = sum(hr_final_ceros)
                d = len(hr_final_ceros)
                hr_f_p = round(c/d)
                min_inicio_ceros = min_inicio
                while 0 in min_inicio_ceros:
                    min_inicio_ceros.remove(0)
                c = sum(min_inicio_ceros)
                d = len(min_inicio_ceros)
                min_i_p = round(c/d)
                min_final_ceros = min_final
                while 0 in min_final_ceros:
                    min_final_ceros.remove(0)
                c = sum(min_final_ceros)
                d = len(min_final_ceros)
                min_f_p = round(c / d)
                print(
                    f'{total_kms} kms recorridos por todos los operarios. \n {total_p} Petroleo gastado por todos los operarios.')
                print(f'El promedio de hora de inicio de los operarios es: {hr_i_p}:{min_i_p}. y el promedio de hora de termino es: {hr_f_p}:{min_f_p}')
                especifico = input('Desea ver a un operario en especifico? si/no: ')
                especifico.lower()
                if especifico == 'si':
                    while detener != 2:
                        ingreso_operarios = int(input('Ingrese el número del operario: '))
                        indice = ingreso_operarios - 1
                        print(f'El operario {ingreso_operarios} \n Recorrió {kms_base_datos[indice]} kms. \n Gastó {petroleo_base_datos[indice]} lts de petroleo.')
                        print(f'Comenzó a conducir al rededor de las {hr_inicio[indice]}:{min_inicio[indice]}.')
                        print(f'Terminó a conducir al rededor de las {hr_final[indice]}:{min_final[indice]}.')
                        continuar = input('Deseas ver otro operario? si/no: ')
                        continuar = continuar.lower()
                        if continuar == 'si':
                            pass
                        elif continuar == 'no':
                            detener = 2
                otras_opciones = input('Desea agregar a un nuevo operario?: si/no ')
                otras_opciones = otras_opciones.lower()
                if otras_opciones == 'si':
                    nuevo_operario = int(input('Ingrese a un nuevo operario: '))
                    operarios.append(nuevo_operario)
                    print(operarios)
                    nueva_clave = input(f'Ingresa la clave para el operario {nuevo_operario}')
                    claves_operarios.append(nueva_clave)
                    kms_base_datos.append(0)
                    petroleo_base_datos.append(0)
                    hr_inicio.append(0)
                    hr_final.append(0)
                    min_inicio.append(0)
                    min_final.append(0)
                menu = input('Deseas cerrar sesión? si/no: ')
                menu = menu.lower()
                if menu == 'si':
                    detener = 1
                    break
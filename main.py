import csv
from datetime import date,datetime,timedelta
from tabulate import tabulate
usuario = input("Ingrese su usuario administrador: ")
contrasena = int(input("ingrese su contraseña: "))

with open('usuarios.csv',mode='r',newline='' ) as usuarios:
    lector = csv.DictReader(usuarios)
    for i in lector:
        usuario_interno = i['usuario']
        contrasena_interna = int(i['contrasena'])

if usuario == usuario_interno:
    if contrasena == contrasena_interna:
        print("login exitoso")
        inicio_sesion = True
        
    else:
        print("contraseña erronea")
else:
    print("Usuario no existe")

while inicio_sesion:
    print(f"Bienvenido: {usuario} ")
    print("Menu")
    print("1.Registrar empleados")
    print("2.Gestionar empleados")
    print("3.Registrar solicitud vacaciones")
    print("4.Salir")
    menu = input("ingrese una opcion (1,2 o 3): ")

    match (int(menu)):
        case 1:
            id_empleado = int(input("ingrese el ID del empleado: "))
            nombre = input("ingrese el nombre y apellidos del empleado: ")
            cargo = input(f"ingrese cargo del empleado:  {nombre}: ")
            area = input(f"ingrese el area del empleado:  {nombre}: ")
            fecha_inicio_contrato = input("ingrese feha de inicio de contrato (YYYY-MM-DD)")

            nuevo_empleado = {
                "empleado_id": id_empleado,
                "nombre_completo":nombre,
                "cargo":cargo,
                "area": area,
                "fecha_inicio_contrato":fecha_inicio_contrato


            }

            with open('empleados.csv',mode='a', newline='',encoding='utf-8') as empleados:
                writer = csv.DictWriter(empleados,fieldnames=['empleado_id','nombre_completo','cargo','area','fecha_inicio_contrato'])
                writer.writerow(nuevo_empleado)
            print("registro exitoso ")
        
        case 2:
            with open('empleados.csv',mode='r',newline='',encoding='utf-8') as empleados:
                lector = csv.DictReader(empleados)
                lista_empleados = list(lector)
            print(tabulate(lista_empleados, headers="keys",tablefmt="grid"))
            menu_empleado = input("ingrese el id de empleado a gestionar: ")
            for i in lista_empleados:
                x = i['empleado_id']
                if x == menu_empleado:
                   empleado_seleccion = i
                   print(empleado_seleccion)
                else:
                    continue


                     
            
        

            
        case 3:

            inicio_contrato = datetime.strptime(empleado_seleccion['fecha_inicio_contrato'], "%Y-%m-%d").date()

            hoy = date.today()
            meses = (hoy.year - inicio_contrato.year)* 12
            if meses<6:
                print("no cuenta con el suficiente tiempo para vacaciones")
            else:

                dias_de_vacaciones = (meses*1.5)
                print(f"cuentas con {dias_de_vacaciones} dias de vacaciones")
                solicitud = int(input("cuantos dias de vacaciones solicita: "))
                fecha_inicio_vacaciones = (input("que fecha va a empezar las vacaciones: "))

                fecha = datetime.strptime(fecha_inicio_vacaciones,"%Y-%m-%d").date()
                contador = 0
                while contador <solicitud:
                    fecha += timedelta(days=1)
                    if fecha.weekday()<5:
                        contador += 1
                        estado = "PENDIENTE"
                print(f"fecha final: {fecha}")
                mes_fecha_final = fecha.month
                anio_fecha_final = fecha.year
                nuevas_vacaciones = {
                    "empleado_id": empleado_seleccion['empleado_id'],
                    "nombre_completo": empleado_seleccion['nombre_completo'],
                    "fecha_inicio_vacaciones":fecha_inicio_vacaciones,
                    "fecha_fin_vacaciones":fecha,
                    "dias_calculados": solicitud,
                    "estado": estado,
                    "mes": mes_fecha_final,
                    "anio": anio_fecha_final


                }
                with open('vacaciones.csv',mode='a', newline='',encoding='utf-8') as vacaciones:
                    writer = csv.DictWriter(vacaciones,fieldnames=['empleado_id','nombre_completo','fecha_inicio_vacaciones','fecha_fin_vacaciones','dias_calculados','estado','mes','anio'])
                    writer.writerow(nuevas_vacaciones)
                
                apro_recha = input("desea visualizar solicitud pendientes de aprobacion o rechazo ? (Y/N)")
                if apro_recha == "Y" or "y":
                    with open('vacaciones.csv',mode='r',newline='' ) as usuarios:
                        lector = csv.DictReader(usuarios)
                        pendientes = []
                        for i in lector:
                            if i['estado'] == "PENDIENTE":
                                pendientes.append(i)
                        print(tabulate(pendientes, headers="keys",tablefmt="grid"))
                        cambio = input("desea cambiar el estado de alguna solicitud (Y/N): ")
                        if cambio == "Y" or "y":
                            print(tabulate(pendientes, headers="keys",tablefmt="grid"))
                            id_cambio = int(input("ingrese el id de la solicitud a cambiar: "))
                            for i in pendientes:
                                cambio_interno = (i['empleado_id'])
                                if id_cambio == int(cambio_interno):
                                    print("1.aprobada")
                                    print("2.rechazada")
                                    nuevo_estado = input("seleccione opcion (1 o 2): ")
                                    if nuevo_estado == "1":
                                        nuevo_estado = "APROBADA"
                                    elif nuevo_estado == "2":
                                        nuevo_estado = "RECHAZADA"
                                    else:
                                        print("opcion invalida")
                                    
                                    with open('vacaciones.csv', mode='r',encoding='utf-8') as vacas:
                                        lector = csv.DictReader(vacas)
                                        lista_vacas = list(lector)

                                    for i in lista_vacas:
                                        if int(i['empleado_id']) == id_cambio and i["estado"] == "PENDIENTE":
                                            i['estado'] = nuevo_estado

                                    with open('vacaciones.csv', mode='w', newline='', encoding='utf-8') as vacas:
                                        writer = csv.DictWriter(vacas, fieldnames=lista_vacas[0].keys())
                                        writer.writeheader()
                                        writer.writerows(lista_vacas)
                                    break

                                    
                              
                                    
                                    
            

                            
                                        


                                    
                                

                


                        # print(tabulate(lista_vacas, headers="keys",tablefmt="grid"))

                    
                else:
                    continue




           
            # with open('vacaciones.csv', mode='r',newline='',encoding='utf-8') as vacaciones:
            #     lector = csv.DictReader(vacaciones)
            #     lista_vaciones = list(lector)
            #     for i in lista_vaciones:
            #         y = (i['empleado_id'])
            #         if y == id_empleado_seleccion:
            #             print(lista_vaciones[int(y)-1])
                    
               
              
                    

          

                    

        case 4:
            print("hasta luego")
            exit()




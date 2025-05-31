import os
clear = lambda: os.system('cls')
opcion = ""
sub_opcion = ""
modificar_opcion = ""
flag = 1
flag_nombre = 1
flag_apellido = 1
flag_edad = 1
flag_correo = 1
flag_direccion = 1
flag_plan = 1
modificar_elemento = 0
cliente_indice_eliminado = 0
#Creo un diccionario para el menu
menu = {'1':"Nuevo Usuario",
        '2':"Modificar Usuario",
        '3':"Eliminar Usuario",
        '4':"Mostrar",
        '5':"Salir"
          }
#Creo un diccionario para el menu plan
plan = {'1':"300 MEGAS - $77740",
        '2':"600 MEGAS - $82000",
        '3':"1000 MEGAS -$90090"
}
#Creo un diccionario para el menu modificar
modificar = {'1':"Nombre",
             '2':"Apellido",
             '3':"Edad",
             '4':"Direccion",
             '5':"Correo",
             '6':"Plan"
} 
clientes = []
cliente1 = ["Josue","Carata","21","Caracas4959","caratajosue@gmail.com","300 MEGAS - $77740"]
cliente2 = ["Norma","Aguirre","28","Nicaragua451","normaaguirre@gmail.com","1000 MEGAS - $90090"]
cliente3 = ["Sasha","Aguirre","30","Bogota3212","sasha@gmail.com","600 MEGAS - $82000"]
cliente4 = ["Gustavo","Lopez","41","Florida4512","gustavo@gmail.com","300 MEGAS - $77740"]
clientes.append(cliente1)
clientes.append(cliente2)
clientes.append(cliente3)
clientes.append(cliente4)
while (opcion != "5"):
    print("=" * 80)
    print(" " * 25,"ENOD Telefonia 📞📶- CRUD")
    print("-" * 80)
    print("=" * 80)   
    print("Seleccione una opción ")
#Valida que la opcion ingresada sea la correcta       
    for opcion in menu:
        print(f"{opcion}) {menu[opcion]}")
    while (opcion := input('Opción: ')) not in menu:
        print('Opción incorrecta, vuelva a intentarlo.')
    match opcion:
        case "1":
            flag = 1
            print("*" * 20,"Registro de Cliente🔛➕","*" * 20)            
            while ( flag != 0):
                nombre  = input("Nombre: ").strip().capitalize()
#Valida que el nombre ingresado sea caracter y que no sea vacio
                while(nombre.isalpha()==False or nombre ==""):
                    if(flag_nombre == 1):
                        nombre = input("Vuelva a ingresar nombre: ").strip().capitalize()
                apellido = input("Apellido: ").strip().capitalize()
#Valida que el apellido ingresado sea caracter y que no sea vacio                
                while(apellido.isalpha() == False or apellido == ""):
                    if(flag_apellido == 1 ):
                        apellido = input("Vuelva a ingresar el apellido: ").strip().capitalize()
                edad = input("Ingrese edad: ")
#Valida que sea numero                
                while(edad.isdigit() == False):
                    if(flag_edad == 1):
                        edad = input("Vuelva a ingresar la edad: ")                    
                direccion = input("Direccion: ").strip().capitalize()
#Valida que la direccion sea caracter y numero, no se me ocurrio como validar con espacio por eso las direcciones se escribe todo junto                
                while(direccion.isalnum() == False): 
                    if(flag_direccion == 1):
                        direccion = input("Vuelva a ingresar direccion: ").strip().capitalize()
                correo = input("Ingrese Email: ").strip().lower()
#Valida que el correo tengo un @ y que no sea vacio
                while(correo.count("@") != 1 and " " not in correo):
                    if(flag_correo == 1):
                        correo = input("Vuelva a ingresar el correo: ").strip().lower()                        
                print("Plan y precio")
                while (sub_opcion != "4"):
                    for sub_opcion in plan:
                        print(f"{sub_opcion}) {plan[sub_opcion]}")
                    while (sub_opcion := input('Opción: ')) not in plan:
                        print('Opción incorrecta, vuelva a intentarlo.')
                    match sub_opcion:
                        case "1":
                            print("Listo plan elejido")
                            plan_selecionado = "300 MEGAS - $77740"
                            break    
                        case "2":
                            print("Listo plan elejido")
                            plan_selecionado = "600 MEGAS - $82000"
                            break
                        case "3":
                            print("Listo plan elejido")
                            plan_selecionado = "1000 MEGAS - $90090"
                            break
                        case "4":
                            print("Gracias por elejir el plan")
#Ingresa todos los datos en una lista cliente                                           
                cliente = [nombre,apellido,edad,direccion,correo,plan_selecionado]
#Ingresa la lista cliente en la lista clientes                
                clientes.append(cliente)
                respuesta = input("Desea Agregar otro cliente: S/N ").lower()
                while(respuesta.isalpha() == False):
                    respuesta = input("Error. Desea agregar otro cliente : S/N ").lower()
                if(respuesta == "n"):
                    flag = 0
            clear()           
        case "2":
            print("-"*70,"ACTUALIZAR USUARIO","-"*70)
#Imprimi los clientes            
            for i, cliente in enumerate(clientes, 1):
                nombre , apellido , edad , direccion , correo , plan_selecionado = cliente #asignación múltiple
                print(f"{i}) |Nombre: {nombre}\t |Apellido: {apellido}\t |Edad: {edad}\t |Direccion: {direccion}\t |Email: {correo}\t |Plan: {plan_selecionado}")      
#Elije el indice y lo guardo             
            modificar_elemento = int(input("Cual desea modificar elija el indice: "))
            clear()
            print("*"*70,"CLIENTE A MODIFICAR","*"*70)
#Creo un cliente donde guardo el cliente a modificar
#modificar_elemento es un indice y le resto 1             
            cliente_modificar = clientes[modificar_elemento-1]
            nombre , apellido , edad , direccion , correo , plan_selecionado = cliente_modificar #asignacion multiple
#Imprimo el cliente a modificar            
            print(f"{modificar_elemento}) |Nombre: {nombre}\t |Apellido: {apellido}\t |Edad: {edad}\t |Direccion: {direccion}\t |Email: {correo}\t |Plan: {plan_selecionado}")
            print(" "*70,"ELIJA UNA OPCION: ")
            print("-"*160)
#Imprimo por pantalla el menu modificar           
            for modificar_opcion in modificar:
                print(f"{modificar_opcion}) {modificar[modificar_opcion]}")
            while (modificar_opcion := input('Opción: ')) not in modificar:
                print('Opción incorrecta, vuelva a intentarlo.')
            match modificar_opcion:
                case '1':
#Modifico el cliente en la poscion que es este caso es el Nombre                    
                    cliente_modificar[0] = input("Ingrese el nuevo nombre: ").strip().capitalize()
                    while(cliente_modificar[0].isalpha()==False or cliente_modificar[0] ==""):
                        if(flag_nombre == 1):
                            cliente_modificar[0] = input("Vuelva a ingresar nombre: ").strip().capitalize()
                    clear()                
                case '2':
                    cliente_modificar[1] = input("Ingrese el nuevo apellido:").strip().capitalize()
                    while(cliente_modificar[1].isalpha()==False or cliente_modificar[1] ==""):
                        if(flag_apellido == 1):
                            cliente_modificar[1] = input("Vuelva a ingresar nombre: ").strip().capitalize()
                    clear()                                   
                case '3':
                    cliente_modificar[2] = input("Ingrese la nueva Edad: ")
                    while(cliente_modificar[2].isdigit() == False):
                        if(flag_edad == 1):
                            cliente_modificar[2] = input("Vuelva a ingresar la edad: ")
                    clear()        
                case '4':
                    cliente_modificar[3] = input("Ingrese la nueva Direccion: ").strip().capitalize()
                    while(cliente_modificar[3].isalnum() == False): 
                        if(cliente_modificar[3] == 1):
                            cliente_modificar[3] = input("Vuelva a ingresar direccion: ").strip().capitalize()                    
                    clear()                
                case '5':
                    cliente_modificar[4] = input("Ingresa el nuevo Correo: ").strip().lower()
                    while(cliente_modificar[4].count("@") != 1 and " " not in cliente_modificar[3]):
                        if(flag_correo == 1):
                            cliente_modificar[4] = input("Vuelva a ingresar el correo: ").strip().lower()
                    clear()                
                case '6':
                    while (sub_opcion != "4"):
                        for sub_opcion in plan:
                            print(f"{sub_opcion}) {plan[sub_opcion]}")
                        while (sub_opcion := input('Opción: ')) not in plan:
                            print('Opción incorrecta, vuelva a intentarlo.')
                        match sub_opcion:
                            case "1":
                                print("Listo plan elejido")
                                cliente_modificar[5] = "300 MEGAS - $77740"
                                break    
                            case "2":
                                print("Listo plan elejido")
                                cliente_modificar[5] = "600 MEGAS - $82000"
                                break
                            case "3":
                                print("Listo plan elejido")
                                cliente_modificar[5] = "1000 MEGAS - $90090"
                                break                                                                                  
                    clear()
        case "3":
            print("*"*70,"CLIENTE A ELIMINAR","*"*70)
            flag = 1
#Utilizo la bandera en el bucle while            
            while(flag != 0):
#Imprimo la lista de cliente                
                for i, cliente in enumerate(clientes, 1):
                    nombre , apellido , edad , direccion , correo , plan_selecionado = cliente #asignación múltiple
                    print(f"{i}) |Nombre: {nombre}\t|Apellido: {apellido}\t|Edad: {edad}\t|Direccion: {direccion}\t|Email: {correo}\t|Plan: {plan_selecionado}|")
                cliente_indice_eliminado = int(input("Ingrese el indice del cliente a eliminar: "))
                
                if (cliente_indice_eliminado <= len(clientes)):
                    cliente_eliminado = clientes[cliente_indice_eliminado-1]
                    nombre , apellido , edad , direccion , correo , plan_selecionado = cliente_eliminado
                    print(f"Cliente a Eliminar\n{cliente_indice_eliminado})Nombre:{nombre}-Apellido:{apellido}-Edad:{edad}-Direccion:{direccion}-Email:{correo}-Plan:{plan_selecionado}")
                    flag_eliminar = 1            
                else:
                    print("Fuera de rango")
                    flag_eliminar = 0
                if(flag_eliminar == 1):    
                    respuesta = input("Esta seguro de eliminar el cliente: S/N" ).lower()
                    while(respuesta.isalpha() == False):
                        respuesta = input("Error. Desea agregar otro cliente : S/N ").lower()
                    if(respuesta == "s"):
                        clientes.pop(cliente_indice_eliminado-1)
                        print("Se Elimino cliente!!!!!")
                        flag = 0
        case "4":
            clear()
            print("*"*70,"LISTA DE CLIENTES","*"*70) 
            for i, cliente in enumerate(clientes, 1):
                nombre , apellido , edad , direccion , correo , plan_selecionado = cliente #asignación múltiple
                print(f"{i}) |Nombre: {nombre}\t|Apellido: {apellido}\t|Edad: {edad}\t|Direccion: {direccion}\t|Email: {correo}\t|Plan: {plan_selecionado}|")
        case "5":
            print("Gracias por utilizar ENOD-Telefonia")
            break
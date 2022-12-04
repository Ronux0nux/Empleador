from EmpleadorClass import *
empleador=None
while True:
    
    print("\n\n Menu \n")
    print("1. agregar empleador")
    print("2. modificar los datos del usuario")
    print("3. ver datos del usuario")
    print("salir")
    opcion=input("selecciona una opcion:")
    
    if (opcion == "1"):
        print("\nescriba los datos basicos del empleador: (no se podran modificar)\n")
        id_employee = input("id empleador:\n")
        fullname = input("nombre completo: \n")
        salary= input("salario:")
        empleador= EmpleadorClass(id_employee,fullname,job,salary)
    
    elif (opcion == "2"):
        while True:
                print("\n///menu para modificar///\n")
                print("\n 1° actualizar id de empleador")
                print("\n 2° actualizar nombre de empleador")
                print("\n 3° actualizar trabajo del empleador")
                print("\n 4° actualizar salario")
                print("\n 5° regresar al menu")
                opcion2 = input("selecciona una opcion")
                if (opcion2 == "1"):
                    id_employee = input("id del empleador")
                    empleador.setId_employee(id_employee)
                elif(opcion == "2"):
                    fullname = input("nombre del empleador")
                    empleador.setFullname(fullname)
                elif(opcion2 == "3"):
                    job = input("trabajo")
                    empleador.setJob(job)
                elif (opcion == "4"):
                    salary = input("salario")
                    empleador.setSalary(salary)
                elif(opcion == "5"):
                    break
                else:
                    print("opcion no valida")
                    
    elif (opcion == "3"):
        print("\n\n datos del empleador" )
        print("Id del empleador" + str(empleador.getId_employee()))
        print("nombre del empleador" + empleador.getFullname())
        print("trabajo del empleador" + empleador.Job())
        print("salario" + str(empleador.getSalary()))
        
    elif (opcion == "4"):
        print("adios")
        break
    else:
            print("opcion no valida")
            
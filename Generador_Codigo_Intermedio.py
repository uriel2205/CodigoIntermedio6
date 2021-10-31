import re

print("===================================================================")
print("================== SELECCIONE UNA OPCION ==========================")
print("===================================================================")
print("1: X = 2 + 5 * y") 
print("2: X = a / a + b * b") 
print("3: X = (a + 2) / 3 + b")
print("4: X = (a + 2) / (3 - b)")
print("5: X = 2 * y - ((4 * y) + z)")
x=int(input("Seleccione una opcion: "))

#LOS CASOS SON SIN REGEX SOLO CON LISTAS, POR ESO, SE TRABAJA SOLO CON UN DIGITO O UN SOLO CARACTER
#===================================================================================================================
if x==1:
    #CASO UNO SIN USO DE REGEX, CON LISTAS.
    p = []
    vs = []
    valor =open("Ejemplo 1.txt").read()#LEEMOS EL ARCHIVO
    suma = -1
    for i in valor:#RECORREMOS LA CADENA INGRESADA
        if i != " ":#SI LA CADENA ES DIFERENTE A UN CONJUNTO VACIO
            p.append(i)#AÑADIMOS LA CADENA INGRESADA A LA LISTA P
#==========================================================================
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA LISTA P VAN DESGLOZANDO LA EXPRESION EN PARTES
            p.remove(p[suma]) # SE ELIMINA "*"
            p.remove(p[suma-1]) #SE ELIMINA EL "5"
            p.remove(p[suma-1]) #SE ELIMINA EL "Y"
    print(temporalCero)
#==========================================================================
    temporalUno = ""
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA 
            if p[-1] == "+" or p[-1]=="-":
                temporalUno = "_t1 = "+ p[-2] + " "+ p[-1] + " " +"_t0"    
            else:
                temporalUno = "_t1 = "+ p[-1] + " "+ p[-2] + " " +"_t0"
    p.remove(p[-1])
    p.remove(p[2])
    print(temporalUno)
#==========================================================================  
    igualdad = ""
    for i in p:
        if i == "x" or "X":
            igualdad = p[0] +" "+ p[1] + " _t1"
    print(igualdad)
#===================================================================================================================
elif x==2:
    p = []
    vs = []
    valor = open("Ejemplo 2.txt").read()
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)   
#==========================================================================
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break 
        else: 
                if i == "/":
                    temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]
                    p.remove(p[suma-1])
                    p.remove(p[suma])
                    p.remove(p[suma-1])
                    break      
    print(temporalCero)
#==========================================================================
    temporalUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 temporalUno = "_t1 = " + p[suma-5] + " " +  p[suma-4] + " " + p[suma-3] 
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    temporalUno = "_t1 = " + p[suma-3] + " " +  p[suma-2] + "_t0"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalUno = "_t1 = " + p[suma] + " " +  p[suma+1] + " " + p[suma+2]   
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalUno = "_t1 = _t0 " + p[suma-1] + " " +  p[suma] 
    print(temporalUno)
#==========================================================================
    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*":
                 temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-4] + " " + temporalUno[0:3]
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    temporalDos = "_t2 = " + p[suma-5] + " " +  p[suma-4] + "_t1"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-1] + " " + temporalUno[0:3]  
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalDos = "_t1 = _t0 " + p[suma+1] + " " +  p[suma+2]
    print(temporalDos)
#==========================================================================
    igualdad = ""    
    for i in p:
        if i == "x" or "X":
            igualdad = p[0] +" "+ p[1] + " _t2"   
    print(igualdad)
#======================================================================================================
elif x==3:
    p = []
    vs = []
    valor = open("Ejemplo 3.txt").read()
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
#=============================================================================
    temporalCero = ""
    for i in p: 
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
#=============================================================================
    temporalUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[4] == "(" :
                temporalUno = "_t1 =" + " _t0 "  + p[suma-5] + " " +  p[suma-6] + " " 
            else:
                temporalUno = "_t1 = " + " _t0 " + p[suma-3] + " " +  p[suma-2] + " "
#=============================================================================
    temporalDos = ""
    for i in p:
        if i == "+" or i == "-": 
            if p[4] == "(" :
                temporalDos = "_t2 = " + " _t1 " + p[suma-7] + " " +  p[suma-8] + " " 
            else:
                temporalDos = "_t2 = " + " _t1 " + p[suma-1] + " " + p[suma] + " " 
    print(temporalCero)
    print(temporalUno)
    print(temporalDos)
#=============================================================================
    igualdad = ""
    for i in p:
        if i == "x" or "X":
            igualdad = p[0] + " " + p[1] + "_t2"
    print(igualdad)
#===================================================================================================================
elif x==4:
    p = []
    vs = []
    valor = open("Ejemplo 4.txt").read()
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    igualdad = ""
    for i in p:
        suma +=1
        if i == "x" or "X":
            igualdad = p[suma-12] + " " + p[suma-11] + " _t3"
    p.remove(p[suma-11])
    p.remove(p[suma-12])
#=============================================================================   
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-15] + " " + p[suma-14] + " " +  p[suma-13] + " " + p[suma-12] + " " + p[suma-11]
            p.remove(p[suma-11])
            p.remove(p[suma-12])
            p.remove(p[suma-13])
            p.remove(p[suma-14])
            p.remove(p[suma-15])
            break 
        else: 
                if i == "+" or i=="-":
                    temporalCero = "_t0 = " + p[suma-15] + " " + p[suma-14] + " " +  p[suma-13] + " " + p[suma-12] + " " + p[suma-11]
                    p.remove(p[suma-11])
                    p.remove(p[suma-12])
                    p.remove(p[suma-13])
                    p.remove(p[suma-14])
                    p.remove(p[suma-15])
                    break      
    print(temporalCero)
#============================================================================================================================
    temporalUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            try:
                temporalUno = "_t1 = " + p[suma-15] + " " + p[suma-14] + " " +  p[suma-13] + " " + p[suma-12] + " " + p[suma-11] 
                p.remove(p[suma-11])
                p.remove(p[suma-12])
                p.remove(p[suma-13])
                p.remove(p[suma-14])
                p.remove(p[suma-15])
            except:
                IndexError: temporalUno = 'null'
                print("===============================================================================")
                print("ERROR")
                print("caso invalido")
                print("===============================================================================")
            break 
        else: 
                if i == "+" or i=="-":
                        try:
                            temporalUno = "_t1 = " + p[suma-15] + " " + p[suma-14] + " " +  p[suma-13] + " " + p[suma-12] + " " + p[suma-11] 
                            p.remove(p[suma-11])
                            p.remove(p[suma-12])
                            p.remove(p[suma-13])
                            p.remove(p[suma-14])
                            p.remove(p[suma-15])
                        except:
                            IndexError: temporalUno = 'null'
                            print("===============================================================================")
                            print("ERROR")
                            print("caso invalido")
                            print("===============================================================================")
                        break
    print(temporalUno)
#================================================================================
    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-18] + " " + temporalUno[0:3]
            break 
        else: 
                if i == "+" or i=="-":
                    temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-18] + " " + temporalUno[0:3]
                    break      
    print(temporalDos)
    print(igualdad)
#================================================================================================================
elif x==5:
    p = []
    S = []
    TC= []
    valor = open("Ejemplo 5.txt").read()
    suma = -1
    suma2 = -1
    for i in valor:
        if i != " ":
            p.append(i)
    igualdad = ""
    for i in p:
        if i == "x" or "X":
            igualdad = p[0] + " " + p[1] + " _t3"
    p.remove("x" or "X")
    p.remove("=")
#================================================================================
    for i in p: 
        suma +=1
        if i =="(" or i ==")":
            if i =="(" or i ==")":
                p.remove(p[suma-13])
                TC.append(p[suma-12])
                p.remove(p[suma-12])
                TC.append(p[suma-11])
                p.remove(p[suma-11])
                TC.append(p[suma-10])
                p.remove(p[suma-10])
                TC.append(p[suma-9])
                p.remove(p[suma-9])
                TC.append(p[suma-8])
                p.remove(p[suma-8])
                TC.append(p[suma-7])
                p.remove(p[suma-7])
                TC.append(p[suma-6])
                p.remove(p[suma-6])
                p.remove(p[suma-5])
                break
#================================================================================
    temporalCero = ""
    for x in TC: 
        suma +=1
        if x =="(" or x ==")":
            if TC[0]=="(":
                temporalCero = "_t0 = " + TC[suma2-6] + " " +  TC[suma2-5] + " " + TC[suma2-4] + " " + TC[suma2-3] + " " + TC[suma2-2]
            else:
                temporalCero = "_t0 = " + TC[suma2-4] + " " +  TC[suma2-3] + " " + TC[suma2-2] + " " + TC[suma2-1] + " " + TC[suma2]
    print(temporalCero)
#================================================================================
    temporalUno = ""
    for x in TC: 
        suma2 +=1
        if x =="+" or x =="-" or x =="*" or x =="/":
            if TC[0]=="(":
                temporalUno = "_t1 = t0 "  + TC[suma2-7] + " " +  TC[suma2-6]  
            else:
                temporalUno = "_t1 = t0 "  + TC[suma2-3] + " " +  TC[suma2-4]      
    print(temporalUno)
#================================================================================
    temporalDos = ""
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalDos = "_t2 = " + p[0] +  " " + p[2] + " " + p[3]  
            break
        else:
            temporalDos = "_t2 = " + " " +p[0]  + " " + p[2] + " " + p[3] 
            break
    print(temporalDos)
#================================================================================
    temporalTres = ""
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalTres = "_t3 = " + temporalDos[0:3] +  " " + p[1] + " " + temporalUno[0:3]
            break
        else:
            temporalTres = "_t3 = " + temporalDos[0:3] +  " " + p[1] + " " + temporalUno[0:3]
            break
    print(temporalTres)
#================================================================================
    print(igualdad)
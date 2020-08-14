'''Un hombre desea saber cuanto dinero se genera por concepto de intereses sobre la
cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y
cuando estos excedan a $7000, y en ese caso desea saber cuanto dinero tendrá finalmente
en su cuenta.'''

print("Bienvenido, aqui podra calcular cuantos intereses generará su capital en el banco\n")
cap=float(input("Digite el capital que tiene en su banco:"))
p_int=float(input("Digite la tasa de interés del banco, ejm. 0.20 si la tasa es del 20%:  \n"))
inte=cap*p_int
if inte> 7000:
    capF= cap+ inte
    print(f"El dinero que genera por intereses es: {inte} y el dinero acumulado en total es: {capF:.1f}\n")

'''Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su
promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.'''
print("Conoce tu calificación final al digitar tus ultimas notas\n")
calif1=float(input("Ingrese la primera calificación en base a 5.0: "))
calif2=float(input("Ingrese la segunda calificación en base a 5.0: "))
calif3=float(input("Ingrese la tercera calificación en base a 5.0: "))
prom=(calif1+calif2+calif3)/3
if prom>=3.0:
    print("Alumno Aprobado!\n")
else:
    print("Alumno Reprobado!\n")

'''En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $1000
¿ Cual será la cantidad que pagara una persona por su compra?'''

print("Bienvenido obten un 20% de descuento en tu compra\n")
compra=float(input("Digite el monto de su compra: "))
if compra > 1000:
    desc=compra*0.20
else:
    print("No obtuvo ningún descuento")
tot_pag=compra-desc
print(f"El total de su compra es: {tot_pag} porque obtuvo un descuento de: {desc}")


'''Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
Si trabaja 40 horas o menos se le paga $16 por hora
Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y
$20 por cada hora extra.'''

print("Bienvenido, aqui podras saber cuanto ganas por horas trabajadas en  la semana\n")
ht=int(input("Digite en un formato de 12 horas cuantas horas has trabajado: "))
if ht > 40:
    hora_extra = ht - 40
    salSem= (hora_extra*20) + (40*16)
else:
    salSem= ht * 16
print(f"tu salario semanal es de: {salSem}")

#algoritmo que lea 2 numeros e imprima de forma ascendente

num1=int(input("Digite un numero: "))
num2=int(input("\nDigite otro numero: "))
if num1<num2:
    print(f"Esta es la forma ascendente: {num1},{num2}")
else:
    print(f"Esta es la forma ascendente: {num2},{num1}")

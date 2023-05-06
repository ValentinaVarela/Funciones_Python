#1. Crear una función que reciba un numero como parametro y devuelva true si es primo y false si no lo es
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


#2. Utilizando la funcion del punto 1, realizar otra funcion que reciba de parametro una lista de numeros y devuelva en una lista solo aquellos que son primos

#3. Crear una funcion que al recibir una lista de numeros devuelva el que mas se repite y cuantas veces lo hace, si hay mas de un "mas repetido", que devuelva cualquiera


def sumar(a, b):
        return a + b

def restar(a, b):
        return a - b

def multiplicar(a, b):
        return a * b

def dividir(a, b):
        if b == 0:
                raise ValueError("No se puede dividir entre 0")
                # raise ZeroDivisionError("No se puede dividir entre 0")
        return a / b


# -------- if else ------------
                # if b!= 0:
                #         return  a / b
                # else:
                #         print ("No se puede dividir entre cero")  


if __name__ == "__main__":
        print(sumar(5, 3))
        print(restar(5, 3))
        print(multiplicar(5, 3))
        print(dividir(9, 3))
import math

def bisseccao(f, a, b, epsilon):
    pm = (a+b)/2
    f_a = f(a)
    f_b = f(b)
    f_pm = f(pm)
    tol = abs(f_pm)
    print("a: %f   b: %f   Ponto médio: %f   f(a): %f   f(b): %f   f(pm): %f   Erro: %f" %(a, b, pm, f_a, f_b, f_pm, tol))
    i = 0
    while(tol > epsilon):
        print("Iteração %d" %i)
        if(f_a*f_pm > 0):
            a = pm
        elif(f_b*f_pm > 0):
            b = pm
        elif(f_pm == 0):
            print("Encontrada solução exata!\n")
            return(f_pm)
        else:
            print("Método falhou...\n")
            return None
        pm = (a+b)/2
        f_a = f(a)
        f_b = f(b)
        f_pm = f(pm)
        tol = abs(f_pm)
        print("a: %f   b: %f   Ponto médio: %f   f(a): %f   f(b): %f   f(pm): %f   Erro: %f" %(a, b, pm, f_a, f_b, f_pm, tol))
        i = i+1
    return (a+b)/2

def main():
    epsilon = 10**-2
    
    #Exercício 1.a.
    f_1a = lambda x: x-2**-x
    a_1a = 0
    b_1a = 1
    print("A raíz do exercício 1.a. é igual a: %f\n" %bisseccao(f_1a,a_1a,b_1a,epsilon))
    print("############################################################################\n")

    #Exercício 1.b.
    f_1b = lambda x: math.exp(x)-x**2+3*x-2
    a_1b = 0
    b_1b = 1
    print("A raíz do exercício 1.b. é igual a: %f\n" %bisseccao(f_1b,a_1b,b_1b,epsilon))
    print("############################################################################\n")

    #Exercício 1.c.
    f_1c = lambda x: 2*x*math.cos(2*x)-(x+1)**2
    a0_1c = -3
    b0_1c = -2
    print("A primeira raíz do exercício 1.c. é igual a: %f\n" %bisseccao(f_1c,a0_1c,b0_1c,epsilon))

    a1_1c = -1
    b1_1c = 0
    print("A segunda raíz do exercício 1.c. é igual a: %f\n" %bisseccao(f_1c,a1_1c,b1_1c,epsilon))
    print("############################################################################\n")

    #Exercício 1.d.
    f_1d = lambda x: x*math.cos(x)-2*x**2+3*x-1
    a0_1d = 0.2
    b0_1d = 0.3
    print("A primeira raíz do exercício 1.d. é igual a: %f\n" %bisseccao(f_1d,a0_1d,b0_1d,epsilon))

    a1_1d = 1.2
    b1_1d = 1.3
    print("A segunda raíz do exercício 1.d. é igual a: %f\n" %bisseccao(f_1d,a1_1d,b1_1d,epsilon))

    #Exercício a PROVA.
    f_prova_a = lambda x: x**4-3*x**3+x**2+x+1
    a_prova_a = 2
    b_prova_a = 2.5
    print("A raíz do exercício prova é igual a: %f\n" %bisseccao(f_prova_a,a_prova_a,b_prova_a,epsilon))
    print("############################################################################\n")


    #Exercício b PROVA
    f_prova_b = lambda x: x**4-3*x**3+x**2+x+1
    a_prova_b = 0.5
    b_prova_b = 1.5
    print("A raíz do exercício prova é igual a: %f\n" %bisseccao(f_prova_b,a_prova_b,b_prova_b,epsilon))
    print("############################################################################\n")

    input("Fim do programa. Pressione <enter> para fechar")
    return 0

main()

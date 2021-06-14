import math

def met_newton(f, fDer, chute, epsilon):
    f_chute = f(chute)
    fDer_chute = fDer(chute)
    tol = abs(f_chute)
    print("Chute inicial: %f   f(chute): %f   f´(chute): %f   Erro: %f" %(chute, f_chute, fDer_chute, epsilon))
    it = 1
    while(tol > epsilon):
        print("Iteração %d" %it)
        chute -= f_chute/fDer_chute
        print("Novo chute: %f" %chute)
        f_chute = f(chute)
        fDer_chute = fDer(chute)
        tol = abs(f_chute)
        it += 1
    return chute

def main():
    epsilon = 10**-5
    
    #Exercício a.
    f_a = lambda x: math.exp(x) + 2**-x + 2*math.cos(x) - 6
    fDer_a = lambda x: math.exp(x) - 2**-x*math.log(2) - 2*math.sin(x)
    chute_a = 2
    print("A raíz do exercício a. é igual a: %f\n" %met_newton(f_a, fDer_a, chute_a, epsilon))
    print("############################################################################\n")

    #Exercício b.
    f_b = lambda x: math.log(x-1) + math.cos(x-1)
    fDer_b = lambda x: 1/(x-1) - math.sin(x-1)
    chute_b = 1.3
    print("A raíz do exercício b. é igual a: %f\n" %met_newton(f_b, fDer_b, chute_b, epsilon))
    print("############################################################################\n")

    #Exercício c.
    f_c = lambda x: 2*x*math.cos(2*x) - (x-2)**2
    fDer_c = lambda x: -2*x - 4*x*math.sin(2*x) + 2*math.cos(2*x) + 4
    chute_c1 = 2
    chute_c2 = 4
    print("A primeira raíz do exercício c. é igual a: %f\n" %met_newton(f_c, fDer_c, chute_c1, epsilon))
    print("A segunda raíz do exercício c. é igual a: %f\n" %met_newton(f_c, fDer_c, chute_c2, epsilon))
    print("############################################################################\n")


main()

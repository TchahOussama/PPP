from math import *
def f(x):
    return exp(x)
def fp(y,pas):
    result = pas
    while f(result)<y:
        result = result + pas

    return result   
def djikstra(sommet, liaison, start): 
    chemin = []
    # Etape 1:
    ######################################
    s = start
    resul = {}
    W = [s]
    pi = {s:0}
    fct = lambda c: pi[c]
    for i in sommet:
        if i!=s:
            if (s,i) in liaison:
                pi[i] = liaison[(s,i)]
                resul[i] = s    
            else : 
                pi[i] = 10000000000000000000          
    # Main loop
    while len(W)!=len(sommet):  
        # Etape 2 : 
        #####################################
        T = sorted(pi, key = fct)
        nn = T[0]
        for i in range(len(T)):
            if T[i] not in W:
                if i<len(T)-1:
                    nn = T[i+1]
                    if nn != T[i]:
                        W.append(T[i])
                        s = T[i]
                        break
                if i==len(T)-1:
                    W.append(T[i])
                    s = T[i]
                    break    
        # Etape 3 : 
        #####################################
        for i in sommet:
            if i not in W:
                if (s,i) in liaison:
                    k = min(pi[i], pi[s]+liaison[(s,i)])
                    if k!=pi[i]:
                        resul[i] = s
                    pi[i] = k      
    a = len(sommet)-1
    chemin.append(a)
    while a!= start:
        prefix = resul[a]
        a = prefix
        chemin.append(a)
    chemin.reverse()
    print(chemin)      
    somme = 0
    for point in range(len(chemin)-1):
        somme = somme + liaison[(chemin[point],chemin[point+1])]
    print(somme)         
    return chemin      
if __name__ == "__main__":
    #simulation:
    alpha = 10
    T = 5
    C = 1
    gamma = []
    delta = 10
    taux = 0.05
    n =1
    ############## calcule de C:
    maxf = f(T)
    s_simulation = 0
    while n*C<maxf:
    
        n = n+1   
    ###########################
    print(n)
    input()    
    ############# fonction gamma         
    for b in range(n+1):
        gamma.append(alpha)
        alpha = alpha+0
    #############################    
    sommet_simulation = [i for i in range (0,n+1)]
    liaison_simulation  = {}
    t = [0]
    for j in range(1,len(sommet_simulation)):
        resulttt = fp(C*j,0.1)
        t.append(resulttt)
    for i in range (len(sommet_simulation)):
        for j in range (i+1, len(sommet_simulation)):
            b = (1+taux)**t[j]
            a = (delta + (j-i)*gamma[j])
            liaison_simulation[(i,j)] = a/b
    djikstra(sommet_simulation,liaison_simulation,s_simulation)            


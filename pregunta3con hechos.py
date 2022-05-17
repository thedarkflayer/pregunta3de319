# -*- coding: utf-8 -*-


from pyswip import Prolog
prolog = Prolog()

prolog.consult("hechos.pl")

    
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"], "es el abuelo de ",elemento["Y"])
    
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["Y"], "es el nieto de ",elemento["X"])
    
for elemento in prolog.query("primo(X,Y)"):
    print(elemento["X"], "es el primo de ",elemento["Y"])
    
for elemento in prolog.query("hermano(X,Y)"):
    print(elemento["X"], "es el hermano de ",elemento["Y"])
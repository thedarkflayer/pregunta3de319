# -*- coding: utf-8 -*-

from pyswip import Prolog
prolog = Prolog()

prolog.assertz("abuelo(jaime,ricardo)")
prolog.assertz("abuelo(jaime,tania)")
prolog.assertz("abuelo(jaime,luis)")
prolog.assertz("primo(tania,luis)")
prolog.assertz("primo(tania,ricardo)")
prolog.assertz("hermano(ricardo,luis)")

list(prolog.query("abuelo(jaime,X)"))==[{"X":"ricardo"},{"Y":"tania"},{"Z":"luis"}]
list(prolog.query("primo(tania,X)"))==[{"X":"luis"},{"Y":"ricardo"}]
    
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["X"], "es el abuelo de ",elemento["Y"])
    
for elemento in prolog.query("abuelo(X,Y)"):
    print(elemento["Y"], "es el nieto de ",elemento["X"])
    
for elemento in prolog.query("primo(X,Y)"):
    print(elemento["X"], "es el primo de ",elemento["Y"])
    
for elemento in prolog.query("hermano(X,Y)"):
    print(elemento["X"], "es el hermano de ",elemento["Y"])



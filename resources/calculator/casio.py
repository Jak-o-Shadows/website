# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:48:56 2011

@author: Jak_o_Shadows
"""


intro_en = """A couple of small programs i have made, using casio basic, for the casio fx-9860G
<br />"""

intro_eo = """Du malgranda programo mi skribis, uzi Casio Basic, por la Casio FX-9860G kalkulilo.
<br />"""

############################################################################################################
bezier_en = """Bezier calculates the coefficients of a bezier curve (in parametric form). Can also draw.
<br />
The code:
<br />
<img src="bezier.PNG" />
The file:
<br />
<a href = "BEZIER.G2M">bezier.g2m</a>
<br />
"""

bezier_eo = """Bezier kalkulas la koeficientoj de la bezier kurbo (en parametra formi). Povas aldone intrigo.
<br />
La kodo:
<br />
<img src="bezier.PNG" />
La dosiero:
<br />
<a href = "BEZIER.G2M">bezier.g2m</a>
<br />
"""
############################################################################################################
complex_en = """<br />
Complex is a program to perform complex number iterations. Complex mode must not be set to real.
<br />
The code
<br />
<img src = "complex.PNG" />
<br />
the file (maybe)
<br />
<a href = "COMPLEX.G2M">complex.g2m</a>
<br />
"""

complex_eo = """<br />
Complex elfaras ripetoj da la ekvacio z_{i+1} = z_{i}^2 + c, kie <em>c</em> estas konstanta, kaj z_{i} estas la ripeti. Utila por Mandlebrot kaj Julia serio.
<br />
The code
<br />
<img src = "complex.PNG" />
<br />
the file (maybe)
<br />
<a href = "COMPLEX.G2M">complex.g2m</a>
<br />
"""
############################################################################################################
euler_en = """
<br />
Euler is a program that does Euler's method.
<br />
<img src = "euler.PNG" />
<br />
<a href = "EULER.G2M">Euler.g2m</a>
<br />
"""

euler_eo = """
<br />
Euler kalkulas la solvajxo da la equation, utila Euler's Method.
<br />
<img src = "euler.PNG" />
<br />
<a href = "EULER.G2M">Euler.g2m</a>
<br />
"""
############################################################################################################
vectProduct_en = """
<br />
VectProd is a program that does the vector product of 2 3D vectors.
<br />
<img src = "vect_product.PNG" />
<br />
<a href = "VECTPROD.G2M">vectprod.g2m</a>
<br />
"""

vectProduct_eo = """
<br />
VectProd kalkulas la 3D kruci product de du 3D vektoroj. [a, b, c] X [d, e, f]
<br />
<img src = "vect_product.PNG" />
<br />
<a href = "VECTPROD.G2M">vectprod.g2m</a>
<br />
"""
############################################################################################################
nCalc_en = """
<br />
NCalc contains two small programs for calculating the number of samples needed to achieve a pre-determined, and supplied width of a confidence interval. Supports normal distrobution confidence intervals and binomail proportion confidence intervals.
<br />
<img src="n-calc-n.PNG" />
<br />and the other:
<br />
<img src = "n-calc-p.PNG">
<br />
<a href = "NCALC.G2M">NCALC.G2M</a>
"""

nCalc_eo = """
<br />
NCalc contains two small programs for calculating the number of samples needed to achieve a pre-determined, and supplied width of a confidence interval. Supports normal distrobution confidence intervals and binomail proportion confidence intervals.
<br />
<img src="n-calc-n.PNG" />
<br />and the other:
<br />
<img src = "n-calc-p.PNG">
<br />
<a href = "NCALC.G2M">NCALC.G2M</a>
"""
############################################################################################################
contents_en = "\n".join([intro_en, bezier_en, complex_en, euler_en, vectProduct_en, nCalc_en])
contents_eo = "\n".join([intro_eo, bezier_eo, complex_eo, euler_eo, vectProduct_eo, nCalc_eo])

contents = {"en": contents_en, "eo": contents_eo}

style = """
"""
title = {"en": """Casio fx-9860G -- Jak-o-Shadows""", "eo" : """Casio fx-9860G -- Jak-o-Shadows"""}
filesNeeded = ["COMPLEX.G2M", "complex.PNG", "BEZIER.G2M", "bezier.PNG", "n-calc-n.PNG", "n0calc0p.PNG", "NCALC.G2M", "vect_product.PNG", "VECTPROD.G2M"]

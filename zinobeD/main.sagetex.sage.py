## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file main.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_0p388 = RealNumber('0.388'); _sage_const_6 = Integer(6); _sage_const_4 = Integer(4); _sage_const_0p043 = RealNumber('0.043'); _sage_const_9 = Integer(9); _sage_const_0p686 = RealNumber('0.686'); _sage_const_0p85098 = RealNumber('0.85098'); _sage_const_24 = Integer(24); _sage_const_0p855 = RealNumber('0.855'); _sage_const_0p47843 = RealNumber('0.47843'); _sage_const_110 = Integer(110); _sage_const_139 = Integer(139); _sage_const_0p345 = RealNumber('0.345'); _sage_const_0p70196 = RealNumber('0.70196'); _sage_const_0p49803 = RealNumber('0.49803'); _sage_const_122 = Integer(122); _sage_const_109 = Integer(109); _sage_const_10 = Integer(10); _sage_const_16 = Integer(16); _sage_const_18 = Integer(18); _sage_const_0p357 = RealNumber('0.357'); _sage_const_0p45490 = RealNumber('0.45490'); _sage_const_72 = Integer(72); _sage_const_0p216 = RealNumber('0.216'); _sage_const_92 = Integer(92); _sage_const_96 = Integer(96); _sage_const_140 = Integer(140); _sage_const_0p3607 = RealNumber('0.3607'); _sage_const_0p239 = RealNumber('0.239')## This file (main.sagetex.sage) was *autogenerated* from main.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('main', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_92 
_st_.blockbegin()
try:
 ColorRC=(_sage_const_0p85098 ,_sage_const_0p47843 ,_sage_const_0p45490 )
 ColorA=(_sage_const_0p3607 ,_sage_const_0p49803 ,_sage_const_0p70196 )
 ColorV=(_sage_const_0p357 ,_sage_const_0p855 ,_sage_const_0p388 )
 ColorC=(_sage_const_0p686 ,_sage_const_0p345 , _sage_const_0p043 )
 ColorG=(_sage_const_0p239 ,_sage_const_0p216 ,_sage_const_0p216 )
 x = var('x')
 funcion1 = _sage_const_1 
 funcion2 = x-_sage_const_1 
 funcion3 = _sage_const_1 /_sage_const_2 *(x**_sage_const_2 -_sage_const_4 *x+_sage_const_2 )
 funcion4 = _sage_const_1 /_sage_const_6 *(x**_sage_const_3 -_sage_const_9 *x**_sage_const_2 +_sage_const_18 *x-_sage_const_6 )
 funcion5 = _sage_const_1 /_sage_const_24 *(x**_sage_const_4 -_sage_const_16 *x**_sage_const_3 +_sage_const_72 *x**_sage_const_2 -_sage_const_96 *x+_sage_const_24 )
 graficaFuncion1 = plot(funcion1,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorA,thickness=_sage_const_2 )
 graficaFuncion2 = plot(funcion2,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorRC,thickness=_sage_const_2 )
 graficaFuncion3 = plot(funcion3,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorV,thickness=_sage_const_2 )
 graficaFuncion4 = plot(funcion4,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorC,thickness=_sage_const_2 )
 graficaFuncion5 = plot(funcion5,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorG,thickness=_sage_const_2 )
except:
 _st_.goboom(_sage_const_109 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_110 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=graficaFuncion1+graficaFuncion2+graficaFuncion3+graficaFuncion4+graficaFuncion5)
except:
 _st_.goboom(_sage_const_110 )
_st_.current_tex_line = _sage_const_122 
_st_.blockbegin()
try:
 ColorRC=(_sage_const_0p85098 ,_sage_const_0p47843 ,_sage_const_0p45490 )
 ColorA=(_sage_const_0p3607 ,_sage_const_0p49803 ,_sage_const_0p70196 )
 ColorV=(_sage_const_0p357 ,_sage_const_0p855 ,_sage_const_0p388 )
 ColorC=(_sage_const_0p686 ,_sage_const_0p345 , _sage_const_0p043 )
 ColorG=(_sage_const_0p239 ,_sage_const_0p216 ,_sage_const_0p216 )
 x = var('x')
 funcion1 = exp(-(x**_sage_const_2 )/_sage_const_2 )
 funcion2 = (x-_sage_const_1 )*exp(-(x**_sage_const_2 )/_sage_const_2 )
 funcion3 = _sage_const_1 /_sage_const_2 *(x**_sage_const_2 -_sage_const_4 *x+_sage_const_2 )*exp(-(x**_sage_const_2 )/_sage_const_2 )
 funcion4 = _sage_const_1 /_sage_const_6 *(x**_sage_const_3 -_sage_const_9 *x**_sage_const_2 +_sage_const_18 *x-_sage_const_6 )*exp(-(x**_sage_const_2 )/_sage_const_2 )
 funcion5 = _sage_const_1 /_sage_const_24 *(x**_sage_const_4 -_sage_const_16 *x**_sage_const_3 +_sage_const_72 *x**_sage_const_2 -_sage_const_96 *x+_sage_const_24 )*exp(-(x**_sage_const_2 )/_sage_const_2 )
 graficaFuncion1 = plot(funcion1,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorA,thickness=_sage_const_2 )
 graficaFuncion2 = plot(funcion2,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorRC,thickness=_sage_const_2 )
 graficaFuncion3 = plot(funcion3,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorV,thickness=_sage_const_2 )
 graficaFuncion4 = plot(funcion4,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorC,thickness=_sage_const_2 )
 graficaFuncion5 = plot(funcion5,(x,_sage_const_0 ,_sage_const_10 ),rgbcolor=ColorG,thickness=_sage_const_2 )
except:
 _st_.goboom(_sage_const_139 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=graficaFuncion1+graficaFuncion2+graficaFuncion3+graficaFuncion4+graficaFuncion5)
except:
 _st_.goboom(_sage_const_140 )
_st_.endofdoc()


#!/bin/bash

#Instalar apt-get install enscript ghostscript


enscript -M A4 --margins=1:1:1:1 -f Courier7 noticias.txt reporte_scan.txt -p prueba1.ps

ps2pdf prueba3.pdf

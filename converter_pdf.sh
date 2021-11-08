#!/bin/bash

#Instalar apt-get install enscript ghostscript

enscript -M A4 --margins=1:1:1:1 -f Courier7 noticias.txt reporte_scan.txt -p Union_info.ps

ps2pdf Union_info.ps

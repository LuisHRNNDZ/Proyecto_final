#!/bin/bash




enscript -M A4 --margins=1:1:1:1 -f Courier7 prueba1 -p prueba1.ps

ps2pdf prueba1.ps prueba3.pdf

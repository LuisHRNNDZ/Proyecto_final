# Escaner de puertos

import nmap

def escan_ports():

    with open('reporte_scan.txt','w') as file:

        ip = '127.0.0.1'

        scanner = nmap.PortScanner()
        p_open = '-p '
        result = scanner.scan(hosts=ip,arguments='-sT -n -Pn -T4')
        count = 0
        
        print ("\nHost : %s" % ip)
        print ("Estado : %s" % scanner[ip].state())

        # Variables para reporte_san.txt
        ho_st = "\nHost : %s" % ip
        es_tado = "\nEstado : %s" % scanner[ip].state()
        file.write(ho_st)
        file.write(es_tado)

        for proto in scanner[ip].all_protocols():
            
            print ("Protocolo : %s" % proto)
            print ()

            # Variable para reporte_scan.txt
            proto_colo = "\nProtocolo : %s" % proto
            file.write(proto_colo)

            lport = scanner[ip][proto].keys()
            sorted(lport)

            for port in lport:

                print("port : %s\tstate : %s" % (port, scanner[ip][proto][port]["state"]))

                #Varible para repote_scan.txt
                puer_tos_op = "\nport : %s\tstate : %s" % (port, scanner[ip][proto][port]["state"])
                file.write(puer_tos_op)

                if count == 0:

                    p_open = p_open+str(port)
                    count = 1 
                else:
                    p_open = p_open+","+str(port)
        
        print ("\nPuertos abiertos: "+ p_open +" "+str(ip))

        # Variable para reporte_scan.txt
        salida = "\nPuertos abiertos: "+ p_open +" "+str(ip)
        file.write(salida)

fuc_llama = escan_ports()

print(fuc_llama)

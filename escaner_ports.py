# Escaner de puertos

import nmap

def escan_ports():

    ip = ''

    scanner = nmap.PortScanner()
    p_open = '-p '
    result = scanner.scan(hosts=ip,arguments='-sT -n -Pn -T4')
    count = 0
    
    print ("\nHost : %s" % ip)
    print ("Estado : %s" % scanner[ip].state())

    for proto in scanner[ip].all_protocols():
        
        print ("Protocolo : %s" % proto)
        print ()

        lport = scanner[ip][proto].keys()
        sorted(lport)

        for port in lport:

            print("port : %s\tstate : %s" % (port, scanner[ip][proto][port]["state"]))

            if count == 0:

                p_open = p_open+str(port)
                count = 1 
            else:
                p_open = p_open+","+str(port)
    
    print ("\nPuertos abiertos: "+ p_open +" "+str(ip))

#fuc_llama = escan_ports()

#print(fuc_llama)

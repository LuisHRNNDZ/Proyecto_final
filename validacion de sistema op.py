import subprocess

try:
        script = subprocess.call('./prueba3.sh')
except OSError:
    print("Tu sistema es Windows, no se ejecutarÃ¡ este script")
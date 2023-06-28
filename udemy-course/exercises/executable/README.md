# Programa ejecutable en el SO

## Comandos

```bash
pip install pyinstaller

pyinstaller programa.py

pip install pipenv

pip list
echo "Instalaciones de python que hay en el so"

pipenv install pyinstaller
echo "Instala pyinstaller en el entorno del proyecto"

pipenv shell
echo "Activar el entorno virtual del proyecto"

pipenv run
echo "Correr un comando dentro del entorno virtual"

pipenv run pip list
echo "Instalaciones de python que estan en el entorno virtual"

pipenv run pyinstaller programa.py

pipenv run pyinstaller --windowed --onefile --clean programa.py

pipenv install Pillow

pipenv run pyinstaller programa.py --windowed --onefile --clean --add-data <public;public> --ico public/gato.ico
```

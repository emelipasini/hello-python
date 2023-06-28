# Mensajes

Este es un paquete de prueba con fines solo educativos.

## Publica el paquete en Pypi

```bash
python setup.py sdist
echo "genera el directorio dist"

pip install build twine

python -m build

python -m twine check dist/*

python -m twine upload -r testpypi dist/*
echo "publica en el repositorio de testing"
echo "aca te pide las credenciales de la cuenta"

python -m twine upload dist/*
echo "publica en el repositorio oficial de Pypi"
echo "aca te pide las credenciales de la cuenta"

echo "al hacer modificaciones y aumentar la version, se repiten los pasos:"
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

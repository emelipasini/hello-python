from setuptools import setup

setup(
    name="Mensajes",
    version="1.0.0",
    description="Un paquete para saludar y despedir",
    author="Author",
    author_email="author@gmail.com",
    url="https://web.com",
    packages=["mensajes", "mensajes.bienvenida", "mensajes.despedida"],
    scripts=["app.py"]
)

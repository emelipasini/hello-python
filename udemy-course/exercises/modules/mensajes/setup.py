from setuptools import setup, find_packages

setup(
    name="mensajes-emep",
    version="1.3.0",
    description="Un paquete para saludar y despedir",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Author",
    author_email="author@gmail.com",
    url="https://repositorio.com",
    license_files=["LICENSE"],
    packages=find_packages(),
    scripts=["app.py"],
    test_suite="tests",
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities"
    ]
)

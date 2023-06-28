import sys

DATABASE_PATH = "database/clientes.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "database/test_clientes.csv"

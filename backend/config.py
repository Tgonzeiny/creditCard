import os
DBConfig = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "Catsndogs123"),
    "database": os.getenv("DB_NAME", "creditCard"),
    "port": int(os.getenv("DB_PORT", "5432"))
}
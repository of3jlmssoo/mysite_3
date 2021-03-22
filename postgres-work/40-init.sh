#!/bin/bash -x
echo $POSTGRES_DB
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER admin;
    ALTER USER admin with encrypted password 'adminpassword';
    CREATE DATABASE myapp;
    GRANT ALL PRIVILEGES ON DATABASE myapp TO admin;
EOSQL


# CREATE USER admin;
# CREATE USER postgres;

# CREATE DATABASE myapp;
# GRANT ALL PRIVILEGES ON DATABASE myapp TO admin;
# GRANT ALL PRIVILEGES ON DATABASE myapp TO postgres;

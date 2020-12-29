CREATE USER users WITH PASSWORD 'users' CREATEDB;
CREATE DATABASE users
    WITH
    OWNER = users
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    CONNECTION LIMIT = -1;

CREATE USER offers WITH PASSWORD 'offers' CREATEDB;
CREATE DATABASE offers
    WITH
    OWNER = offers
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    CONNECTION LIMIT = -1;
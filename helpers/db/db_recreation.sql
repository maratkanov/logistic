DROP DATABASE IF EXISTS logistic;
DROP USER IF EXISTS l_user;

CREATE DATABASE logistic;
CREATE USER l_user WITH PASSWORD 'el_passo';
ALTER ROLE l_user SET client_encoding TO 'utf8';
ALTER ROLE l_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE l_user SET TIMEZONE TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE logistic TO l_user;

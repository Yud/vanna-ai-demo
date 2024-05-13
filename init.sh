#!/bin/bash
createdb -U postgres dvdrental
pg_restore -c -U postgres -d dvdrental -v "/tmp/dvdrental.tar"
psql -U postgres -d dvdrental -c "CREATE ROLE readonly_user WITH LOGIN PASSWORD 'mypass_1234';"
psql -U postgres -d dvdrental -c "GRANT CONNECT ON DATABASE dvdrental TO readonly_user;"
psql -U postgres -d dvdrental -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;"

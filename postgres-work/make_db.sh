su postgres -c "createuser -w -d -r -s admin"
su postgres -c "createdb -O myapp admin"
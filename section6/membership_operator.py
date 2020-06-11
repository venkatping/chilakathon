#!/usr/local/bin/python3
valid_java=['1.6','1.7','1.8','1.9']
host_java='1.5'
if host_java in valid_java:
	print("host consists of valid java version")
else:
	print("host have invalid java version")

db_users=['db_admin','db_conf','db_installation']

random_user="db_admin"

if random_user in db_users:
	print("yes this user is allowed to start db")
else:
	print("this iser is not allowed to start db")



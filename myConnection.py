from MySQLdb import connect,cursors
# MySql database connection config
MYSQL_HOST = "localhost"
MYSQL_USER = "user"
MYSQL_PASS = ""
MYSQL_DB = "rkfake"
def condb():
	return connect(host=MYSQL_HOST, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB, cursorclass=cursors.DictCursor).cursor()
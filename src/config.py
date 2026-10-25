#configuracion para conexion a una base de datos

class DevelopmetConfig():
    DEBUG=True
    MYSQL_HOST='localhost'#mi servidor local
    MYSQL_USER='Torres'#usuario
    MYSQL_PASSWORD ='root'#contraseña
    MYSQL_DB ='api_utl'#nombre de la base de datos a conectar
    MYSQL_CURSORCLASS ="Cursor"


config={
    'development':DevelopmetConfig
}



import pymongo

# Configuración de MongoDB
MONGO_HOST = "localhost"
MONGO_PUERTO = "27018,27019"  # Puertos separados por comas, sin espacios
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"
MONGO_BASEDATOS = "Tienda"

# Conexión a MongoDB
try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
    cliente.server_info()  # Verifica conexión
    print("Conexión exitosa a MongoDB")
except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
    print(f"Error de conexión: Tiempo excedido. Detalles: {error_tiempo}")
    exit()
except pymongo.errors.ConnectionFailure as error_conexion:
    print(f"Error de conexión: Fallo al conectarse. Detalles: {error_conexion}")
    exit()

# Seleccionar la base de datos
db = cliente[MONGO_BASEDATOS]

# Función para insertar un equipo
def InsertEquipo(db, equipo):
    coleccion = db["Empleado"]
    resultado = coleccion.insert_one(equipo)
    print(f"Equipo insertado con ID: {resultado.inserted_id}")

def ListarEquipos(db):
    coleccion = db["Empleado"]
    print("Empleados en la colección:")
    for equipo in coleccion.find():
        print(equipo)
        
# Programa principal
if __name__ == "__main__":
    #Inserta un equipo como ejemplo
    nuevo_empleado = {"nombre": "Jose", "Edad": "23", "Ocupacion":"Fotografo"}
    InsertEquipo(db, nuevo_empleado)

    #Lista los equipos
    ListarEquipos(db)
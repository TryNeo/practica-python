import mysql.connector

"""
Una de las primeras practicas con las que siempre nos toparemos al nosotros comenzar en el tema de base de datos, es con el ya conocido CRUD (Create, Read, Update and Delete)

Es por ello que, en esta ocasión, será necesario desarrolles un pequeño programe el cual nos permita dar de alta, listar, modificar y eliminar usuarios de una base de datos. No te preocupes, la tabla es muy sencilla, como puedes observar. 😋

CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(50) NOT NULL UNIQUE
El programa debe cumplir con los siguiente requerimiento.

El usuario podrá visualizar, mediante un menú simple, las opciones que el programa le ofrece.
Se podrán dar crear nuevos usuarios en la base de datos.
Se podrán listar todos los usuarios de la base de datos.
Se podrá modificar usuarios de la base de datos.
Se podrá eliminar usuarios de la base de datos.
En caso se intente insertar un registro duplicado se deberá notificar al usuario del error.
"""
class Crud:
    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    @property
    def menu(self):
        print("""\tMenu Usuario\n\n1.Añadir\n2.Listar\n3.Editar\n4.eliminar\n5.Salir
        """)

    def connecting(self):
        try:
            self.mydb = mysql.connector.connect(host='localhost',
                                                user='root',
                                                passwd='admin',
                                                db='crud')
            self.mysqlcursor = self.mydb.cursor()
        except mysql.connector.errors.ProgrammingError as error:
            print("Review the Error -->", error)

    def add_user(self, username, email):
        self.connecting()
        try:
            query = """INSERT INTO usuario (username,email) values (%s,%s)"""
            get_data = (username, email)
            self.mysqlcursor.execute(query, get_data)
            self.mydb.commit()
            print("Usuario Ingresado Exitosamente")
            self.mydb.close()
        except mysql.connector.errors.IntegrityError:
            print(f"Este {username + '/' + email}  ya existe  , no puedes ingresar repetidos!")
    def list_users(self):
        self.connecting()
        query = """SELECT id,username,email FROM usuario"""
        self.mysqlcursor.execute(query)
        listado = self.mysqlcursor.fetchall()
        lista = []
        if listado == lista:
            print("No hay datos a listar")
        else:
            print("\t..::Consulta de Usuarios::..")
            for i in listado:
                print(f"id:{i[0]}\nusuario:{i[1]}\nemail:{i[2]}\n")

    def update_user(self, username):
        self.connecting()
        query = """SELECT id,username FROM usuario WHERE usuario.username=%s"""
        get_data = (username,)
        self.mysqlcursor.execute(query, get_data)
        validar = self.mysqlcursor.fetchall()
        lista = []
        if validar == lista:
            print(f"el usuario {username} no existe")
        else:
            try:
                user = input("nuevo usuario:")
                email = input("nuevo email:")
                query = """UPDATE usuario SET usuario.username =%s,usuario.email = %s WHERE usuario.id =%s"""
                get_data = (user, email,validar[0][0])
                self.mysqlcursor.execute(query, get_data)
                self.mydb.commit()
                print("Usuario Editado Exitosamente")
                self.mydb.close()
            except mysql.connector.errors.IntegrityError:
                print(f"Este {user + '/' + email}  ya existe  , no puedes ingresar repetidos!")

    def delet_user(self, username):
        self.connecting()
        query = """SELECT id,username FROM usuario WHERE usuario.username=%s"""
        get_data = (username,)
        self.mysqlcursor.execute(query, get_data)
        validar = self.mysqlcursor.fetchall()
        lista = []
        if validar == lista:
            print(f"el usuario {username} no existe")
        else:
            print(f"¿Desea Eliminar este usuario {user}?")
            op = input("Y/N:")
            if op.lower() == "y":
                query = "DELETE FROM usuario WHERE usuario.id="+str(validar[0][0])
                self.mysqlcursor.execute(query)
                self.mydb.commit()
                print("Usuario Eliminado Exitosamente")
                self.mydb.close()
            else:
                print("Usuario no eliminado")

if __name__ == '__main__':
    crud = Crud()
    crud.menu
    while True:
        op = input("selecione una opcion:")
        if op == "1":
            user = input("usuario:")
            email = input("email:")
            crud.add_user(user, email)
        elif op == "2":
            crud.list_users()
        elif op == "3":
            user = input("buscar usuario:")
            crud.update_user(user)
        elif op == "4":
            user = input("buscar usuario:")
            crud.delet_user(user)
        elif op == "5":
            print("\nSaliendo del menu...")
            break
        else:
            print("\nError! selecione una opcion correcta")


"""
Dada la siguiente lista de usuarios.

users = [
    { 'name': 'Luis', 'age': 27 },
    { 'name': 'Raquel', 'age': 13 },
    { 'name': 'Eduardo', 'age': 35 },
    { 'name': 'Fernando', 'age': 12},
    { 'name': 'Esmeralda', 'age': 45 },
    { 'name': 'Sophie', 'age': 9}
]
Mostrar en consola el nombre de los 3 primeros usuarios más jóvenes.

Salida.

Shopie
Fernando
Raquel
Ayuda: Puedes hacer uso de un expresión lambda para acceder a las llaves de la lista.

"""

if __name__ == '__main__':
    users = [
        { 'name': 'Luis', 'age': 27 },
        { 'name': 'Raquel', 'age': 13 },
        { 'name': 'Eduardo', 'age': 35 },
        { 'name': 'Fernando', 'age': 12},
        { 'name': 'Esmeralda', 'age': 45 },
        { 'name': 'Sophie', 'age': 9}
    ]

    for i in sorted(users, key=lambda user: user['age'])[:3]:
        print(i['name'])
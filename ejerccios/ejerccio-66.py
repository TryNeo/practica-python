
"""
Desarrolla un script el cual nos permita validar contraseñas para los usuarios de PyWombat. El script debe cumplir con los siguiente requerimientos.

Las validaciones deben hacerse sobre la función _is_valid_password_.
La función debe poseer como parámetro la variable password.
La función debe recibir como argumento (al momento de su llamado) una string en texto plano.
La función debe retornar un True en caso el parámetro cumpla con las validaciones de una contraseña segura.
La función debe retornar un False en caso el parámetro no cumpla con las validaciones de contraseña segura.
Una contraseña será segura siempre y cuando cumpla con los siguientes puntos.

Poseer una longitud mínima de 6 caracteres.
Contar con por lo menos una letra en Mayusculas.
Contar con por lo menos dos dígitos.
Los dígitos no deben ser consecutivos. Por ejemplo 123 o 456 no son combinaciones validas. Por el contrario 168 y 414 si lo son.
Poseer por lo menos con un carácter espacial (?*%&@)
Es posible que necesites recorrer carácter por carácter la contraseña.
El módulo string sin duda puede ser de mucha utilidad.
Restricciones:

No es posible utilizar expresiones regulares (Quizás en otro momento).
"""

import string


def is_valid_password(password):
	if len(password) > 6:
		if not any(i in string.ascii_uppercase for i in password):
			return False
		else:
			if not any(i in string.digits for i in password):
				return False
			else:
				if not any(i in string.punctuation for i in password):
					return False
				else:
					return True
	else:
		return False

def main():
    print("\tEjerccio 66")
    print("")
    password = input("password:")
    resultado = is_valid_password(password)
    print(resultado)


if __name__ == '__main__':
    main()

import model.UsuarioModel as um

def crear_usuarios():
    #Crear un arreglo de usuarios
    usuarios = []
    #Crear elementos para el arreglo
    usuario1 = um.Usuario('Administrador','','admin','admin','admin','admin@sample.com.pe','','','','','')
    usuario2 = um.Usuario('Juan Domingo','Benate Mendoza','jbenate','123456','usuario','jbenatem@gmail.com', '989022161','Lima','Lima','La Molina','Av. Alameda el Corregidor 3185 dpto. 301 Urb. Las Praderas')
    #Ingresar elementos en el arreglo
    usuarios.append(usuario1)
    usuarios.append(usuario2)

    return usuarios
class Usuario:
    def __init__(self, nombres, apellidos, usuario, contraseña, rol, correo, telefono, departamento, provincia, distrito, direccion):
        self.nombres = nombres
        self.apellidos = apellidos
        self.usuario = usuario
        self.contraseña = contraseña
        self.correo = correo
        self.teléfono = telefono
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.direccion = direccion

    def set_nombres(self, nombres):
        self.nombres = nombres

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_contraseña(self, contraseña):
        self.contraseña = contraseña
    
    def set_rol(self, rol):
        self.rol = rol

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono
    
    def set_departamento(self, departamento):
        self.departamento = departamento

    def set_provincia(self, provincia):
        self.provincia = provincia

    def set_distrito(self, distrito):
        self.distrito = distrito

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_nombres(self):
        return self.nombres

    def get_apellidos(self):
        return self.apellidos

    def get_usuario(self):
        return self.usuario
    
    def get_contraseña(self):
        return self.contraseña

    def get_rol(self):
        return self.rol
    
    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    def get_departamento(self):
        return self.departamento

    def get_provincia(self):
        return self.provincia

    def get_distrito(self):
        return self.distrito

    def get_direccion(self):
        return self.direccion
import model.ProductoModel as pm

def crear_productos():
    #Crear un arreglo de productos
    productos = []
    #Crear elementos para el arreglo
    producto1 = pm.Ropa('Camiseta de Fútbol Barcelona Local 2019/2020', 'Nike', 250.50, 'https://pontelacamiseta.pe/wp-content/uploads/2019/06/01-9.jpg', 'Azulgrana', 'M')
    producto2 = pm.Ropa('Camiseta de Fútbol Barcelona Visitante 2019/2020', 'Nike', 250.50, 'https://http2.mlstatic.com/camiseta-barcelona-visitante-20192020-version-aficionado-D_NQ_NP_813044-MPE31460471688_072019-F.jpg', 'Amarillo', 'M')
    producto3 = pm.Ropa('Camiseta de Fútbol Alianza Lima Local 2020', 'Nike', 210.50, 'https://http2.mlstatic.com/camiseta-alianza-lima-2020-ymrv-sport-D_NQ_NP_916914-MPE40761859617_022020-F.jpg', 'Azulgrana', 'S')
    producto4 = pm.Ropa('Camiseta de Fútbol Alianza Lima Visitante 2020', 'Nike', 210.50, 'https://http2.mlstatic.com/camiseta-alianza-lima-2020-alterna-nike-original-D_NQ_NP_765285-MPE40600585168_012020-F.jpg', 'Negro', 'L')
    #Ingresar elementos en el arreglo
    productos.append(producto1)
    productos.append(producto2)
    productos.append(producto3)
    productos.append(producto4)

    return productos
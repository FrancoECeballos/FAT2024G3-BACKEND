DROP DATABASE IF EXISTS EXPRONTAENTREGADB;

CREATE DATABASE IF NOT EXISTS PRONTAENTREGADB;

USE PRONTAENTREGADB;

CREATE TABLE IF NOT EXISTS Direccion(
    id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(255),
    numero INT,
    localidad VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Organizacion (
    id_Organizacion INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS TipoUsuario (
    id_tipoUsuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    nombreUsuario VARCHAR(255),
    contrasenia INT,
    dni VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(255),
    id_direccion INT,
    id_tipoUsuario INT,
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion),
	CONSTRAINT fk_tipo_usuario FOREIGN KEY (id_tipoUsuario) REFERENCES TipoUsuario(id_tipoUsuario)

);

CREATE TABLE IF NOT EXISTS Casa (
    id_casa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_Organizacion INT,
    id_direccion INT,
    CONSTRAINT fk_organizacion_casa FOREIGN KEY (id_Organizacion) REFERENCES Organizacion(id_Organizacion),
    CONSTRAINT fk_direccion2 FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS DetalleCasaUsuario (
    id_detalleCasaUsuario INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    id_casa INT,
    id_usuario INT,
    CONSTRAINT fk_casa_detalle FOREIGN KEY (id_casa) REFERENCES Casa(id_casa),
    CONSTRAINT fk_usuario_detalle FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS UnidadMedida(
    id_unidadMedida INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS CategoriaProducto (
    id_categoriaProducto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_categoriaProducto INT,
    id_unidadMedida INT,
    CONSTRAINT fk_categoria_producto FOREIGN KEY (id_categoriaProducto) REFERENCES CategoriaProducto(id_categoriaProducto),
    CONSTRAINT fk_unidadMedida FOREIGN KEY (id_unidadMedida) REFERENCES UnidadMedida(id_unidadMedida)
);

CREATE TABLE IF NOT EXISTS StockProducto (
    id_stockProducto INT AUTO_INCREMENT PRIMARY KEY,
    id_casa INT,
    id_producto INT,
    cantidad INT,
    CONSTRAINT fk_producto_stock FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
	CONSTRAINT fk_casa_stockProducto FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)

);

CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    hora TIME,
    id_casa INT,
    id_usuario INT,
	CONSTRAINT fk_usuario_pedido FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    CONSTRAINT fk_casa_pedido FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);

CREATE TABLE IF NOT EXISTS EstadoProductoPedido(
    id_estadoProductoPedido INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS DetallePedidoProducto (
    id_detallePedidoProducto INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_pedido INT,
    id_producto INT,
    id_estadoProductoPedido INT,
    CONSTRAINT fk_pedido_detalle FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    CONSTRAINT fk_producto_detalle FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_estado_producto_pedido FOREIGN KEY (id_estadoProductoPedido) REFERENCES EstadoProductoPedido(id_estadoProductoPedido)
);

CREATE TABLE IF NOT EXISTS Oferta (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    hora TIME,
    id_usuario INT,
    id_casa INT,
    CONSTRAINT fk_casa_oferta FOREIGN KEY (id_casa) REFERENCES Casa(id_casa),
    CONSTRAINT fk_usuario_oferta FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS EstadoProductoOferta(
    id_estadoProductoOferta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS DetalleOfertaProducto (
    id_detalleOfertaProducto INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_oferta INT,
    id_producto INT,
    id_estadoProductoOferta INT,
    CONSTRAINT fk_oferta_detalle FOREIGN KEY (id_oferta) REFERENCES Oferta(id_oferta),
    CONSTRAINT fk_producto_detalle_oferta FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_estado_producto_oferta FOREIGN KEY (id_estadoProductoOferta) REFERENCES EstadoProductoOferta(id_estadoProductoOferta)
);

CREATE TABLE IF NOT EXISTS Transporte (
    id_transporte INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255),
    modelo VARCHAR(255),
    patente VARCHAR(20),
    kilometraje INT,
    estadoITV VARCHAR(255),
    anio DATETIME,
    id_Organizacion INT,
    CONSTRAINT fk_organizacion FOREIGN KEY (id_Organizacion) REFERENCES Organizacion(id_Organizacion)
);

-- Inserciones para la tabla Direccion
INSERT INTO Direccion (calle, numero, localidad) VALUES 
    ('Calle Fornica', 25, 'Localidad Abedul'),
    ('Calle Ignacio', 103, 'Localidad Betular'),
    ('Calle Gonzalo', 6, 'Localidad Carlos Paz'),
    ('Calle Martinez', 42, 'Localidad Dildo')
    ('Calle Sergio', 25, 'Localidad Abedul'),
    ('Calle Roca', 103, 'Localidad Colonia Carolla'),
    ('Calle Menem', 6, 'Localidad La Estanzuela'),
    ('Calle Evita', 42, 'Localidad Perón');

-- Inserciones para la tabla Organizacion
INSERT INTO Organizacion (descripcion) VALUES 
    ('Manos Abiertas CBA'),
    ('Manos Abiertas BSAS'),
    ('Open Hands USA');

-- Inserciones para la tabla TipoUsuario
INSERT INTO TipoUsuario (nombre, descripcion) VALUES 
    ('Admin', 'Es admin'),
    ('Voluntario', 'Es el voluntario'),
    ('SuperUser', 'Es el superadmin');

-- Inserciones para la tabla Usuario
INSERT INTO Usuario (nombre, apellido, contrasenia, nombreUsuario, dni, telefono, email, id_direccion, id_tipoUsuario) VALUES 
    ('Joaquin', 'Lopez', 'Pa$$word', 'JoaLopez', '12345678A', '25129735', 'JoaquinL@hotmail.com', 1, 3),
    ('Timoteo', 'Wuewuan', 'QwerTY', 'TimoelWawan','98765432B', '46505926', 'TimoteoW@gmail.com.com', 3, 2),
    ('Teresa', 'Diaz', '12435687', 'TeresitaD','56789123C', '36007395', 'TereDiaz@gmail.com', 4, 1);

-- Inserciones para la tabla Casa
INSERT INTO Casa (nombre, descripcion, id_Organizacion, id_direccion) VALUES 
    ('Mama Antula', 'Descripción', 1, 5),
    ('El Aljibe', 'Descripción', 1, 7),
    ('La Casa de la Bondad', 'Descripción', 1, 6);

-- Inserciones para la tabla DetalleCasaUsuario
INSERT INTO DetalleCasaUsuario (descripcion, id_casa, id_usuario) VALUES 
    ('Mama Antula', 1, 1),
    ('Ofrecen apoyo escolar, actividades culturales, deportivas, talleres sobre crianza, alimentación saludable y asesoramiento sobre trámites.', 2, 2),
    ('Cuenta con un equipo de voluntarios y profesionales que trabajan juntos para lograr su misión de amar y servir a cada uno de sus beneficiarios.', 3, 3); 

-- Inserciones para la tabla UnidadMedida
INSERT INTO UnidadMedida (nombre, descripcion) VALUES 
    ('Kg', 'Son Kilogramos'),
    ('Litros', 'Son Litros'),
    ('Unidad', 'Es cada paquete');

-- Inserciones para la tabla CategoriaProducto
INSERT INTO CategoriaProducto (nombre, descripcion) VALUES 
    ('Perecedero', 'Productos con fecha de vencimiento.'),
    ('No perecederos', 'Productos in fecha de vencimiento.'),
    ('Elatados', 'Productos en lata.');

-- Inserciones para la tabla Producto
INSERT INTO Producto (nombre, descripcion, id_categoriaProducto, id_unidadMedida) VALUES 
    ('Arroz', 'Paquete de arroz de 1KgArroz', 2, 1),
    ('Fideos', 'Paquete de fideideos', 2, 3),
    ('Pure de tomate', 'Pure de tomate 500 ml', 1, 2);

-- Inserciones para la tabla StockProducto
INSERT INTO StockProducto (id_casa, id_producto, cantidad) VALUES 
    (1, 1, 50),
    (2, 2, 100),
    (3, 3, 30);

-- Inserciones para la tabla Pedido
INSERT INTO Pedido (fecha, hora, id_casa, id_usuario) VALUES 
    ('2024-06-14', '09:05:00', 1, 1),
    ('2024-04-08', '13:00:00', 2, 2),
    ('2024-09-23', '17:27:00', 3, 3);

-- Inserciones para la tabla Oferta
INSERT INTO Oferta (fecha, hora, id_usuario, id_casa) VALUES 
    ('2024-01-14', '08:01:31', 1, 1),
    ('2023-08-10', '16:08:10', 3, 2),
    ('2024-04-30', '14:27:57', 2, 3);

-- Inserciones para la tabla EstadoProductoPedido
INSERT INTO EstadoProductoPedido (nombre, descripcion) VALUES 
    ('Pendiente', 'Solo es un pedido y no se hizo nada'),
    ('En Proceso', 'Transporte se encarga de llevar este pedido que ahora esta en procesosta en proceso el pedido'),
    ('Finalizado', 'El pedido llego a la casal pedido ya esta finalizado.');

-- Inserciones para la tabla EstadoProductoOferta
INSERT INTO EstadoProductoOferta (nombre, descripcion) VALUES 
    ('Disponible', 'La oferta aun esta disponible y los usuarios pueden verla para reservarla'),
    ('Reservado', 'La oferta esta reservada y los usuarios dejan verla'),
    ('Reclamado', 'La oferta que etaba en reserva ya fue transportada hasta la casa que la reclamo');

-- Inserciones para la tabla Transporte
INSERT INTO Transporte (marca, modelo, patente, kilometraje, estadoITV, anio, id_Organizacion) VALUES 
    ('Toyota', 'Hilux', 'NXD838', 10000, 'En Forma', '2022-01-01', 1),
    ('Renault', 'Logan', 'AA001AB', 20000, 'Vencido', '2020-01-01', 2),
    ('Peugeot', '3008 GT', 'AG500AA', 30000, 'En Forma', '2018-01-01', 3);

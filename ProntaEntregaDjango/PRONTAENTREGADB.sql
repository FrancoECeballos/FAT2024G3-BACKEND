DROP DATABASE IF EXISTS PRONTAENTREGADB;

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
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS TipoDocumento (
    id_tipoDocumento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
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
    password VARCHAR(255),
    documento VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(255),
    genero INT,
    fechaUnion DATETIME,
    last_login DATETIME DEFAULT CURRENT_TIMESTAMP,
    `is_superuser` BOOLEAN DEFAULT FALSE,
    id_direccion INT,
    id_tipoUsuario INT,
    id_tipoDocumento INT,
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion),
    CONSTRAINT fk_tipo_usuario FOREIGN KEY (id_tipoUsuario) REFERENCES TipoUsuario(id_tipoUsuario),
    CONSTRAINT fk_tipo_documento FOREIGN KEY (id_tipoDocumento) REFERENCES TipoDocumento(id_tipoDocumento)
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
    fechaIngreso DATE,
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

CREATE TABLE IF NOT EXISTS Stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_casa INT,
	CONSTRAINT fk_casa_stock FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
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

CREATE TABLE IF NOT EXISTS DetalleStockProducto (
    id_detalleStockProducto INT AUTO_INCREMENT PRIMARY KEY,
    cantidad INT,
    id_stock INT,
    id_producto INT,
    CONSTRAINT fk_stock_detalle FOREIGN KEY (id_stock) REFERENCES Stock(id_stock),
    CONSTRAINT fk_producto_detalle_stock FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    horaInicio TIME,
    fechaVencimiento DATE,
    horaVencimiento TIME,
    id_casa INT,
    id_usuario INT,
	CONSTRAINT fk_usuario_pedido FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    CONSTRAINT fk_casa_pedido FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);

CREATE TABLE IF NOT EXISTS EstadoPedido(
    id_estadoPedido INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS DetallePedido (
    id_detallePedido INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_pedido INT,
    id_producto INT,
    id_estadoPedido INT,
    CONSTRAINT fk_pedido_detalle FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    CONSTRAINT fk_producto_detalle FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_estado_pedido FOREIGN KEY (id_estadoPedido) REFERENCES EstadoPedido(id_estadoPedido)
);

CREATE TABLE IF NOT EXISTS Oferta (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    horaInicio TIME,
    fechaVencimiento DATE,
    horaVencimiento TIME,
    id_usuario INT,
    id_casa INT,
    CONSTRAINT fk_casa_oferta FOREIGN KEY (id_casa) REFERENCES Casa(id_casa),
    CONSTRAINT fk_usuario_oferta FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS EstadoOferta(
    id_estadoOferta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS DetalleOferta (
    id_detalleOferta INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_oferta INT,
    id_producto INT,
    id_estadoOferta INT,
    CONSTRAINT fk_oferta_detalle FOREIGN KEY (id_oferta) REFERENCES Oferta(id_oferta),
    CONSTRAINT fk_producto_detalle_oferta FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_estado_oferta FOREIGN KEY (id_estadoOferta) REFERENCES EstadoOferta(id_estadoOferta)
);

CREATE TABLE IF NOT EXISTS Transporte (
    id_transporte INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255),
    modelo VARCHAR(255),
    patente VARCHAR(20),
    kilometraje INT,
    estadoITV VARCHAR(255),
    anio YEAR,
    id_Organizacion INT,
    CONSTRAINT fk_organizacion FOREIGN KEY (id_Organizacion) REFERENCES Organizacion(id_Organizacion)
);

-- Inserciones para la tabla Direccion
INSERT INTO Direccion (calle, numero, localidad) VALUES 
    ('Calle Fornica', 25, 'Localidad Abedul'),
    ('Calle Ignacio', 103, 'Localidad Betular'),
    ('Calle Gonzalo', 6, 'Localidad Carlos Paz'),
    ('Calle Martinez', 42, 'Localidad Dildo'),
    ('Calle Sergio', 25, 'Localidad Abedul'),
    ('Calle Roca', 103, 'Localidad Colonia Carolla'),
    ('Calle Menem', 6, 'Localidad La Estanzuela'),
    ('Calle Evita', 42, 'Localidad Perón');

-- Inserciones para la tabla Organizacion
INSERT INTO Organizacion (nombre, descripcion, telefono, email) VALUES 
    ('Manos Abiertas','Manos Abiertas de la provincia de Córdoba', '0351 423 5140', 'cordoba@manosabiertas.org.ar');

-- Inserciones para la tabla TipoUsuario
INSERT INTO TipoUsuario (nombre, descripcion) VALUES 
    ('Admin', 'Es admin'),
    ('Voluntario', 'Es el voluntario'),
    ('SuperUser', 'Es el superadmin');

INSERT INTO TipoDocumento (nombre, descripcion) VALUES 
    ('DNI', 'Es un documento de identidad'),
    ('Pasaporte', 'Es un documento de viaje'),
    ('Cedula', 'Es un documento de identidad');

-- Inserciones para la tabla Usuario
INSERT INTO Usuario (nombre, apellido, password, nombreUsuario, documento, id_tipoDocumento, telefono, email, id_direccion, id_tipoUsuario) VALUES 
    ('Joaquin', 'Lopez', 'contra', 'JoaLopez', '12345678A', 1, '25129735', 'JoaquinL@hotmail.com', 1, 3),
    ('Timoteo', 'Wuewuan', 'QwerTY', 'TimoelWawan','98765432B', 2,'46505926', 'TimoteoW@gmail.com.com', 3, 2),
    ('Teresa', 'Diaz', '12435687', 'TeresitaD','56789123C', 3,'36007395', 'TereDiaz@gmail.com', 4, 1);

-- Inserciones para la tabla Casa
INSERT INTO Casa (nombre, descripcion, id_Organizacion, id_direccion) VALUES 
    ('Mama Antula', 'Descripción', 1, 5),
    ('El Aljibe', 'Descripción', 1, 7),
    ('La Casa de la Bondad', 'Descripción', 1, 6);

-- Inserciones para la tabla DetalleCasaUsuario
INSERT INTO DetalleCasaUsuario (descripcion, fechaIngreso, id_casa, id_usuario) VALUES 
    ('Se ofrece a cuidar de personas con necesidad', '2023-12-26', 1, 1),
    ('Ofrecen apoyo escolar, actividades culturales, deportivas, talleres sobre crianza, alimentación saludable y asesoramiento sobre trámites.', '2024-01-12', 2, 2),
    ('Cuenta con un equipo de voluntarios y profesionales que trabajan juntos para lograr su misión de amar y servir a cada uno de sus beneficiarios.', '2024-3-09', 3, 3); 

-- Inserciones para la tabla UnidadMedida
INSERT INTO UnidadMedida (nombre, descripcion) VALUES 
    ('Kg', 'Son Kilogramos'),
    ('Litros', 'Son Litros'),
    ('Unidad', 'Es cada paquete');

-- Inserciones para la tabla Stock
INSERT INTO Stock (id_casa) VALUES 
    (1),
    (2),
    (3);

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

-- Inserciones para la tabla Pedido
INSERT INTO Pedido (fechaInicio, horaInicio, fechaVencimiento, horaVencimiento, id_casa, id_usuario) VALUES 
    ('2024-06-14', '09:05:00', '2024-06-28', '09:05:00', 1, 1),
    ('2024-04-08', '13:00:00', '2024-04-15', '13:00:00', 2, 2),
    ('2024-09-23', '17:27:00', '2024-10-23', '17:27:00', 3, 3);

-- Inserciones para la tabla Oferta
INSERT INTO Oferta (fechaInicio, horaInicio, fechaVencimiento, horaVencimiento, id_usuario, id_casa) VALUES 
    ('2024-01-14', '08:01:31', '2024-01-28', '08:01:31', 1, 1),
    ('2023-08-10', '16:08:10', '2023-08-17', '16:08:10', 3, 2),
    ('2024-04-30', '14:27:57', '2024-05-30', '14:27:57', 2, 3);

-- Inserciones para la tabla EstadoPedido
INSERT INTO EstadoPedido (nombre, descripcion) VALUES 
    ('Pendiente', 'Solo es un pedido y no se hizo nada'),
    ('En Proceso', 'Transporte se encarga de llevar este pedido que ahora esta en procesosta en proceso el pedido'),
    ('Finalizado', 'El pedido llego a la casal pedido ya esta finalizado.');

-- Inserciones para la tabla EstadoOferta
INSERT INTO EstadoOferta (nombre, descripcion) VALUES 
    ('Disponible', 'La oferta aun esta disponible y los usuarios pueden verla para reservarla'),
    ('Reservado', 'La oferta esta reservada y los usuarios dejan verla'),
    ('Reclamado', 'La oferta que etaba en reserva ya fue transportada hasta la casa que la reclamo');

-- Inserciones para la tabla Transporte
INSERT INTO Transporte (marca, modelo, patente, kilometraje, estadoITV, anio, id_Organizacion) VALUES 
    ('Toyota', 'Hilux', 'NXD838', 10000, 'En Forma', '2022', 1),
    ('Renault', 'Logan', 'AA001AB', 20000, 'Vencido', '2020', 1),
    ('Peugeot', '3008 GT', 'AG500AA', 30000, 'En Forma', '2018', 1);

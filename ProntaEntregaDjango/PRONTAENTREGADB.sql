DROP DATABASE IF EXISTS PRONTAENTREGADB;

CREATE DATABASE IF NOT EXISTS PRONTAENTREGADB;

USE PRONTAENTREGADB;

create table if not exists codigos_de_verificacion(
codigos_id int auto_increment not null,
codigo int,
primary key (codigos_id)
);

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

CREATE TABLE IF NOT EXISTS CustomUsuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    nombreusuario VARCHAR(255),
    password VARCHAR(255),
    documento VARCHAR(20),
    telefono VARCHAR(20),
    email VARCHAR(255),
    genero INT,
    imagen VARCHAR(255),
    fechaUnion DATETIME,
    last_login DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_direccion INT,
    id_tipoDocumento INT,
    `is_staff` BOOLEAN DEFAULT FALSE,
    `is_superuser` BOOLEAN DEFAULT FALSE,
    `is_active` BOOLEAN DEFAULT TRUE,
    `is_verified` BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_direccion FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion),
    CONSTRAINT fk_tipo_documento FOREIGN KEY (id_tipoDocumento) REFERENCES TipoDocumento(id_tipoDocumento)
);

CREATE TABLE CustomUsuario_groups (
    customusuario_id INT,
    group_id INT,
    PRIMARY KEY (customusuario_id, group_id),
    FOREIGN KEY (customusuario_id) REFERENCES CustomUsuario(id_usuario) ON DELETE CASCADE
);

-- For user_permissions:
CREATE TABLE CustomUsuario_user_permissions (
    customusuario_id INT,
    permission_id INT,
    PRIMARY KEY (customusuario_id, permission_id),
    FOREIGN KEY (customusuario_id) REFERENCES CustomUsuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS notificacion(
    notificacion_id INT auto_increment NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255),
    viewed BOOLEAN DEFAULT FALSE,
    fecha_creacion DATE,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario) ON DELETE CASCADE,
    PRIMARY KEY (notificacion_id)
);

CREATE TABLE IF NOT EXISTS Obra (
    id_obra INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_Organizacion INT,
    id_direccion INT,
    imagen VARCHAR(255),
    CONSTRAINT fk_organizacion_obra FOREIGN KEY (id_Organizacion) REFERENCES Organizacion(id_Organizacion),
    CONSTRAINT fk_direccion2 FOREIGN KEY (id_direccion) REFERENCES Direccion(id_direccion)
);

CREATE TABLE IF NOT EXISTS DetalleObraUsuario (
    id_detalleObraUsuario INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    fechaIngreso DATE,
    id_obra INT,
    id_usuario INT,
    id_tipoUsuario INT,
    CONSTRAINT fk_obra_detalle FOREIGN KEY (id_obra) REFERENCES Obra(id_obra),
    CONSTRAINT fk_usuario_detalle FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario),
    CONSTRAINT fk_tipo_usuario FOREIGN KEY (id_tipoUsuario) REFERENCES TipoUsuario(id_tipoUsuario)
);

CREATE TABLE IF NOT EXISTS UnidadMedida(
    id_unidadMedida INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    identificador VARCHAR(20),
    paquete BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS Stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_obra INT,
	CONSTRAINT fk_obra_stock FOREIGN KEY (id_obra) REFERENCES Obra(id_obra)
);

CREATE TABLE IF NOT EXISTS Categoria (
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS CategoriaProducto (
    id_categoriaProducto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_categoria INT,
    CONSTRAINT fk_categoria_categoriaproducto FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE IF NOT EXISTS Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_categoriaProducto INT,
    id_unidadMedida INT,
    imagen VARCHAR(255),
    CONSTRAINT fk_categoria_producto FOREIGN KEY (id_categoriaProducto) REFERENCES CategoriaProducto(id_categoriaProducto),
    CONSTRAINT fk_unidadMedida_producto FOREIGN KEY (id_unidadMedida) REFERENCES UnidadMedida(id_unidadMedida)
);

CREATE TABLE IF NOT EXISTS DetalleStockProducto (
    id_detalleStockProducto INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    descripcion VARCHAR(255),
    imagen VARCHAR(255),
    cantidad INT,
    cantidadUnidades INT DEFAULT 1,
    id_stock INT,
    id_producto INT,
    id_unidadMedida INT,
    CONSTRAINT fk_producto_detalle_stock FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_unidadMedida FOREIGN KEY (id_unidadMedida) REFERENCES UnidadMedida(id_unidadMedida),
    CONSTRAINT fk_stock_detalle FOREIGN KEY (id_stock) REFERENCES Stock(id_stock)
);

CREATE TABLE IF NOT EXISTS EstadoPedido(
    id_estadoPedido INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    horaInicio TIME,
    fechaVencimiento DATE,
    horaVencimiento TIME,
    cantidad INT,
    urgente INT,
    id_obra INT,
    id_usuario INT,
    id_producto INT,
    id_estadoPedido INT,
    CONSTRAINT fk_producto_pedido FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
	CONSTRAINT fk_usuario_pedido FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario),
    CONSTRAINT fk_obra_pedido FOREIGN KEY (id_obra) REFERENCES Obra(id_obra),
    CONSTRAINT fk_estado_pedido FOREIGN KEY (id_estadoPedido) REFERENCES EstadoPedido(id_estadoPedido)
);

CREATE TABLE IF NOT EXISTS AportePedido (
    id_aportePedido INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_pedido INT,
    CONSTRAINT fk_aportePedido FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

CREATE TABLE IF NOT EXISTS EstadoOferta(
    id_estadoOferta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Oferta (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    horaInicio TIME,
    fechaVencimiento DATE,
    horaVencimiento TIME,
    cantidad INT,
    id_usuario INT,
    id_obra INT,
    id_producto INT,
    id_estadoOferta INT,
    CONSTRAINT fk_producto_oferta FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_obra_oferta FOREIGN KEY (id_obra) REFERENCES Obra(id_obra),
    CONSTRAINT fk_usuario_oferta FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario),
	CONSTRAINT fk_estado_oferta FOREIGN KEY (id_estadoOferta) REFERENCES EstadoOferta(id_estadoOferta)
);

CREATE TABLE IF NOT EXISTS AporteOferta (
    id_aporteOferta INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT,
    id_oferta INT,
    CONSTRAINT fk_oferta_detalle FOREIGN KEY (id_oferta) REFERENCES Oferta(id_oferta)
);

CREATE TABLE IF NOT EXISTS Transporte (
    id_transporte INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255),
    modelo VARCHAR(255),
    patente VARCHAR(20),
    kilometraje INT,
    estadoITV VARCHAR(255),
    anio YEAR,
    imagen VARCHAR(255),
    necesita_mantenimiento BOOLEAN DEFAULT FALSE,
    descripcion_mantenimiento VARCHAR(1000)
);

CREATE TABLE IF NOT EXISTS DetalleObraTransporte (
	id_detalleObraTransporte INT AUTO_INCREMENT PRIMARY KEY,
	id_obra INT,
    id_transporte INT,
	CONSTRAINT fk_obra FOREIGN KEY (id_obra) REFERENCES Obra(id_obra),
    CONSTRAINT fk_transporte FOREIGN KEY (id_transporte) REFERENCES Transporte(id_transporte)
    );

CREATE TABLE IF NOT EXISTS DetalleObraPedido (
    id_DetalleObraPedido INT AUTO_INCREMENT PRIMARY KEY,
    id_obra int,
    id_pedido int,
    CONSTRAINT fk_obra_detalle_2 FOREIGN KEY (id_obra) REFERENCES Obra(id_obra),
    CONSTRAINT fk_pedido_detalle_2 FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

-- Inserciones para la tabla Direccion
INSERT INTO Direccion (calle, numero, localidad) VALUES 
    ('Calle Fornica', 25, 'Localidad Abedul'),
    ('Calle Ignacio', 103, 'Localidad Betular'),
    ('Calle Gonzalo', 6, 'Localidad Carlos Paz'),
    ('Calle Martinez', 42, 'Localidad Budin'),
    ('Calle Sergio', 25, 'Localidad Abedul'),
    ('Calle Roca', 103, 'Localidad Colonia Carolla'),
    ('Calle Menem', 6, 'Localidad La Estanzuela'),
    ('Calle Evita', 42, 'Localidad Perón'),
    ('Calle Desconocida', 0, 'Localidad Desconocida'), -- Asilo a refugiados sirios, Nuestra familia Siria / Acompañamiento a jóvenes adolecentes, Señor Común / Acompañamiento a personas que sufren soledad, Madre Teresa / Acompañamiento a mamás, Madre de la Ternura / Ejercicios espirituales gratuitos, Mamá Antula
	('Brasil 680, X5000CCP Córdoba', 680, 'B° Güemes'), -- Hogar de niños, Jose Bainotti
    ('X5000FGC, Libertad 171, X5000 FGC', 171, 'B° Centro'), -- Hospedería y centro de día de hombres, P. Alberto Hurtado
    ('Brasil 581, X5000CCK ', 581, 'B° Güemes'), -- Centro de Cuidados Paliativos, Casa de la Bondad
    ('Turrado Juárez 2188, 5000 Córdoba', 2188, 'B° Colinas de Vélez Sársfield'), -- Acompañamiento a mujeres HIV, Caminar de Nuevo
    ('Ruta prov. 28 al pie de Los Gigantes (ex nacional 20 km 784), Córdoba', 784, 'al pie de Los Gigantes'), -- Escuela Albergue, Nuestra Señora del Valle
    ('Establecimiento Carcelario Padre Luchesse (Cárcel de Bower)', 797, 'Santa María'), -- Acompañamientos a Privados de libertad, Cura Brochero
    ('Ruta N° 5, Km. 20', 20, 'Camino a Alta Gracia'); -- Casa de Retiros, Señorita Isabel de Hungría
    

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
INSERT INTO CustomUsuario (nombre, apellido, nombreusuario, password, documento, telefono, email, genero, imagen, fechaUnion, last_login, id_direccion, id_tipoDocumento, is_staff, is_superuser, is_active) VALUES 
    ('Joaquin', 'Lopez', 'JoaLopez', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '25129735', '+54 3517639546', 'JoaquinL@hotmail.com', 1, 'profilePictures/cn-joaco-lopez-foto-web_sq.webp', NOW(), NOW(), 1, 1, FALSE, FALSE, TRUE),
    ('Timoteo', 'Wuewuan', 'TimoelWawan', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '46505926', '+54 3517639546', 'TimoteoW@gmail.com', 1, 'profilePictures/llama.webp', NOW(), NOW(), 3, 2, FALSE, FALSE, TRUE),
    ('Teresa', 'Diaz', 'TeresitaD', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '39284767', '+54 3517639546', 'TereDiaz@gmail.com', 1, 'profilePictures/GFYCP26UX5ER3KN5AGRXQAMZ7Q.webp', NOW(), NOW(), 4, 3, FALSE, FALSE, TRUE),
    ('Admin', 'Istrador', 'admin', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'admin@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 1, 1, TRUE, TRUE, TRUE);

-- Inserciones para la tabla Obra
INSERT INTO Obra (nombre, descripcion, id_Organizacion, id_direccion, imagen) VALUES 
    ('Mama Antula', 'Ejercicios espirituales gratuitos', 1, 9, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Cura Brochero', 'Acompañamientos a Privados de libertad', 1, 15, 'obras/logo.png'),
    ('Casa de la Bondad', 'Centro de Cuidados Paliativos', 1, 12, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Jose Bainotti', 'Hogar de niños', 1, 10, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('P. Alberto Hurtado', 'Hospedería y centro de día de hombres', 1, 11, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Caminar de Nuevo', 'Acompañamiento a mujeres HIV', 1, 13, 'obras/logo.png'),
    ('Nuestra Señora del Valle', 'Escuela Albergue', 1, 14, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Nuestra familia Siria', 'Escuela Albergue', 1, 9, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Señor Común', 'Acompañamiento a jóvenes adolecentes', 1, 9, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Madre Teresa', 'Acompañamiento a personas que sufren soledad', 1, 9, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Madre de la Ternura', 'Acompañamiento a mamás', 1, 9, 'obras/manos_10152900384813092_5921720902835658172_o-300x300.webp'),
    ('Señorita Isabel de Hungría', 'Casa de Retiros', 1, 16, 'obras/logo.png');

-- Inserciones para la tabla DetalleObraUsuario
INSERT INTO DetalleObraUsuario (descripcion, fechaIngreso, id_obra, id_usuario, id_tipousuario) VALUES 
    ('Se ofrece a cuidar de personas con necesidad', '2023-12-26', 1, 1, 2),
    ('Ofrecen apoyo escolar, actividades culturales, deportivas, talleres sobre crianza, alimentación saludable y asesoramiento sobre trámites.', '2024-01-12', 2, 2, 2),
    ('Cuenta con un equipo de voluntarios y profesionales que trabajan juntos para lograr su misión de amar y servir a cada uno de sus beneficiarios.', '2024-3-09', 3, 3, 2); 

-- Inserciones para la tabla UnidadMedida
INSERT INTO UnidadMedida (nombre, descripcion, identificador, paquete) VALUES 
    ('Kilogramos', 'Son Kilogramos', 'Kg', FALSE),
    ('Litros', 'Son Litros', 'l', FALSE),
    ('Gramos', 'Son Gramos', 'g', FALSE),
    ('Paquete en Kg', 'Es un paquete en Kilogramos', 'x', TRUE),
    ('Paquete en l', 'Es un paquete en Litros', 'x', TRUE),
    ('Paquete en g', 'Es un paquete en Gramos', 'x', TRUE),
    ('Unidad', 'Un objecto', '', FALSE),
    ('Miligramos', 'Son Gramos', 'g', TRUE);

-- Inserciones para la tabla Stock
INSERT INTO Stock (id_obra) VALUES 
    (1),
    (2),
    (3);

-- Inserciones para la tabla Categoria
INSERT INTO Categoria (nombre, descripcion) VALUES 
    ('Comida', 'Alimentos, enlatados, percederos y no percederos,etc.'),
    ('Medicina', 'Pastillas y Tabletas.'),
    ('Muebles', 'Muebles que pueden ser ofrecidos.');

-- Inserciones para la tabla CategoriaProducto
INSERT INTO CategoriaProducto (nombre, descripcion, id_categoria) VALUES 
    ('Perecedero', 'Productos con fecha de vencimiento.', 1),
    ('No perecederos', 'Productos sin fecha de vencimiento.', 1),
    ('Enlatados', 'Productos en lata.', 1),
	('Medicina', 'Medicinas', 2),
    ('Muebles', 'Muebles', 3);

-- Inserciones para la tabla Producto
INSERT INTO Producto (nombre, descripcion, id_categoriaProducto, id_unidadMedida, imagen) VALUES 
    ('Arroz', 'Paquete de arroz de 1Kg', 2, 1, 'productos/Lucchetti_Arroz_Largo_Fino_1_kg__Bolsa_.webp'),
    ('Fideos', 'Paquete de fideideos', 2, 1, 'productos/spaguetti__70855.jpg'),
    ('Pure de tomate', 'Pure de tomate 500 ml', 1, 1, 'productos/Pur-de-Tomate-Marolio-520-Gr-1-4243.webp'),
	('Yerba', 'Paquete de Yerba de 1Kg', 1, 4, 'productos/yerba.jpg'),
    ('Queso Cremoso', 'Orna de Queso cremoso de 4 Kg', 2, 1, 'productos/queso.jpg'),
    ('Avena', 'Paquete de avena de 400 g', 2, 6, 'productos/avena.jpg'),
    ('Paracetamol', 'Analgésico y antipirético de 500 mg', 4, 8, 'productos/Paracetamol.jpg'),
    ('Ibuprofeno', 'Antiinflamatorio de 400 mg', 4, 8, 'productos/Ibuprofeno.jpg'),
    ('Amoxicilina', 'Antibiótico de 500 mg', 4, 8, 'productos/Amoxicilina.png'),
    ('Pupitre', 'Pupitre basico', 5, 7, 'productos/mueble1.jpg'),
    ('Placar', 'Placar 2 puertas basico', 5, 7, 'productos/mueble2.jpg');

-- Inserciones para la tabla EstadoPedido
INSERT INTO EstadoPedido (nombre, descripcion) VALUES 
    ('Pendiente', 'Solo es un pedido y no se hizo nada'),
    ('En Proceso', 'Transporte se encarga de llevar este pedido que ahora esta en procesosta en proceso el pedido'),
    ('Finalizado', 'El pedido llego a la obral pedido ya esta finalizado.');

-- Inserciones para la tabla Pedido
INSERT INTO Pedido (fechaInicio, horaInicio, fechaVencimiento, horaVencimiento, cantidad, id_obra, id_usuario, id_producto, urgente, id_estadoPedido) VALUES 
    ('2024-06-14', '09:05:00', '2024-06-28', '09:05:00', 200, 1, 1, 3, 1, 1),
    ('2024-04-08', '13:00:00', '2024-04-15', '13:00:00', 200, 2, 2, 1, 2, 2),
    ('2024-09-23', '17:27:00', '2024-10-23', '17:27:00', 200, 3, 3, 2, 3, 3),
	('2024-06-14', '09:05:00', '2024-06-28', '09:05:00', 200, 1, 1, 4, 1, 1),
    ('2024-04-08', '13:00:00', '2024-04-15', '13:00:00', 200, 2, 2, 5, 2, 2),
    ('2024-09-23', '17:27:00', '2024-10-23', '17:27:00', 200, 3, 3, 6, 3, 3),
	('2024-06-14', '09:05:00', '2024-06-28', '09:05:00', 200, 1, 1, 7, 1, 1),
    ('2024-04-08', '13:00:00', '2024-04-15', '13:00:00', 200, 2, 2, 8, 2, 2),
    ('2024-09-23', '17:27:00', '2024-10-23', '17:27:00', 200, 3, 3, 9, 3, 3),
    ('2024-04-08', '13:00:00', '2024-04-15', '13:00:00', 1, 2, 1, 10, 2, 2),
    ('2024-09-23', '17:27:00', '2024-10-23', '17:27:00', 1, 3, 1, 11, 3, 3);

-- Inserciones para la tabla EstadoOferta
INSERT INTO EstadoOferta (nombre, descripcion) VALUES 
    ('Disponible', 'La oferta aun esta disponible y los usuarios pueden verla para reservarla'),
    ('Reservado', 'La oferta esta reservada y los usuarios dejan verla'),
    ('Reclamado', 'La oferta que etaba en reserva ya fue transportada hasta la obra que la reclamo');

-- Inserciones para la tabla Oferta
INSERT INTO Oferta (fechaInicio, horaInicio, fechaVencimiento, horaVencimiento, cantidad, id_usuario, id_obra, id_producto, id_estadoOferta) VALUES 
    ('2024-01-14', '08:01:31', '2024-01-28', '08:01:31', 200, 1, 1, 3, 1),
    ('2023-08-10', '16:08:10', '2023-08-17', '16:08:10', 200, 3, 2, 2, 2),
    ('2024-04-30', '14:27:57', '2024-05-30', '14:27:57', 200, 2, 3, 1, 3),
    ('2024-01-10', '02:10:01', '2024-02-10', '08:01:31', 20, 1, 1, 4, 1),
    ('2023-08-02', '13:00:10', '2023-09-02', '16:08:10', 12, 3, 2, 5, 2),
    ('2024-04-01', '06:27:00', '2024-05-01', '14:27:57', 30, 2, 3, 6, 3),
    ('2024-01-10', '02:10:01', '2024-02-10', '08:01:31', 20, 1, 1, 7, 1),
    ('2023-08-02', '13:00:10', '2023-09-02', '16:08:10', 15, 3, 2, 8, 2),
    ('2024-04-01', '06:27:00', '2024-05-01', '14:27:57', 5, 2, 3, 9, 3),
    ('2023-08-02', '13:00:10', '2023-09-02', '16:08:10', 1, 1, 3, 10, 2),
    ('2024-04-01', '06:27:00', '2024-05-01', '14:27:57', 1, 1, 2, 11, 3);

-- Inserciones para la tabla Transporte
INSERT INTO Transporte (marca, modelo, patente, kilometraje, estadoITV, anio, imagen, necesita_mantenimiento, descripcion_mantenimiento) VALUES 
    ('Toyota', 'Hilux', 'NXD838', 10000, 'En Forma', '2022', 'vehiculos/toyota-hilux-on-the-road.webp', FALSE, ''),
    ('Renault', 'Logan', 'AA001AB', 20000, 'Vencido', '2020', 'vehiculos/renault-sandero-y-logan-1269058.webp', FALSE, ''),
    ('Peugeot', '3008 GT', 'AG500AA', 30000, 'En Forma', '2018', 'vehiculos/zaatogjy9axfzmntave4.webp', FALSE, '');
    
    -- Inserciones para la tabla DetalleObraTransporte
    INSERT INTO DetalleObraTransporte (id_obra, id_transporte) VALUES 
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 3);

insert into DetalleStockProducto (titulo, descripcion, imagen, cantidad, cantidadUnidades, id_stock, id_producto, id_unidadMedida) values
	("titulo", "descripcion", "productos/detalles/no_image.png", 100, 1, 1, 2, 1),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 200, 1, 3, 3, 1),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 300, 1, 2, 1, 3),
	("titulo", "descripcion", "productos/detalles/no_image.png", 1, 20, 1, 1, 3),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 16, 1, 3, 2, 1),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 400, 30, 3, 6, 6),
	("titulo", "descripcion", "productos/detalles/no_image.png", 500, 20, 2, 7, 8),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 400, 15, 2, 8, 8),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 500, 5, 1, 9, 8),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 1, 1, 1, 10, 7),
    ("titulo", "descripcion", "productos/detalles/no_image.png", 1, 1, 1, 11, 7);
    
insert into AportePedido (descripcion,cantidad,id_pedido) values 
('desc1',10,1),
('desc2',20,2),
('desc3',30,3)
;
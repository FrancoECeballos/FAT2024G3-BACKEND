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
    abreviacion VARCHAR(20),
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
    CONSTRAINT fk_transporte_obra FOREIGN KEY (id_transporte) REFERENCES Transporte(id_transporte)
);

CREATE TABLE IF NOT EXISTS Stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_obra INT,
	CONSTRAINT fk_obra_stock FOREIGN KEY (id_obra) REFERENCES Obra(id_obra)
);

CREATE TABLE IF NOT EXISTS Categoria (
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    imagen VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    id_categoria INT,
    unidadMedida INT,
    talle VARCHAR(255),
    cantidad_por_unidad INT,
    imagen VARCHAR(255),
    perecedero BOOLEAN DEFAULT FALSE,
    tiene_talle BOOLEAN DEFAULT FALSE,
    enlatado BOOLEAN DEFAULT FALSE,
    requiere_refrigeracion BOOLEAN DEFAULT FALSE,
    sin_TAC BOOLEAN DEFAULT FALSE,
    sin_azucares BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE IF NOT EXISTS DetalleStockProducto (
    id_detalleStockProducto INT AUTO_INCREMENT PRIMARY KEY,
    cantidad FLOAT,
    checkpoint BOOLEAN,
    fecha_creacion DATETIME,
    id_stock INT,
    id_producto INT,
    id_usuario INT,
    CONSTRAINT fk_producto_detalle_stock FOREIGN KEY (id_producto) REFERENCES Producto(id_producto),
    CONSTRAINT fk_stock_detalle_stock FOREIGN KEY (id_stock) REFERENCES Stock(id_stock),
    CONSTRAINT fk_usuario_detalle_stock FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS EstadoPedido(
    id_estadoPedido INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    fechaVencimiento DATE,
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
    cantidad INT not null,
    fechaAportado DATE,
    id_pedido INT,
    id_obra INT,
    id_usuario INT,
    CONSTRAINT fk_aportePedido FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
	CONSTRAINT fk_usuario_aportePedido FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario),
    CONSTRAINT fk_obra_aportePedido FOREIGN KEY (id_obra) REFERENCES Obra(id_obra)
);

CREATE TABLE IF NOT EXISTS EstadoOferta(
    id_estadoOferta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Oferta (
    id_oferta INT AUTO_INCREMENT PRIMARY KEY,
    fechaInicio DATE,
    fechaVencimiento DATE,
    cantidad INT,
    id_usuario INT,
    id_obra INT,
    id_producto INT,
    id_estadoOferta INT,
    CONSTRAINT fk_producto_oferta FOREIGN KEY (id_producto)
        REFERENCES Producto (id_producto),
    CONSTRAINT fk_obra_oferta FOREIGN KEY (id_obra)
        REFERENCES Obra (id_obra),
    CONSTRAINT fk_usuario_oferta FOREIGN KEY (id_usuario)
        REFERENCES CustomUsuario (id_usuario),
    CONSTRAINT fk_estado_oferta FOREIGN KEY (id_estadoOferta)
        REFERENCES EstadoOferta (id_estadoOferta)
);

CREATE TABLE IF NOT EXISTS AporteOferta (
    id_aporteOferta INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255),
    cantidad INT not null,
    fechaAportado DATE,
    fechaEntrega DATE, 
    id_oferta INT,
    id_obra INT,
    id_usuario INT,
    CONSTRAINT fk_aporteOferta FOREIGN KEY (id_oferta) REFERENCES Oferta(id_oferta),
	CONSTRAINT fk_usuario_aporteOferta FOREIGN KEY (id_usuario) REFERENCES CustomUsuario(id_usuario),
    CONSTRAINT fk_obra_aporteOferta FOREIGN KEY (id_obra) REFERENCES Obra(id_obra)
);
    
CREATE TABLE IF NOT EXISTS Entrega (
	id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    fechaCreacion DATE,
	id_pedido INT NULL,
    id_oferta INT NULL,
    CONSTRAINT fk_pedido FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    CONSTRAINT fk_oferta FOREIGN KEY (id_oferta) REFERENCES Oferta(id_oferta)
);

CREATE TABLE IF NOT EXISTS EstadoEntrega(
    id_estadoEntrega INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS EntregaAporte (
	id_entregaAporte INT AUTO_INCREMENT PRIMARY KEY,
    fechaEntrega DATE, 
    id_entrega INT,
	id_aportePedido INT NULL,
    id_aporteOferta INT NULL,
    id_transporte INT,
    id_estadoEntrega INT, 
    CONSTRAINT fk_entrega FOREIGN KEY (id_entrega) REFERENCES Entrega(id_entrega),
    CONSTRAINT fk_aportePedido_entrega FOREIGN KEY (id_aportePedido) REFERENCES AportePedido(id_aportePedido),
    CONSTRAINT fk_aporteOferta_entrega FOREIGN KEY (id_aporteOferta) REFERENCES AporteOferta(id_aporteOferta),
    CONSTRAINT fk_estadoEntrega FOREIGN KEY (id_estadoEntrega) REFERENCES EstadoEntrega(id_estadoEntrega),
    CONSTRAINT fk_transporte FOREIGN KEY (id_transporte) REFERENCES Transporte(id_transporte)
);

CREATE TABLE IF NOT EXISTS DetalleObraPedido (
    id_DetalleObraPedido INT AUTO_INCREMENT PRIMARY KEY,
    id_stock int,
    id_pedido int,
    CONSTRAINT fk_stock_detalle_2 FOREIGN KEY (id_stock) REFERENCES Stock(id_stock),
    CONSTRAINT fk_pedido_detalle_2 FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);

-- Inserciones para la tabla Direccion
INSERT INTO Direccion (calle, numero, localidad) VALUES 
    ('Av. Republica de China', 25, 'Valle Escondido'),
    ('Calle San Martín', 50, 'Centro'),
    ('Av. Libertad', 123, 'Barrio Norte'),
    ('Calle Los Andes', 75, 'La Colina'),
    ('Av. Independencia', 80, 'Villa del Parque'),
    ('Calle Belgrano', 45, 'San Isidro'),
    ('Av. Ejercito Argentino', 6, 'Cordoba'),
    ('Calle Evita', 42, 'Localidad Perón'),
    ('Calle Desconocida', 0, 'Localidad Desconocida'), -- Asilo a refugiados sirios, Nuestra familia Siria / Acompañamiento a jóvenes adolecentes, Sueño Común / Acompañamiento a personas que sufren soledad, Madre Teresa / Acompañamiento a mamás, Madre de la Ternura / Ejercicios espirituales gratuitos, Mamá Antula
	('Brasil 680, X5000CCP Córdoba', 680, 'B° Güemes'), -- Hogar de niños, Jose Bainotti
    ('X5000FGC, Libertad 171, X5000 FGC', 171, 'B° Centro'), -- Hospedería y centro de día de hombres, P. Alberto Hurtado
    ('Brasil 581, X5000CCK ', 581, 'B° Güemes'), -- Centro de Cuidados Paliativos, Casa de la Bondad
    ('Turrado Juárez 2188, 5000 Córdoba', 2188, 'B° Colinas de Vélez Sársfield'), -- Acompañamiento a mujeres HIV, Caminar de Nuevo
    ('Ruta prov. 28 al pie de Los Gigantes (ex nacional 20 km 784), Córdoba', 784, 'al pie de Los Gigantes'), -- Escuela Albergue, Nuestra Señora del Valle
    ('Establecimiento Carcelario Padre Luchesse (Cárcel de Bower)', 797, 'Santa María'), -- Acompañamientos a Privados de libertad, Cura Brochero
    ('Ruta N° 5, Km. 20', 20, 'Camino a Alta Gracia'), -- Casa de Retiros, Señorita Isabel de Hungría
    ('Calle Sol de Mayo', 100, 'Nueva Cordoba'),
    ('Av. Las Heras', 200, 'General Paz'),
    ('Calle Lavalle', 150, 'Alberdi'),
    ('Av. Colon', 300, 'Centro'),
    ('Calle Buenos Aires', 250, 'Nueva Cordoba'),
    ('Av. Sabattini', 600, 'San Vicente'),
    ('Calle San Juan', 80, 'Centro'),
    ('Calle Italia', 120, 'General Paz'),
    ('Av. La Voz del Interior', 700, 'Aeropuerto'),
    ('Calle Obispo Trejo', 450, 'Centro'),
    ('Calle Paraguay', 340, 'General Paz'),
    ('Calle Dean Funes', 210, 'Centro'),
    ('Calle Salta', 180, 'Alta Cordoba'),
    ('Calle Mendoza', 130, 'Alberdi'),
    ('Av. Santa Fe', 275, 'General Paz'),
    ('Calle Tucumán', 190, 'Centro'),
    ('Calle Catamarca', 500, 'San Vicente'),
    ('Calle La Rioja', 175, 'Alta Cordoba'),
    ('Av. Fuerza Aérea', 540, 'Las Palmas'),
    ('Calle Bolivia', 600, 'Parque Liceo');
    

-- Inserciones para la tabla Organizacion
INSERT INTO Organizacion (nombre, descripcion, telefono, email) VALUES 
    ('Manos Abiertas','Manos Abiertas de la provincia de Córdoba', '0351 423 5140', 'cordoba@manosabiertas.org.ar');

-- Inserciones para la tabla TipoUsuario
INSERT INTO TipoUsuario (nombre, abreviacion, descripcion) VALUES 
    ('Voluntario', 'user', 'Es un voluntario, usuario común del sistema'),
    ('Moderador', 'mod', 'Es un moderador de esta Obra, puede manejar usuarios'),
    ('Administrador', 'admin', 'Es un administrador de la organización, puede manejar obras y usuarios');

INSERT INTO TipoDocumento (nombre, descripcion) VALUES 
    ('DNI', 'Es un documento de identidad'),
    ('Pasaporte', 'Es un documento de viaje'),
    ('Cedula', 'Es un documento de identidad');

-- Inserciones para la tabla Usuario
INSERT INTO CustomUsuario (nombre, apellido, nombreusuario, password, documento, telefono, email, genero, imagen, fechaUnion, last_login, id_direccion, id_tipoDocumento, is_staff, is_superuser, is_active) VALUES 
    ('Joaquin', 'Lopez', 'JoaLopez', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '25129735', '+54 3517639546', 'JoaquinL@hotmail.com', 1, 'profilePictures/the-legend-of-zelda-minimalista_8000x4500_xtrafondos.com.jpg', NOW(), NOW(), 1, 1, FALSE, FALSE, TRUE),
    ('Timoteo', 'Wuewuan', 'TimoelWawan', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '46505926', '+54 3517639546', 'TimoteoW@gmail.com', 1, 'profilePictures/One_billion_Draculas.jpeg', NOW(), NOW(), 3, 2, FALSE, FALSE, TRUE),
    ('Teresa', 'Diaz', 'TeresitaD', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '39284767', '+54 3517639546', 'TereDiaz@gmail.com', 1, 'profilePictures/maria.jpeg', NOW(), NOW(), 4, 3, FALSE, FALSE, TRUE),
    ('Admin', 'Istrador', 'admin', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'admin@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 1, 1, TRUE, TRUE, TRUE),
    ('Alberto Hurtado', 'Admin1', 'albertohurtado', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 3514234682', 'hospederia.cba@manosabiertas.org.ar', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 2, 1, TRUE, FALSE, TRUE), -- Hospedería y centro de día de hombres, P. Alberto Hurtado
    ('Casa de la Bondad', 'Admin2', 'casabondad', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 3518947780', 'casadelabondad.cba@manosabiertas.org.ar', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 5, 1, TRUE, FALSE, TRUE), -- Centro de Cuidados Paliativos, Casa de la Bondad
    ('Caminar de Nuevo', 'Admin3', 'caminarnuevo', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Caminar@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 6, 1, TRUE, FALSE, TRUE), -- Acompañamiento a mujeres HIV, Caminar de Nuevo
    ('Señora del Valle', 'Admin4', 'señoravalle', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Valle@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 6, 1, TRUE, FALSE, TRUE), -- Escuela Albergue, Nuestra Señora del Valle
    ('Familia Siria', 'Admin5', 'familiasiria', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Siria@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 7, 1, TRUE, FALSE, TRUE), -- Asilo a refugiados sirios, Nuestra familia Siria
    ('Sueño Común', 'Admin6', 'señorcomun', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Común@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 8, 1, TRUE, FALSE, TRUE), -- Acompañamiento a jóvenes adolecentes, Sueño Común
    ('Madre Teresa', 'Admin7', 'madreteresa', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Teresa@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 2, 1, TRUE, FALSE, TRUE), -- Acompañamiento a personas que sufren soledad, Madre Teresa
    ('Cura Brochero', 'Admin8', 'curabrochero', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Brochero@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 8, 1, TRUE, FALSE, TRUE), -- Acompañamientos a Privados de libertad, Cura Brochero
    ('Madre de la Ternura', 'Admin9', 'madreternura', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Ternura@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 1, 1, TRUE, FALSE, TRUE), -- Acompañamiento a mamás, Madre de la Ternura
    ('Mamá Antula', 'Admin10', 'mamaantula', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Antula@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 8, 1, TRUE, FALSE, TRUE), -- Ejercicios espirituales gratuitos, Mamá Antula
    ('Isabel de Hungría', 'Admin11', 'isabelhungria', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'Hungría@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 3, 1, TRUE, FALSE, TRUE), -- Casa de Retiros, Señorita Isabel de Hungría
    ('Jose', 'Bainotti', 'admin7', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'jose@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- Hogar de niños, Jose Bainotti,
    ('Santa', 'Clara', 'adminferia', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'santaclara@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- Feria Santa Clara
    ('Recursos', 'Materiales', 'adminmateriales', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'materiales@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- Recursos Materiales
    ('Recursos', 'Economicos', 'admineconomico', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'economicos@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- Recursos Economicos
    ('Admin', 'Voluntariado', 'adminvoluntariado', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'voluntariado@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- Voluntariado
    ('Administrador', 'Sede', 'adminsede', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'sede@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, TRUE, FALSE, TRUE), -- ADMINISTRACION/SEDE
    ('Voluntario', '1', 'voluntario1preba', 'pbkdf2_sha256$720000$byAGpfEaFDWh8edVUetdkL$yWaV0a6nPiFOqq5mWRfbOdiL25rDzMBXKGb1awJYJuM=', '00000000', '+54 00000000', 'voluntario.1.prueba@admin', 3, 'profilePictures/perro-gafas.webp', NOW(), NOW(), 10, 1, False, FALSE, False), -- Default user sin obra
    ('Matias', 'Gonzalez', 'matiasg', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '33225478', '+54 3517631111', 'matiasg@gmail.com', 1, 'profilePictures/dino.png', NOW(), NOW(), 17, 1, FALSE, FALSE, TRUE),
    ('Lucia', 'Martinez', 'luciam', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '41356789', '+54 3517632222', 'luciam@gmail.com', 2, 'profilePictures/llama.webp', NOW(), NOW(), 18, 2, FALSE, FALSE, TRUE),
    ('Santiago', 'Lopez', 'santil', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '38567890', '+54 3517633333', 'santil@gmail.com', 1, 'profilePictures/the-legend-of-zelda-minimalista_8000x4500_xtrafondos.com.jpg', NOW(), NOW(), 19, 1, FALSE, FALSE, TRUE),
    ('Carla', 'Suarez', 'carlas', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '29765432', '+54 3517634444', 'carlas@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 20, 2, FALSE, FALSE, TRUE),
    ('Pablo', 'Fernandez', 'pablof', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '34512345', '+54 3517635555', 'pablof@gmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 21, 1, FALSE, FALSE, TRUE),
    ('Natalia', 'Perez', 'nataliap', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '39123456', '+54 3517636666', 'nataliap@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 22, 2, FALSE, FALSE, TRUE),
    ('Andres', 'Gutierrez', 'andresg', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '40765432', '+54 3517637777', 'andresg@gmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 23, 1, FALSE, FALSE, TRUE),
    ('Valeria', 'Lopez', 'valerial', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '39233456', '+54 3517638888', 'valerial@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 24, 2, FALSE, FALSE, TRUE),
    ('Federico', 'Ramirez', 'federicor', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '38123432', '+54 3517639999', 'federicor@gmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 25, 1, FALSE, FALSE, TRUE),
    ('Julia', 'Hernandez', 'juliah', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '41234567', '+54 3517640000', 'juliah@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 26, 2, FALSE, FALSE, TRUE),
    ('Emiliano', 'Gomez', 'emilianog', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '30234567', '+54 3517641111', 'emilianog@gmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 27, 1, FALSE, FALSE, TRUE),
    ('Micaela', 'Torres', 'micaelat', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '41123457', '+54 3517642222', 'micaelat@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 28, 2, FALSE, FALSE, TRUE),
    ('Leandro', 'Sosa', 'leandros', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '36345678', '+54 3517643333', 'leandros@gmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 29, 1, FALSE, FALSE, TRUE),
    ('Ana', 'Mendez', 'anam', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '38765432', '+54 3517644444', 'anam@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 30, 2, FALSE, FALSE, TRUE),
    ('Juan', 'Alvarez', 'JuanA', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '31123456', '+54 3517890123', 'juan.alvarez@hotmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 31, 1, FALSE, FALSE, TRUE),
    ('Marta', 'Sanchez', 'MartaS', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '27123456', '+54 3518901234', 'martasanchez@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 32, 1, FALSE, FALSE, TRUE),
    ('Luis', 'Diaz', 'LuisD', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '25123456', '+54 3519012345', 'luis.diaz@yahoo.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 33, 1, FALSE, FALSE, TRUE),
    ('Paula', 'Moreno', 'PaulaM', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '24123456', '+54 3510123456', 'paula.moreno@gmail.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 34, 1, FALSE, FALSE, TRUE),
    ('Tomas', 'Garcia', 'TomasG', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '23123456', '+54 3511123456', 'tomasgarcia@hotmail.com', 1, 'profilePictures/user_default.png', NOW(), NOW(), 35, 1, FALSE, FALSE, TRUE),
    ('Clara', 'Castro', 'ClaraC', 'pbkdf2_sha256$720000$RkSTwAdm8dhu9zo4lLWKyb$faBGt4+ZG9bo+kihGfvj97sxktvsALIe3Q+c4bnvEqU=', '22123456', '+54 3512234567', 'claracastro@yahoo.com', 2, 'profilePictures/user_default.png', NOW(), NOW(), 36, 1, FALSE, FALSE, TRUE);
	
-- Inserciones para la tabla Obra
INSERT INTO Obra (nombre, descripcion, id_Organizacion, id_direccion, imagen) VALUES 
    ('Mama Antula', 'Ejercicios espirituales gratuitos', 1, 9, 'obras/logo.png'),
    ('Cura Brochero', 'Acompañamientos a Privados de libertad', 1, 15, 'obras/logo.png'),
    ('Casa de la Bondad', 'Centro de Cuidados Paliativos', 1, 12, 'obras/logo.png'),
    ('Jose Bainotti', 'Hogar de niños', 1, 10, 'obras/logo.png'),
    ('P. Alberto Hurtado', 'Hospedería y centro de día de hombres', 1, 11, 'obras/logo.png'),
    ('Caminar de Nuevo', 'Acompañamiento a mujeres HIV', 1, 13, 'obras/logo.png'),
    ('Nuestra Señora del Valle', 'Escuela Albergue', 1, 14, 'obras/logo.png'),
    ('Nuestra familia Siria', 'Escuela Albergue', 1, 9, 'obras/logo.png'),
    ('Sueño Común', 'Acompañamiento a jóvenes adolecentes', 1, 9, 'obras/logo.png'),
    ('Madre Teresa', 'Acompañamiento a personas que sufren soledad', 1, 9, 'obras/logo.png'),
    ('Madre de la Ternura', 'Acompañamiento a mamás', 1, 9, 'obras/logo.png'),
    ('Señorita Isabel de Hungría', 'Casa de Retiros', 1, 16, 'obras/logo.png'), --
    ('Santa Clara', 'Feria', 1, 9, 'obras/logo.png'),
    ('Recursos Materiales', 'Material', 1, 9, 'obras/logo.png'),
    ('Recursos Economicos', 'Capital', 1, 9, 'obras/logo.png'),
    ('Voluntariado', 'Voluntariado', 1, 9, 'obras/logo.png'),
    ('Administracion/Sede', 'Sede', 1, 9, 'obras/logo.png');

-- Inserciones para la tabla DetalleObraUsuario
INSERT INTO DetalleObraUsuario (descripcion, fechaIngreso, id_obra, id_usuario, id_tipousuario) VALUES 
    ('Se ofrece a cuidar de personas con necesidad', '2023-12-26', 1, 1, 1),
    ('Ofrecen apoyo escolar, actividades culturales, deportivas, talleres sobre crianza, alimentación saludable y asesoramiento sobre trámites.', '2024-01-12', 2, 2, 1),
    ('Cuenta con un equipo de voluntarios y profesionales que trabajan juntos para lograr su misión de amar y servir a cada uno de sus beneficiarios.', '2024-3-09', 3, 3, 1), 
	('Administrar la obra Mama Antula', '2023-12-26', 1, 14, 2),
    ('Administrar la obra Cura Brochero', '2024-01-12', 2, 12, 2),
    ('Administrar la obra Casa de la Bondad', '2024-3-09', 3, 6, 2),
    ('Administrar la obra Jose Bainotti', '2023-12-26', 4, 16, 2),
    ('Administrar la obra P. Alberto Hurtado', '2024-01-12', 5, 5, 2),
    ('Administrar la obra Caminar de Nuevo', '2024-3-09', 6, 7, 2),
    ('Administrar la obra Nuestra Señora del Valle', '2023-12-26', 7, 8, 2),
    ('Administrar la obra Nuestra familia Siria', '2024-01-12', 8, 9, 2),
    ('Administrar la obra Sueño Común', '2024-3-09', 9, 10, 2),
    ('Administrar la obra Madre Teresa', '2023-12-26', 10, 11, 2),
    ('Administrar la obra Madre de la Ternura', '2024-01-12', 11, 13, 2),
    ('Administrar la obra Señorita Isabel de Hungría', '2024-3-09', 12, 15, 2),
    ('Administrar la feria Santa Clara', '2024-3-09', 13, 17, 2),
    ('Administrar Recursos Materiales', '2024-3-09', 14, 18, 2),
    ('Administrar Recursos Economicos', '2024-3-09', 15, 19, 2),
    ('Administrar el Voluntariado', '2024-3-09', 16, 20, 2),
    ('Administrar la Sede', '2024-3-09', 17, 21, 2),
    ('Apoyo en la distribución de alimentos a personas necesitadas', '2023-12-26', 1, 23, 1),
    ('Colaboración en talleres de desarrollo personal y emocional', '2024-01-12', 2, 24, 1),
    ('Ayuda en la organización de eventos comunitarios', '2024-03-09', 3, 25, 1), 
    ('Coordinación del equipo de voluntarios en la obra Mama Antula', '2023-12-26', 1, 26, 2),
    ('Gestión administrativa y apoyo logístico en la obra Cura Brochero', '2024-01-12', 2, 27, 2),
    ('Supervisión de actividades en la obra Casa de la Bondad', '2024-03-09', 3, 28, 2),
    ('Responsable de coordinación de voluntariado en la obra Jose Bainotti', '2023-12-26', 4, 29, 2),
    ('Encargado de logística en la obra P. Alberto Hurtado', '2024-01-12', 5, 30, 2),
    ('Gestión de recursos en la obra Caminar de Nuevo', '2024-03-09', 6, 31, 2),
    ('Supervisión de actividades y voluntariado en la obra Nuestra Señora del Valle', '2023-12-26', 7, 32, 2),
    ('Coordinación de la obra Nuestra familia Siria', '2024-01-12', 8, 33, 2),
    ('Responsable de organización en la obra Sueño Común', '2024-03-09', 9, 34, 2),
    ('Encargado de la obra Madre Teresa', '2023-12-26', 10, 35, 2),
    ('Apoyo en la obra Madre de la Ternura', '2024-01-12', 11, 36, 2);


-- Inserciones para la tabla Stock
INSERT INTO Stock (id_obra) VALUES 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10),
    (11),
    (12),
    (13),
    (14),
    (15),
    (16),
    (17);

-- Inserciones para la tabla Categoria
INSERT INTO Categoria (nombre, descripcion, imagen) VALUES 
    ('Comida', 'Alimentos, enlatados, percederos y no percederos,etc.', 'categorias/comidaLogo.png'),
    ('Ropa', 'Ropa, para vestir', 'categorias/ropaLogo.png'),
    ('Muebles', 'Muebles que pueden ser ofrecidos.', 'categorias/mueblesLogo.png');

-- Inserciones para la tabla Producto
INSERT INTO Producto (nombre, descripcion, id_categoria, unidadMedida, imagen, perecedero) VALUES 
    ('Arroz', 'Paquete de arroz de 1Kg', 1, 1, 'productos/Lucchetti_Arroz_Largo_Fino_1_kg__Bolsa_.webp', FALSE),
    ('Fideos', 'Paquete de fideideos', 1, 1, 'productos/spaguetti__70855.jpg', FALSE),
    ('Pure de tomate', 'Pure de tomate 500 ml', 1, 2, 'productos/Pur-de-Tomate-Marolio-520-Gr-1-4243.webp', FALSE),
	('Yerba', 'Paquete de Yerba de 1Kg', 1, 1, 'productos/yerba.jpg', FALSE),
    ('Queso Cremoso', 'Orna de Queso cremoso de 4 Kg', 1, 1, 'productos/queso.jpg', TRUE),
    ('Avena', 'Paquete de avena de 400 g', 1, 1, 'productos/avena.jpg', FALSE),
    ('Harina', 'Paquete de harina de trigo 1Kg', 1, 1, 'productos/harina.webp', FALSE),
    ('Leche', 'Botella de leche de 1 litro', 1, 2, 'productos/leche.webp', TRUE),
    ('Azúcar', 'Paquete de azúcar de 1Kg', 1, 1, 'productos/azucar.webp', FALSE),
    ('Aceite', 'Botella de aceite de girasol 1 litro', 1, 2, 'productos/aceite.webp', FALSE),
    ('Galletitas', 'Paquete de galletitas dulces 200g', 1, 1, 'productos/galletitas.webp', FALSE),
    ('Jugo de Naranja', 'Jugo de naranja en caja 1 litro', 1, 2, 'productos/jugoNaranja.webp', TRUE);
    
INSERT INTO Producto (nombre, descripcion, id_categoria, unidadMedida, imagen) VALUES 
    ('Pupitre', 'Pupitre basico', 3, 0, 'productos/mueble1.jpg'),
    ('Placar', 'Placar 2 puertas basico', 3, 0, 'productos/mueble2.jpg'),
    ('Silla', 'Silla de madera básica', 3, 0, 'productos/silla.webp'),
    ('Mesa de comedor', 'Mesa de comedor para 4 personas', 3, 0, 'productos/mesaCOmedor.webp'),
    ('Estante', 'Estante de pared de madera', 3, 0, 'productos/Estante.webp'),
    ('Sofá', 'Sofá de 2 plazas', 3, 0, 'productos/Sofá.webp'),
    ('Escritorio', 'Escritorio básico de madera', 3, 0, 'productos/Escritorio.webp');

INSERT INTO Producto (nombre, descripcion, id_categoria, unidadMedida, talle, imagen, perecedero) VALUES 
    ('Camisa', 'Camisa de manga larga', 2, 0, "l", 'productos/camisa.webp', FALSE),
    ('Pantalón', 'Pantalón de mezclilla', 2, 0, "s", 'productos/pantalon.webp', FALSE),
    ('Vestido', 'Vestido elegante', 2, 0, "xl", 'productos/vestido.webp', FALSE),
    ('Camiseta', 'Camiseta de algodón', 2, 0, 'm', 'productos/Camiseta-negra.webp', FALSE),
    ('Chaleco', 'Chaleco abrigado', 2, 0, 'l', 'productos/Chaleco.webp', FALSE),
    ('Falda', 'Falda corta', 2, 0, 's', 'productos/Falda.webp', FALSE),
    ('Abrigo', 'Abrigo de invierno', 2, 0, 'xl', 'productos/Abrigo.webp', FALSE),
    ('Zapatos', 'Zapatos deportivos', 2, 0, '42', 'productos/Zapatos.webp', FALSE);

-- Inserciones para la tabla EstadoPedido
INSERT INTO EstadoPedido (nombre, descripcion) VALUES 
    ('Pendiente', 'Solo es un pedido y no se hizo nada'),
    ('En Proceso', 'Transporte se encarga de llevar este pedido que ahora esta en procesosta en proceso el pedido'),
    ('Finalizado', 'El pedido llego a la obral pedido ya esta finalizado.'),
    ('Cancelado', 'El pedido fue cancelado por el usuario que lo hizo'),
    ('Vencido', 'El pedido ya vencio y no se puede reservar');

-- Inserciones para la tabla Pedido
INSERT INTO Pedido (fechaInicio, fechaVencimiento, cantidad, id_obra, id_usuario, id_producto, urgente, id_estadoPedido) VALUES 
    ('2024-06-14', '2024-06-28', 200, 1, 1, 3, 1, 1),
    ('2024-04-08', '2024-04-15', 200, 2, 2, 1, 2, 2),
    ('2024-09-23', '2024-10-23', 200, 3, 3, 2, 3, 3),
    ('2024-06-14', '2024-06-28', 200, 1, 1, 4, 1, 1),
    ('2024-04-08', '2024-04-15', 200, 2, 2, 5, 2, 2),
    ('2024-09-23', '2024-10-23', 200, 3, 3, 6, 3, 3),
    ('2024-06-14', '2024-06-28', 200, 1, 1, 7, 1, 1),
    ('2024-04-08', '2024-04-15', 200, 2, 2, 8, 2, 2),
    ('2024-09-23', '2024-10-23', 200, 3, 3, 1, 3, 3),
    ('2024-04-08', '2024-04-15', 1, 2, 1, 2, 2, 2),
    ('2024-09-23', '2024-10-23', 1, 3, 1, 3, 3, 3),
    ('2024-07-01', '2024-07-15', 150, 1, 2, 9, 1, 1),
    ('2024-05-10', '2024-05-24', 300, 3, 3, 10, 1, 1),
    ('2024-03-05', '2024-03-19', 250, 2, 2, 11, 1, 4),
    ('2024-06-20', '2024-07-05', 100, 4, 4, 12, 1, 1),
    ('2024-07-10', '2024-07-24', 200, 5, 5, 13, 1, 1),
    ('2024-04-15', '2024-04-29', 180, 6, 6, 14, 1, 2),
    ('2024-07-30', '2024-08-14', 220, 7, 7, 15, 2, 1),
    ('2024-05-20', '2024-06-03', 130, 8, 8, 16, 2, 1),
    ('2024-04-01', '2024-04-15', 150, 9, 9, 17, 1, 3),
    ('2024-03-22', '2024-04-05', 250, 10, 10, 18, 1, 5),
    ('2024-08-01', '2024-08-15', 120, 11, 11, 19, 2, 1),
    ('2024-02-10', '2024-02-24', 90, 12, 12, 20, 1, 4),
    ('2024-06-05', '2024-06-19', 110, 13, 13, 21, 1, 1),
    ('2024-03-15', '2024-03-29', 100, 14, 14, 22, 3, 2),
    ('2024-07-20', '2024-08-03', 200, 15, 15, 23, 1, 1),
    ('2024-04-05', '2024-04-19', 300, 16, 16, 24, 3, 1),
    ('2024-05-12', '2024-05-26', 175, 17, 17, 25, 1, 5),
    ('2024-06-17', '2024-07-01', 80, 17, 18, 26, 3, 1),
    ('2024-07-07', '2024-07-21', 100, 12, 19, 27, 1, 1),
    
    -- Pedidos adicionales para productos ya existentes
    ('2024-04-01', '2024-04-15', 250, 10, 1, 1, 1, 1),
    ('2024-05-20', '2024-06-03', 180, 14, 2, 1, 1, 3),
    ('2024-06-01', '2024-06-15', 140, 15, 3, 2, 3, 1),
    ('2024-04-10', '2024-04-24', 160, 16, 4, 3, 1, 2),
    ('2024-08-15', '2024-08-29', 90, 8, 5, 4, 3, 1),
    ('2024-09-01', '2024-09-15', 200, 2, 6, 5, 1, 4),
    ('2024-07-25', '2024-08-08', 130, 3, 7, 6, 3, 1),
    ('2024-06-30', '2024-07-14', 220, 6, 8, 7, 1, 2);

-- select d.id_DetalleObraPedido, d.id_stock, d.id_pedido, p.id_obra from Stock s inner join DetalleObraPedido d ON s.id_stock = d.id_stock inner join Pedido p ON d.id_pedido = p.id_pedido where s.id_obra = p.id_obra group by (d.id_DetalleObraPedido) order by (d.id_DetalleObraPedido);

INSERT INTO DetalleObraPedido(id_stock, id_pedido) VALUES
    (5, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 2),
    (10, 3),
    (11, 3),
    (12, 3),
    (4, 4),
    (5, 4),
    (6, 4),
    (7, 5),
    (8, 5),
    (9, 5),
    (10, 6),
    (11, 6),
    (12, 6),
    (13, 7),
    (14, 7),
    (15, 7),
    (16, 8),
    (17, 8),
    (6, 9),
    (8, 9),
    (4, 9),
    (5, 10),
    (6, 10),
    (7, 10),
    (8, 11),
    (9, 11),
    (10, 11),
    (11, 12),
    (12, 12),
    (13, 12),
    (14, 13),
    (15, 13),
    (16, 13),
    (17, 14),
    (5, 14),
    (8, 14),
    (3, 15),
    (5, 15),
    (6, 16),
    (7, 16),
    (8, 16),
    (9, 17),
    (10, 17),
    (11, 17),
    (12, 18),
    (13, 18),
    (14, 18),
    (15, 19),
    (16, 19),
    (17, 19),
    (4, 20),
    (7, 20),
    (3, 20),
    (4, 21),
    (5, 21),
    (6, 21),
    (7, 22),
    (8, 22),
    (9, 22),
    (10, 23),
    (11, 23),
    (17, 23),
    (14, 24),
    (15, 24),
    (16, 25),
    (17, 25),
    (8, 25),
    (6, 26),
    (3, 26),
    (4, 26),
    (5, 27),
    (6, 27),
    (7, 27),
    (8, 28),
    (9, 28),
    (10, 28),
    (11, 29),
    (12, 29),
    (13, 29),
    (14, 30),
    (15, 30),
    (16, 30),
    (17, 31),
    (3, 31),
    (4, 31),
    (3, 32),
    (4, 32),
    (5, 32),
    (6, 33),
    (7, 33),
    (8, 33),
    (9, 34),
    (10, 34),
    (11, 34),
    (12, 35),
    (13, 35),
    (14, 35),
    (15, 36),
    (16, 36),
    (17, 36),
    (9, 37),
    (2, 37),
    (4, 38),
    (5, 38);

-- Inserciones para la tabla EstadoOferta
INSERT INTO EstadoOferta (nombre, descripcion) VALUES 
    ('Disponible', 'La oferta aun esta disponible y los usuarios pueden verla para reservarla'),
    ('Reservado', 'La oferta esta reservada y los usuarios dejan verla'),
    ('Reclamado', 'La oferta que etaba en reserva ya fue transportada hasta la obra que la reclamo'),
    ('Cancelado', 'La oferta fue cancelada por el usuario que la ofrecio'),
    ('Vencido', 'La oferta ya vencio y no se puede reservar');

-- Inserciones para la tabla Oferta
INSERT INTO Oferta (fechaInicio, fechaVencimiento, cantidad, id_usuario, id_obra, id_producto, id_estadoOferta) VALUES 
    ('2024-01-14', '2024-01-28', 200, 1, 1, 3, 1),
    ('2023-08-10', '2023-08-17', 200, 3, 2, 2, 2),
    ('2024-04-30', '2024-05-30', 200, 2, 3, 1, 3),
    ('2024-01-10', '2024-02-10', 20, 1, 1, 4, 1),
    ('2023-08-02', '2023-09-02', 12, 3, 2, 5, 2),
    ('2024-04-01', '2024-05-01', 30, 2, 3, 6, 3),
    ('2024-01-10', '2024-02-10', 20, 1, 1, 7, 1),
    ('2023-08-02', '2023-09-02', 15, 3, 2, 8, 2),
    ('2024-04-01', '2024-05-01', 5, 2, 3, 1, 3),
    ('2023-08-02', '2023-09-02', 1, 1, 3, 2, 2),
    ('2024-04-01', '2024-05-01', 1, 1, 2, 3, 3),
    ('2024-02-01', '2024-02-15', 100, 1, 4, 3, 1),
    ('2023-09-15', '2023-09-30', 150, 2, 5, 2, 2),
    ('2024-03-15', '2024-03-31', 250, 3, 6, 1, 3),
    ('2024-05-01', '2024-05-15', 300, 1, 7, 4, 1),
    ('2024-06-10', '2024-06-20', 50, 2, 8, 5, 2),
    ('2024-07-01', '2024-07-15', 75, 3, 9, 6, 3),
    ('2024-08-15', '2024-08-30', 20, 1, 10, 7, 1),
    ('2024-09-05', '2024-09-20', 90, 2, 11, 8, 2),
    ('2024-10-01', '2024-10-15', 130, 3, 12, 1, 3),
    ('2024-11-10', '2024-11-24', 25, 1, 13, 2, 1),
    ('2024-12-01', '2024-12-15', 10, 2, 14, 3, 2),
    ('2024-12-20', '2024-12-31', 15, 3, 15, 4, 3),
    ('2024-01-15', '2024-01-30', 60, 1, 16, 5, 1),
    ('2024-02-20', '2024-03-05', 80, 2, 17, 6, 2),
    ('2024-03-10', '2024-03-20', 140, 3, 4, 7, 3),
    ('2024-04-20', '2024-05-05', 200, 1, 5, 8, 1),
    ('2024-05-15', '2024-05-30', 95, 2, 6, 1, 2),
    ('2024-01-05', '2024-01-20', 120, 1, 1, 2, 1),
    ('2024-02-15', '2024-03-01', 200, 2, 3, 3, 1),
    ('2024-03-05', '2024-03-20', 75, 1, 5, 4, 1),
    ('2024-04-25', '2024-05-10', 90, 3, 7, 5, 1),
    ('2024-05-15', '2024-05-30', 180, 2, 9, 6, 1);

-- Inserciones para la tabla Transporte
INSERT INTO Transporte (marca, modelo, patente, kilometraje, estadoITV, anio, imagen, necesita_mantenimiento, descripcion_mantenimiento) VALUES 
    ('Toyota', 'Hilux', 'NXD838', 10000, 'En Forma', '2022', 'vehiculos/toyota-hilux-on-the-road.webp', FALSE, ''),
    ('Renault', 'Logan', 'AA001AB', 20000, 'Vencido', '2020', 'vehiculos/renault-sandero-y-logan-1269058.webp', FALSE, ''),
    ('Peugeot', '3008 GT', 'AG500AA', 30000, 'En Forma', '2018', 'vehiculos/zaatogjy9axfzmntave4.webp', FALSE, ''),
    ('Renault', 'Kangoo', 'AB123CD', 15000, 'En Forma', '2019', 'vehiculos/renault-kangoo.webp', FALSE, ''),
    ('Fiat', 'Dobló', 'EF456GH', 25000, 'En Forma', '2018', 'vehiculos/fiat-doblo.webp', FALSE, ''),
    ('Peugeot', 'Partner', 'IJ789KL', 20000, 'En Forma', '2020', 'vehiculos/peugeot-partner.webp', FALSE, ''),
    ('Citroen', 'Berlingo', 'MN012OP', 18000, 'Vencido', '2017', 'vehiculos/citroen-berlingo.webp', FALSE, ''),
    ('Ford', 'Transit Connect', 'QR345ST', 22000, 'En Forma', '2020', 'vehiculos/ford-transit-connect.webp', FALSE, ''),
    ('Opel', 'Combo', 'UV678WX', 19000, 'En Forma', '2019', 'vehiculos/opel-combo.webp', FALSE, ''),
    ('Mercedes-Benz', 'Citan', 'YZ901AB', 16000, 'En Forma', '2021', 'vehiculos/mercedes-benz-citan.webp', FALSE, ''),
    ('Volkswagen', 'Caddy', 'CD234EF', 23000, 'En Forma', '2020', 'vehiculos/volkswagen-caddy.webp', FALSE, ''),
    ('Nissan', 'NV200', 'GH567IJ', 21000, 'En Forma', '2021', 'vehiculos/nissan-nv200.webp', FALSE, ''),
    ('Toyota', 'Proace City', 'KL890MN', 17000, 'En Forma', '2020', 'vehiculos/toyota-proace-city.webp', FALSE, ''),
    ('Hyundai', 'H350', 'OP123QR', 24000, 'Vencido', '2018', 'vehiculos/hyundai-h350.webp', FALSE, ''),
    ('Kia', 'Bongo', 'ST456UV', 20000, 'En Forma', '2019', 'vehiculos/kia-bongo.webp', FALSE, ''),
    ('Chevrolet', 'N300', 'WX789YZ', 26000, 'En Forma', '2020', 'vehiculos/chevrolet-n300.webp', FALSE, ''),
    ('Suzuki', 'Every', 'AB901CD', 13000, 'En Forma', '2021', 'vehiculos/suzuki-every.webp', FALSE, '');
    
    -- Inserciones para la tabla DetalleObraTransporte
INSERT INTO DetalleObraTransporte (id_obra, id_transporte) VALUES 
	(1, 1),
	(1, 2),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17);

INSERT INTO DetalleStockProducto (cantidad, checkpoint, fecha_creacion, id_stock, id_producto, id_usuario) VALUES
    (100, FALSE, '2023-01-01 08:00:00', 1, 2, 1),
    (200, FALSE, '2023-01-02 09:00:00', 3, 3, 2),
    (300, FALSE, '2023-01-03 10:00:00', 2, 1, 3),
    (20, FALSE, '2023-01-04 11:00:00', 1, 1, 2),
    (16, FALSE, '2023-01-05 12:00:00', 3, 2, 4),
    (400, FALSE, '2023-01-06 13:00:00', 3, 6, 1),
    (500, FALSE, '2023-01-07 14:00:00', 2, 7, 5),
    (400, FALSE, '2023-01-08 15:00:00', 2, 8, 4),
    (500, FALSE, '2023-01-09 16:00:00', 1, 1, 3),
    (1, FALSE, '2023-01-10 17:00:00', 1, 2, 1),
    (1, FALSE, '2023-01-11 18:00:00', 1, 3, 2),
    (150, FALSE, '2023-05-01 08:00:00', 1, 3, 1),
    (250, FALSE, '2023-05-02 09:00:00', 1, 4, 1),
    (100, FALSE, '2023-05-03 10:00:00', 2, 5, 2),
    (300, FALSE, '2023-05-04 11:00:00', 3, 1, 2),
    (80, FALSE, '2023-05-05 12:00:00', 2, 6, 1),
    (120, FALSE, '2023-05-06 13:00:00', 1, 7, 1),
    (200, FALSE, '2023-05-07 14:00:00', 2, 2, 3),
    (400, FALSE, '2023-05-08 15:00:00', 3, 3, 2),
    (50, FALSE, '2023-05-09 16:00:00', 1, 8, 5),
    (300, FALSE, '2023-05-10 17:00:00', 1, 9, 1),
    (20, FALSE, '2023-09-09 08:00:00', 2, 20, 4),
    (30, FALSE, '2023-09-10 09:00:00', 3, 21, 5),
    (15, FALSE, '2023-09-11 10:00:00', 4, 22, 6),
    (10, FALSE, '2023-09-12 11:00:00', 5, 23, 7),
    (17, FALSE, '2023-09-13 12:00:00', 6, 24, 8),
    (9, FALSE, '2023-09-14 13:00:00', 7, 25, 9),
    (16, FALSE, '2023-09-15 14:00:00', 8, 26, 10),
    (20, FALSE, '2023-09-16 15:00:00', 1, 27, 11);
    
INSERT INTO AportePedido (descripcion, cantidad, fechaAportado, id_pedido, id_obra, id_usuario) VALUES 
	('desc1', 10, CURDATE(), 1, 4, 5),
	('desc2', 20, CURDATE(), 2, 5, 6),
	('desc3', 30, CURDATE(), 3, 6, 7);

INSERT INTO AporteOferta (descripcion, cantidad, fechaAportado, id_oferta, id_obra, id_usuario) VALUES 
	('desc1', 10, CURDATE(), 1, 3, 4),
	('desc2', 20, CURDATE(), 2, 2, 3),
	('desc3', 30, CURDATE(), 3, 1, 2);
    
INSERT INTO EstadoEntrega (nombre, descripcion) VALUES 
    ('Pendiente', 'Solo es un pedido y no se hizo nada'),
    ('En Proceso', 'Transporte se encarga de llevar este pedido que ahora esta en procesosta en proceso el pedido'),
    ('Finalizado', 'El pedido llego a la obral pedido ya esta finalizado.'),
    ('Cancelado', 'El pedido fue cancelado por el usuario que lo hizo'),
    ('Vencido', 'El pedido ya vencio y no se puede reservar');

INSERT INTO Entrega (fechaCreacion, id_pedido, id_oferta) VALUES 
    (CURDATE(), 1, NULL),
    (CURDATE(), NULL, 1);

INSERT INTO EntregaAporte (id_entrega, fechaEntrega, id_aportePedido, id_aporteOferta, id_estadoEntrega) VALUES 
    (1, DATE_ADD(CURDATE(), INTERVAL 7 DAY), 1, NULL, 1),
    (2, DATE_ADD(CURDATE(), INTERVAL 7 DAY), NULL, 1, 1);
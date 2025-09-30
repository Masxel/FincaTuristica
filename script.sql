
CREATE DATABASE db_fincaturistica;

CREATE TABLE `db_fincaturistica`.`reserva` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `fechallegada` DATE NOT NULL,
    `fechasalida` DATE NOT NULL,
    `idcliente` int NOT NULL,
    `idhabitacion` int NOT NULL,
    `estadoreserva` int NOT NULL,
    PRIMARY KEY(`id`)
);


CREATE TABLE `db_fincaturistica`.`estadoreserva` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`habitacion` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `tipohabitacion` VARCHAR(45) NOT NULL,
    `precio` int NOT NULL,
    `capacidad` int NOT NULL,
    `estado` int NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_habitacion__estado` FOREIGN KEY (`estado`) REFERENCES `estado`(`id`)
);

CREATE TABLE `db_fincaturistica`.`estadohabitacion` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`empleados` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `telefono` VARCHAR(15) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    `cargo` int NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`cargo` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`insumos` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `cantidad` int NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL, 
    `precio` int NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`cliente` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `telefono` VARCHAR(15) NOT NULL,
    `email` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`factura` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `fecha` DATE NOT NULL,
    `total` int NOT NULL,
    `idreserva` int NOT NULL,
    `idmetodopago` int NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_factura__reserva` FOREIGN KEY (`idreserva`) REFERENCES `reserva`(`id`),
    CONSTRAINT `fk_factura__metodo_pago` FOREIGN KEY (`idmetodopago`) REFERENCES `metodo_pago`(`id`)
);

CREATE TABLE `db_fincaturistica`.`metodo_pago` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
    PRIMARY KEY(`id`)
);

--Son zonas como piscinas, jacuzzis, canchas deportivas, salones de eventos, etc.
CREATE TABLE `db_fincaturistica`.`zonas_entretenimiento` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    PRIMARY KEY(`id`)
);

-- Eventos especiales, como bodas, cumpleaños, conferencias, etc.
CREATE TABLE `db_fincaturistica`.`eventos` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(45) NOT NULL,
    `descripcion` VARCHAR(200) NOT NULL,
    `fecha` DATE NOT NULL,
    PRIMARY KEY(`id`)
);
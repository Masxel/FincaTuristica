
CREATE DATABASE db_fincaturistica;

CREATE TABLE `db_fincaturistica`.`reserva` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `fechareserva` DATE NOT NULL,
    `fechallegada` DATE NOT NULL,
    `fechasalida` DATE NOT NULL,
    `idcliente` int NOT NULL,
    `idhabitacion` int NOT NULL,
    `estadoreserva` int NOT NULL,
    `metodopago` int NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_fincaturistica`.`metodopago` (
    `id` INT AUTO_INCREMENT NOT NULL,
    `descripcion` VARCHAR(45) NOT NULL,
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



CREATE DATABASE Clientes;

USE Clientes;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100),
    telefono VARCHAR(15) NOT NULL,
    correo VARCHAR(100),
    contrasena VARCHAR(255) NOT NULL 
);

DROP TABLE clientes;

SELECT * FROM usuarios;

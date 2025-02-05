CREATE DATABASE Clientes;

USE Clientes;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    correo VARCHAR(100),
    contrasena VARCHAR(255) NOT NULL 
);

DROP TABLE usuarios;

SELECT * FROM usuarios;

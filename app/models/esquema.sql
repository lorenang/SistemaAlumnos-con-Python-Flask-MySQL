CREATE DATABASE ispp;
USE ispp;

CREATE TABLE tipoUser (
  idtipoUser INT NOT NULL AUTO_INCREMENT,
  tipoUsuario VARCHAR(20) NULL,
  PRIMARY KEY (idtipoUser));

CREATE TABLE user ( 
  idUsuario INT AUTO_INCREMENT,
  usuario VARCHAR(20) NOT NULL,
  email VARCHAR(100) NULL,
  password char(255) NOT NULL,
  fechaCreacionLogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  fullname VARCHAR(50) NOT NULL,
  estadoLogin VARCHAR(8) NOT NULL,
  idtipoUsuario INT,
  FOREIGN KEY (idtipoUsuario) REFERENCES tipoUser (idtipoUser),
  PRIMARY KEY(idUsuario)
);

CREATE TABLE Alumno (
   idAlumno INT auto_increment,
   dniAlumno BIGINT NOT NULL,
   cuilAlumno BIGINT NOT NULL,
   nombreAlumno VARCHAR(40) NOT NULL,
   apellidoAlumno VARCHAR (20) NOT NULL,
   fechaNacAlumno DATE,
   direccionAlumno VARCHAR (200),
   observacionesAlumno VARCHAR (200),
   telefono BIGINT NOT NULL,
   secundariaAlumno VARCHAR (50),
   anioEgSecAlumno YEAR,
   anioIngAlumISPP YEAR,
   anioEgAlumISPP YEAR,
   emailAlumno VARCHAR(100) NOT NULL,
   idUser INT,
   PRIMARY KEY (idAlumno),
   FOREIGN KEY (idUser) REFERENCES user (idUsuario) );
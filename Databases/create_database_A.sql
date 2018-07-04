CREATE DATABASE base_A;

CREATE USER 'userA'@'localhost' IDENTIFIED BY 'userA';
GRANT ALL PRIVILEGES ON base_A.* To 'userA'@'localhost' REQUIRE X509;
flush privileges;

CREATE TABLE `base_A`.`usuario`( -- dados usados para a autenticação
`username` VARCHAR(400) NOT NULL,
`password` VARCHAR(400) NOT NULL,
PRIMARY KEY (`username`));

CREATE TABLE `base_A`.`pessoa`(
`cpf` NUMERIC(11) NOT NULL,
`nome` VARCHAR(400) NOT NULL,
`endereco` VARCHAR(400) NOT NULL,
PRIMARY KEY (`cpf`));

CREATE TABLE `base_A`.`divida` (
`id_divida` INT NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
`cpf` NUMERIC(11) NOT NULL,
`credor` NUMERIC(14) NOT NULL,
PRIMARY KEY (`id_divida`),
FOREIGN KEY (`cpf`) REFERENCES `base_A`.`pessoa`(`cpf`));

DROP PROCEDURE `BuscaDivida`;

DELIMITER $$
USE `base_A`$$
CREATE PROCEDURE `BuscaDividas` (
in p_cpf NUMERIC(11)
)
BEGIN
    select id_divida, CAST(valor as CHAR(15)), CAST(credor AS CHAR(14)) from divida where divida.cpf = p_cpf; 
END$$
DELIMITER ;

DELIMITER $$
USE `base_A`$$
CREATE PROCEDURE `BuscaPessoa` (
    in p_cpf NUMERIC(11)
)
BEGIN
    select nome, endereco from pessoa where cpf=p_cpf; 
END$$
DELIMITER ;


DELIMITER $$
USE `base_A`$$
CREATE PROCEDURE `AutenticaUsusario` (
IN p_username VARCHAR(400)
)
BEGIN
     select * from usuario where username = p_username;
END$$

DELIMITER ;

DELIMITER $$
USE `base_A`$$
CREATE PROCEDURE `criaUsuario` (
IN p_username varchar(400),
IN p_password varchar(400)
)
BEGIN

if (SELECT exists (select 1 from usuario where username = p_username)) THEN
    select 'Username Exists !!';
ELSE
insert into usuario
(username, password) values( p_username, p_password);
END IF;
END$$
DELIMITER ;

INSERT INTO usuario (username,password)
VALUES ('joel','12345');

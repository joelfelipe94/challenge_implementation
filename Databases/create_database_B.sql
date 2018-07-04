CREATE DATABASE base_B;

CREATE USER 'userB'@'localhost' IDENTIFIED BY 'userB';
GRANT ALL PRIVILEGES ON base_B.* To 'userB'@'localhost' REQUIRE SSL;
flush privileges;

CREATE TABLE `base_B`.`pessoa` (
`id_pessoa` INT NOT NULL,
`idade` INT NOT NULL,
`endereco` VARCHAR(400) NOT NULL, 
`fonte_de_renda` VARCHAR(400) NOT NULL,
`renda` NUMERIC(15,2) NOT NULL,
PRIMARY KEY (`id_pessoa`));

CREATE TABLE `base_B`.`bem` (
`id_bem` INT NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
`id_pessoa` INT NOT NULL,
`descricao` VARCHAR(400) NOT NULL,
PRIMARY KEY (`id_bem`),
FOREIGN KEY (`id_pessoa`) REFERENCES `base_B`.`pessoa`(`id_pessoa`));

CREATE TABLE `base_B`.`usuario`( -- dados usados para a autenticação
`username` VARCHAR(400) NOT NULL,
`password` VARCHAR(400) NOT NULL,
PRIMARY KEY (`username`));



DELIMITER $$
USE `base_B`$$
CREATE PROCEDURE `AutenticaUsusario` (
IN p_username VARCHAR(400)
)
BEGIN
     select * from usuario where username = p_username;
END$$

DELIMITER ;

DELIMITER $$
USE `base_B`$$
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

drop procedure BuscaBens;

DELIMITER $$
USE `base_B`$$
CREATE PROCEDURE `BuscaBens` (
in p_id_pessoa INT
)
BEGIN
select id_bem, CAST(valor as CHAR(15)), descricao from bem where id_pessoa = p_id_pessoa;
END$$
DELIMITER ;


DELIMITER $$
USE `base_A`$$
CREATE PROCEDURE `BuscaPessoas` ()
BEGIN
    select idade, endereco, fonte_de_renda, CAST(renda as CHAR(15)) from pessoa; 
END$$
DELIMITER ;


INSERT INTO usuario (username,password)
VALUES ('joel','12345');
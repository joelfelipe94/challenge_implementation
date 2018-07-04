CREATE DATABASE base_C;

CREATE USER 'userC'@'localhost' IDENTIFIED BY 'userC';
GRANT ALL PRIVILEGES ON base_C.* To 'userC'@'localhost';



CREATE TABLE `base_C`.`consulta` (
`id_consulta` INT NOT NULL,
`cpf` NUMERIC(11) NOT NULL,
`data_hora` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
`resultado` TEXT NOT NULL,
PRIMARY KEY (`id_consulta`));

CREATE TABLE `base_C`.`movimento` (
`id_movimento` INT NOT NULL,
`cpf` NUMERIC(11) NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
`descricao` VARCHAR(400) NOT NULL,
PRIMARY KEY (`id_movimento`));

CREATE TABLE `base_C`.`compra_cartao_credito` (
`id_compra_cartao_credito` INT NOT NULL,
`cpf` NUMERIC(11) NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
`beneficiario` VARCHAR(400) NOT NULL,
PRIMARY KEY (`id_compra_cartao_credito`));

DELIMITER $$
USE `base_C`$$
CREATE PROCEDURE `BuscaConsultas` (
)
BEGIN
    select id_consulta, CAST(cpf as CHAR(11)), DATE_FORMAT(data_hora, '%h:%m:%s %d-%m-%Y'), resultado from consulta; 
END$$
DELIMITER ;


DELIMITER $$
USE `base_C`$$
CREATE PROCEDURE `BuscaMovimentosCPF` (
    IN p_cpf NUMERIC(11) 
)
BEGIN
    select id_movimento, CAST(valor as CHAR(15)), descricao from movimento where cpf = p_cpf; 
END$$
DELIMITER ;
CREATE DATABASE base_B;

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
'descricao' VARCHAR(400) NOT NULL
PRIMARY KEY (`id_bem`),
FOREIGN KEY (`id_pessoa`) REFERENCES `base_B`.`pessoa`(`id_pessoa`));


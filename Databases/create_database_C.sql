CREATE DATABASE base_C;

CREATE TABLE `base_C`.`consulta` (
`id_consulta` INT NOT NULL,
`cpf` NUMERIC(11) NOT NULL,
`data_hora` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
`resultado` TEXT NOT NULL
PRIMARY KEY (`id_consulta`));

CREATE TABLE `base_C`.`monvimento` (
`id_movimento` INT NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
'descricao' VARCHAR(400) NOT NULL
PRIMARY KEY (`id_movimento`));

CREATE TABLE `base_C`.`compra_cartao_credito` (
`id_compra_cartao_credito` INT NOT NULL,
`valor` NUMERIC(15,2) NOT NULL,    
'beneficiario' VARCHAR(400) NOT NULL
PRIMARY KEY (`id_compra_cartao_credito`));


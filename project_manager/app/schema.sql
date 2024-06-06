-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema project_manager
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project_manager
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project_manager` DEFAULT CHARACTER SET utf8 ;
USE `project_manager` ;

-- -----------------------------------------------------
-- Table `project_manager`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Usuario` (
  `idUsuario` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  PRIMARY KEY (`idUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Gerente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Gerente` (
  `idUsuario` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Gerente_Usuario1_idx` (`idUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_Gerente_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Projeto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Projeto` (
  `idProjeto` INT NOT NULL,
  `idGerente` INT NOT NULL,
  `data_inicio` DATE NULL,
  `nome` VARCHAR(45) NULL,
  `descricao` VARCHAR(45) NULL,
  `data_fim` DATE NULL,
  PRIMARY KEY (`idProjeto`),
  INDEX `fk_Projeto_Gerente1_idx` (`idGerente` ASC) VISIBLE,
  CONSTRAINT `fk_Projeto_Gerente1`
    FOREIGN KEY (`idGerente`)
    REFERENCES `project_manager`.`Gerente` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Tarefa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Tarefa` (
  `idTarefa` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  `data_criacao` DATE NULL,
  `descricao` VARCHAR(45) NULL,
  `prazo` DATE NULL,
  `status` VARCHAR(45) NULL,
  `idProjeto` INT NOT NULL,
  PRIMARY KEY (`idTarefa`),
  INDEX `fk_Tarefa_Projeto1_idx` (`idProjeto` ASC) VISIBLE,
  CONSTRAINT `fk_Tarefa_Projeto1`
    FOREIGN KEY (`idProjeto`)
    REFERENCES `project_manager`.`Projeto` (`idProjeto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Comentario` (
  `idComentario` INT NOT NULL,
  `mensagem` VARCHAR(45) NULL,
  `idUsuario` INT NOT NULL,
  `idTarefa` INT NOT NULL,
  `idDestinatario` INT NULL,
  PRIMARY KEY (`idComentario`),
  INDEX `fk_Comentario_Usuario1_idx` (`idUsuario` ASC) VISIBLE,
  INDEX `fk_Comentario_Tarefa1_idx` (`idTarefa` ASC) VISIBLE,
  INDEX `fk_Comentario_Usuario2_idx` (`idDestinatario` ASC) VISIBLE,
  CONSTRAINT `fk_Comentario_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comentario_Tarefa1`
    FOREIGN KEY (`idTarefa`)
    REFERENCES `project_manager`.`Tarefa` (`idTarefa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comentario_Usuario2`
    FOREIGN KEY (`idDestinatario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Participa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Participa` (
  `idUsuario` INT NOT NULL,
  `idProjeto` INT NOT NULL,
  PRIMARY KEY (`idUsuario`, `idProjeto`),
  INDEX `fk_Participa_Projeto1_idx` (`idProjeto` ASC) VISIBLE,
  CONSTRAINT `fk_Participa_Usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Participa_Projeto1`
    FOREIGN KEY (`idProjeto`)
    REFERENCES `project_manager`.`Projeto` (`idProjeto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Recebe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Recebe` (
  `idUsuario` INT NOT NULL,
  `idTarefa` INT NOT NULL,
  PRIMARY KEY (`idUsuario`, `idTarefa`),
  INDEX `fk_Recebe_Tarefa1_idx` (`idTarefa` ASC) VISIBLE,
  CONSTRAINT `fk_Recebe_Usuario`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Recebe_Tarefa1`
    FOREIGN KEY (`idTarefa`)
    REFERENCES `project_manager`.`Tarefa` (`idTarefa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_manager`.`Cred`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_manager`.`Cred` (
  `Usuario_idUsuario` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Usuario_idUsuario`),
  CONSTRAINT `fk_cred_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `project_manager`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema introse
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema introse
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `introse` DEFAULT CHARACTER SET utf8 ;
USE `introse` ;

-- -----------------------------------------------------
-- Table `introse`.`accounts_payable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`accounts_payable` (
  `date` DATETIME NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `id_apv` INT(11) NOT NULL,
  `amount` DECIMAL(13,2) NULL DEFAULT '0.00',
  PRIMARY KEY (`id_apv`),
  UNIQUE INDEX `apv_id_UNIQUE` (`id_apv` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`customer` (
  `customer_id` INT(11) NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(100) NOT NULL,
  `address` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`accounts_receivable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`accounts_receivable` (
  `customer_id` INT(11) NOT NULL,
  `receive_id` INT(11) NOT NULL AUTO_INCREMENT,
  `date` DATETIME NOT NULL,
  `inv_id` INT(11) NOT NULL,
  `amount` DECIMAL(13,2) NULL DEFAULT NULL,
  `date_paid` DATETIME NULL DEFAULT NULL,
  `pr_id` INT(11) NULL DEFAULT NULL,
  `payment` DECIMAL(13,2) NULL DEFAULT NULL,
  PRIMARY KEY (`receive_id`),
  INDEX `fk_customer_id_idx` (`customer_id` ASC),
  CONSTRAINT `fk_customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `introse`.`customer` (`customer_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`book keeping`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`book keeping` (
  `idbook keeping` INT(11) NOT NULL AUTO_INCREMENT,
  `amount` DECIMAL(10,0) NOT NULL DEFAULT '0',
  `nonvat` DECIMAL(10,0) NULL DEFAULT '0',
  `innumber` DECIMAL(10,0) NULL DEFAULT NULL,
  `customer` VARCHAR(45) NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idbook keeping`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`column_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`column_group` (
  `id_group` INT(11) NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_group`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`column_name_table`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`column_name_table` (
  `id_column` INT(11) NOT NULL AUTO_INCREMENT,
  `id_group` INT(11) NOT NULL,
  `column_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_column`),
  INDEX `fk_id_group_idx` (`id_group` ASC),
  CONSTRAINT `fk_id_group`
    FOREIGN KEY (`id_group`)
    REFERENCES `introse`.`column_group` (`id_group`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`credit_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`credit_type` (
  `id_element` INT(11) NOT NULL AUTO_INCREMENT,
  `id_apv` INT(11) NOT NULL,
  `type_name` VARCHAR(100) NULL DEFAULT NULL,
  `type_value` DECIMAL(13,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_element`),
  INDEX `fk_id_apv_idx` (`id_apv` ASC),
  CONSTRAINT `fk_id_apv`
    FOREIGN KEY (`id_apv`)
    REFERENCES `introse`.`accounts_payable` (`id_apv`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 82
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`employee` (
  `employee_id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`employee_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2300
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`employee_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`employee_type` (
  `id_element` INT(11) NOT NULL AUTO_INCREMENT,
  `employee_id` INT(11) NOT NULL,
  `employee_role` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id_element`),
  INDEX `fk_employee_id_idx` (`employee_id` ASC),
  CONSTRAINT `fk_employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `introse`.`employee` (`employee_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`inventory` (
  `idinventory` INT(11) NOT NULL AUTO_INCREMENT,
  `productName` VARCHAR(45) NOT NULL,
  `supplier` VARCHAR(45) NULL DEFAULT NULL,
  `packagingType` VARCHAR(45) NULL DEFAULT NULL,
  `perunitprice` FLOAT NOT NULL,
  `retailprice` FLOAT NOT NULL,
  `quantity` INT(11) NOT NULL,
  `lastupdated` DATETIME NULL DEFAULT NULL,
  `vatable` TINYINT(4) NULL DEFAULT NULL,
  PRIMARY KEY (`idinventory`),
  UNIQUE INDEX `idinventory_UNIQUE` (`idinventory` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `introse`.`vouchers payable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `introse`.`vouchers payable` (
  `apvno` INT(11) NOT NULL,
  `date` DATETIME NOT NULL,
  `particulars` VARCHAR(45) NOT NULL,
  `voucherspayable` FLOAT NULL DEFAULT '0',
  `purchasesvatable` FLOAT NULL DEFAULT '0',
  `purchVATexempt` FLOAT NULL DEFAULT '0',
  `inputTax` FLOAT NULL DEFAULT '0',
  `LCGDrawing` FLOAT NULL DEFAULT '0',
  `Salaries&Wages` FLOAT NULL DEFAULT '0',
  `CommissionIncentive` FLOAT NULL DEFAULT '0',
  `Rebates` FLOAT NULL DEFAULT '0',
  `profFee` FLOAT NULL DEFAULT '0',
  `Tax&Licences` FLOAT NULL DEFAULT '0',
  `Meals&Snacks` FLOAT NULL DEFAULT '0',
  `Gas&Oil` FLOAT NULL DEFAULT '0',
  `officeSupplies` FLOAT NULL DEFAULT '0',
  `rentalFee` FLOAT NULL DEFAULT '0',
  `Tel&Postage` FLOAT NULL DEFAULT '0',
  `Light&Water` FLOAT NULL DEFAULT '0',
  `transpoExpenses` FLOAT NULL DEFAULT '0',
  `insuranceExpense` FLOAT NULL DEFAULT '0',
  `repairs` FLOAT NULL DEFAULT '0',
  `representation` FLOAT NULL DEFAULT '0',
  `donation` FLOAT NULL DEFAULT '0',
  `marketingExpense` FLOAT NULL DEFAULT '0',
  `housingAllowance` FLOAT NULL DEFAULT '0',
  `housekeeping` FLOAT NULL DEFAULT '0',
  `evat` FLOAT NULL DEFAULT '0',
  `medicalExpense` FLOAT NULL DEFAULT '0',
  `employeePartiesRecreation` FLOAT NULL DEFAULT '0',
  `interestExpense` FLOAT NULL DEFAULT '0',
  `christmasExpense` FLOAT NULL DEFAULT '0',
  `deliveryExpense` FLOAT NULL DEFAULT '0',
  `sssPremCont` FLOAT NULL DEFAULT '0',
  `phicPremCont` FLOAT NULL DEFAULT '0',
  `advancesOthers` FLOAT NULL DEFAULT '0',
  `advancesEmployees` FLOAT NULL DEFAULT '0',
  `carLoanCapitalLoan` FLOAT NULL DEFAULT '0',
  `outputTaxPayable` FLOAT NULL DEFAULT '0',
  `expandedwTaxPayable` FLOAT NULL DEFAULT '0',
  `wholdingTaxPayable` FLOAT NULL DEFAULT '0',
  `sssPremPayable` FLOAT NULL DEFAULT '0',
  `phicPremPayable` FLOAT NULL DEFAULT '0',
  `salaryLoansEmployees` FLOAT NULL DEFAULT '0',
  `maternityBenefits` FLOAT NULL DEFAULT '0',
  `newBuildingConstruction` FLOAT NULL DEFAULT '0',
  `transferFunds` FLOAT NULL DEFAULT '0',
  `difficiencyTax` FLOAT NULL DEFAULT '0',
  `incomeTax` FLOAT NULL DEFAULT '0',
  `sundryAccount` FLOAT NULL DEFAULT '0',
  `DR` FLOAT NULL DEFAULT '0',
  `CR` FLOAT NULL DEFAULT '0',
  `retainerFee` FLOAT NULL DEFAULT '0',
  `advertisingExpense` FLOAT NULL DEFAULT '0',
  PRIMARY KEY (`apvno`),
  UNIQUE INDEX `apvno_UNIQUE` (`apvno` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

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
AUTO_INCREMENT = 20
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

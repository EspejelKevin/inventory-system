CREATE DATABASE IF NOT EXISTS inventorysystem;
USE inventorysystem;


CREATE TABLE IF NOT EXISTS Category(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL
);


CREATE TABLE IF NOT EXISTS Product(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(200) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    sku VARCHAR(50) NOT NULL UNIQUE,
    category_id INT NOT NULL,
    CONSTRAINT fk_category_product 
    FOREIGN KEY (category_id) 
    REFERENCES Category(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Client(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS Seller(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE,
    address VARCHAR(100) NOT NULL,
    company VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS Inventory(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL,
    update_date DATE NOT NULL,
    description VARCHAR(100) NOT NULL,
    movement_type VARCHAR(50) NOT NULL,
    product_id INT NOT NULL,
    code VARCHAR(255) NOT NULL UNIQUE,
    CONSTRAINT fk_product_inventory
    FOREIGN KEY (product_id) 
    REFERENCES Product(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Sale(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    folio VARCHAR(50) NOT NULL UNIQUE,
    subtotal DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    sale_date DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS SaleDetails(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    sale_id INT NOT NULL,
    seller_id INT NOT NULL,
    client_id INT NOT NULL,
    product_id INT NOT NULL,
    CONSTRAINT fk_sale_saledetails
    FOREIGN KEY (sale_id) 
    REFERENCES Sale(id) ON DELETE CASCADE,
    CONSTRAINT fk_seller_saledetails
    FOREIGN KEY (seller_id) 
    REFERENCES Seller(id) ON DELETE CASCADE,
    CONSTRAINT fk_client_saledetails
    FOREIGN KEY (client_id) 
    REFERENCES Client(id) ON DELETE CASCADE,
    CONSTRAINT fk_product_saledetails
    FOREIGN KEY (product_id) 
    REFERENCES Product(id) ON DELETE CASCADE
);
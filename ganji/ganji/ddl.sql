-- ddl table ganji_shhouse
DROP TABLE IF EXISTS `ganji_shhouse`;
CREATE TABLE `ganji_shhouse` (
`id` int(255) unsigned NOT NULL AUTO_INCREMENT,
`puid` varchar(255) DEFAULT NULL,
`title` varchar(255) DEFAULT NULL,
`model` varchar(255) DEFAULT NULL,
`area` varchar(255) DEFAULT NULL,
`direction` varchar(128) DEFAULT NULL,
`height` varchar(128) DEFAULT NULL,
`style` varchar(128) DEFAULT NULL,
`address` varchar(255) DEFAULT NULL,
`sale_type` varchar(128) DEFAULT NULL,
`price` int(64) DEFAULT NULL,
`price_type` varchar(64) DEFAULT NULL,
`unit_price` varchar(64) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4
;

CREATE USER 'xuser'@'localhost' IDENTIFIED BY 'Hello12345.';
GRANT ALL ON *.* to 'xuser'@'localhost';
FLUSH PRIVILEGES;
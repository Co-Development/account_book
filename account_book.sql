CREATE TABLE `account_book` (
`id`  int NOT NULL AUTO_INCREMENT COMMENT '主键' ,
`create_name`  varchar(50) NOT NULL COMMENT '创建人' ,
`money`  int NOT NULL COMMENT '金额' ,
`create_time`  datetime NOT NULL COMMENT '创建时间' ,
`note`  varchar(255) NULL COMMENT '备注' ,
PRIMARY KEY (`id`)
)
;

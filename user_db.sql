create database userTest;

-- @'%' 表示所有机器可以连接
CREATE USER user_test@'%' IDENTIFIED BY 'user_test_paasword';

-- 授权
grant all privileges on userTest.* to user_test;

create table user (
    id bigint not null AUTO_INCREMENT comment 'id',
    name varchar(50) not null comment '姓名',
    age int  not null comment '年龄',
    sex varchar(10) not null  comment '性别',
    birth datetime null comment '生日',
    creator bigint not null comment '创建人id',
    create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP comment '创建时间',
    update_time timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP comment '更新时间',
    primary key(id)
);
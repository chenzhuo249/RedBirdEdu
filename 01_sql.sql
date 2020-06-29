create database myStu default charset utf8;

use myStu;

create table stu (
id int primary key auto_increment,
name varchar(4) not null default ""
);

create table sco (
id int primary key auto_increment,
course varchar(5) not null,
score tinyint not null,
stu_id int not null,
constraint stu_fk foreign key(stu_id) references stu(id)
on delete cascade on update cascade
);

select sco.id, stu.name, sco.course, sco.score
from stu right join sco
on stu.id = sco.stu_id;

select sco.id, stu.name, sco.course, sco.score,
case
when sco.score >= 90 then "优秀"
when sco.score >= 80 then "良好"
when sco.score >= 60 then "及格"
else "不及格"
end as grade
from stu right join sco
on stu.id = sco.stu_id;


-- 有时我们要把查询的结果保存到新表里，创建新表，查询，插入显得十分麻烦。
-- 其实直接可以搞定。例如把表2的查询结果插入表1：
-- 如果表存在：
insert into tab1 select * from tab2

-- 如果表不存在：
create table tab1 as select * from tab2


insert into stu_sco
select sco.id, stu.name, sco.course, sco.score,
case
when sco.score >= 90 then "优秀"
when sco.score >= 80 then "良好"
when sco.score >= 60 then "及格"
else "不及格"
end as grade
from stu right join sco
on stu.id = sco.stu_id;


create table stu_sco as
select sco.id, stu.name, sco.course, sco.score,
case
when sco.score >= 90 then "优秀"
when sco.score >= 80 then "良好"
when sco.score >= 60 then "及格"
else "不及格"
end as grade
from stu right join sco
on stu.id = sco.stu_id;



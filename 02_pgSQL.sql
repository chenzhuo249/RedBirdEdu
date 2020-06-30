
create table stu (
id smallserial primary key,
name varchar(4),
age smallint,
score smallint
);

create table all_stu as
select id, name, score,
case
when score >= 90 then '优秀'
when score >= 80 then '良好'
when score >= 60 then '及格'
else '不及格'
end as grade
from stu;


create table new_bjg as
select id, name, age,
case
when score < 60 then '不及格'
end as grade
from stu where score < 60;





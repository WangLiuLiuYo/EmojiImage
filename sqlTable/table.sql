drop table if exists mypics;
create table mypics(
id int auto_increment,
picdata mediumblob not null,
picinfo varchar(50) default 'no description',
suffix char(10) default 'jpg',
primary key(id)
);
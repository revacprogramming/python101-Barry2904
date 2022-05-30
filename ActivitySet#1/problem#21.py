'''
create database ages;

use ages;

CREATE TABLE Ages 
( 
name VARCHAR(128), 
age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Jaymie', 17);
INSERT INTO Ages (name, age) VALUES ('Chizaram', 35);
INSERT INTO Ages (name, age) VALUES ('Macaulay', 13);
INSERT INTO Ages (name, age) VALUES ('Brodi', 17);
INSERT INTO Ages (name, age) VALUES ('Milie', 30);
INSERT INTO Ages (name, age) VALUES ('Fearn', 21);
'''
#for sql_lite
#SELECT hex(name||age) AS X FROM Ages ORDER BY X;
#for MySQL
#select hex(concat(name,age)) as x from ages order by x;

#ANSWER:- 42726F64693137
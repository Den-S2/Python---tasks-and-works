-- create database Academy; use Academy;
-- create table `Depart` (id int auto_increment, Financing double, Namdep nvarchar(100), primary key(id));
-- insert into `Depart` (Financing, Namdep) values ('1000.0', 'NamedepA')
-- insert into `Depart` (Financing, Namdep) values ('12500.0', 'NamedepB')
-- insert into `Depart` (Financing, Namdep) values ('14000.0', 'NamedepC')
-- insert into `Depart` (Financing, Namdep) values ('25500.0', 'NamedepD')
-- insert into `Depart` (Financing, Namdep) values ('36000.0', 'NamedepE')
-- select * from academy.depart
-- create table `Faculties` (id int auto_increment, Namdis nvarchar(100), Dean nvarchar(100), primary key(id));
-- insert into `Faculties` (Namdis, Dean) values ('Dias','Math')
-- insert into `Faculties` (Namdis, Dean) values ('Bredola','Biology')
-- insert into `Faculties` (Namdis, Dean) values ('Mariam','Economy')
-- insert into `Faculties` (Namdis, Dean) values ('Osteris','IT')
-- insert into `Faculties` (Namdis, Dean) values ('Tubery','Phisic')
-- select * from academy.faculties
-- create table `Groups` (id int auto_increment, Namgr nvarchar(100), Ratting int, Year int, primary key(id));
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupA','1','1')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupB','2','2')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupC','3','3')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupD','4','4')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupE','5','5')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupF','5','2')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupJ','5','3')
-- insert into `Groups` (Namgr, Ratting, Year) values ('GroupG','5','4')
-- insert into `Groups` (Namgr, Ratting, Year) values ('Groupasd','1','5')
-- insert into `Groups` (Namgr, Ratting, Year) values ('Groupdff','2','5')
-- insert into `Groups` (Namgr, Ratting, Year) values ('Groupfgf','3','5')
-- insert into `Groups` (Namgr, Ratting, Year) values ('Grouphht','4','5')
-- select * from academy.Groups
-- create table `Teachers` (id int auto_increment, namtea nvarchar(100), surtea nvarchar(100), EmplDate date, IsAssist int, IsProff int, Position nvarchar(100), Premium double, Salary double, primary key(id));
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Disasse','Brty','2001-10-03','0','1','dean','3100','12200')
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Broasd','Versu','2000-07-05','1','0','teacher','1200','15200')
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Malura','Vuu','2011-08-05','0','1','dean','5330','5200')
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Sakuta','Sadist','1999-12-03','1','0','teacher','10','3200')
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Uttina','Abigu','2005-01-20','0','1','dean','31','8200')
-- insert into `Teachers` (namtea, surtea, EmplDate, IsAssist, IsProff, Position, Premium, Salary) values ('Tubesy','Gatuu','2018-05-08','1','0','teacher','500','9200')
-- select * from academy.teachers
-- select * from academy.faculties order by id desc
-- select Namgr, Ratting from academy.groups
-- select namtea from academy.teachers where (Salary/Premium *100) > 100
-- select * from academy.faculties
-- select surtea from academy.teachers where Salary > 10500
-- select Namdep from academy.depart where Financing >= 11000 and Financing <= 25000
-- select Namdis from academy.faculties where Dean != 'IT' 
-- select surtea,Position from academy.teachers where IsProff = 0 
-- select surtea,Salary,Position from academy.teachers where IsProff = 0 and Premium between 150 and 550 
-- select surtea,Salary from academy.teachers where IsAssist = 1
-- select surtea,Position from academy.teachers where EmplDate <= '2000-01-01'
-- select Namdis from academy.faculties order by Namdis 
-- select surtea from academy.teachers where IsAssist = 1 and Premium+Salary < 12000
-- select Namgr from academy.groups where Year = 5 and Ratting between 2 and 4
-- select surtea from academy.teachers where IsAssist = 1 and Premium < 200 or Salary < 550
-- create database Messanger; use Messanger;
-- create table `Auth` (id int auto_increment, Login nvarchar(100), Passwd nvarchar(100), primary key(id));
-- insert into `Auth` (Login, Passwd) values ('Asergood', 'aass23ss2')
-- insert into `Auth` (Login, Passwd) values ('Byend', 'dada24wd3')
-- insert into `Auth` (Login, Passwd) values ('Lotus', 'nene45ad2')
-- insert into `Auth` (Login, Passwd) values ('Dekarshow', 'atac43er4')
-- create table `User` (id int auto_increment, Nameuser nvarchar(100), Surnauser nvarchar(100), Elnauser nvarchar(100), Infouser nvarchar(100), primary key(id)); 
-- insert into `User` (Nameuser, Surnauser, Elnauser, Infouser) values ('Samantus', 'Jager', 'Juck', 'fly on dron')
-- insert into `User` (Nameuser, Surnauser, Elnauser, Infouser) values ('Samuel', 'Rodrigues', 'Antony',  'Jetstream Sam')
-- insert into `User` (Nameuser, Surnauser, Elnauser, Infouser) values ('Sandy', 'Baffuvaly', 'Corg', 'Love watch cinema')
-- create table `Friend` (id int auto_increment, Namefrie nvarchar(100), Linkad nvarchar(100), Dateadd date, primary key(id)); 
-- insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Torry', 'Samantus', '2022-09-10')
-- insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Lucy', 'Samuel', '2022-11-01')
--  insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Santy', 'Sandy', '2022-08-02')
<<<<<<< HEAD
-- insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Lotty', 'Carl', '2022-08-02')
-- insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Cobby', 'Carl', '2022-08-02')
-- insert into `Friend` (Namefrie, Linkad, Dateadd) values ('Cobby', 'Sandy', '2022-08-02')
=======
>>>>>>> b06f06eb24ceab5c2cd954f2ad59adb772dc2f03
-- create table `Publish` (id int auto_increment, Linkpub nvarchar(100), Infopub nvarchar(100), primary key(id)); 
-- insert into `Publish` (Linkpub, Infopub) values ('Samantus', 'live stream TV')
-- insert into `Publish` (Linkpub, Infopub) values ('Samuel', 'Fight on street')
-- insert into `Publish` (Linkpub, Infopub) values ('Sandy', 'random pool')
<<<<<<< HEAD
-- select Namefrie, count(Namefrie) from `Friend` where Linkad = 'Samuel'
 -- SELECT Namefrie, count(Namefrie) from `Friend` where Linkad = 'Samuel'

-- create database Museum; use Museum;
-- create table `Auth` (id int auto_increment, Login nvarchar(100), Passwd nvarchar(100), primary key(id));
-- insert into `Auth` (Login, Passwd) values ('Asergood', 'aass23ss2')
-- insert into `Auth` (Login, Passwd) values ('Byend', 'dada24wd3')
-- insert into `Auth` (Login, Passwd) values ('Lotus', 'nene45ad2')
-- insert into `Auth` (Login, Passwd) values ('Dekarshow', 'atac43er4')
-- create table `Exponate` (id int auto_increment, Namexpo nvarchar(100), Infoexpo nvarchar(100), primary key(id)); 
-- insert into `Exponate` (Namexpo, Infoexpo) values ('Santus', 'Height arm-chair')
-- insert into `Exponate` (Namexpo, Infoexpo) values ('Tampoo', 'Not shy wall')
-- insert into `Exponate` (Namexpo, Infoexpo) values ('Rectus', 'Fight sword')
-- insert into `Exponate` (Namexpo, Infoexpo) values ('Tesuroo', 'Book of dead')
-- create table `People` (id int auto_increment, Namepeop nvarchar(100), Surnapeop nvarchar(100), Linkad nvarchar(100), primary key(id)); 
-- insert into `People` (Namepeop, Surnapeop, Linkad) values ('Torry', 'Samantus', 'Santus')
-- insert into `People` (Namepeop, Surnapeop, Linkad) values ('Lucy', 'Samuel', 'Tampoo')
-- insert into `People` (Namepeop, Surnapeop, Linkad) values ('Luu', 'Samf', 'Tampoo')
-- insert into `People` (Namepeop, Surnapeop, Linkad) values ('Santy', 'Sandy', 'Rectus')

-- create database Note; use Note;
-- create table `Auth` (id int auto_increment, Login nvarchar(100), Passwd nvarchar(100), primary key(id));
-- insert into `Auth` (Login, Passwd) values ('Asergood', 'aass23ss2')
-- insert into `Auth` (Login, Passwd) values ('Byend', 'dada24wd3')
-- insert into `Auth` (Login, Passwd) values ('Lotus', 'nene45ad2')
-- insert into `Auth` (Login, Passwd) values ('Dekarshow', 'atac43er4')
-- create table `Notepad` (id int auto_increment, Namenot nvarchar(100), Infonot nvarchar(100), Datenot date, primary key(id)); 
-- insert into `Notepad` (Namenot, Infonot, Datenot) values ('Santus', 'Height arm-chair', '2022-11-02')
-- insert into `Notepad` (Namenot, Infonot, Datenot) values ('Tampoo', 'Not shy wall', '2011-05-05')
-- insert into `Notepad` (Namenot, Infonot, Datenot) values ('Rectus', 'Fight sword', '2020-09-29')
-- insert into `Notepad` (Namenot, Infonot, Datenot) values ('Tesuroo', 'Book of dead', '2021-12-12')

=======
 select Namefrie, count(Namefrie) from `Friend` where Linkad = 'Samuel'
>>>>>>> b06f06eb24ceab5c2cd954f2ad59adb772dc2f03

use rs2_db;

-- drop table if exists `session`;
drop table if exists comment;
drop table if exists rating;
drop table if exists post;
drop table if exists member;
drop table if exists opportunity;

-- create table `session` (
--        email varchar(30) not null primary key,
--        st timestamp,  
--        ip char(15))
       
-- ENGINE = InnoDB; 

create table member(
    email varchar(30),
    `password` varchar(200) not null,
    `name` varchar(40) not null,
    `type` enum('Student','Alum', 'Professor'),
    primary key(email)
)
ENGINE = InnoDB;

create table opportunity(
    pid int not null primary key,
    email varchar(30),
    field varchar(25),
    title varchar(25),
    institution varchar(30),
    startDate date,
    `location` varchar(50),
    experienceType varchar(25),
    experienceLevel set('Freshman', 'Sophomore', 'Junior', 'Senior', 'Any'),
    `description` varchar(1250),
    appLink nvarchar(2000),
    sponsorship set('Yes', 'No', 'Maybe')
)
ENGINE = InnoDB;

create table post(
    email varchar(30),
    pid int,
    foreign key (email) references member(email)
    on delete cascade 
    on update cascade,
    foreign key (pid) references opportunity(pid)
    on delete cascade 
    on update cascade
)
ENGINE = InnoDB;

create table comment(
    pid int,
    institution varchar(30),
    title varchar(25),
    comment varchar(250),
    foreign key (pid) references opportunity(pid)
    on delete cascade
    on update cascade
)
ENGINE = InnoDB;

create table rating (
    pid int, 
    email varchar(30),
    rating enum('1','2','3','4','5'),
    foreign key (pid) references opportunity(pid)
    on delete cascade
    on update cascade,
    foreign key (email) references member(email)
    on delete cascade
    on update cascade
)
ENGINE = InnoDB;

-- create table favorites (
--     link varchar(250),
--     uid varchar(15),
--     foreign key (uid) references user (uid)
--         on update restrict,
--     foreign key (link) references application (link)
--         on update restrict
-- )
-- ENGINE = InnoDb;
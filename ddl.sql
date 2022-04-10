use rs2_db;


drop table if exists comment;
drop table if exists rating;
drop table if exists post;
drop table if exists member;
drop table if exists opportunity;


create table member(
    email varchar(30),
    `password` varchar(200) not null,
    `name` varchar(40) not null,
    `type` enum('Student','Alum', 'Professor'),
    primary key(email)
)
ENGINE = InnoDB;

create table opportunity(
    pid int,
    title varchar(25),
    institution varchar(30),
    `type` varchar(25),
    field varchar(25),
    `description` varchar(1250),
    `location` varchar(50),
    app_link nvarchar(2000),
    exp_level set('First year', 'Sophomore', 'Juniors', 'Seniors', 'Any'),
    primary key(pid)
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
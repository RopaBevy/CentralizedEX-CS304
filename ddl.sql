<<<<<<< HEAD
=======
use rs2_db; --centralex_db
>>>>>>> fe96754bb7b7a41acc8f1cde3baaa32cb5d32fc8

drop table if exists comment;
drop table if exists rating;
drop table if exists post;
drop table if exists profilePic;
drop table if exists member;
drop table if exists opportunity;


create table member(
    email varchar(30),
    profession varchar(50) not null,
    institution varchar(70) not null,
    `password` varchar(200) not null,
    `name` varchar(40) not null,
<<<<<<< HEAD
    about varchar(400) not null,
=======
    profession varchar(100) not null,
    institution varchar(30),
>>>>>>> fe96754bb7b7a41acc8f1cde3baaa32cb5d32fc8
    `type` enum('Student','Alum', 'Professor'),
    primary key(email)

)
ENGINE = InnoDB;

create table opportunity(
    pid int not null auto_increment,
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
    sponsorship set('Yes', 'No', 'Maybe'),
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
    primary key (pid,email),
    foreign key (pid) references opportunity(pid)
    on delete cascade
    on update cascade,
    foreign key (email) references member(email)
    on delete cascade
    on update cascade
)
ENGINE = InnoDB;


create table profilePic (
    email varchar(30) primary key,
    filename varchar(50),
    foreign key (email) references member(email) 
        on delete cascade on update cascade
);

ALTER TABLE opportunity ADD  averageRating float;
use centralex_db;

drop table if exists comment;
drop table if exists rating;
drop table if exists post;
drop table if exists profilePic;
drop table if exists member;
drop table if exists opportunity;


create table member(
    email varchar(30),
    `name` varchar(40) not null,
    `password` varchar(200) not null,
    `type` enum('Student','Alum', 'Professor'),
    profession varchar(50) not null,
    institution varchar(70) not null,
    about varchar(100),
    primary key(email)
)
ENGINE = InnoDB;

create table opportunity(
    pid int not null auto_increment,
    email varchar(30),
    field varchar(25),
    title varchar(25),
    institution varchar(40),
    season set ('Fall', 'Winter', 'Spring', 'Summer'),
    year char(4),
    `location` varchar(50),
    experienceType varchar(25),
    experienceLevel set('Freshman', 'Sophomore', 'Junior', 'Senior', 'Any'),
    `description` varchar(1250),
    appLink nvarchar(2000),
    sponsorship enum('Yes', 'No', 'Maybe'),
    primary key(pid)
)
ENGINE = InnoDB;

create table post(
    email varchar(30),
    pid int,
    primary key (email, pid),
    foreign key (email) references member(email)
    on delete cascade 
    on update cascade,
    foreign key (pid) references opportunity(pid)
    on delete cascade 
    on update cascade
)
ENGINE = InnoDB;

create table comment(
    comment_id int not null auto_increment,
    email varchar(30),
    pid int,
    comment varchar(250),
    primary key(comment_id),
    foreign key (email) references member(email)
    on delete cascade
    on update cascade,
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

create table favorites(
    pid int,
    email varchar(30),
    primary key(pid, email),
    foreign key (pid) references opportunity(pid)
        on delete cascade
        on update cascade,
    foreign key (email) references member(email)
        on delete cascade
        on update cascade
)
ENGINE = InnoDb;

create table profilePic (
    email varchar(30) primary key,
    filename varchar(50),
    foreign key (email) references member(email) 
        on delete cascade on update cascade
);

ALTER TABLE opportunity ADD  averageRating float;
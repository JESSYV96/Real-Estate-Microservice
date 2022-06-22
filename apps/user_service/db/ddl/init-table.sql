create table if not exists user (
  userId int auto_increment not null,
  firstname varchar(100) not null,
  lastname varchar(100) not null,
  email varchar(100) unique not null,
  password varchar not null
  primary key(userId)
);
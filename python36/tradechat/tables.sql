drop table if exists comments;
create table comments (
  id integer primary key autoincrement,
  comment text not null,
  user text not null,
  time text not null
);

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  name text not null,
  password text not null
);
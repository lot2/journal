/*drop table if exists sys_users;*/
create table if not exists sys_users (
  user_id integer primary key,
  user_group varchar(10),
  user_name varchar(30),
  password varchar(10),
  email varchar(50),
  telephone varchar(20),
  status varchar(2) default '1',
  create_date timestamp not null default current_timestamp
);
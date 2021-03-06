CREATE DATABASE if not exists journal DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;

create table if not exists journal.sys_users (
  user_id integer auto_increment primary key,
  user_group varchar(10),
  user_name varchar(30),
  password varchar(10),
  email varchar(50),
  telephone varchar(20),
  status varchar(2) default '1',
  create_date timestamp not null default current_timestamp
) DEFAULT CHARSET=utf8;

create table if not exists journal.journal_new (
  journal_id integer auto_increment primary key,
  journal_date varchar(20),
  user_id integer,
  status varchar(2) default '1',
  create_date timestamp not null default current_timestamp,
  last_update_date timestamp not null default current_timestamp
) DEFAULT CHARSET=utf8;

create table if not exists journal.journal_new_detail (
  task_id integer auto_increment primary key,
  journal_id integer,
  contents varchar(2000),
  issue varchar(20),
  spend_time varchar(50),
  schedule varchar(50),
  problem varchar(2000),
  solution varchar(2000),
  remark varchar(2000),
  task_status varchar(2) default '1',
  row_num integer
)auto_increment=1000000 DEFAULT CHARSET=utf8;

INSERT INTO journal.sys_users(user_id, user_name, password, status) VALUES ('1', 'admin', '123', '1');
commit;
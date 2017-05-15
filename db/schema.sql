drop table if exists tomatoes;
create table tomatoes (
    id integer primary key autoincrement,
    data blob not null
)
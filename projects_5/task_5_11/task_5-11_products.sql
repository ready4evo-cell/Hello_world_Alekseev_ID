select * from products where category = 'Электроника';
select * from products where category = 'Одежда' and name like '%женские%';
select * from products where category in ('Продукты', 'Книги');
select * from products where category <> 'Бытовая техника';
select * from products where category in ('Электроника', 'Одежда', 'Книги');
select * from products where (category = 'Электроника' AND name LIKE '%Samsung%') or category = 'Бытовая техника';
select * from products where (category in ('Электроника', 'Одежда', 'Бытовая техника') AND id BETWEEN 1 AND 15 AND name NOT LIKE '%Samsung%') or category = 'Книги';
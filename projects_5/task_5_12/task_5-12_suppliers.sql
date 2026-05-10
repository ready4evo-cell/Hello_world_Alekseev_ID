select product_id, count(*) as suppliers_count from suppliers group by product_id order by product_id asc;

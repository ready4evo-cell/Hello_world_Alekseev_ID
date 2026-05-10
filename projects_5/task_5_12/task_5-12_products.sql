select category, count(*) from products group by category;
select category, count(*) as total_count from products group by category order by total_count desc;
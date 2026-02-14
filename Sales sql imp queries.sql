USE sales_dashboard;

DESCRIBE sales_data;
SELECT * FROM sales_data LIMIT 5;
select * from sales_data;

SELECT merchantid, totalunitssold
FROM sales_data
ORDER BY totalunitssold DESC
LIMIT 10;

SELECT merchantid, averagediscount
FROM sales_data
ORDER BY averagediscount DESC
LIMIT 10;

SELECT AVG(urgencytextrate) AS avg_urgency_text_rate, AVG(totalurgencycount) AS avg_urgency_count
FROM sales_data;

SELECT merchantid, listedproducts
FROM sales_data
ORDER BY listedproducts DESC
LIMIT 10;

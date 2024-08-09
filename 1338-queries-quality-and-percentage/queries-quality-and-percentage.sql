# Write your MySQL query statement below
SELECT query_name, 
ROUND(AVG(cast(rating as decimal)/position), 2) AS quality,
ROUND(SUM(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
# Write your MySQL query statement below
SELECT a.id as Id
FROM Weather a
INNER JOIN Weather b on a.recordDate = DATE_ADD(b.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature

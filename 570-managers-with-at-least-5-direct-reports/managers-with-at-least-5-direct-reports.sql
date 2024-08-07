# Write your MySQL query statement below
SELECT A.name
FROM Employee AS A
JOIN Employee B ON A.id = B.managerId
GROUP BY B.managerId
HAVING COUNT(B.managerId) >= 5;
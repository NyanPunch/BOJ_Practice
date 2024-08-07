# Write your MySQL query statement below
SELECT P.product_name, S.year, S.price
FROM Sales S JOIN Product P ON S.Product_id = P.product_id
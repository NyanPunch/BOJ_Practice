# Write your MySQL query statement below
SELECT round(avg(order_date = customer_pref_delivery_date)*100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) in (
    select customer_id, min(order_date)
    from Delivery
    group by customer_id
);
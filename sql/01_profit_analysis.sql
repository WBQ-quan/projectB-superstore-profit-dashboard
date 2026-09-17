-- 1. 地区利润
SELECT Region, ROUND(SUM(Profit), 2) AS total_profit
FROM global_superstore
GROUP BY Region
ORDER BY total_profit DESC;

-- 2. 品类利润
SELECT Category, ROUND(SUM(Profit), 2) AS total_profit
FROM global_superstore
GROUP BY Category
ORDER BY total_profit DESC;

-- 3. 亏损子品类（使用双引号 "Sub-Category"）
SELECT "Sub-Category", ROUND(SUM(Profit), 2) AS total_profit
FROM global_superstore
GROUP BY "Sub-Category"
ORDER BY total_profit ASC
LIMIT 5;

-- 4. Tables 高折扣与利润率（修复括号 + 双引号字段）
SELECT AVG(Discount) AS avg_discount, 
       ROUND(SUM(Profit)*1.0 / SUM(Sales), 4) AS profit_margin
FROM global_superstore
WHERE "Sub-Category" = 'Tables';

SELECT stocks.symbol, stocks.price, SUM(log.shares) as shares, SUM(log.amount) as total
FROM users
JOIN log ON users.id = log.user_id
JOIN stocks ON log.symbol_id = stocks.id
WHERE log.user_id = 1 AND log.symbol_id = 1
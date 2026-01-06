CREATE SCHEMA IF NOT EXISTS lululemon;
SET search_path TO lululemon;

CREATE TABLE stores (
  store_id       INT PRIMARY KEY,
  store_name     TEXT NOT NULL,
  city           TEXT NOT NULL,
  state          TEXT NOT NULL,
  region         TEXT NOT NULL,
  base_traffic   INT  NOT NULL
);
CREATE TABLE products (
  product_id   INT PRIMARY KEY,
  product_name TEXT NOT NULL,
  category     TEXT NOT NULL,
  base_price   NUMERIC(10,2) NOT NULL
);
CREATE TABLE promotions (
  promotion_id      INT PRIMARY KEY,
  promo_name        TEXT NOT NULL,
  discount_percent  INT NOT NULL CHECK (discount_percent IN (10,20,30)),
  start_date        DATE NOT NULL,
  end_date          DATE NOT NULL,
  CHECK (end_date >= start_date)
);
CREATE TABLE transactions (
  transaction_id BIGINT PRIMARY KEY,
  transaction_date DATE NOT NULL,
  store_id INT NOT NULL REFERENCES stores(store_id),
  product_id INT NOT NULL REFERENCES products(product_id),
  quantity INT NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(10,2) NOT NULL,
  promotion_id INT NULL REFERENCES promotions(promotion_id)
);
CREATE TABLE store_promotions (
  store_id INT NOT NULL REFERENCES stores(store_id),
  promotion_id INT NOT NULL REFERENCES promotions(promotion_id),
  PRIMARY KEY (store_id, promotion_id)
);

SELECT t.*
FROM transactions t
LEFT JOIN store_promotions sp
  ON sp.store_id = t.store_id AND sp.promotion_id = t.promotion_id
WHERE t.promotion_id IS NOT NULL

  AND sp.promotion_id IS NULL;
CREATE INDEX idx_txn_date ON transactions(transaction_date);
CREATE INDEX idx_txn_store_date ON transactions(store_id, transaction_date);
CREATE INDEX idx_txn_product_date ON transactions(product_id, transaction_date);
CREATE INDEX idx_txn_promo ON transactions(promotion_id);

SELECT
  CASE WHEN promotion_id IS NULL THEN 'no_promo' ELSE 'promo' END AS promo_flag,
  AVG(quantity) AS avg_qty,
  SUM(quantity) AS total_qty,
  COUNT(*) AS lines
FROM transactions
GROUP BY 1;

SELECT
  p.discount_percent,
  AVG(t.quantity) AS avg_qty
FROM transactions t
JOIN promotions p ON p.promotion_id = t.promotion_id
GROUP BY p.discount_percent
ORDER BY p.discount_percent;

SELECT
  CASE
    WHEN EXTRACT(DOW FROM transaction_date) IN (0,6) THEN 'weekend'
    ELSE 'weekday'
  END AS day_type,
  SUM(quantity) AS total_qty,
  AVG(quantity) AS avg_line_qty
FROM transactions
GROUP BY 1;

SELECT
  CASE
    WHEN EXTRACT(MONTH FROM transaction_date) BETWEEN 5 AND 8 THEN 'summer'
    ELSE 'non_summer'
  END AS season,
  SUM(quantity) AS total_qty
FROM transactions
GROUP BY 1;

CREATE OR REPLACE VIEW v_txn AS
SELECT
  t.*,
  pr.category,
  CASE WHEN t.promotion_id IS NULL THEN 0 ELSE 1 END AS is_promoted
FROM transactions t
JOIN products pr ON pr.product_id = t.product_id;

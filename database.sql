DROP TABLE IF EXISTS order_history;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS menu;

CREATE TABLE menu (
    menu_id INTEGER PRIMARY KEY,
    menu_name TEXT,
    category TEXT,
    price REAL
);

CREATE TABLE order_history (
    order_id INTEGER,
    menu_id INTEGER,
    quantity INTEGER,
    order_date TEXT
);

CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_type TEXT,
    amount REAL
);
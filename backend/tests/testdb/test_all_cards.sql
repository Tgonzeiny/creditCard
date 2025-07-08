CREATE TABLE IF NOT EXISTS credit_cards (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    network TEXT NOT NULL,
    issuer TEXT NOT NULL
);
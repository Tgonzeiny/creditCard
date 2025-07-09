CREATE TABLE IF NOT EXISTS cardrewards (
    id SERIAL PRIMARY KEY,
    card_id INTEGER NOT NULL REFERENCES allcards(id) ON DELETE CASCADE,
    mcc_category TEXT NOT NULL,
    multiplier NUMERIC(4,2) NOT NULL
);

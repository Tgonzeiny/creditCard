CREATE TABLE usercards (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    card_id INTEGER REFERENCES allcards(id) ON DELETE CASCADE,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (user_id, card_id)
);

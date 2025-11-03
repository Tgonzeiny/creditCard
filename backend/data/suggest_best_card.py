def suggest_best_card(mcc_code, user_cards):
    max_card = None
    best_rate = 0.0

    for card in user_cards:
        rewards = card.get("rewards", {})
        categories = card.get("categories", [])
        base_rate = rewards.get("base_rate", 1.0)

        current_rate = categories.get(str(mcc_code), base_rate)

        if current_rate > best_rate:
            best_rate = current_rate
            best_card = card["card_name"]

    return {
        "recommeanded_Card" : best_card,
        "reward_rate" : best_rate,
    }
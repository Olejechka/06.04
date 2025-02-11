import json

rules = [
    {
        "condition": lambda facts: facts["age"] < 18 and facts["activity_level"] == "низкий",
        "action": lambda facts: "Рекомендуется 60 минут умеренной или высокой физической активности в день."
    },
    {
        "condition": lambda facts: 18 <= facts["age"] <= 64 and facts["weight"] > 100,
        "action": lambda facts: "Рекомендуются низкоударные нагрузки (плавание, ходьба, йога)."
    },
    {
        "condition": lambda facts: facts["age"] > 65 and facts["has_chronic_diseases"],
        "action": lambda facts: "Перед началом физических нагрузок рекомендуется консультация с врачом."
    },
    {
        "condition": lambda facts: facts["activity_level"] == "высокий" and not facts["has_chronic_diseases"],
        "action": lambda facts: "Рекомендуется чередование аэробных и силовых тренировок."
    },
    {
        "condition": lambda facts: facts["activity_level"] == "низкий" and facts["has_chronic_diseases"],
        "action": lambda facts: "Рекомендуется лечебная физкультура или прогулки."
    },
    {
        "condition": lambda facts: 18 <= facts["age"] <= 64 and facts["activity_level"] == "низкий",
        "action": lambda facts: "Рекомендуется начинать с легкой физической активности, например, прогулок."
    },
    {
        "condition": lambda facts: 18 <= facts["age"] <= 64 and facts["weight"] <= 100 and facts["activity_level"] == "низкий",
        "action": lambda facts: "Рекомендуется 150 минут умеренной активности в неделю (например, быстрая ходьба)."
    },
    {
        "condition": lambda facts: facts["activity_level"] == "высокий" and facts["has_chronic_diseases"],
        "action": lambda facts: "Перед интенсивными тренировками рекомендуется консультация с врачом."
    },
    {
        "condition": lambda facts: 18 <= facts["age"] <= 64 and facts["activity_level"] == "средний" and not facts["has_chronic_diseases"],
        "action": lambda facts: "Рекомендуется поддерживать 150–300 минут умеренной активности в неделю."
    },
    {
        "condition": lambda facts: facts["activity_level"] == "средний" and not facts["has_chronic_diseases"],
        "action": lambda facts: "Добавьте силовые тренировки 2-3 раза в неделю для укрепления мышц."
    }
]

def get(facts):
    for rule in rules:
        if rule["condition"](facts):
            return rule["action"](facts)
    return "Продолжайте в том же духе :)"

def save(recommendation, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({"fitness_recommendation": recommendation}, f, ensure_ascii=False, indent=4)

def main():
    facts = {
        "age": int(input("Введите ваш возраст: ")),
        "weight": float(input("Введите ваш вес (кг): ")),
        "activity_level": input("Введите уровень активности (низкий, средний, высокий): ").strip().lower(),
        "has_chronic_diseases": input("Есть ли у вас хронические заболевания? (да/нет): ").strip().lower() == "да"
    }

    fitness_recommendation = get(facts)
    print("Рекомендация по фитнесу:", fitness_recommendation)

    save(fitness_recommendation, 'fitness_recommendation.json')

if __name__ == "__main__":
    main()

from api import get_categories, get_products

temp_data = {}

def low_controller(message, bot):
    bot.send_message(
        message.chat.id,
        "Вы выбрали фильтрацию по убыванию. Выберите одну из категорий"
    )
    bot.send_message(
        message.chat.id,
        " | ".join(get_categories())
    )

    temp_data[message.chat.id] = {}

    bot.register_next_step_handler(message, lambda m: category_controller(m, bot))


def category_controller(message, bot):
    bot.send_message(
        message.chat.id,
        "Отлично! Категория для фильтрации выбрана. Укажите количество результатов для получения."
    )
    temp_data[message.chat.id]['category'] = message.text
    bot.register_next_step_handler(message, lambda m: amount_controller(m, bot))


def amount_controller(message, bot):
    temp_data[message.chat.id]['amount'] = message.text
    bot.send_message(
        message.chat.id,
        f"Выборка из {message.text} товаров"
    )
    sorted_products = sorted(get_products(temp_data[message.chat.id]['category']), key=lambda x: x['price'])[:int(temp_data[message.chat.id]['amount'])]
    for i in sorted_products:
        bot.send_message(
            message.chat.id,
            f"{i['title']} | {i['price']}"
        )



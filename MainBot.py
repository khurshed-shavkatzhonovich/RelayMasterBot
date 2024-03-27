from telethon import TelegramClient, events

# Данные номеров и id
api_id = '23671676'
api_hash = '38a91769321c3e2918fd2efaa8b4faf0'
phone_numbers = ['+992929438936', '+992501070777']  # Номера телефонов с аккаунтами Telegram
receiver_id = 7054883903  # ID пользователя, который получает сообщения
forward_to_id = 749700324  # ID пользователя, на которого пересылаем сообщения

async def main():
    # Создаем клиент для аккаунта, который получает сообщения
    receiver_client = TelegramClient('receiver', api_id, api_hash)
    await receiver_client.start()

    # Создаем клиент для аккаунта, на который пересылаем сообщения
    forward_client = TelegramClient('forwarder', api_id, api_hash)
    await forward_client.start()

    # Устанавливаем обработчик для получения сообщений
    @receiver_client.on(events.NewMessage)
    async def handler(event):
        # Проверяем, пришло ли сообщение от кого-либо для receiver_id
        if event.message.sender_id != forward_to_id:
            # Копируем только-что присланное сообщение для receiver_id
            copied_message = await event.message.forward_to(receiver_id)
            # Отправляем скопированное сообщение от имени receiver_id на аккаунт forward_to_id
            await forward_client.send_message(forward_to_id, copied_message)

    # Запускаем клиенты
    await receiver_client.run_until_disconnected()
    await forward_client.run_until_disconnected()

# Запускаем основную функцию
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

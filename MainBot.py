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
        # Получаем ID отправителя и ID сообщения
        sender_id = event.message.sender_id
        message_id = event.message.id
        if sender_id != receiver_id:  # Если отправитель не является получателем
            # Копируем сообщение и отправляем на нужного пользователя
            await forward_client.forward_messages(forward_to_id, event.message)

    # Запускаем клиенты
    await receiver_client.run_until_disconnected()
    await forward_client.run_until_disconnected()

# Запускаем основную функцию
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

class DiscordNotifier:

    def __init__(self, bot):

        self.bot = bot

    async def send(self, channel_id, message):

        channel = self.bot.get_channel(channel_id)

        if channel:

            await channel.send(message)
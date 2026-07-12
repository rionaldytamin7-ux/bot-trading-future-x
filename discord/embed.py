import discord

class TradeEmbed:

    def build(self, trade):

        embed = discord.Embed(

            title="RIO AI FUTURES",

            color=0x00ff00

        )

        embed.add_field(

            name="Symbol",

            value=trade["symbol"]

        )

        embed.add_field(

            name="Side",

            value=trade["side"]

        )

        embed.add_field(

            name="Entry",

            value=trade["entry"]

        )

        embed.add_field(

            name="TP",

            value=trade["take_profit"]

        )

        embed.add_field(

            name="SL",

            value=trade["stop_loss"]

        )

        return embed
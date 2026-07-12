@bot.command()

async def ping(ctx):

    await ctx.send("RIO AI ONLINE")

@bot.command()

async def status(ctx):

    await ctx.send(

        "Bot Running"

    )

@bot.command()

async def balance(ctx):

    await ctx.send(

        account.get_balance()

    )

@bot.command()

async def position(ctx):

    await ctx.send(

        position_manager.summary()

    )

@bot.command()

async def dashboard(ctx):

    await ctx.send(

        dashboard.text()

    )

@bot.command()

async def daily(ctx):

    await ctx.send(

        reports.daily()

    )

@bot.command()

async def weekly(ctx):

    await ctx.send(

        reports.weekly()

    )

!backtest BTCUSDT 2025-01-01 2025-12-31
backtest.run(...)

!scan

!restart
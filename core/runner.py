from core.banner import show_banner
from core.logger import get_logger
from core.health import run_system_check

#v1.2
from core.command_engine import CommandEngine

from database.database import init_database

#updates
# context = MarketContextEngine()

# result = context.analyze(
#     market_data
# )

from exchange.binance_client import BinanceClient
from exchange.account import Account
from exchange.market import Market
from exchange.client import BinanceClient
from exchange.market import MarketData

from indicators.indicator_engine import IndicatorEngine

from strategy.strategy_manager import StrategyManager
from strategy.regime_detector import RegimeDetector
from strategy.patterns.pattern_engine import PatternEngine
# from strategy.market_context import MarketContextEngine
# from strategy.decision_engine import DecisionEngine
# from dashboard.dashboard import Dashboard

from analytics.statistics import Statistics
from analytics.timeframe_engine import MultiTimeframeEngine

from market_context.context_engine import MarketContextEngine

from ai.scoring import AIScoring
from ai.decision import AIDecision

from risk.entry_engine import EntryEngine

from execution.position_manager import PositionManager
from execution.trade_manager import TradeManager
from risk.position_manager import PositionSizing

from backtest.runner import BacktestRunner

from reports.discord import DiscordReporter
from reports.daily_report import DailyReport
from reports.weekly_report import WeeklyReport

from config.watchlist import WATCHLIST

logger = get_logger()

def run_cycle(symbol):

    logger.info(
        "===================================="
    )

    logger.info(
        "NEW MARKET CYCLE"
    )

    logger.info(
        "===================================="
    )

#WHERE IS THIS GPTT
    df = market.get_market(symbol)
    indicator_result = indicator.calculate(df)
    pattern_result = pattern.detect(df)
    context_result = context.calculate(
        df,
        indicator_result
    )
    decision_result = decision.decide(
        indicator_result,
        pattern_result,
        context_result
    )
    decision_result["signal"] == "WAIT"
    return

#AND THIS WHERE
    trade = entry_engine.calculate(
        ...
    )
    trade["quantity"] = sizing.calculate(
        ...
    )
    trade_manager.open_trade(
        trade
    )
    position_manager.monitor(
        trade
    )

    stats.update()
    dashboard.print()
    discord.send()

# pattern engine
    pattern_engine = PatternEngine()

    pattern_result = pattern_engine.analyze(
        df)

    logger.info(
        pattern_result)

    #risk manager
    
    indicator_engine = IndicatorEngine()


    indicators = indicator_engine.calculate(
        df
    )
    strategy = StrategyManager()
    signal = strategy.analyze(
        indicators
    )
    logger.info(signal)

    # ============================
    # MULTI TIMEFRAME ANALYSIS
    # ============================
    mtf_engine = MultiTimeframeEngine()

    mtf_result = mtf_engine.analyze({

        "trend_4h": "NEUTRAL",

        "structure_1h": "NONE",

        "pattern_15m": "NONE",

        "entry_5m": "WAIT",

        "execution_1m": "WAIT"

    })

    logger.info(
        mtf_result)

    # ============================
    # AI DECISION ENGINE
    # ============================
    ai_score_engine = AIScoring()

    score = ai_score_engine.calculate({

        "market_context": market_context,

        "pattern": pattern_result.get(
            "patterns",
            [{}])[0],

        "multi_tf": mtf_result,

        "volume_status":
        result.get(
            "volume_status")})

    decision_engine = AIDecision()

    decision = decision_engine.decide(score)

    logger.info({
        "AI_SCORE": score,
        "DECISION": decision})

    # ============================
    # ENTRY SETUP ENGINE
    # ============================
    if decision != "WAIT":
        entry_engine = EntryEngine(
            leverage=10)

        trade_setup = entry_engine.calculate(

            for symbol in WATCHLIST:
                logger.info(f"Scanning {symbol}")
                try:
                    run_cycle(symbol)
                except Exception as e:
                    logger.error(f"{symbol} : {e}"),

            side=decision,
            price=float(
                df["close"].iloc[-1]),
            support=float(
                pattern_result["support"]),
            resistance=float(
                pattern_result["resistance"]),
            risk_reward=2
        )

        sizing = PositionSizing(risk_percent=1)

        trade_setup["quantity"] = sizing.calculate(
            balance=balance,
            entry_price=trade_setup["entry"],
            stop_loss=trade_setup["stop_loss"],
            leverage=trade_setup["leverage"]
)

        logger.info(
            trade_setup)
  # POSITION MANAGER (FOR VIRTUAL TRADE)
    position_manager = PositionManager()

    if trade_setup:
        active = position_manager.open_position(
            trade_setup
        )
        logger.info(
            {
                "OPEN POSITION":
                active
            })
        
    position = PositionManager(client)

    if position.is_open(symbol):

        logger.info(
            f"{symbol} Position OPEN"
        )

        logger.info(
            f"Floating PNL : {position.floating_pnl(symbol)}"
        )

#CEGAH TP/SL TERBALIK
        if trade["side"] == "BUY":

            if trade["stop_loss"] >= trade["entry"]:
                raise ValueError("Invalid Stop Loss")

            if trade["take_profit"] <= trade["entry"]:
                raise ValueError("Invalid Take Profit")

        else:

            if trade["stop_loss"] <= trade["entry"]:
                raise ValueError("Invalid Stop Loss")

            if trade["take_profit"] >= trade["entry"]:
                raise ValueError("Invalid Take Profit")

 # TRADE MANAGER (FOR W/R DATA TRADE AND SUMMARY)       
    trade_manager = TradeManager()
    saved_trade = trade_manager.save_open_trade(active)
    
    logger.info(
        {
            "DATABASE TRADE SAVED":
            saved_trade.id
        }
    )

#STATUS POSISI      
    current_price = float(df["close"].iloc[-1])

    position_status = position_manager.check_position(current_price)

    logger.info(position_status)
    # ============================
    # MARKET CONTEXT
    # ============================

    context_engine = MarketContextEngine()



#MARKET DOMINANCE
    market_context = context_engine.analyze({

        "btc_trend":"NEUTRAL",

        "btc_dominance":"UNKNOWN",

        "eth_btc":"UNKNOWN"

    })


    logger.info(
        market_context
    )


    try:
        discord = DiscordReporter()
        logger.info("Discord Ready")

    except Exception as e:
        logger.error(f"Discord Error : {e}")
    # ==============================
    # TEST MODE ONLY
    # Aktifkan jika ingin test
    # run_system_check()
    # ==============================

    stats = Statistics()

    logger.info(
        stats.get_summary())

#BACKTEST PROGRAM
    backtest = BacktestRunner()

    result = backtest.run(
        symbol,
        "1h")

    logger.info(
        {"BACKTEST RESULT":result})

#DAILY REPORT PROGRAM
daily = DailyReport()

report = daily.generate()

logger.info(report)

# discord.send_daily_report(report)

weekly = WeeklyReport()

report = weekly.generate()

logger.info(

    report

)

# discord.send_weekly_report(report)

#v1.2
command = CommandEngine()

result = command.execute(

    "stats"

)

logger.info(result)

#test backtest
result = command.execute(

    "backtest",

    "BTCUSDT",

    "4h"

)

logger.info(result)



def start():
    client = BinanceClient()

    market = MarketData(client)

    indicator = IndicatorEngine()

    pattern = PatternEngine()

    context = MarketContextEngine()

    ### decision = DecisionEngine()

    trade_manager = TradeManager(client)

    position_manager = PositionManager(client)

    stats = Statistics()

    ### dashboard = Dashboard()


    # BANNER 
    show_banner()

    logger.info("Loading Configuration...")

    # Database
    logger.info("Initializing Database...")
    init_database()
    logger.info("Database Ready")

    # Logger
    logger.info("Logger Ready")

    # Binance
    logger.info("Connecting Binance...")

    try:
        binance = BinanceClient()
        binance.ping()
        logger.info("Binance Connected")
        logger.info("Loading Futures Account...")

        account = Account()

        market = Market()

        logger.info("Futures Account Ready")

        price = market.get_price(symbol)

        logger.info(

            f"(symbol) Price : {price['price']}")

        
    except Exception as e:
        logger.error(f"Binance Error : {e}")

        #WALLET ACCOUNT BINANCE
    try:

        balance = account.get_balance()
        logger.info(
            "Wallet Loaded")

        for asset in balance:
            if asset["asset"] == "USDT":

                logger.info(
                    f"USDT Balance : {asset['balance']}")
    except Exception as e:
        logger.warning(
            f"Wallet Check Skip : {e}")

#load market data
    logger.info("Loading Market Data...")
    try:
        df = market.get_dataframe(
            "BTCUSDT",
            "1m",
            200)

        logger.info(
            df.tail())

    except Exception as e:
        logger.error(
            f"Market Data Error : {e}")
        return   

    # ============================
    # INDICATOR ENGINE
    # ============================

    indicator = IndicatorEngine()
    result = indicator.calculate(
        df)
    logger.info(
        result)


    # Discord
    logger.info("Loading Discord...")

    # indicator
    indicator = IndicatorEngine()

    result = indicator.calculate(df)

    regime = RegimeDetector()

    market_state = regime.analyze(
        result
    )


    logger.info(
        market_state
    )
    
    logger.info(result)


    logger.info("=" * 60)
    logger.info("RIO AI FUTURES IS ONLINE")
    logger.info("=" * 60)

#AI SCORE bfore start position
    candidates = []

    candidates.append({

        "symbol": symbol,

        "score": ai_score,

        "decision": decision,

        "trade": trade_setup

    })

    candidates = sorted(

        candidates,

        key=lambda x: x["score"],

        reverse=True

    )

    best_trade = None

    for candidate in candidates:

        if candidate["decision"] != "WAIT":

            best_trade = candidate

            break

#idk
    if position_manager.is_open(

        best_trade["symbol"]

    ):

        logger.info(

            "Position already exists."

        )

        return

#LOOP PROGRAM
    import time

    logger.info(
        "Starting Live Trading Loop..."
    )

    while True:

        for symbol in WATCHLIST:

            run_cycle(symbol)

        time.sleep(30)

#YANG LAMA CODING LOOP PROGRAM
    # while True:

    #     try:
    #         run_cycle()

    #     except Exception as e:
    #         logger.error(e)

    #     time.sleep(30)

    logger.info(
        f"Cycle Time : {datetime.now()}"
    )

    if position_manager.is_open(symbol):

        logger.info(
            "Open Position Found"
        )
        return
    
    if decision == "WAIT":

        logger.info(
            "No Trade Signal"
        )
        return

logger.info(
    "Cycle Finished"
)

logger.info(
    "Take Profit Created"
)

logger.info(
    "Stop Loss Created"
)

dashboard = stats.live_dashboard()

logger.info("=" * 60)

logger.info("RIO AI FUTURES DASHBOARD")

logger.info("=" * 60)

logger.info(f"Balance        : {dashboard['balance']}")

logger.info(f"Floating PNL   : {dashboard['floating']}")

logger.info(f"Today Profit   : {dashboard['today_profit']}")

logger.info(f"Trade Today    : {dashboard['today_trade']}")

logger.info(f"Open Position  : {dashboard['open_position']}")

logger.info(f"Win Rate       : {dashboard['win_rate']} %")

logger.info("=" * 60)

###AI INPUT FEATURE ENGINE (SKIP DULU INI NANTI BANGET SAJA)
# feature_engine = FeatureEngine()

# features = feature_engine.build(

#     market_result,

#     pattern_result,

#     context_result,

#     mtf_result,

#     trade_setup

# )

###dataset
# row = features.copy()

# row["result"] = trade.result

# row["pnl"] = trade.pnl

# row["win"] = trade.win

# dataset.append(row)



### RENCANA NANTI 
# PHASE 2.50 🟢
# MULTI POSITION MANAGER
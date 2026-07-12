"""
====================================================
RIO AI FUTURES
Professional Binance Futures Trading Bot
====================================================
"""

from datetime import datetime
import platform

from config import Config


def show_banner():

    print("\n")

    print("=" * 60)
    print("                 RIO AI FUTURES")
    print("        Professional Trading Platform")
    print("=" * 60)

    print(f"Version      : {Config.VERSION}")
    print(f"Environment  : {Config.MODE.upper()}")
    print(f"Python       : {platform.python_version()}")
    print(f"Started At   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("-" * 60)
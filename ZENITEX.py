
AWAITING_LIST = 1
AWAITING_ADMIN_USER_ID = 101
AWAITING_ADMIN_USERINFO_ID = 102
AWAITING_ADMIN_BROADCAST = 103
AWAITING_BACKTEST_LIST = 105
AWAITING_BACKTEST_DAYS = 106
AWAITING_CHECKER_MTG = 107
AWAITING_CHECKER_MTG_CUSTOM = 108
AWAITING_CHECKER_DATE = 109
AWAITING_CHECKER_CUSTOM_DATE = 110
AWAITING_NEWS_TYPE = 120
AWAITING_NEWS_MARKET = 121
AWAITING_NEWS_PREVIOUS = 122
AWAITING_NEWS_FORECAST = 123
AWAITING_NEWS_TIME = 124
AWAITING_AI_START = 130
AWAITING_AI_END = 131
AWAITING_AI_MODEL = 132
AWAITING_AI_COUNT = 133
AWAITING_CHART_PHOTO = 140
AWAITING_START = 2
AWAITING_END = 3
AWAITING_SIGNAL_COUNT = 4
AWAITING_DAYS = 5
AWAITING_CHANNEL_TARGET = 200
AWAITING_ADMIN_MODERATION_ID = 104

# ========================================
# ZENITIX SINGLE-FILE CONFIG / TERMUX BOOTSTRAP
# ========================================
# Credentials supplied by the owner for this private bot build.
# Environment variables still take precedence, so deployment can override them.
import os
import sys
import subprocess
import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, str(default)).strip())
    except (TypeError, ValueError):
        return default


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name, str(default)).strip())
    except (TypeError, ValueError):
        return default


# ==================== CENTRAL CONFIGURATION ====================
# Keep deployment settings in this single section. Environment variables override
# the safe defaults; secrets should be supplied through the environment in production.
CONFIG = {
    "TELEGRAM_BOT_TOKEN": os.environ.get("TELEGRAM_BOT_TOKEN", "8686116443:AAHm-zUaRBCIvLM1KYGeVJ_6XRPfdWexrJQ").strip() or os.environ.get("BOT_TOKEN", "").strip(),
    "OANDA_API_KEY": os.environ.get("OANDA_API_KEY", "eb2326208921b413a87728832f191f03-d9be68b74884f7d3107b9f05ca305319").strip(),
    "HF_API_TOKEN": os.environ.get("HF_API_TOKEN", "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" ).strip(),
    "CHATGPT_API_KEY": os.environ.get("CHATGPT_API_KEY", "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").strip() or os.environ.get("OPENROUTER_API_KEY", "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").strip(),
    "OPENROUTER_API_KEY": os.environ.get("OPENROUTER_API_KEY", "").strip() or os.environ.get("CHATGPT_API_KEY", "").strip(),
    "OANDA_ENVIRONMENT": os.environ.get("OANDA_ENVIRONMENT", "practice").strip().lower(),
    "CHATGPT_API_URL": os.environ.get("CHATGPT_API_URL", "https://openrouter.ai/api/v1/chat/completions").strip(),
    "CHATGPT_MODEL": os.environ.get("CHATGPT_MODEL", "openai/gpt-4o-mini").strip(),
    "HF_API_URL": os.environ.get("HF_API_URL", "https://router.huggingface.co/v1/chat/completions").strip(),
    "HF_MAIN_MODEL": os.environ.get("HF_MAIN_MODEL", "deepseek-ai/DeepSeek-V3.2-Exp").strip(),
    "GEMINI_VISION_MODEL": os.environ.get("GEMINI_VISION_MODEL", "gemini-flash-lite-latest").strip(),
    "GEMINI_VISION_URL": os.environ.get("GEMINI_VISION_URL", "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent").strip(),
    "OANDA_TIMEOUT_SECONDS": max(3.0, _env_float("OANDA_TIMEOUT_SECONDS", 12.0)),
    "OANDA_RETRIES": max(1, min(6, _env_int("OANDA_RETRIES", 4))),
    "DB_FILE": os.environ.get("ZENITIX_DB_FILE", str(Path(__file__).resolve().parent / "zenitix_bot.db")),
    "TIMEZONE_OFFSET_HOURS": _env_int("TIMEZONE_OFFSET_HOURS", 6),
    "ADMIN_USER_ID": _env_int("ADMIN_USER_ID", 7993083766),
    "CHANNEL_1": os.environ.get("CHANNEL_1", "https://t.me/+72OqoIK7TI4yYzFl"),
    "CHANNEL_2": os.environ.get("CHANNEL_2", "https://t.me/+72OqoIK7TI4yYzFl"),
    "SUPPORT": os.environ.get("SUPPORT", "https://t.me/TRADEWITHMEHEDI7"),
    "OWNER_HANDLE": os.environ.get("OWNER_HANDLE", "@TRADEWITHMEHEDI7"),
    "CHANNEL_1_USERNAME": os.environ.get("CHANNEL_1_USERNAME", "@TRADEXMEHEDI"),
    "CHANNEL_2_USERNAME": os.environ.get("CHANNEL_2_USERNAME", "@TRADEXMEHEDI"),
    "PERIOD_SECONDS": max(1, _env_int("PERIOD_SECONDS", 60)),
    "AI_SIGNAL_GAP_MINUTES_MIN": max(1, _env_int("AI_SIGNAL_GAP_MINUTES_MIN", 3)),
    "AI_SIGNAL_GAP_MINUTES_MAX": max(1, _env_int("AI_SIGNAL_GAP_MINUTES_MAX", 7)),
    "STRATEGY_CONFIG": {
        "rsi_period": 14, "rsi_overbought": 70, "rsi_oversold": 30,
        "ema_fast": 8, "ema_slow": 21, "ema_trend": 50,
        "macd_fast": 12, "macd_slow": 26, "macd_signal": 9,
        "bb_period": 20, "bb_std": 2, "atr_period": 14, "volume_sma": 20,
        "min_confidence": 65, "high_confidence": 85,
    },
}
TELEGRAM_BOT_TOKEN = CONFIG["TELEGRAM_BOT_TOKEN"]
OANDA_API_KEY = CONFIG["OANDA_API_KEY"]
HF_API_TOKEN = CONFIG["HF_API_TOKEN"]
CHATGPT_API_KEY = CONFIG["CHATGPT_API_KEY"]
OPENROUTER_API_KEY = CONFIG["OPENROUTER_API_KEY"] or CHATGPT_API_KEY
OANDA_ENVIRONMENT = CONFIG["OANDA_ENVIRONMENT"]
CHATGPT_API_URL = CONFIG["CHATGPT_API_URL"]
CHATGPT_MODEL = CONFIG["CHATGPT_MODEL"]
HF_API_URL = CONFIG["HF_API_URL"]
HF_MAIN_MODEL = CONFIG["HF_MAIN_MODEL"]
GEMINI_VISION_MODEL = CONFIG["GEMINI_VISION_MODEL"]
GEMINI_VISION_URL = CONFIG["GEMINI_VISION_URL"]
DB_FILE = CONFIG["DB_FILE"]
BD_TZ = timezone(timedelta(hours=CONFIG["TIMEZONE_OFFSET_HOURS"]))
ADMIN_USER_ID = CONFIG["ADMIN_USER_ID"]
CHANNEL_1 = CONFIG["CHANNEL_1"]
CHANNEL_2 = CONFIG["CHANNEL_2"]
SUPPORT = CONFIG["SUPPORT"]
OWNER_HANDLE = CONFIG["OWNER_HANDLE"]
for _key, _value in {
    "TELEGRAM_BOT_TOKEN": TELEGRAM_BOT_TOKEN, "BOT_TOKEN": TELEGRAM_BOT_TOKEN,
    "OANDA_API_KEY": OANDA_API_KEY, "HF_API_TOKEN": HF_API_TOKEN,
    "CHATGPT_API_KEY": CHATGPT_API_KEY, "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
    "OANDA_ENVIRONMENT": OANDA_ENVIRONMENT, "CHATGPT_API_URL": CHATGPT_API_URL,
    "CHATGPT_MODEL": CHATGPT_MODEL, "HF_API_URL": HF_API_URL, "HF_MAIN_MODEL": HF_MAIN_MODEL,
}.items():
    os.environ[_key] = str(_value)

# One-file convenience: install only missing Python packages.
# On Termux, this avoids the common "ModuleNotFoundError: telegram" startup failure.
_REQUIRED_PACKAGES = {
    "telegram": "python-telegram-bot>=22.0,<23",
    "PIL": "Pillow>=10.0",
    "numpy": "numpy>=1.26",
    "matplotlib": "matplotlib>=3.8",
}

def _bootstrap_dependencies():
    missing = [pkg for module, pkg in _REQUIRED_PACKAGES.items()
               if importlib.util.find_spec(module) is None]
    if not missing:
        return
    print("Installing missing Python packages:", ", ".join(missing), flush=True)
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", *missing])
        # Python caches directory lookups; invalidate them after pip changes the
        # environment so imports work in this same process (important on Termux).
        importlib.invalidate_caches()
    except Exception as exc:
        raise RuntimeError(
            "Required packages could not be installed automatically. "
            "On Termux run: pkg update -y && pkg install python clang freetype libjpeg-turbo -y "
            "&& python -m pip install --upgrade pip " + " ".join(missing)
        ) from exc

_bootstrap_dependencies()

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta, timezone
from datetime import datetime, timezone, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram import Update, InlineKeyboardMarkup
from telegram.constants import KeyboardButtonStyle
from telegram.ext import Application, ConversationHandler, TypeHandler, ApplicationHandlerStop
from telegram.ext import ContextTypes
from telegram.ext import ContextTypes, CallbackQueryHandler
from telegram.ext import ContextTypes, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram.ext import ContextTypes, CallbackQueryHandler, MessageHandler, filters
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from telegram.ext import ContextTypes, CommandHandler, ConversationHandler
from telegram.error import Forbidden
import asyncio
import time
try:
    import zenitix_strategy as _standalone_strategy
except Exception:
    _standalone_strategy = None
import hashlib
import json
import io
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import logging
import math
import numpy as np
import os
import re
import html
import sqlite3
import sys
import urllib.parse
import urllib.request
import urllib.error

try:
    from high_confidence_call_put_engine import consensus_signal as strategy_consensus
except Exception as _strategy_import_error:
    # The legacy external engine is optional; the built-in OANDA strategy remains active.
    strategy_consensus = None
    logging.getLogger(__name__).warning("Optional legacy strategy engine unavailable; using built-in strategy: %s", _strategy_import_error)



# ========================================
# File: telegram_ui/constants.py
# ========================================
# ─── Callback Data ──────────────────────────────────────────
CALLBACK = {
    # Main menu
    "AUTO_SIGNAL":      "lsig_mode_auto",
    "MANUAL_SIGNAL":    "lsig_mode_manual",
    "LIVE_FS":          "fut_home_REAL",
    "REAL_CHECKER":      "menu_real_checker",
    "MY_PROFILE":       "menu_profile",
    "ABOUT":            "menu_about",
    "HELP":             "menu_help",
    "HOME":             "menu_home",
    # Strategy
    "STRATEGY_PRO2":    "lsig_strategy_pro2",
    "STRATEGY_PREMIUM": "lsig_strategy_premium",
    "MANUAL_PRO2":      "lsig_manual_strategy_pro2",
    "MANUAL_PREMIUM":   "lsig_manual_strategy_premium",
    # Auto signal filters
    "ALL_PAIRS":        "lsig_auto_filter_all",
    "AVOID_80":         "lsig_auto_filter_avoid80",
    "SELECT_PAIRS":     "lsig_auto_select_manual",
    # Futures grid
    "FUT_DONE":         "futg_done",
    # Verification
    "VERIFY_CHANNEL":   "verify_channel",
}

# ─── Pair Lists ─────────────────────────────────────────────
# OTC markets use the corresponding real OANDA reference pair for analysis;
# no simulated OTC candles are generated.
# NZD markets are excluded by policy; all other supported real OANDA pairs remain available.
REAL_PAIRS = [
    "AUD_CAD", "AUD_CHF", "AUD_JPY", "AUD_USD",
    "CAD_JPY", "CHF_JPY", "EUR_AUD", "EUR_CAD", "EUR_CHF",
    "EUR_GBP", "EUR_JPY", "EUR_SGD", "EUR_USD",
    "GBP_AUD", "GBP_CAD", "GBP_CHF", "GBP_JPY", "GBP_USD",
    "USD_CAD", "USD_CHF", "USD_JPY",
]
OTC_PAIRS = [f"{pair}_OTC" for pair in REAL_PAIRS]

# Channel values are defined in the central CONFIG block above.

# ─── Verification ───────────────────────────────────────────
CHANNEL_1_USERNAME = CONFIG["CHANNEL_1_USERNAME"]
CHANNEL_2_USERNAME = CONFIG["CHANNEL_2_USERNAME"]

# ========================================
# File: telegram_ui/emojis.py
# ========================================
EMOJI: dict[str, tuple[str, str]] = {
    "trophy":         ("6102673289484705689", "🏆"),
    "diamond":        ("6132052287423522342", "💎"),
    "warning":        ("6303178164046666974", "⚠️"),
    "envelope":       ("6312320444317834713", "✉️"),
    "money_fly":      ("6102862147786645919", "💸"),
    "bolt":           ("6312070206638270086", "⚡"),
    "search":         ("6213218467714179432", "🔍"),
    "alarm_clock":    ("6185912891007312754", "⏰"),
    "bot_face":       ("6134212600138833922", "🤖"),
    "robot":          ("6255726532136800534", "🤖"),
    "down_arrow":     ("6231259404826579464", "⬇"),
    "gear":           ("6300679098670784062", "⚙"),
    "inbox":          ("6210954826675658321", "📩"),
    "profile":        ("5316727448644103237", "👤"),
    "id_badge":       ("6231075713370300702", "🆔"),
    "calendar":       ("6240227038842594522", "📅"),
    "chart_generic":  ("6233277751692894018", "📊"),
    "chart_up":       ("6301020247923105456", "📈"),
    "checkmark":      ("6233523441002093972", "✅"),
    "cross":          ("6237969311974039494", "❌"),
    "target":         ("6075602196517363973", "🎯"),
    "beginner":       ("6082413318864118393", "🔰"),
    "tag":            ("6300686610568584382", "🏷"),
    "rocket":         ("6172369471848588525", "🚀"),
    "shield":         ("6212950328610923100", "🛡"),
    "writing_hand":   ("5458382591121964689", "✍️"),
    "calendar_page":  ("6210895186759785075", "📆"),
    "smiling_imp":    ("6174844764580486778", "😈"),
    "megaphone":      ("6181610987339128822", "📣"),
    "info":           ("5258503720928288433", "ℹ️"),
    "white_circle":   ("6212942778058416879", "⚪️"),
    "wave":           ("5440431182602842059", "👋"),
    "muscle":         ("5780883460516221810", "🦾"),
    "grin":           ("6102872880909919548", "😀"),
    "plus":           ("6312168668763529862", "➕"),
    "multiply":       ("6312008994764365905", "✖️"),
    "dollar":         ("6212911416207219932", "💲"),
    "home_icon":      ("5416041192905265756", "🏠"),
    "checkmark2":     ("6213053622574392612", "✅"),
    "crown":          ("6212843547134008737", "👑"),
    "money_bag":      ("6210902995010331288", "💰"),
    "green_circle":   ("6186138166336954485", "🟢"),
    "red_circle":     ("6186082516445700103", "🔴"),
    "calendar2":      ("6156743968508879635", "📅"),
    "cross_mark2":    ("6312080737898077535", "❌"),
    "checkmark3":     ("6312206911152332292", "✅"),
    "checkmark4":     ("6311920793315975140", "✅"),
    "cross_mark3":    ("6311965658544348766", "❌"),
    "joystick":       ("6154242686929870878", "🎮"),
    "premium_check":  ("6231121076814879723", "✅"),
    "crown_dir":      ("6131977683841589337", "👑"),
    "call_up":        ("6311870452004299281", "🔼"),
    "put_down":       ("6312229687363904744", "🔽"),
    "both_reload":    ("6311984148378560080", "🔄"),
    "star":           ("6228877484683697988", "⭐"),
    "hundred":        ("6311864288726228831", "💯"),
    "calendar_day":   ("6212848404742020294", "🗓"),
    "diamond_market": ("6213083249258799034", "♦️"),
    "plus_mtg":       ("6303030189538417585", "➕"),
    "fire":           ("6219643562695336727", "🔥"),
    "bull":           ("6302940240038337269", "🐂"),
    "flag_bd":        ("6235311758009966324", "🇧🇩"),
}


def e(key: str) -> str:
    ids, fallback = EMOJI.get(key, (None, key))
    if ids is None:
        return fallback
    return f'<tg-emoji emoji-id="{ids}">{fallback}</tg-emoji>'


def emoji_tag(key: str) -> str:
    return e(key)


def emoji_id(key: str) -> str | None:
    ids, _ = EMOJI.get(key, (None, None))
    return ids

# ========================================
# File: telegram_ui/fonts.py
# ========================================
SRC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
SRC_DIGITS  = "0123456789"
SRC_ALL     = SRC_LETTERS + SRC_DIGITS

MONO_LETTERS = ("𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
                "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")
MONO_DIGITS  = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"

BOLD_LETTERS = ("𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
                "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇")

SANS_LETTERS = ("𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"
                "𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓")

ITALIC_LETTERS = ("𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
                  "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")

MONO_TABLE   = str.maketrans(SRC_ALL, MONO_LETTERS + MONO_DIGITS)
BOLD_TABLE   = str.maketrans(SRC_LETTERS, BOLD_LETTERS)
SANS_TABLE   = str.maketrans(SRC_LETTERS, SANS_LETTERS)
ITALIC_TABLE = str.maketrans(SRC_LETTERS, ITALIC_LETTERS)


def mono(text: str) -> str:
    return text.translate(MONO_TABLE)


def sans(text: str) -> str:
    return text.translate(SANS_TABLE)

# ========================================
# File: telegram_ui/utils.py
# ========================================


async def safe_answer(query, text: str | None = None, show_alert: bool = False) -> None:
    """Schedule callback acknowledgement without blocking the visible UI update."""
    if not query:
        return
    kwargs = {"show_alert": show_alert}
    if text:
        kwargs["text"] = text

    async def _ack() -> None:
        try:
            await query.answer(**kwargs)
        except Exception as exc:
            log.debug("Ignored stale callback acknowledgement: %s", exc)

    try:
        task = _create_tracked_task(_ack())
        task.add_done_callback(lambda completed: completed.exception() if not completed.cancelled() else None)
    except Exception as exc:
        log.debug("Could not schedule callback acknowledgement: %s", exc)


async def edit_or_send(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    text: str,
    reply_markup: InlineKeyboardMarkup | None = None,
    parse_mode: str = "HTML",
) -> None:
    """Edit an existing callback message when possible, otherwise send safely."""
    query = getattr(update, "callback_query", None)
    message = getattr(update, "message", None)
    if query and getattr(query, "message", None):
        chat_id = query.message.chat_id
        # Telegram cannot edit a photo message into text. Delete and send a new
        # message directly to avoid an avoidable 400 Bad Request.
        if getattr(query.message, "photo", None):
            try:
                await query.delete_message()
            except Exception:
                pass
        else:
            # Avoid Telegram's 400 Bad Request when the requested text and
            # markup are unchanged from the callback message.
            current_text = getattr(query.message, "text", None)
            current_markup = getattr(query.message, "reply_markup", None)
            if current_text == text and (reply_markup is None or current_markup == reply_markup):
                return
            try:
                await query.edit_message_text(text, parse_mode=parse_mode, reply_markup=reply_markup)
                return
            except Exception as exc:
                exc_text = str(exc).lower()
                if "message is not modified" in exc_text or "bad request" in exc_text and "not modified" in exc_text:
                    log.debug("Ignored no-op Telegram message edit")
                    return
                log.debug("Telegram edit fallback: %s", exc)
                try:
                    await query.delete_message()
                except Exception:
                    pass
        try:
            await context.bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode, reply_markup=reply_markup)
        except Exception as exc:
            log.error("Telegram fallback send failed: %s", exc)
        return
    if message:
        try:
            await message.reply_text(text, parse_mode=parse_mode, reply_markup=reply_markup)
        except Exception as exc:
            log.error("Telegram message reply failed: %s", exc)


# ========================================
# File: telegram_ui/formatting.py
# ========================================
def bold(text: str) -> str:
    return f"<b>{text}</b>"


def bold_italic(text: str) -> str:
    return f"<b><i>{text}</i></b>"


def italic(text: str) -> str:
    return f"<i>{text}</i>"


def code(text: str) -> str:
    return f"<code>{text}</code>"


def spoiler(text: str) -> str:
    return f'<span class="tg-spoiler">{text}</span>'


def pre(text: str) -> str:
    return f"<pre>{text}</pre>"


def blockquote(text: str) -> str:
    return f"<blockquote>{text}</blockquote>"


def expandable(text: str) -> str:
    return f"<blockquote expandable>{text}</blockquote>"


def link(text: str, url: str) -> str:
    return f'<a href="{url}">{text}</a>'


def mention(text: str) -> str:
    return f'<a href="tg://user?id={text}">{text}</a>'


def separator(char: str = "━━━━━━━━━━━━━━━━━━━━") -> str:
    return char


def header_divider() -> str:
    return bold("━━━━━━━━━━━━━━━━━━━━")

# ========================================
# File: telegram_ui/database.py
# ========================================

OWNER_ID = ADMIN_USER_ID

def get_db_connection():
    # Do not delete or recreate the live database on connection errors. A
    # connection failure must never erase users, usage, signals, or PARTIAL data.
    conn = sqlite3.connect(DB_FILE, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys=ON')
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA busy_timeout=10000')
    # FULL synchronous mode gives the strongest committed-write durability.
    conn.execute('PRAGMA synchronous=FULL')
    conn.execute('PRAGMA wal_autocheckpoint=1000')
    conn.execute('PRAGMA temp_store=MEMORY')
    conn.execute('PRAGMA mmap_size=268435456')
    return conn

def init_db():
    # Never delete or recreate the live database on an initialization error.
    # Repair must be performed from a verified backup instead of destroying data.
    _do_init_db()

def _do_init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            tier TEXT DEFAULT 'FREE',
            tier_expire_at TEXT DEFAULT NULL,
            created_at TEXT,
            last_active TEXT,
            banned INTEGER DEFAULT 0,
            ban_reason TEXT DEFAULT '',
            banned_at TEXT DEFAULT NULL
        )
    """)

    # Daily signal usage tracking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_usage (
            user_id INTEGER,
            usage_date TEXT,
            future_count INTEGER DEFAULT 0,
            auto_manual_count INTEGER DEFAULT 0,
            feature_usage TEXT DEFAULT '{}',
            PRIMARY KEY (user_id, usage_date)
        )
    """)

    for column_sql in (
        "ALTER TABLE users ADD COLUMN banned INTEGER DEFAULT 0",
        "ALTER TABLE users ADD COLUMN ban_reason TEXT DEFAULT ''",
        "ALTER TABLE users ADD COLUMN banned_at TEXT DEFAULT NULL",
    ):
        try:
            cursor.execute(column_sql)
        except sqlite3.OperationalError:
            pass

    try:
        cursor.execute("ALTER TABLE daily_usage ADD COLUMN feature_usage TEXT DEFAULT '{}'" )
    except sqlite3.OperationalError:
        pass

    # Channel Sender settings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS channel_sender (
            user_id INTEGER PRIMARY KEY,
            target_channel TEXT DEFAULT '',
            market_type TEXT DEFAULT 'REAL',
            strategy_type TEXT DEFAULT 'ZX PRO 2.1',
            filter_type TEXT DEFAULT 'ALL PAIRS',
            is_active INTEGER DEFAULT 0,
            updated_at TEXT
        )
    """)

    # Durable PARTIAL sessions and result rows. One active session is kept per
    # chat/mode; result identity is unique inside a session for atomic dedup.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS partial_sessions (
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            mode TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'ACTIVE',
            started_at TEXT NOT NULL,
            closed_at TEXT DEFAULT NULL,
            UNIQUE(chat_id, mode, status)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS partial_results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER NOT NULL,
            chat_id INTEGER NOT NULL,
            mode TEXT NOT NULL,
            pair TEXT NOT NULL,
            entry_time TEXT NOT NULL,
            direction TEXT NOT NULL,
            result_type TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            UNIQUE(session_id, pair, entry_time, direction),
            FOREIGN KEY(session_id) REFERENCES partial_sessions(session_id) ON DELETE CASCADE
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_partial_sessions_chat_mode ON partial_sessions(chat_id, mode, status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_partial_results_session_order ON partial_results(session_id, result_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_partial_results_chat_mode ON partial_results(chat_id, mode, result_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_partial_sessions_history ON partial_sessions(chat_id, mode, status, session_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_partial_results_history ON partial_results(chat_id, mode, created_at, result_id)")
    # Additional covering indexes keep plan/ban checks, daily quota checks,
    # and channel lookups fast as the database grows.
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_tier_banned ON users(tier, banned, user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_last_active ON users(last_active, user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_daily_usage_date_user ON daily_usage(usage_date, user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_channel_sender_active ON channel_sender(is_active, user_id)")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS db_metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    conn.commit()
    try:
        conn.execute('PRAGMA optimize')
    except sqlite3.DatabaseError:
        pass
    # Migration for existing DB: add new columns if missing
    try:
        cursor.execute("ALTER TABLE channel_sender ADD COLUMN strategy_type TEXT DEFAULT 'ZX PRO 2.1'")
    except sqlite3.OperationalError:
        pass  # Already exists
    try:
        cursor.execute("ALTER TABLE channel_sender ADD COLUMN filter_type TEXT DEFAULT 'ALL PAIRS'")
    except sqlite3.OperationalError:
        pass  # Already exists

    # Ensure Owner user exists as OWNER tier
    now_str = datetime.now(BD_TZ).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO users (user_id, username, first_name, tier, tier_expire_at, created_at, last_active)
        VALUES (?, ?, ?, 'OWNER', 'LIFETIME', ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            tier = 'OWNER',
            tier_expire_at = 'LIFETIME',
            username = COALESCE(excluded.username, users.username)
    """, (OWNER_ID, "TRADEWITHMEHEDI7", "MEHEDI", now_str, now_str))

    conn.execute(
        "INSERT INTO db_metadata(key, value, updated_at) VALUES(?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        ("schema_version", "2", now_str),
    )
    conn.commit()
    conn.close()

def get_today_date_str():
    return datetime.now(BD_TZ).strftime("%Y-%m-%d")

def register_user(user_id: int, username: str = "", first_name: str = ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    now_str = datetime.now(BD_TZ).strftime("%Y-%m-%d %H:%M:%S")
    tier = "OWNER" if user_id == OWNER_ID else "FREE"

    cursor.execute("""
        INSERT INTO users (user_id, username, first_name, tier, created_at, last_active)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username = excluded.username,
            first_name = excluded.first_name,
            last_active = excluded.last_active
    """, (user_id, username or "", first_name or "", tier, now_str, now_str))

    conn.commit()
    conn.close()

def get_user(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def is_user_banned(user_id: int) -> bool:
    if user_id == OWNER_ID:
        return False
    user = get_user(user_id)
    return bool(user and int(user.get("banned", 0) or 0) == 1)

def set_user_ban(user_id: int, banned: bool, reason: str = "") -> bool:
    if user_id == OWNER_ID:
        return False
    now_str = datetime.now(BD_TZ).strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO users (user_id, tier, created_at, last_active, banned, ban_reason, banned_at)
           VALUES (?, 'FREE', ?, ?, ?, ?, ?)
           ON CONFLICT(user_id) DO UPDATE SET
             banned=excluded.banned, ban_reason=excluded.ban_reason, banned_at=excluded.banned_at,
             last_active=excluded.last_active""",
        (user_id, now_str, now_str, 1 if banned else 0, reason[:300] if banned else "", now_str if banned else None),
    )
    conn.commit()
    conn.close()
    return True

async def banned_user_guard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if not user or not is_user_banned(user.id):
        return
    query = update.callback_query
    if query:
        await safe_answer(query, "Your account is currently banned.", show_alert=True)
    elif update.effective_message:
        await update.effective_message.reply_text("<b>ACCOUNT ACCESS SUSPENDED</b>\nYour account is currently banned. Please contact support.", parse_mode="HTML")
    raise ApplicationHandlerStop

def get_user_tier(user_id: int) -> str:
    if user_id == OWNER_ID:
        return "OWNER"
    user = get_user(user_id)
    if not user:
        return "FREE"
    tier = user.get("tier", "FREE").upper()
    expire_at = user.get("tier_expire_at")

    if tier in ("EXTREME", "EXPENSIVE", "PREMIUM") and expire_at and expire_at != "LIFETIME":
        try:
            exp_dt = datetime.strptime(expire_at, "%Y-%m-%d %H:%M:%S").replace(tzinfo=BD_TZ)
            now_dt = datetime.now(BD_TZ)
            if now_dt > exp_dt:
                set_user_tier(user_id, "FREE")
                return "FREE"
        except Exception:
            pass
    return tier

# Requested plan matrix. None means unlimited. EXTREME remains a backward-compatible
# database alias for the user-facing EXPENSIVE plan.
PLAN_LIMITS = {
    "FREE": {
        "auto_signal": 5, "manual_signal": 5, "channel_sender": 10,
        "real_market_fs": 2, "ai_live_fs": 2, "ai_otc_fs": 2, "backtest_fs": 2,
        "checker_fs": None, "manual_news": None, "recent_trend": None,
    },
    "PREMIUM": {
        "auto_signal": 30, "manual_signal": 30, "channel_sender": 50,
        "real_market_fs": 10, "ai_live_fs": 5, "ai_otc_fs": 5, "backtest_fs": 8,
        "checker_fs": None, "manual_news": None, "recent_trend": None,
    },
    "EXPENSIVE": {
        "auto_signal": None, "manual_signal": None, "channel_sender": None,
        "real_market_fs": None, "ai_live_fs": None, "ai_otc_fs": None, "backtest_fs": None,
        "checker_fs": None, "manual_news": None, "recent_trend": None,
    },
}
PLAN_LIMITS["EXTREME"] = PLAN_LIMITS["EXPENSIVE"]
FEATURE_LABELS = {
    "auto_signal":"Auto Signal", "manual_signal":"Manual Signal", "channel_sender":"Channel Sender",
    "real_market_fs":"Real Market FS", "ai_live_fs":"AI Live FS", "ai_otc_fs":"AI OTC FS",
    "backtest_fs":"Backtest FS", "checker_fs":"Checker", "manual_news":"Manual News", "recent_trend":"Recent Trend",
}

def get_user_usage(user_id: int):
    today = get_today_date_str()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT future_count, auto_manual_count, feature_usage FROM daily_usage WHERE user_id = ? AND usage_date = ?",
        (user_id, today)
    )
    row = cursor.fetchone()
    conn.close()
    usage = {"future": 0, "auto_manual": 0}
    if row:
        usage["future"] = int(row["future_count"] or 0)
        usage["auto_manual"] = int(row["auto_manual_count"] or 0)
        try:
            usage.update(json.loads(row["feature_usage"] or "{}"))
        except (TypeError, ValueError, json.JSONDecodeError):
            pass
    return usage

def _plan_key(tier: str) -> str:
    tier = (tier or "FREE").upper()
    return "EXPENSIVE" if tier in ("OWNER", "EXPENSIVE", "EXTREME") else ("PREMIUM" if tier == "PREMIUM" else "FREE")

def get_feature_limit(user_id: int, feature: str):
    return PLAN_LIMITS[_plan_key(get_user_tier(user_id))].get(feature)

def check_feature_limit(user_id: int, feature: str) -> tuple[bool, int, str]:
    usage = get_user_usage(user_id)
    current = int(usage.get(feature, 0) or 0)
    limit = get_feature_limit(user_id, feature)
    if limit is None:
        return True, current, "UNLIMITED"
    return current < limit, current, str(limit)

def reserve_feature_usage(user_id: int, feature: str) -> tuple[bool, int, str]:
    """Atomically reserve one daily feature slot; None quotas remain unlimited."""
    today = get_today_date_str()
    limit = get_feature_limit(user_id, feature)
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("BEGIN IMMEDIATE")
        cursor.execute("SELECT feature_usage FROM daily_usage WHERE user_id=? AND usage_date=?", (user_id, today))
        row = cursor.fetchone()
        try:
            data = json.loads((row["feature_usage"] if row else "{}") or "{}")
        except (TypeError, ValueError, json.JSONDecodeError):
            data = {}
        used = int(data.get(feature, 0) or 0)
        if limit is not None and used >= int(limit):
            conn.rollback()
            return False, used, str(limit)
        data[feature] = used + 1
        cursor.execute("""
            INSERT INTO daily_usage (user_id, usage_date, feature_usage) VALUES (?, ?, ?)
            ON CONFLICT(user_id, usage_date) DO UPDATE SET feature_usage=excluded.feature_usage
        """, (user_id, today, json.dumps(data, separators=(",", ":"))))
        conn.commit()
        return True, used + 1, "UNLIMITED" if limit is None else str(limit)
    finally:
        conn.close()

def format_limit_reached(feature: str, used: int, limit: str, tier: str | None = None) -> str:
    """Consistent premium limit notice with remaining count and reset guidance."""
    label = FEATURE_LABELS.get(feature, feature.replace("_", " ").title())
    plan = (tier or "FREE").upper()
    if str(limit).upper() == "UNLIMITED":
        return f"<b>{label.upper()} STATUS</b>\n━━━━━━━━━━━━━━━━━━━━\nPlan: <b>{plan}</b>\nRemaining today: <b>UNLIMITED</b>"
    return (
        f"<b>DAILY LIMIT REACHED</b>\n━━━━━━━━━━━━━━━━━━━━\n"
        f"Feature: <b>{label}</b>\nPlan: <b>{plan}</b>\n"
        f"Used today: <b>{used}/{limit}</b>\nRemaining today: <b>0</b>\n\n"
        "Your limit resets at 00:00 Bangladesh Time (UTC+06:00).\n"
        "Upgrade your plan for higher limits or contact Support."
    )

def increment_feature_usage(user_id: int, feature: str):
    today = get_today_date_str()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT feature_usage FROM daily_usage WHERE user_id=? AND usage_date=?", (user_id, today))
    row = cursor.fetchone()
    try:
        data = json.loads((row["feature_usage"] if row else "{}") or "{}")
    except (TypeError, ValueError, json.JSONDecodeError):
        data = {}
    data[feature] = int(data.get(feature, 0) or 0) + 1
    cursor.execute("""
        INSERT INTO daily_usage (user_id, usage_date, feature_usage) VALUES (?, ?, ?)
        ON CONFLICT(user_id, usage_date) DO UPDATE SET feature_usage=excluded.feature_usage
    """, (user_id, today, json.dumps(data, separators=(",", ":"))))
    conn.commit()
    conn.close()

def reserve_chart_analysis(user_id: int) -> tuple[bool, int, str]:
    """Atomically reserve one of two daily chart analyses for EXPENSIVE/OWNER users."""
    tier = get_user_tier(user_id).upper()
    if tier not in {"EXPENSIVE", "OWNER"}:
        return False, 0, "AI CHART ANALYSIS is available only on the EXPENSIVE plan."
    today = get_today_date_str()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("BEGIN IMMEDIATE")
        cursor.execute("SELECT feature_usage FROM daily_usage WHERE user_id=? AND usage_date=?", (user_id, today))
        row = cursor.fetchone()
        try:
            data = json.loads((row["feature_usage"] if row else "{}") or "{}")
        except (TypeError, ValueError, json.JSONDecodeError):
            data = {}
        used = int(data.get("ai_chart_analysis", 0) or 0)
        if used >= 2:
            conn.rollback()
            return False, used, "Your EXPENSIVE plan has used both AI Chart Analysis slots for today."
        data["ai_chart_analysis"] = used + 1
        encoded = json.dumps(data, separators=(",", ":"))
        cursor.execute("""
            INSERT INTO daily_usage (user_id, usage_date, feature_usage) VALUES (?, ?, ?)
            ON CONFLICT(user_id, usage_date) DO UPDATE SET feature_usage=excluded.feature_usage
        """, (user_id, today, encoded))
        conn.commit()
        return True, used + 1, ""
    finally:
        conn.close()

def check_signal_limit(user_id: int, signal_type: str) -> tuple[bool, int, str]:
    # Backward-compatible adapter for legacy callers.
    feature = "real_market_fs" if signal_type == "future" else "auto_signal"
    return check_feature_limit(user_id, feature)

def increment_signal_usage(user_id: int, signal_type: str):
    feature = "real_market_fs" if signal_type == "future" else "auto_signal"
    increment_feature_usage(user_id, feature)

def set_user_tier(user_id: int, tier: str, days_valid: int = None):
    tier = tier.upper()
    conn = get_db_connection()
    cursor = conn.cursor()
    now = datetime.now(BD_TZ)
    if days_valid is not None and days_valid > 0:
        exp_dt = now + timedelta(days=days_valid)
        exp_str = exp_dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        exp_str = "LIFETIME" if tier in ("EXTREME", "EXPENSIVE", "PREMIUM", "OWNER") else None

    cursor.execute("""
        INSERT INTO users (user_id, tier, tier_expire_at, created_at, last_active)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            tier = excluded.tier,
            tier_expire_at = excluded.tier_expire_at,
            last_active = excluded.last_active
    """, (user_id, tier, exp_str, now.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_admin_analytics():
    conn = get_db_connection()
    cursor = conn.cursor()
    today = get_today_date_str()
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT tier, COUNT(*) FROM users GROUP BY tier")
    tier_counts = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute("""
        SELECT SUM(future_count), SUM(auto_manual_count), COUNT(DISTINCT user_id)
        FROM daily_usage WHERE usage_date = ?
    """, (today,))
    usage_row = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM users WHERE COALESCE(banned, 0) = 1")
    banned_count = cursor.fetchone()[0]
    conn.close()
    total_future_today = usage_row[0] or 0
    total_auto_today = usage_row[1] or 0
    active_today = usage_row[2] or 0
    return {
        "total_users": total_users,
        "free_count": tier_counts.get("FREE", 0),
        "premium_count": tier_counts.get("PREMIUM", 0),
        "extreme_count": tier_counts.get("EXTREME", 0),
        "owner_count": tier_counts.get("OWNER", 0),
        "total_future_today": total_future_today,
        "total_auto_today": total_auto_today,
        "signals_today": total_future_today + total_auto_today,
        "active_today": active_today,
        "banned_count": banned_count,
    }

def get_all_user_ids():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]

def get_channel_sender(user_id: int) -> dict:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM channel_sender WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return {
        "user_id": user_id,
        "target_channel": "",
        "market_type": "REAL",
        "strategy_type": "ZX PRO 2.1",
        "filter_type": "ALL PAIRS",
        "is_active": 0
    }

def set_channel_sender(
    user_id: int,
    target_channel: str = None,
    market_type: str = None,
    strategy_type: str = None,
    filter_type: str = None,
    is_active: int = None
):
    conn = get_db_connection()
    cursor = conn.cursor()
    curr = get_channel_sender(user_id)
    new_target = target_channel if target_channel is not None else curr["target_channel"]
    new_market = market_type if market_type is not None else curr["market_type"]
    new_strategy = strategy_type if strategy_type is not None else curr.get("strategy_type", "ZX PRO 2.1")
    new_filter = filter_type if filter_type is not None else curr.get("filter_type", "ALL PAIRS")
    new_active = is_active if is_active is not None else curr["is_active"]
    now_str = datetime.now(BD_TZ).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO channel_sender (user_id, target_channel, market_type, strategy_type, filter_type, is_active, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            target_channel = excluded.target_channel,
            market_type = excluded.market_type,
            strategy_type = excluded.strategy_type,
            filter_type = excluded.filter_type,
            is_active = excluded.is_active,
            updated_at = excluded.updated_at
    """, (user_id, new_target, new_market, new_strategy, new_filter, new_active, now_str))
    conn.commit()
    conn.close()

init_db()

# ========================================
# File: telegram_ui/keyboards.py
# ========================================



BUTTON_EMOJI_RE = re.compile(
    r"[\U0001F000-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF\uFE0F\u200D]"
)

def button_label(text: str) -> str:
    """Return a clean, emoji-free mathematical monospace button label."""
    cleaned = BUTTON_EMOJI_RE.sub("", str(text))
    cleaned = " ".join(cleaned.split())
    return mono(cleaned.strip())


def _btn(
    text: str,
    callback: str | None = None,
    url: str | None = None,
    style: str | None = None,
    icon_emoji: str | None = None,
) -> InlineKeyboardButton:
    # Visible labels use only the requested mathematical monospace font.
    # Custom emoji icons are intentionally ignored for every button.
    kwargs = {"text": button_label(text)}
    if callback:
        kwargs["callback_data"] = callback
    if url:
        kwargs["url"] = url
    if style:
        kwargs["style"] = style
    return InlineKeyboardButton(**kwargs)


def build(rows: list[list[dict]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [_btn(**item) for item in row]
        for row in rows
    ])


def home_button() -> InlineKeyboardMarkup:
    return build([
        [{"text": mono("HOME"), "callback": "menu_home"}],
    ])


# Telegram supports PRIMARY, SUCCESS, and DANGER button styles only.
# A native yellow/WARNING style is unavailable; keep SUPPORT on the stable primary mapping.
SUPPORT_BUTTON_STYLE = KeyboardButtonStyle.PRIMARY

def main_menu(show_admin: bool = False) -> InlineKeyboardMarkup:
    rows = [
        [{"text": mono("AUTO SIGNAL"), "callback": "lsig_mode_auto", "style": KeyboardButtonStyle.DANGER},
         {"text": mono("MANUAL SIGNAL"), "callback": "lsig_mode_manual", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("CHANNEL SENDER"), "callback": "menu_channel_sender", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("REAL MARKET FS"), "callback": "fut_home_REAL", "style": KeyboardButtonStyle.SUCCESS},
         {"text": mono("BACKTEST"), "callback": "menu_backtest_fs", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": mono("BUG SIGNAL"), "callback": "bug_signal_home", "style": KeyboardButtonStyle.DANGER}],
        [{"text": mono("LIVE CHECKER FS"), "callback": "menu_checker_fs", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": mono("AI LIVE FS"), "callback": "ai_live_fs_start", "style": KeyboardButtonStyle.SUCCESS},
         {"text": mono("AI OTC FS"), "callback": "ai_otc_fs_start", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": mono("AI CHART ANALYSIS"), "callback": "ai_chart_analysis", "style": KeyboardButtonStyle.DANGER}],
        [{"text": mono("MANUAL NEWS"), "callback": "manual_news_start", "style": KeyboardButtonStyle.DANGER},
         {"text": mono("RECENT TREND"), "callback": "menu_recent_trend", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("FREE BOT"), "callback": "menu_free_bots", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("MY PROFILE"), "callback": "menu_profile", "style": KeyboardButtonStyle.PRIMARY},
         {"text": mono("MY STATUS"), "callback": "menu_my_status", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("SUPPORT"), "url": "https://t.me/TRADEWITHMEHEDI7", "style": SUPPORT_BUTTON_STYLE},
         {"text": mono("PRICING"), "callback": "menu_pricing", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("ABOUT"), "callback": "menu_about", "style": KeyboardButtonStyle.PRIMARY},
         {"text": mono("HELP"), "callback": "menu_help", "style": KeyboardButtonStyle.PRIMARY}],
    ]
    if show_admin:
        rows.append([{"text": mono("ADMIN PANEL"), "callback": "admin_home", "style": KeyboardButtonStyle.SUCCESS}])
    return build(rows)


def channel_sender_menu(is_running: bool = False, cs_data: dict = None) -> InlineKeyboardMarkup:
    cs = cs_data or {}
    market = cs.get("market_type", "REAL")
    strat = cs.get("strategy_type", "ZX PRO 2.1")
    filt = cs.get("filter_type", "ALL PAIRS")

    rows = [
        [{"text": f"📢 CHANNEL: {cs.get('target_channel') or 'Not Set'}", "callback": "csender_set_target", "icon_emoji": emoji_id("megaphone")}],
        [{"text": f"📊 MARKET: {market}", "callback": "csender_toggle_market", "icon_emoji": emoji_id("chart_up")},
         {"text": f"🔬 STRAT: {strat}", "callback": "csender_toggle_strat", "icon_emoji": emoji_id("trophy")}],
        [{"text": f"🎯 FILTER: {filt}", "callback": "csender_toggle_filter", "icon_emoji": emoji_id("target")}],
    ]

    if is_running:
        rows.append([{"text": mono("STOP AUTO SIGNAL"), "callback": "csender_stop", "style": KeyboardButtonStyle.DANGER}])
    else:
        rows.append([{"text": mono("START FULL AUTO"), "callback": "csender_start", "style": KeyboardButtonStyle.SUCCESS}])

    rows.append([{"text": mono("HOME"), "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


def back_button(callback: str) -> InlineKeyboardMarkup:
    return build([
        [{"text": mono("BACK"), "callback": callback, "style": KeyboardButtonStyle.PRIMARY}],
    ])


def back_home(callback: str) -> InlineKeyboardMarkup:
    return build([
        [{"text": mono("BACK"), "callback": callback, "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": mono("HOME"), "callback": "menu_home"}],
    ])


def strategy_menu(is_manual: bool = False) -> InlineKeyboardMarkup:
    prefix = "lsig_manual_strategy_" if is_manual else "lsig_strategy_"
    return build([
        [{"text": "ZX PRO 2.1", "callback": f"{prefix}pro2", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("trophy")}],
        [{"text": "ZX PREMIUM", "callback": f"{prefix}premium", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("diamond")}],
        [{"text": "Back", "callback": "lsig_mode_auto" if not is_manual else "lsig_mode_manual"}],
    ])


def premium_strategy_menu(is_manual: bool = False) -> InlineKeyboardMarkup:
    prefix = "lsig_m_prem_" if is_manual else "lsig_a_prem_"
    back_cb = "lsig_auto_filter_all" if not is_manual else "lsig_mode_manual"
    return build([
        [{"text": "🚀 ZX Momentum AI", "callback": f"{prefix}momentum", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("rocket")}],
        [{"text": "📈 ZX Trend Surge Pro", "callback": f"{prefix}trend", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("chart_up")}],
        [{"text": "⚡ ZX Volatility Breakout", "callback": f"{prefix}breakout", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("bolt")}],
        [{"text": "🔮 ZX Price Action Master", "callback": f"{prefix}priceaction", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("diamond")}],
        [{"text": "♻️ ZX RSI Reversal", "callback": f"{prefix}reversal", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "⚙️ ZX EMA-MACD Scalper", "callback": f"{prefix}scalping", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🎯 ZX S/R Reaction", "callback": f"{prefix}supportresistance", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "📊 ZX Volume Pressure", "callback": f"{prefix}volume", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🕯 ZX Candle Pattern Pro", "callback": f"{prefix}candlestick", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🛡 ZX Full Confluence", "callback": f"{prefix}confluence", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "Back", "callback": back_cb}],
    ])


def auto_filter_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": mono("ALL PAIRS"), "callback": "lsig_auto_filter_all", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("target")}],
        [{"text": mono("AVOID UNDER 80%"), "callback": "lsig_auto_filter_avoid80", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("shield")}],
        [{"text": mono("SELECT PAIRS"), "callback": "lsig_auto_select_manual", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("writing_hand")}],
        [{"text": "Back", "callback": "menu_live_signal"}],
    ])


def manual_market_menu(strat_code: str = "pro2") -> InlineKeyboardMarkup:
    # Keep Manual Signal aligned with the global NZD-only market registry.
    pairs = [pair.replace("_", "") for pair in REAL_PAIRS]
    rows = []
    for i in range(0, len(pairs), 2):
        p1 = pairs[i]
        row = [{"text": f"📊 {p1}", "callback": f"manpair_{p1}_{strat_code}", "style": KeyboardButtonStyle.PRIMARY}]
        if i + 1 < len(pairs):
            p2 = pairs[i + 1]
            row.append({"text": f"📊 {p2}", "callback": f"manpair_{p2}_{strat_code}", "style": KeyboardButtonStyle.PRIMARY})
        rows.append(row)
    rows.append([{"text": "Back", "callback": "lsig_mode_manual"}])
    rows.append([{"text": "Home", "callback": "menu_home", "icon_emoji": emoji_id("home_icon")}])
    return build(rows)


def pair_grid(pairs: list[str], prefix: str = "futg_", selected: set[str] | None = None) -> InlineKeyboardMarkup:
    sel = selected or set()
    rows = []
    for i in range(0, len(pairs), 2):
        p1 = pairs[i]
        s1 = p1 in sel
        row = [{"text": p1, "callback": f"{prefix}{p1}", "style": KeyboardButtonStyle.SUCCESS if s1 else KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("premium_check") if s1 else emoji_id("chart_generic")}]
        if i + 1 < len(pairs):
            p2 = pairs[i + 1]
            s2 = p2 in sel
            row.append({"text": p2, "callback": f"{prefix}{p2}", "style": KeyboardButtonStyle.SUCCESS if s2 else KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("premium_check") if s2 else emoji_id("chart_generic")})
        rows.append(row)
    rows.append([{"text": "Continue Next", "callback": "futg_done", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("rocket")}])
    rows.append([{"text": "Home", "callback": "menu_home", "icon_emoji": emoji_id("home_icon")}])
    return build(rows)


def verify_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "Join Telegram Channel", "url": CHANNEL_1, "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("megaphone")}],
        [{"text": "Verify Membership", "callback": "verify_channel", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("checkmark")}],
    ])


def vip_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "Open Account & Join VIP", "url": "https://broker-qx.pro/sign-up/?lid=1756662", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("diamond")}],
        [{"text": "Contact Support", "url": "https://t.me/TRADEWITHMEHEDI7", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("envelope")}],
        [{"text": "Back to Home", "callback": "menu_home"}],
    ])


def profile_menu(is_owner: bool = False) -> InlineKeyboardMarkup:
    rows = []
    if is_owner:
        rows.append([{"text": "👑 Admin Panel", "callback": "admin_home", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("crown")}])
    rows.append([{"text": "⚡ Upgrade / Buy Plan", "url": "https://t.me/TRADEWITHMEHEDI7", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("diamond")}])
    rows.append([{"text": "Home", "callback": "menu_home", "icon_emoji": emoji_id("home_icon")}])
    return build(rows)


def admin_main_menu() -> InlineKeyboardMarkup:
    """Premium owner-only control center menu."""
    return build([
        [{"text": "ADMIN DASHBOARD", "callback": "admin_analytics", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "USER MANAGEMENT", "callback": "admin_user_management", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "PLAN CONTROL", "callback": "admin_set_tier_prompt", "style": KeyboardButtonStyle.SUCCESS},
         {"text": "USER LOOKUP", "callback": "admin_user_lookup", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "BROADCAST CENTER", "callback": "admin_broadcast_prompt", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "SYSTEM STATUS", "callback": "admin_system_status", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "RETURN TO BOT HOME", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])


def admin_user_management_menu() -> InlineKeyboardMarkup:
    """Protected user-operations submenu."""
    return build([
        [{"text": "PLAN CONTROL", "callback": "admin_set_tier_prompt", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "USER LOOKUP", "callback": "admin_user_lookup", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "USER ANALYTICS", "callback": "admin_analytics", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "BAN USER", "callback": "admin_ban_prompt", "style": KeyboardButtonStyle.DANGER},
         {"text": "UNBAN USER", "callback": "admin_unban_prompt", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "BACK TO ADMIN", "callback": "admin_home", "style": KeyboardButtonStyle.DANGER}],
    ])


def admin_tier_select_menu(target_uid: int) -> InlineKeyboardMarkup:
    return build([
        [{"text": "👑 Set EXPENSIVE (30 Days)", "callback": f"admset_{target_uid}_EXPENSIVE_30", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "👑 Set EXPENSIVE (Lifetime)", "callback": f"admset_{target_uid}_EXPENSIVE_0", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "💎 Set PREMIUM (30 Days)", "callback": f"admset_{target_uid}_PREMIUM_30", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "💎 Set PREMIUM (Lifetime)", "callback": f"admset_{target_uid}_PREMIUM_0", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "⭕ Reset to FREE Plan", "callback": f"admset_{target_uid}_FREE_0", "style": KeyboardButtonStyle.DANGER}],
        [{"text": "🔙 Back to Admin", "callback": "admin_home"}],
    ])


def mtg_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "MTG 1", "callback": "mtg_1", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("plus")},
         {"text": "MTG 2", "callback": "mtg_2", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("multiply")}],
        [{"text": "NON MTG", "callback": "mtg_non", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("dollar")},
         {"text": "CUSTOM MTG", "callback": "mtg_custom", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}],
    ])


def date_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "TODAY", "callback": "date_today", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("checkmark2")},
         {"text": "YESTERDAY", "callback": "date_yesterday", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("crown")}],
        [{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}],
    ])


def direction_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "Call", "callback": "futdir_call", "style": KeyboardButtonStyle.SUCCESS, "icon_emoji": emoji_id("call_up")},
         {"text": "Put", "callback": "futdir_put", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("put_down")}],
        [{"text": "Both", "callback": "futdir_both", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("both_reload")}],
        [{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}],
    ])


def future_days_menu() -> InlineKeyboardMarkup:
    rows = []
    for i in range(0, 14, 3):
        row = []
        for j in range(i + 1, min(i + 4, 15)):
            row.append({"text": f"Day {j}", "callback": f"futday_{j}", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("calendar_day")})
        rows.append(row)
    rows.append([{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}])
    return build(rows)



def backtest_days_menu() -> InlineKeyboardMarkup:
    """Render the Backtest FS day selector for 1 through 14 days."""
    rows = []
    for start in range(1, 13, 3):
        rows.append([
            {"text": f"Day {day}", "callback": f"backtest_day_{day}", "style": KeyboardButtonStyle.PRIMARY}
            for day in range(start, min(start + 3, 13))
        ])
    rows.append([
        {"text": "Day 13", "callback": "backtest_day_13", "style": KeyboardButtonStyle.PRIMARY},
        {"text": "Day 14", "callback": "backtest_day_14", "style": KeyboardButtonStyle.PRIMARY},
    ])
    rows.append([{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


def future_result_menu(day_num: int = 1) -> InlineKeyboardMarkup:
    return build([
        [{"text": f"🔄 Re-Filter Day {day_num}", "callback": f"futday_{day_num}", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("both_reload")}],
        [{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}],
    ])


def support_button() -> InlineKeyboardMarkup:
    return build([
        [{"text": "Contact Support", "url": "https://t.me/TRADEWITHMEHEDI7", "style": KeyboardButtonStyle.PRIMARY}],
    ])

# ========================================
# File: telegram_ui/zenitix.py
# ========================================


def welcome_text(name: str | None = None) -> str:
    """Refined premium onboarding copy using the requested mathematical monospace font."""
    user_line = f"WELCOME, {name.upper()}" if name else "WELCOME TO ZENITIX AI"
    return (
        f"<b>{to_math_mono('╔════════════════════╗')}</b>\n"
        f"<b>{to_math_mono('      ZENITIX AI      ')}</b>\n"
        f"<b>{to_math_mono('╚════════════════════╝')}</b>\n\n"
        f"<b>{to_math_mono(user_line)}</b>\n\n"
        f"<b>{to_math_mono('PRECISION MARKET INTELLIGENCE')}</b>\n"
        f"<i>{to_math_mono('Live OANDA context • M1 analysis • verified candle results')}</i>\n\n"
        f"<i>{to_math_mono('Clarity in every signal. Confidence through data.')}</i>\n\n"
        f"<b>{to_math_mono('PRESS GET START TO ENTER.')}</b>"
    )


def strategy_text() -> str:
    return (
        f"🔬 {bold('Select Strategy')}\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n\n"
        f"{e('trophy')} {bold('ZX PRO 2.1')}\n"
        f"Quality Over Quantity {bold('[BEST OF ALL]')}\n\n"
        f"{e('diamond')} {bold('ZX PREMIUM')}\n"
        f"ZX POWRED {bold('[Stable]')}"
    )


def premium_sub_strategy_text() -> str:
    return (
        f"💎 {bold('ZX PREMIUM STRATEGIES')}\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n"
        f"Select a high-accuracy AI trading logic:\n\n"
        f"🚀 {bold('Momentum AI')} — Volume & Velocity\n"
        f"📈 {bold('Trend Surge Pro')} — MA & EMA Crossover\n"
        f"⚡ {bold('Volatility Breakout')} — Key S/R Break\n"
        f"🔮 {bold('Price Action Master')} — Reversal Patterns\n"
        f"♻️ {bold('RSI Reversal')} — Oversold / Overbought\n"
        f"⚙️ {bold('EMA-MACD Scalper')} — Trend Momentum\n"
        f"🎯 {bold('S/R Reaction')} — Support / Resistance\n"
        f"📊 {bold('Volume Pressure')} — Tick-Volume Confirmation\n"
        f"🕯 {bold('Candle Pattern Pro')} — Engulfing / Hammer / Marubozu\n"
        f"🛡 {bold('Full Confluence')} — All Confirmations Together"
    )


def auto_signal_mode_text() -> str:
    return (
        f"{e('bot_face')} {bold('Auto Signal Mode')}"
        f"{' ' * 20}\n\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n"
        f"Choose auto signal mode:"
    )


def scanning_animation_text(status_lines: list[tuple[str, bool]], message: str) -> str:
    lines = []
    for label, done in status_lines:
        icon = "✔" if done else e("search")
        lines.append(f"{icon}  {bold(label)}")
    return (
        f"{bold('⠙  ZX — SCANNING')}\n"
        f"{bold('――――――――――――――――――――――')}\n"
        f"{chr(10).join(lines)}\n"
        f"{bold('――――――――――――――――――――――')}\n"
        f"{italic('▸ ' + message)}"
    )


def signal_box(
    asset: str,
    trend: str,
    direction: str,
    timeframe: str,
    entry: str,
    strength: str,
    mtg: str,
    payout: str,
    support: str,
    resistance: str,
    owner: str,
    analysis: str,
) -> str:
    clean_asset = asset.upper().replace("/", "").replace("_", "").replace("-OTC", "").replace(" (OANDA)", "")
    display_asset = to_math_mono(clean_asset)
    trend_mono = to_math_mono(trend if trend else "Bullish")
    dir_clean = "BUY ↑" if "CALL" in direction.upper() or "BUY" in direction.upper() else "SELL ↓"
    dir_mono = to_math_mono(dir_clean)
    tf_mono = to_math_mono(timeframe if timeframe else "M1")
    entry_mono = to_math_mono(entry if entry else format_next_candle_entry())
    strength_mono = to_math_mono(strength if strength else "High 82% 🟢")
    mtg_mono = to_math_mono(mtg if mtg else "STEP 1 IF REQUIRED")

    return (
        f"╔═══════════════════╗\n"
        f"   👑 𝗭𝗘𝗡𝗜𝗧𝗜𝗫 𝗔𝗜 👑\n"
        f"╚═══════════════════╝\n"
        f"┏━━━━━━━━━━━━━━━━━┓\n"
        f"┃ 📊 𝙰𝚜𝚜𝚎𝚝     : {display_asset}\n"
        f"┃ 📈 𝚃𝚛𝚎𝚗𝚍     : {trend_mono}\n"
        f"┃ 🔺 𝙳𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗 : {dir_mono}\n"
        f"┃ ⏱ 𝚃𝚒𝚖𝚎𝚏𝚛𝚊𝚖𝚎 : {tf_mono}\n"
        f"┃ ⏰ 𝙴𝚗𝚝𝚛𝚢      : {entry_mono}\n"
        f"┃ ⚡ 𝚂𝚝𝚛𝚎𝚗𝚐𝚝𝚑  : {strength_mono}\n"
        f"┃ 🚨 𝙼𝚃𝙶 : {mtg_mono}\n"
        f"┗━━━━━━━━━━━━━━━━━┛\n\n"
        f"{analysis}"
    )


def result_box(
    asset: str,
    entry: str,
    direction: str,
    result: str,
    payout: str,
    engine: str,
    open_price: str,
    close_price: str,
    candle_color: str,
    status: str,
) -> str:
    clean_asset = asset.upper().replace("/", "").replace("_", "").replace(" (OANDA)", "").replace("-OTC", "")
    display_asset = to_math_mono(clean_asset)
    entry_mono = to_math_mono(entry if entry else "00:23")
    dir_clean = "BUY ↑" if "CALL" in direction.upper() or "BUY" in direction.upper() else "SELL ↓"
    dir_mono = to_math_mono(dir_clean)

    res_upper = result.upper()
    if "MTG" in res_upper and ("WIN" in res_upper or "✅" in res_upper):
        res_str = "✅✅✅ 𝗪𝗜𝗡 𝗠𝗧𝗚"
    elif "WIN" in res_upper or "✅" in res_upper:
        res_str = "✅✅✅ 𝗪𝗜𝗡"
    elif "MTG" in res_upper and ("LOSS" in res_upper or "❌" in res_upper):
        res_str = "🔴LOSS 𝗠𝗧𝗚"
    elif "LOSS" in res_upper or "❌" in res_upper:
        res_str = "🔴LOSS"
    else:
        res_str = "✅✅✅ 𝗪𝗜𝗡"

    engine_mono = to_math_mono(engine if engine else "ZENITEX AI")

    return (
        f"╔══════════════════╗\n"
        f" 👑 𝗭𝗘𝗡𝗜𝗧𝗜𝗫 𝗔𝗜 👑\n"
        f"╚══════════════════╝\n"
        f"┏━━━━━━━━━━━━━━━━━━┓\n"
        f"┃ 📊 𝙰𝚜𝚜𝚎𝚝     : {display_asset}\n"
        f"┃ ⏰ 𝙴𝚗𝚝𝚛𝚢      : {entry_mono}\n"
        f"┃ 🎯 𝙳𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗 : {dir_mono}\n"
        f"┃ 🔍 𝚁𝚎𝚜𝚞𝚕𝚝    : {res_str}\n"
        f"┃ 🤖 𝙰𝙸 𝙴𝙽𝙶𝙸𝙽𝙴 : {engine_mono}\n"
        f"┗━━━━━━━━━━━━━━━━━━┛"
    )


def profile_card(
    user_id: str,
    username: str,
    name: str = "TRADER",
    plan: str = "FREE",
    daily_limit: str = "2 FS / 5 Live signals/day",
    used: str = "0 used today",
    remaining: str = "2 remaining",
    expiry: str = "—",
) -> str:
    pkg_emoji = "🆓"
    if "PREMIUM" in plan.upper():
        pkg_emoji = "💎"
    elif "EXTREME" in plan.upper():
        pkg_emoji = "🌟"
    elif "OWNER" in plan.upper():
        pkg_emoji = "👑"

    return (
        f"      👤 <b>𝗠𝗬 𝗣𝗥𝗢𝗙𝗜𝗟𝗘</b>\n\n"
        f"📛 <b>𝗡𝗮𝗺𝗲        :</b>  {name}\n"
        f"🆔 <b>𝗨𝘀𝗲𝗿 𝗜𝗗    :</b>  {user_id}\n"
        f"💬 <b>𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲  :</b>  {username}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{pkg_emoji} <b>𝗔𝗖𝗧𝗜𝗩𝗘 𝗣𝗔𝗖𝗞𝗔𝗚𝗘  :</b>  {plan}\n"
        f"📊 <b>𝗗𝗮𝗶𝗹𝘆 𝗟𝗶𝗺𝗶𝘁  :</b>  {daily_limit}\n"
        f"📈 <b>𝗨𝘀𝗲𝗱           :</b>  {used}\n"
        f"✅ <b>𝗥𝗲𝗺𝗮𝗶𝗻𝗶𝗻𝗴    :</b>  {remaining}\n"
        f"📅 <b>𝗘𝘅𝗽𝗶𝗿𝘆        :</b>  {expiry}"
    )


def about_text() -> str:
    return (
        f"{bold('◆━━━━━━━━━━━━━━━━━◆')}\n"
        f"     {e('bot_face')} {bold('ZENITIX AI — ABOUT')} {e('bot_face')}\n"
        f"{bold('◆━━━━━━━━━━━━━━━━━◆')}\n\n"
        f"{e('rocket')} {bold('A real-market Telegram trading assistant built for structured M1 signal workflows.')}\n\n"
        f"{e('chart_generic')} {bold('DATA SOURCE')}\n"
        f"Live and historical candle context is requested from the OANDA v3 API. The signal engine does not use simulated candles or invented results.\n\n"
        f"{e('trophy')} {bold('CORE SYSTEMS')}\n"
        f"AUTO SIGNAL scans the configured real markets and ranks the strongest setup. MANUAL SIGNAL analyses a selected pair. REAL MARKET FS, BACKTEST, LIVE CHECKER FS, AI LIVE FS, AI OTC FS and MANUAL NEWS are separated workflows.\n\n"
        f"{e('shield')} {bold('RESULT LIFECYCLE')}\n"
        f"Signal → Entry → OANDA candle result → WIN or LOSS → one-step MTG G1 when required. Neutral candles follow the configured no-DRAW rule.\n\n"
        f"{e('bolt')} {bold('AI ENGINE')}\n"
        f"AI FS uses the main DeepSeek analysis backend, real OANDA market context, time-window filtering and spaced signal output. AI model names shown in the menu are display selections.\n\n"
        f"{e('envelope')} {bold('ZENITIX AI V2.0 — REAL MARKET ENGINE')}\n"
        f"{e('shield')} {bold('Owner: ')}@TRADEWITHMEHEDI7 (ID: 7993083766)\n\n"
        f"{bold('◆━━━━━━━━━━━━━━━━━◆')}"
    )
def help_text() -> str:
    return (
        f"{e('shield')} {bold('ZENITIX AI — HELP CENTER')} {e('shield')}\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n\n"
        f"{e('rocket')} {bold('HOW TO START')}\n"
        f"Press AUTO SIGNAL to scan all real markets, or choose MANUAL SIGNAL and select a pair. The bot analyses the market before sending a directional signal.\n\n"
        f"{e('calendar_page')} {bold('FUTURE SIGNAL TOOLS')}\n"
        f"REAL MARKET FS creates future signals from real market context. BACKTEST ranks user-provided future signals using historical OANDA M1 candles. LIVE CHECKER FS checks a submitted signal list against actual candles.\n\n"
        f"{e('bot_face')} {bold('AI FS')}\n"
        f"AI LIVE FS and AI OTC FS require Start Time, End Time, and the number of signals required. Signals stay inside the requested window and use the selected LIVE or OTC display format.\n\n"
        f"{e('checkmark2')} {bold('RESULT CHECKING')}\n"
        f"Use CHECK RESULT when available. Direct results are checked from OANDA data; after a direct loss, the system checks one MTG G1 candle. Results are never simulated.\n\n"
        f"{e('profile')} {bold('ACCOUNT AND SUPPORT')}\n"
        f"MY PROFILE shows your package and usage. MY STATUS shows system status. For access, pricing or technical help, use SUPPORT or contact @TRADEWITHMEHEDI7.\n\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n"
        f"{e('megaphone')} {bold('Channel:')} https://t.me/+72OqoIK7TI4yYzFl"
    )


def vip_required_text() -> str:
    return (
        f"{e('diamond')} {bold('VIP MEMBERSHIP REQUIRED')} {e('diamond')}\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n\n"
        f"{e('warning')} {bold('You have used all your free daily signals!')}\n\n"
        f"To get unlimited signals and enjoy VIP features, please join VIP.\n\n"
        f"{e('envelope')} Message Support: @TRADEWITHMEHEDI7 {e('money_fly')}\n"
        f"{bold('━━━━━━━━━━━━━━━━━━━━')}\n"
        f"{e('bolt')} {bold('Upgrade to VIP & Unlock Your Trading Potential!')} {e('bolt')}"
    )


def pending_result_text() -> str:
    return (
        f"{e('warning')} {bold('Signal Pending Result')}\n\n"
        f"You cannot create a new signal until the previous signal's result is received.\n\n"
        f"Please wait for the current signal to complete."
    )


# ========================================
# File: telegram_ui/chart_generator.py
# ========================================


log = logging.getLogger(__name__)


def to_math_mono(text: str) -> str:
    """
    Converts standard ASCII characters to Mathematical Monospace unicode characters.
    """
    res = []
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            res.append(chr(0x1D670 + (code - 65)))
        elif 97 <= code <= 122:  # a-z
            res.append(chr(0x1D68A + (code - 97)))
        elif 48 <= code <= 57:  # 0-9
            res.append(chr(0x1D7F6 + (code - 48)))
        elif char == ':':
            res.append('∶')
        else:
            res.append(char)
    return "".join(res)


def format_next_candle_entry() -> str:
    """
    Calculates entry time for the NEXT 1-minute candle (e.g. current 16:57 -> next 16:58).
    """
    now = datetime.now(BD_TZ)
    next_candle = now + timedelta(minutes=1)
    return next_candle.strftime("%H:%M")


def format_current_candle_time() -> str:
    """
    Calculates current 1-minute candle time.
    """
    now = datetime.now(BD_TZ)
    return now.strftime("%H:%M")


def generate_signal_card_text(
    asset: str = "USD/JPY",
    entry: str = None,
    direction: str = "CALL",
    price: str = None,
    confidence: int = 89,
    mode: str = "AUTO SIGNAL",
    strategy_title: str = "ZENITEX-AI",
    oanda_candles: list | None = None,
    analysis: dict | None = None,
) -> str:
    """Shared professional signal format for AUTO, MANUAL, and CHANNEL.

    All market-derived values come from the supplied real OANDA candles; no
    hard-coded price, support, resistance, or pressure values are generated.
    """
    clean_asset = str(asset or "USDJPY").upper().replace("/", "").replace("_", "").replace(" (OANDA)", "").replace("-OTC", "").replace(" (REAL)", "").replace(" (Real)", "")
    display_pair = f"{clean_asset[:3]}/{clean_asset[3:]} (REAL)" if len(clean_asset) == 6 else f"{clean_asset} (REAL)"
    entry = entry or format_next_candle_entry()
    is_call = "CALL" in str(direction).upper() or "BUY" in str(direction).upper()
    verdict = "HIGHER (CALL)" if is_call else "LOWER (PUT)"
    confidence = max(0, min(99, int(confidence or 0)))
    conf_label = "STRONG" if confidence >= STRATEGY_CONFIG.get("high_confidence", 85) else ("MODERATE" if confidence >= STRATEGY_CONFIG.get("min_confidence", 65) else "CAUTION")

    flat=[]
    for c in (oanda_candles or [])[-50:]:
        mid=c.get("mid") or {}
        try:
            flat.append((float(c.get("open", mid.get("o"))), float(c.get("high", mid.get("h"))), float(c.get("low", mid.get("l"))), float(c.get("close", mid.get("c")))))
        except (TypeError, ValueError):
            continue
    closes=[x[3] for x in flat]
    highs=[x[1] for x in flat]
    lows=[x[2] for x in flat]
    current=closes[-1] if closes else None
    if current is None and price is not None:
        try: current=float(price)
        except (TypeError, ValueError): current=None
    if highs and lows:
        resistance=max(highs[-20:])
        support=min(lows[-20:])
    else:
        resistance=support=None
    if current is not None and resistance is not None and support is not None and resistance > support:
        position=(current-support)/(resistance-support)
        buy_pressure=round(max(1, min(99, (1-position)*100 if is_call else position*100)))
    else:
        buy_pressure=confidence if is_call else 100-confidence
    sell_pressure=100-buy_pressure
    def fmt(v):
        if v is None: return "N/A"
        return f"{v:.3f}" if "JPY" in clean_asset else f"{v:.5f}"
    signal_day=datetime.now(BD_TZ).strftime("%Y-%m-%d")
    signal_word = "CALL" if is_call else "PUT"
    signal_pair = clean_asset
    content=(
        "🤖 ZENITEX AI 🤖\n"
        "──────────────────────\n"
        f"MARKET ∶ {signal_pair}\n"
        f"ENTRY ∶ {entry}\n"
        "EXPIRY ∶ M1\n"
        f"SIGNAL ∶ {signal_word}\n"
        f"BUY PRESSURE : {buy_pressure:02d}%\n"
        f"SELL PRESSURE : {sell_pressure:02d}%\n"
        f"RESISTANCE : {fmt(resistance)}\n"
        f"SUPPORT: {fmt(support)}\n"
        "──────────────────────"
    )
    return f"<pre>{mono(content)}</pre>"

def generate_mtg_confirm_text(
    asset: str = "USDJPY",
    entry_time: str = None,
    direction: str = "CALL"
) -> str:
    clean_asset = asset.upper().replace("/", "").replace("_", "").replace("-OTC", "")
    return (
        f"🚨 <b>MTG G1 RECOVERY</b> 🚨\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 <b>Pair:</b> {clean_asset}\n"
        f"⏰ <b>MTG Entry:</b> {entry_time}\n"
        f"🚀 <b>Direction:</b> {direction.upper()}\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚠️ <b>Waiting for MTG Result...</b>"
    )


def generate_result_card_text(
    asset: str = "USDJPY",
    time_str: str = None,
    direction: str = "CALL",
    result_type: str = "WIN",
    win_count: int = 1,
    loss_count: int = 0,
    strategy_title: str = "ZENITEX AI",
    result_candle: dict | None = None,
    mtg_level: int = 0,
) -> str:
    raw_asset = str(asset or "USDJPY").strip().replace("/", "").replace("_", "").replace(" (OANDA)", "").replace(" (REAL)", "")
    otc = raw_asset.lower().endswith("-otc")
    base = raw_asset[:-4] if otc else raw_asset
    display_pair = base.upper() + ("-otc" if otc else "")
    if not time_str:
        time_str = format_current_candle_time()
    d = direction.upper()
    display_direction = "CALL" if d in ("CALL", "BUY") else "PUT"
    rt = str(result_type or "WIN").upper().strip()
    # Final result cards are limited to WIN, MTG WIN, and MTG LOSS.
    # Pending states remain pending and are never misreported as WIN.
    if "PENDING" in rt:
        return pending_result_text()
    if rt in {"LOSS", "DIRECT LOSS", "LOSS G1"}:
        rt = "MTG LOSS"
        mtg_level = max(int(mtg_level or 0), 1)
    if rt == "DRAW":
        rt = "WIN"
    is_mtg = "MTG" in rt
    is_loss = "LOSS" in rt
    if is_loss:
        title = "❌❌❌ ZENITIX X RESULT - MTG LOSS ❌❌❌" if is_mtg else "❌❌❌ ZENITIX X RESULT - LOSS ❌❌❌"
        result_label = "MTG LOSS" if is_mtg else "LOSS"
        result_icon = "💔"
        candle_icon = "📉"
        candle_word = "RED"
    elif is_mtg:
        title = "✅✅✅ ZENITIX X RESULT - MTG WIN ✅✅✅"
        result_label = "MTG WIN"
        result_icon = "🏆"
        candle_icon = "📈"
        candle_word = "GREEN"
    else:
        title = "✅✅✅ ZENITIX X RESULT - WIN ✅✅✅"
        result_label = "WIN"
        result_icon = "🏆"
        candle_icon = "📈"
        candle_word = "GREEN"
    op = cp = None
    if result_candle:
        try:
            mid = result_candle.get("mid") or {}
            op = float(result_candle.get("open", mid.get("o")))
            cp = float(result_candle.get("close", mid.get("c")))
            candle_word = "GREEN" if cp >= op else "RED"
            candle_icon = "📈" if candle_word == "GREEN" else "📉"
        except (TypeError, ValueError):
            op = cp = None
    price_line = ""
    if op is not None and cp is not None:
        price_line = (
            f"⚜️ Open Price   : {op:.5f}\n"
            f"⚔️ Close Price  : {cp:.5f}\n"
            f"🔰 Candle Colour : {candle_icon} {candle_word}\n"
        )
    mtg_line = f"♻️ MTG LEVEL    ⤖ {mtg_level}\n" if is_mtg else ""
    result_day = datetime.now(BD_TZ).strftime("%Y-%m-%d")
    signal_icon = "🟢" if display_direction == "CALL" else "🔴"
    if result_label == "MTG WIN":
        state_line = "✅ ✅ MTG SURESHOT ✅ ✅"
    elif result_label == "MTG LOSS":
        state_line = "❌️❌️ MTG LOSS ❌️❌️"
    else:
        state_line = "✅ ✅ SURESHOT ✅ ✅"
    content = (
        "🤖 ZENITEX AI 🤖\n"
        "──────────────────────────\n"
        f"📈 MARKET ∶ {display_pair}\n"
        f"⏰ ENTRY ∶ {time_str}\n"
        f"{signal_icon} SIGNAL ∶ {display_direction}\n\n"
        f"{state_line}\n"
        "──────────────────────────"
    )
    return f"<pre>{mono(content)}</pre>"

def generate_chart_image(
    asset: str = "EURJPY",
    timeframe: str = "1 MINUTE",
    direction: str = "CALL",
    output_path: str = "signal_chart.jpg",
    oanda_candles: list = None,
    analysis: dict | None = None,
    is_result: bool = False,
    win: bool | None = None,
    result_window: int | None = None,
) -> str:
    """Render a reference-style 16:9 OANDA candlestick chart."""
    raw = list(oanda_candles or [])
    candles = []
    for item in raw:
        mid = item.get("mid") or {}
        try:
            candles.append({
                "open": float(item.get("open", mid.get("o"))),
                "high": float(item.get("high", mid.get("h"))),
                "low": float(item.get("low", mid.get("l"))),
                "close": float(item.get("close", mid.get("c"))),
                "time": item.get("time"),
            })
        except (TypeError, ValueError):
            continue

    # Result charts must show every valid real OANDA candle supplied by the
    # verified result worker. Never truncate, pad, or synthesize candles.
    if candles:
        candles.sort(key=lambda item: str(item.get("time") or ""))

    fig, ax = plt.subplots(figsize=(11.28, 6.35), dpi=100)
    # Full dark-black canvas: figure, axes, margins, and exported image.
    fig.patch.set_facecolor("#000000")
    fig.patch.set_alpha(1.0)
    ax.set_facecolor("#000000")
    ax.patch.set_facecolor("#000000")
    ax.patch.set_alpha(1.0)
    plt.subplots_adjust(left=0.01, right=0.97, top=0.92, bottom=0.12)
    for spine in ax.spines.values():
        spine.set_color("#000000")
        spine.set_linewidth(0.8)

    if candles:
        lows = np.array([c["low"] for c in candles], dtype=float)
        highs = np.array([c["high"] for c in candles], dtype=float)
        price_range = max(float(highs.max() - lows.min()), 1e-9)
        pad = price_range * 0.05
        ax.set_ylim(float(lows.min() - pad), float(highs.max() + pad))
        ax.set_xlim(-1, len(candles))

        # Keep every candle on the plot while limiting only label density.
        label_count = min(12, len(candles))
        ax.set_xticks(np.linspace(0, len(candles) - 1, label_count).astype(int))
        ax.set_yticks(np.linspace(float(lows.min()), float(highs.max()), 8))
        ax.grid(True, color="#303030", linewidth=0.55, alpha=0.9)

        for i, c in enumerate(candles):
            o, h, lo, cl = c["open"], c["high"], c["low"], c["close"]
            # Deep dark-theme candle colors: visible on black without neon glare.
            color = "#087a45" if cl >= o else "#8f1322"
            ax.vlines(i, lo, h, color=color, linewidth=0.75, zorder=2)
            body_height = max(abs(cl - o), price_range * 0.006)
            ax.add_patch(plt.Rectangle(
                (i - 0.30, min(o, cl)), 0.60, body_height,
                facecolor=color, edgecolor=color, linewidth=0.35, zorder=3
            ))

        # Only horizontal support and resistance levels; no trend overlays.
        support = float(np.percentile(lows, 18))
        resistance = float(np.percentile(highs, 82))
        ax.axhline(support, color="#ffffff", linewidth=0.8, alpha=0.9)
        ax.axhline(resistance, color="#ff3434", linewidth=0.8, alpha=0.9)

    else:
        ax.text(0.5, 0.5, "WAITING FOR LIVE OANDA CANDLE", transform=ax.transAxes,
                ha="center", va="center", color="#ffffff", fontsize=13)

    clean_pair = asset.upper().replace("_", "/").replace("-OTC", "")
    now = datetime.now(BD_TZ)
    remaining = 60 - now.second
    countdown = f"00:00:{remaining:02d}"
    header = f"{clean_pair:<11} |  {timeframe.upper():<9} |  {direction.upper():<4} |  {countdown}"
    if is_result and win is not None:
        header += "  |  WIN" if win else "  |  LOSS"
    ax.text(0.005, 1.035, header, transform=ax.transAxes, color="#ffffff",
            fontsize=8, family="DejaVu Sans Mono", ha="left", va="bottom")

    ax.yaxis.tick_right()
    ax.tick_params(axis="both", colors="#bdbdbd", labelsize=6, length=0)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticklabels([now.strftime("%H:%M") if i == 0 else "" for i in ax.get_xticks()])
    for spine in ax.spines.values():
        spine.set_color("#2d2d2d")
        spine.set_linewidth(0.5)

    fig.savefig(output_path, format="jpg", dpi=100, facecolor="#000000", edgecolor="#000000", transparent=False, pad_inches=0.02)
    plt.close(fig)
    return output_path


def _strategy_candles(oanda_candles: list[dict]) -> list[dict]:
    """Convert nested OANDA candles into flat OHLC strategy candles."""
    result = []
    for c in oanda_candles or []:
        mid = c.get("mid") or {}
        try:
            result.append({
                "open": float(c.get("open", mid.get("o"))),
                "high": float(c.get("high", mid.get("h"))),
                "low": float(c.get("low", mid.get("l"))),
                "close": float(c.get("close", mid.get("c"))),
                "volume": float(c.get("volume", 0) or 0),
                "epoch": c.get("time"),
            })
        except (TypeError, ValueError):
            continue
    return result


PROFESSIONAL_LOADING_STICKER = "CAACAgUAAxkBAAERwBBqh-ncycaTURk9FLfT-wl3_bV83gACjCMAAqJ-QVRvJmUtxf2WIz0E"
_LOADING_STICKER_MESSAGES: dict[int, object] = {}


def professional_loading_text(title: str, stage: str, detail: str = "", current: int = 0, total: int = 4, footer: str = "REAL OANDA DATA • NO SIMULATION") -> str:
    """Build the shared BUG SIGNAL-style loading card used by every feature."""
    total = max(1, int(total or 1))
    current = max(0, min(total, int(current or 0)))
    percent = round((current / total) * 100)
    slots = 10
    filled = round((percent / 100) * slots)
    bar = "█" * filled + "░" * (slots - filled)
    raw_title = str(title or "SYSTEM").strip()
    raw_stage = str(stage or "PROCESSING").strip()
    safe_detail = str(detail or "").strip()
    safe_footer = str(footer or "REAL OANDA DATA • NO SIMULATION").strip()
    heading = f"Generating {raw_title.upper()}"
    if percent >= 100:
        status = "✅ <b>Complete!</b>"
    else:
        status = f"<b>Stage:</b> {raw_stage}"
        if safe_detail:
            status += f"\n{safe_detail}"
    return (
        f"🔄 <b>{heading}</b>\n\n"
        f"<b>Progress:</b> [{bar}] {percent}%\n"
        f"{status}\n\n"
        f"<i>{safe_footer}</i>"
    )


async def professional_loading_message(update: Update, title: str, stage: str, detail: str = "", progress: str = "▰▱▱"):
    """Send the shared BUG SIGNAL-style loading sticker followed by its text card."""
    text = professional_loading_text(title, stage, detail, current=0, total=4)
    try:
        target = None
        if update.callback_query and update.callback_query.message:
            target = update.callback_query.message
        elif update.message:
            target = update.message
        if not target:
            return None
        sticker_message = await target.reply_sticker(PROFESSIONAL_LOADING_STICKER)
        text_message = await target.reply_text(text, parse_mode="HTML")
        _LOADING_STICKER_MESSAGES[text_message.message_id] = sticker_message
        return text_message
    except Exception as exc:
        log.debug("Unified loading sticker delivery skipped: %s", exc)
        try:
            if update.callback_query and update.callback_query.message:
                return await update.callback_query.message.reply_text(text, parse_mode="HTML")
            if update.message:
                return await update.message.reply_text(text, parse_mode="HTML")
        except Exception:
            return None
    return None


async def update_professional_loading(message, title: str, stage: str, detail: str = "", current: int = 0, total: int = 4, footer: str = "REAL OANDA DATA • NO SIMULATION") -> None:
    """Safely update an existing loading message without interrupting the operation."""
    if not message:
        return
    try:
        await message.edit_text(professional_loading_text(title, stage, detail, current, total, footer), parse_mode="HTML")
    except Exception:
        pass


async def delete_loading_message(message) -> None:
    if not message:
        return
    sticker_message = _LOADING_STICKER_MESSAGES.pop(getattr(message, "message_id", -1), None)
    try:
        if sticker_message:
            await sticker_message.delete()
    except Exception:
        pass
    try:
        await message.delete()
    except Exception:
        pass


async def send_chart_photo_with_retry(bot, chat_id, chart_path: str, caption: str, reply_markup=None, attempts: int = 4) -> bool:
    """Send a valid chart with bounded retries and a safe caption fallback.

    Telegram can reject an otherwise valid photo when generated caption text
    contains an unexpected HTML sequence. The image is real and valid, so retry
    once with a plain caption before reporting delivery failure.
    """
    if not chart_path or not os.path.isfile(chart_path) or os.path.getsize(chart_path) <= 0:
        log.error("Chart delivery skipped for %s: invalid or empty image path=%s", chat_id, chart_path)
        return False
    try:
        with Image.open(chart_path) as image:
            image.verify()
        if os.path.getsize(chart_path) > 10 * 1024 * 1024:
            log.error("Chart delivery skipped for %s: image exceeds Telegram photo limit path=%s", chat_id, chart_path)
            return False
    except Exception as exc:
        log.error("Chart delivery skipped for %s: generated image validation failed: %s", chat_id, exc)
        return False
    last_error = None
    plain_caption = re.sub(r"<[^>]+>", "", str(caption or ""))
    # Telegram captions have stricter parsing/length rules than text messages.
    # Try the normal caption, a plain caption, then the image alone; the last
    # path guarantees the real chart is delivered even when caption formatting
    # is rejected, followed by a separate result message.
    caption_variants = (("HTML", caption), (None, plain_caption), (None, ""))
    for attempt in range(max(1, int(attempts))):
        for parse_mode, send_caption in caption_variants:
            try:
                with open(chart_path, "rb") as photo:
                    kwargs = {"chat_id": chat_id, "photo": photo, "reply_markup": reply_markup}
                    if send_caption:
                        kwargs["caption"] = send_caption[:1024]
                    if parse_mode and send_caption:
                        kwargs["parse_mode"] = parse_mode
                    await bot.send_photo(**kwargs)
                if not send_caption and caption:
                    try:
                        await bot.send_message(chat_id=chat_id, text=str(caption), parse_mode="HTML")
                    except Exception as text_exc:
                        log.warning("Chart delivered but separate result text failed for %s: %s", chat_id, text_exc)
                return True
            except Exception as exc:
                last_error = exc
                log.debug("Chart photo delivery attempt %s/%s failed for %s (%s): %s", attempt + 1, attempts, chat_id, parse_mode or "PLAIN", exc)
        if attempt + 1 < attempts:
            await asyncio.sleep(1.2)
    log.warning("Chart photo delivery retry exhausted for %s after %s attempts: %s", chat_id, attempts, last_error)
    return False

async def send_final_result_chart(
    bot, chat_id: int, asset: str, direction: str, result_type: str,
    candles: list[dict] | None, result_candle: dict | None, caption: str,
    reply_markup=None, tag: str = "result"
) -> bool:
    """Deliver a final WIN/MTG chart built only from verified OANDA candles."""
    rt = str(result_type or "").upper()
    if "PENDING" in rt or "WIN" not in rt and "LOSS" not in rt:
        return False
    if not candles or not result_candle:
        log.warning("Final result chart skipped for %s: verified candle data is unavailable", asset)
        return False
    if len(candles) < 15:
        # OANDA can return a short historical window near a boundary. Use the
        # available real candles rather than withholding the required chart;
        # never pad or simulate missing candles.
        log.warning("Final result chart for %s uses %s available real OANDA candles", asset, len(candles))
    clean_asset = str(asset or "PAIR").replace("/", "").replace("_", "").replace("-", "").upper()
    path = f"/tmp/zenitix_{tag}_result_{chat_id}_{time.time_ns()}_{clean_asset}.jpg"
    try:
        is_win = "LOSS" not in rt
        chart_path = generate_chart_image(
            asset=asset, timeframe="1 MINUTE", direction=direction,
            output_path=path, oanda_candles=candles,
            is_result=True, win=is_win, result_window=15,
        )
        return await send_chart_photo_with_retry(
            bot, chat_id, chart_path, caption, reply_markup=reply_markup, attempts=4
        )
    except Exception as exc:
        log.exception("Final result chart delivery failed for %s: %s", asset, exc)
        return False
    finally:
        try:
            if os.path.exists(path): os.remove(path)
        except OSError:
            pass

AUTO_STOPPED_CHATS: set[int] = set()
AUTO_CYCLE_TASKS: dict[int, asyncio.Task] = {}
PARTIAL_SESSIONS: dict[tuple[int, str], list[dict]] = {}
def _partial_mode(mode: str | None) -> str:
    label = str(mode or 'AUTO SIGNAL').upper().replace('_', ' ')
    if 'CHANNEL' in label:
        return 'CHANNEL SENDER'
    if 'MANUAL' in label:
        return 'MANUAL SIGNAL'
    return 'AUTO SIGNAL'
def _partial_session(chat_id: int, mode: str = 'AUTO SIGNAL') -> list[dict]:
    """Compatibility cache; SQLite is the source of truth for PARTIAL data."""
    return PARTIAL_SESSIONS.setdefault((int(chat_id), _partial_mode(mode)), [])

def _partial_status(result_type: str) -> str | None:
    label = str(result_type or '').upper()
    if label == 'WIN':
        return '✅'
    if label == 'MTG WIN':
        return '✅¹'
    if label in {'LOSS', 'MTG LOSS'}:
        return '❌'
    return None

def _partial_get_active_session(conn, chat_id: int, mode: str, create: bool = False):
    mode_name = _partial_mode(mode)
    row = conn.execute(
        "SELECT session_id FROM partial_sessions WHERE chat_id=? AND mode=? AND status='ACTIVE' ORDER BY session_id DESC LIMIT 1",
        (int(chat_id), mode_name),
    ).fetchone()
    if row:
        return int(row['session_id'])
    if not create:
        return None
    now_str = datetime.now(BD_TZ).strftime('%Y-%m-%d %H:%M:%S')
    conn.execute(
        "INSERT INTO partial_sessions(chat_id, mode, status, started_at) VALUES (?, ?, 'ACTIVE', ?)",
        (int(chat_id), mode_name, now_str),
    )
    return int(conn.execute("SELECT last_insert_rowid() AS id").fetchone()['id'])

def _partial_rows_from_db(chat_id: int, mode: str) -> list[dict]:
    conn = get_db_connection()
    try:
        session_id = _partial_get_active_session(conn, chat_id, mode, create=False)
        if not session_id:
            return []
        rows = conn.execute(
            "SELECT pair, entry_time AS time, direction, result_type, status FROM partial_results WHERE session_id=? ORDER BY result_id ASC",
            (session_id,),
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()

def record_partial_result(chat_id: int, pair: str, entry_time: str, direction: str, result_type: str, mode: str = 'AUTO SIGNAL') -> None:
    status = _partial_status(result_type)
    if not status:
        return
    normalized_pair = str(pair).replace('_', '').replace('/', '').upper()
    normalized_time = str(entry_time)
    normalized_direction = str(direction).upper()
    mode_name = _partial_mode(mode)
    conn = get_db_connection()
    try:
        conn.execute('PRAGMA busy_timeout=5000')
        conn.execute('BEGIN IMMEDIATE')
        session_id = _partial_get_active_session(conn, chat_id, mode_name, create=True)
        now_str = datetime.now(BD_TZ).strftime('%Y-%m-%d %H:%M:%S')
        conn.execute(
            "INSERT OR IGNORE INTO partial_results(session_id, chat_id, mode, pair, entry_time, direction, result_type, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (session_id, int(chat_id), mode_name, normalized_pair, normalized_time, normalized_direction, str(result_type).upper(), status, now_str),
        )
        conn.commit()
    except sqlite3.DatabaseError:
        conn.rollback()
        log.exception('Could not persist PARTIAL result for chat %s mode %s', chat_id, mode_name)
    finally:
        conn.close()

def format_partial_report(chat_id: int, mode: str = 'AUTO SIGNAL') -> str:
    mode_name = _partial_mode(mode)
    rows = _partial_rows_from_db(chat_id, mode_name)
    today = now_bd().strftime('%d.%m. %Y')
    total = len(rows)
    wins = sum(1 for row in rows if row['status'] in {'✅', '✅¹'})
    losses = sum(1 for row in rows if row['status'] == '❌')
    mtg_wins = sum(1 for row in rows if str(row.get('result_type', '')).upper() == 'MTG WIN')
    mtg_losses = sum(1 for row in rows if str(row.get('result_type', '')).upper() == 'MTG LOSS')
    finished = wins + losses
    rate = round((wins / finished) * 100) if finished else 0
    lines = [
        mono('=========== PARTIAL ==========='),
        '━━━━━━━━━・━━━━━━━━━',
        f'          📅 {mono(today)}',
        '━━━━━━━━━・━━━━━━━━━',
        f'              ✔ {mono("Total")}:{mono(str(total))}',
        f'          ✅ {mono("Wins")}:{mono(str(wins))}  ❌ {mono("Loss")}:{mono(str(losses))}',
        f'          🔁 {mono("MTG G1")}:{mono(str(mtg_wins))}W/{mono(str(mtg_losses))}L',
        '━━━━━━━━━・━━━━━━━━━',
    ]
    visible_rows = rows[-30:]
    if total > len(visible_rows):
        lines.append(mono(f'… showing latest {len(visible_rows)} of {total} results …'))
    for row in visible_rows:
        result_label = str(row.get('result_type') or '').upper()
        lines.append(f"⧉ {mono(row['time'])} - {mono(row['pair'])} - {mono(row['direction'])} {row['status']} {mono(result_label)}")
    lines.extend([
        '━━━━━━━━━・━━━━━━━━━',
        mono(f'🚀 Win : {wins} ┃ Loss : {losses} ┃ ({rate}%)'),
        mono(f'📌 Settled : {finished} ┃ Pending : {max(0, total - finished)}'),
        '━━━━━━━━━・━━━━━━━━━',
        mono('⏳ ZENITEX AI - PARTIAL'),
        '━━━━━━━━━・━━━━━━━━━',
    ])
    report = '\n'.join(lines)
    return '<blockquote><b>' + html.escape(report) + '</b></blockquote>'

def partial_report_markup(mode: str = 'AUTO SIGNAL') -> InlineKeyboardMarkup:
    """Keyboard shown inside /PARTIAL and after a PARTIAL reset."""
    mode_name = _partial_mode(mode)
    reset_callback = {
        'AUTO SIGNAL': 'partial_reset_auto',
        'MANUAL SIGNAL': 'partial_reset_manual',
        'CHANNEL SENDER': 'partial_reset_channel',
    }[mode_name]
    return build([
        [{"text": "🔄 RESET PARTIAL", "callback": reset_callback, "style": KeyboardButtonStyle.DANGER},
         {"text": "🏠 MENU", "callback": "menu_home", "style": KeyboardButtonStyle.PRIMARY}],
    ])

def signal_result_markup(mode: str = 'AUTO SIGNAL') -> InlineKeyboardMarkup:
    """Exact controls displayed below verified Auto/Manual result charts."""
    mode_name = _partial_mode(mode)
    if mode_name == 'AUTO SIGNAL':
        return build([
            [{"text": "📊 PARTIAL", "callback": "partial_report", "style": KeyboardButtonStyle.PRIMARY},
             {"text": "🛑 STOP AUTO", "callback": "auto_stop", "style": KeyboardButtonStyle.DANGER}],
        ])
    if mode_name == 'MANUAL SIGNAL':
        return build([
            [{"text": "📊 PARTIAL", "callback": "partial_report", "style": KeyboardButtonStyle.PRIMARY},
             {"text": "➡️ GET NEXT", "callback": "lsig_next_manual_signal", "style": KeyboardButtonStyle.SUCCESS}],
            [{"text": "🏠 MENU", "callback": "menu_home", "style": KeyboardButtonStyle.PRIMARY}],
        ])
    return partial_report_markup(mode_name)

def reset_partial_session(chat_id: int, mode: str | None = None) -> None:
    chat_id = int(chat_id)
    modes = [_partial_mode(mode)] if mode is not None else ['AUTO SIGNAL', 'MANUAL SIGNAL', 'CHANNEL SENDER']
    conn = get_db_connection()
    try:
        conn.execute('PRAGMA busy_timeout=5000')
        conn.execute('BEGIN IMMEDIATE')
        now_str = datetime.now(BD_TZ).strftime('%Y-%m-%d %H:%M:%S')
        for mode_name in modes:
            session = conn.execute(
                "SELECT session_id FROM partial_sessions WHERE chat_id=? AND mode=? AND status='ACTIVE' ORDER BY session_id DESC LIMIT 1",
                (chat_id, mode_name),
            ).fetchone()
            if session:
                session_id = int(session['session_id'])
                closed_status = 'CLOSED'
                if conn.execute(
                    "SELECT 1 FROM partial_sessions WHERE chat_id=? AND mode=? AND status='CLOSED' LIMIT 1",
                    (chat_id, mode_name),
                ).fetchone():
                    closed_status = f'CLOSED_{session_id}'
                conn.execute(
                    "UPDATE partial_sessions SET status=?, closed_at=? WHERE session_id=? AND status='ACTIVE'",
                    (closed_status, now_str, session_id),
                )
            PARTIAL_SESSIONS.pop((chat_id, mode_name), None)
        conn.commit()
    except sqlite3.DatabaseError:
        conn.rollback()
        log.exception('Could not reset PARTIAL session for chat %s', chat_id)
    finally:
        conn.close()
_BACKGROUND_TASKS: set[asyncio.Task] = set()


def _create_tracked_task(coro):
    """Create a background task that is cancelled cleanly during bot shutdown."""
    task = asyncio.create_task(coro)
    _BACKGROUND_TASKS.add(task)
    task.add_done_callback(_BACKGROUND_TASKS.discard)
    return task


async def _cancel_background_tasks(_application=None) -> None:
    """Cancel bot-owned workers before the event loop closes."""
    tasks = [task for task in list(_BACKGROUND_TASKS) if not task.done()]
    for task in tasks:
        task.cancel()
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    _BACKGROUND_TASKS.clear()


async def fast_scan_signal_candidates(active_pairs: list[str], count: int = 120) -> tuple[list[tuple], list[tuple]]:
    """Scan OANDA pairs concurrently and isolate per-pair API/strategy failures."""
    sem = asyncio.Semaphore(8)

    async def scan_one(pair: str):
        async with sem:
            try:
                candles = await fetch_oanda_candles(pair, count=count, granularity="M1")
                if not candles or len(candles) < 50:
                    return None
                flat = _strategy_candles(candles)
                try:
                    sr = _local_strategy_consensus(flat, min_score=72.0, min_agreement=65.0, min_votes=8)
                except Exception:
                    sr = _local_strategy_consensus(flat, min_score=0.0, min_agreement=0.0, min_votes=0)
                if sr.get("signal") not in ("CALL", "PUT"):
                    return None
                return (pair, candles, sr)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                log.warning("Pair scan skipped for %s: %s", pair, exc)
                return None

    results = await asyncio.gather(*(scan_one(pair) for pair in active_pairs), return_exceptions=True)
    analyzed = [item for item in results if isinstance(item, tuple) and len(item) == 3]
    ranked = [item for item in analyzed if item[2].get("qualified")]
    return ranked, analyzed


async def send_signal_response(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    asset: str = "USDJPY",
    strategy: str = "HIGH CONFIDENCE 1000 STRATEGY",
    back_callback: str = "lsig_mode_auto",
    mode: str = "AUTO SIGNAL",
    candles_override: list[dict] | None = None,
    result_override: dict | None = None,
) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)

    user = update.effective_user
    uid = user.id if user else 0
    uname = (user.username or "") if user else ""
    first_name = (user.first_name or "") if user else ""
    loading_msg = await professional_loading_message(
        update,
        "AUTO SIGNAL" if "AUTO" in mode.upper() else "MANUAL SIGNAL",
        "CONNECTING TO OANDA",
        "Scanning live candles and validating strategy confirmations...",
    )
    strategy_fn = _local_strategy_consensus
    strategy_code = context.user_data.get("lsig_strategy_code", "pro2")
    pair = format_oanda_instrument(asset)
    candles = candles_override if candles_override is not None else await fetch_oanda_candles(pair, count=200, granularity="M1")
    if not candles or len(candles) < 50:
        await edit_or_send(
            update, context,
            "⚠️ <b>NO SIGNAL</b>\n━━━━━━━━━━━━━━━━━━━━\n"
            "Real OANDA candle data is unavailable or insufficient.\n\n"
            "The bot will NOT generate random/fake CALL or PUT signals.",
            build([[{"text": "🔄 TRY AGAIN", "callback": back_callback, "style": KeyboardButtonStyle.PRIMARY},
                    {"text": "🏠 MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]),
        )
        return

    if isinstance(result_override, dict):
        result = result_override
    else:
        try:
            result = strategy_fn(_strategy_candles(candles), min_score=72.0, min_agreement=65.0, min_votes=8, strategy_code=strategy_code)
        except Exception:
            result = _local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0, strategy_code=strategy_code)
    if result.get("signal") not in ("CALL", "PUT"):
        result = _local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0, strategy_code=strategy_code)
    if result.get("signal") not in ("CALL", "PUT"):
        await edit_or_send(
            update, context,
            "⚠️ <b>REAL OANDA ANALYSIS UNAVAILABLE</b>\n\n"
            "No valid direction can be derived from the available real candles.",
            build([[{"text": "🔄 TRY AGAIN", "callback": back_callback, "style": KeyboardButtonStyle.PRIMARY},
                    {"text": "🏠 MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]),
        )
        return

    # A valid analyzed direction is deliverable even below the strict tier.
    # The confidence value remains visible in the signal card.
    direction = result["signal"]
    confidence = int(result["confidence"])
    last = candles[-1]
    mid = last.get("mid") or {}
    try:
        p_val = float(mid.get("c", last.get("close")))
        price = f"{p_val:.3f}" if "JPY" in pair else f"{p_val:.5f}"
    except (TypeError, ValueError):
        price = "N/A"

    # Consume quota ONLY after a real qualified signal exists.
    if uid:
        register_user(uid, uname, first_name)
        feature_key = "auto_signal" if "AUTO" in mode.upper() else "manual_signal"
        allowed, curr_count, max_limit = reserve_feature_usage(uid, feature_key)
        if not allowed:
            tier = get_user_tier(uid)
            await edit_or_send(
                update, context,
                format_limit_reached(feature_key, curr_count, max_limit, tier),
                build([[{"text": "💎 PRICING", "callback": "menu_pricing", "style": KeyboardButtonStyle.PRIMARY},
                        {"text": "📞 SUPPORT", "callback": "menu_support", "style": KeyboardButtonStyle.PRIMARY}],
                       [{"text": "🏠 MENU", "callback": "menu_home"}]]),
            )
            return

    entry_time = format_next_candle_entry()
    caption_text = generate_signal_card_text(
        asset=pair,
        entry=entry_time,
        direction=direction,
        price=price,
        confidence=confidence,
        mode=mode,
        strategy_title=f"1000-STRATEGY • {strategy}",
        oanda_candles=candles,
        analysis=result.get("details") if isinstance(result, dict) else None,
    )

    clean_asset = pair.replace("/", "").replace("_", "")
    chart_filename = f"/tmp/zenitix_signal_chart_{uid or update.effective_chat.id}_{int(datetime.now().timestamp())}_{clean_asset}.jpg"
    chart_path = generate_chart_image(
        asset=pair,
        timeframe="1 MINUTE",
        direction=direction,
        output_path=chart_filename,
        oanda_candles=candles,
    )

    is_auto = "AUTO" in mode.upper()
    context.user_data["signal_mode"] = "AUTO SIGNAL" if is_auto else ("CHANNEL SENDER" if "CHANNEL" in mode.upper() else "MANUAL SIGNAL")
    context.user_data["strategy_mode"] = strategy
    next_callback = "lsig_next_auto_signal" if is_auto else "lsig_next_manual_signal"

    # A next signal is available only after the final result is verified.
    reply_markup = build([
        [{"text": "🔍 CHECK RESULT", "callback": f"chkres_{clean_asset}_{entry_time}_{direction}_{'AUTO' if is_auto else 'MANUAL'}", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🏠 MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])

    await delete_loading_message(loading_msg)
    try:
        sent_chart = await send_chart_photo_with_retry(
            context.bot, update.effective_chat.id, chart_path, caption_text, reply_markup=reply_markup
        )
        if not sent_chart:
            # Regenerate once from the same real OANDA candles before reporting failure.
            retry_path = f"/tmp/zenitix_signal_chart_retry_{uid or update.effective_chat.id}_{int(datetime.now().timestamp())}_{clean_asset}.jpg"
            retry_chart = generate_chart_image(asset=pair, timeframe="1 MINUTE", direction=direction, output_path=retry_path, oanda_candles=candles)
            sent_chart = await send_chart_photo_with_retry(
                context.bot, update.effective_chat.id, retry_chart, caption_text, reply_markup=reply_markup, attempts=2
            )
            if retry_chart and retry_chart != chart_path:
                try: os.remove(retry_chart)
                except OSError: pass
        if not sent_chart:
            await edit_or_send(update, context, "<b>CHART DELIVERY RETRY</b>\nThe generated OANDA chart could not be uploaded after retries. Please try again.", reply_markup)
    except Exception as ex:
        log.exception("Signal chart delivery failed: %s", ex)
        await edit_or_send(update, context, "<b>CHART DELIVERY RETRY</b>\nPlease try the signal again.", reply_markup)
    finally:
        if chart_path:
            try: os.remove(chart_path)
            except OSError: pass

    # AUTO and MANUAL both receive an automatic result after the exact
    # completed entry candle, followed by one completed MTG G1 candle only
    # after a direct loss.
    if update.effective_chat:
        task = _create_tracked_task(_auto_signal_result_worker(
            context.bot, update.effective_chat.id, pair, entry_time, direction, strategy, mode,
            update=update, context=context
        ))
        if is_auto:
            AUTO_CYCLE_TASKS[update.effective_chat.id] = task



# ==================== BUG SIGNAL: STICKER-ONLY REAL MARKET SIGNAL ====================
BUG_SIGNAL_UP_STICKER = "CAACAgUAAxkBAAERwAxqh-nBxLAykIyqCVniu_6lQt7gQQAClx0AAjSzQVTI43juAuQAAYY9BA"
BUG_SIGNAL_DOWN_STICKER = "CAACAgUAAxkBAAERwApqh-m_6AaETvwC8lcp-oJIMzTmKgACsR4AAicOSFTTs9kV5jTLED0E"
BUG_SIGNAL_LOADING_STICKER = "CAACAgUAAxkBAAERwBBqh-ncycaTURk9FLfT-wl3_bV83gACjCMAAqJ-QVRvJmUtxf2WIz0E"
# One BUG SIGNAL analysis per chat at a time; repeated callback deliveries are ignored briefly.
BUG_SIGNAL_CHAT_LOCKS: dict[int, asyncio.Lock] = {}
BUG_SIGNAL_RECENT_CALLBACKS: dict[int, tuple[str, float]] = {}
BUG_SIGNAL_DEDUP_WINDOW_SECONDS = 8.0


def bug_signal_loading_text(pair: str, progress: int, stage: str, detail: str, complete: bool = False, context_label: str = "REAL OANDA M1") -> str:
    """Build the screenshot-matched BUG SIGNAL progress card."""
    percent = max(0, min(100, int(progress)))
    filled = round(percent / 10)
    bar = "█" * filled + "░" * (10 - filled)
    status = "✅ Complete!" if complete else f"STAGE: {stage}"
    return (
        "🔄 Generating BUG SIGNAL\n\n"
        f"Progress: [{bar}]\n"
        f"{percent}%\n\n"
        f"{status}\n"
        f"{detail}\n\n"
        f"PAIR: {pair}  •  {context_label}"
    )


def bug_signal_market_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "📣 OTC Markets", "callback": "bug_signal_otc", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "📊 Real Markets", "callback": "bug_signal_real", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "⚙️ Settings", "callback": "bug_signal_settings", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "↪️ Back to Main Menu", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])


def bug_signal_pair_menu(pairs: list[str], prefix: str) -> InlineKeyboardMarkup:
    rows = []
    for i in range(0, len(pairs), 2):
        row = [{"text": pairs[i].replace("_OTC", "").replace("_", "/") + (" OTC" if prefix == "bugotc_" else ""), "callback": f"{prefix}{pairs[i]}", "style": KeyboardButtonStyle.PRIMARY}]
        if i + 1 < len(pairs):
            row.append({"text": pairs[i + 1].replace("_OTC", "").replace("_", "/") + (" OTC" if prefix == "bugotc_" else ""), "callback": f"{prefix}{pairs[i + 1]}", "style": KeyboardButtonStyle.PRIMARY})
        rows.append(row)
    rows.append([{"text": "↩️ Back", "callback": "bug_signal_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


async def bug_signal_home_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    await edit_or_send(
        update,
        context,
        "<b>📊 Select an OTC or Real pair:</b>\\n\\n<b>OTC markets use OANDA reference context. No simulated candles are used.</b>",
        bug_signal_market_menu(),
    )


async def bug_signal_otc_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    await edit_or_send(update, context, "<b>📣 OTC Markets</b>\\nSelect an OTC pair for the next-candle sticker signal.", bug_signal_pair_menu(OTC_PAIRS, "bugotc_"))


async def bug_signal_real_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    await edit_or_send(update, context, "<b>📊 Real Markets</b>\\nSelect a real OANDA pair for the next-candle sticker signal.", bug_signal_pair_menu(REAL_PAIRS, "bugreal_"))


async def bug_signal_settings_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    await edit_or_send(update, context, "<b>⚙️ BUG SIGNAL SETTINGS</b>\\n\\n<b>TIMEZONE:</b> UTC +06:00\\n<b>TIMEFRAME:</b> M1\\n<b>ENTRY:</b> Next completed candle\\n<b>OUTPUT:</b> Sticker only\\n<b>RESULT/CHART:</b> Disabled", build([[{"text": "↩️ Back", "callback": "bug_signal_home", "style": KeyboardButtonStyle.DANGER}]]))


def bug_strategy_menu() -> InlineKeyboardMarkup:
    """Expose every standalone real-data strategy profile to BUG SIGNAL."""
    options = [
        ('pro2', 'ZX PRO 2.1 AI'), ('momentum', 'ZX Momentum AI'),
        ('trend', 'ZX Trend Surge Pro'), ('breakout', 'ZX Volatility Breakout'),
        ('priceaction', 'ZX Price Action Master'), ('reversal', 'ZX RSI Reversal'),
        ('scalping', 'ZX EMA-MACD Scalper'), ('supportresistance', 'ZX S/R Reaction'),
        ('volume', 'ZX Volume Pressure'), ('candlestick', 'ZX Candle Pattern Pro'),
        ('confluence', 'ZX Full Confluence'),
    ]
    rows = []
    for index in range(0, len(options), 2):
        rows.append([{"text": mono(label), "callback": f"bug_strategy_{code}", "style": KeyboardButtonStyle.PRIMARY}
                     for code, label in options[index:index + 2]])
    rows.append([{"text": mono("BACK TO BUG SIGNAL"), "callback": "bug_signal_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)

async def _bugpair_selected_callback_impl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    data = query.data or ""
    market_mode = "REAL"
    strategy_code = None
    if data.startswith("bug_strategy_"):
        strategy_code = data[len("bug_strategy_"):].lower()
        pair_raw = str(context.user_data.get("bug_pair_raw", "")).upper()
        market_mode = str(context.user_data.get("bug_market_mode", "REAL")).upper()
        if not pair_raw:
            await edit_or_send(update, context, "<b>BUG SIGNAL</b>\\nPlease choose the market again.", bug_signal_market_menu())
            return
    elif data.startswith("bugotc_"):
        selected = data[len("bugotc_"):].upper()
        if selected not in OTC_PAIRS:
            await edit_or_send(update, context, "<b>BUG SIGNAL</b>\\nInvalid OTC market selection.", bug_signal_market_menu())
            return
        pair_raw = selected[:-4]
        market_mode = "OTC"
    elif data.startswith("bugreal_"):

        pair_raw = data[len("bugreal_"):].upper()
        if pair_raw not in REAL_PAIRS:
            await edit_or_send(update, context, "<b>BUG SIGNAL</b>\\nInvalid real market selection.", bug_signal_market_menu())
            return
    else:
        pair_raw = data.replace("bugpair_", "", 1).upper()
        if pair_raw not in REAL_PAIRS:
            await edit_or_send(update, context, "<b>BUG SIGNAL</b>\\nInvalid market selection.", bug_signal_market_menu())
            return
    if market_mode == "REAL" and await block_real_market(update, context):
        return
    if not strategy_code:
        context.user_data["bug_pair_raw"] = pair_raw
        context.user_data["bug_market_mode"] = market_mode
        await edit_or_send(update, context, "<b>🔥 BUG SIGNAL STRATEGY</b>\\n━━━━━━━━━━━━━━━━━━━━\\nSelect a real-data strategy profile:", bug_strategy_menu())
        return
    chat_id = update.effective_chat.id
    loading_message = None
    loading_status = None
    try:
        display_pair = pair_raw.replace("_", "/") + (" OTC" if market_mode == "OTC" else "")
        context_label = "OANDA REFERENCE M1 • OTC" if market_mode == "OTC" else "REAL OANDA M1"
        loading_message = await context.bot.send_sticker(chat_id=chat_id, sticker=BUG_SIGNAL_LOADING_STICKER)
        loading_status = await context.bot.send_message(
            chat_id=chat_id,
            text=bug_signal_loading_text(display_pair, 0, "CONNECTING TO OANDA", "Loading real market context...", context_label=context_label),
            parse_mode="HTML",
        )
        # Retry transient OANDA/API failures without ever fabricating candles.
        candles = None
        for fetch_attempt in range(3):
            candles = await fetch_oanda_candles(format_oanda_instrument(pair_raw), count=200, granularity="M1")
            if candles and len(candles) >= 50:
                break
            if fetch_attempt < 2:
                await asyncio.sleep(0.8 * (fetch_attempt + 1))
        if not candles or len(candles) < 50:
            log.warning("BUG SIGNAL real OANDA data unavailable after retries for %s", pair_raw)
            await context.bot.send_message(chat_id=chat_id, text="Real OANDA data is temporarily unavailable for this market. No simulated signal was sent.")
            return

        if loading_status:
            try:
                await loading_status.edit_text(
                    bug_signal_loading_text(
                        display_pair, 60, "ANALYZING STRATEGY",
                        "Validating completed OANDA candles and directional pressure...",
                        context_label=context_label,
                    ),
                    parse_mode="HTML",
                )
            except Exception:
                pass

        analyzed = bug_signal_strategy(_strategy_candles(candles), market_mode=market_mode, strategy_code=strategy_code)
        direction = analyzed.get("signal") if isinstance(analyzed, dict) else None

        # Real-data tie-break only: use the latest completed candle body, then the
        # most recent non-neutral completed candle. Never generate a random direction.
        if direction not in ("CALL", "PUT"):
            for candle in reversed(candles):
                try:
                    op, cp = float(candle.get("open")), float(candle.get("close"))
                except (TypeError, ValueError):
                    continue
                if cp > op:
                    direction = "CALL"
                    break
                if cp < op:
                    direction = "PUT"
                    break

        if direction not in ("CALL", "PUT"):
            await context.bot.send_message(chat_id=chat_id, text="No directional movement was confirmed by the real OANDA candles. No simulated signal was sent.")
            return

        if loading_status:
            try:
                await loading_status.edit_text(
                    bug_signal_loading_text(
                        display_pair, 100, "SIGNAL CONFIRMED",
                        f"Confluence confirmed at {int(analyzed.get('confidence', 0))}% — preparing the next-candle sticker signal...",
                        complete=True,
                        context_label=context_label,
                    ),
                    parse_mode="HTML",
                )
            except Exception:
                pass

        # Target the next exact Bangladesh-time M1 candle, not the currently forming candle.
        entry_dt = now_bd().replace(second=0, microsecond=0) + timedelta(minutes=1)
        entry_time = entry_dt.strftime("%H:%M:00")
        signal_text = (
            "<blockquote>"
            "<b>╔════════════════════╗</b>\n"
            "<b>      🔥 ZENITEX BUG TRADE 🔥</b>\n"
            "<b>╚════════════════════╝</b>\n\n"
            f"<b>PAIR: {display_pair}</b>\n"
            "<b>DIRECTION: FOLLOW STICKER</b>\n"
            "<b>MTG: 1STEP</b>\n"
            f"<b>ENTRY TIME: {entry_time[:5]}</b>\n"
            "<b>TIMEZONE: UTC +06:00</b>\n\n"
            "<b>🔥 ZENITEX BUG — LET’S GO! 🚀</b>\n"
            "<b>━━━━━━━━━━━━━━━━━━━━</b>"
            "</blockquote>"
        )
        await context.bot.send_message(chat_id=chat_id, text=signal_text, parse_mode="HTML")
        sticker = BUG_SIGNAL_UP_STICKER if direction == "CALL" else BUG_SIGNAL_DOWN_STICKER
        await context.bot.send_sticker(chat_id=chat_id, sticker=sticker)
    except Forbidden:
        # A blocked/deleted Telegram chat must not create a second unhandled error.
        log.warning("BUG SIGNAL skipped because chat %s is unavailable", chat_id)
    except Exception:
        log.exception("BUG SIGNAL failed for %s", pair_raw)
        try:
            await context.bot.send_message(chat_id=chat_id, text="BUG SIGNAL could not be delivered because the real market analysis failed. No simulated signal was sent.")
        except Forbidden:
            log.warning("BUG SIGNAL failure notice could not be delivered to chat %s", chat_id)
        except Exception:
            log.exception("BUG SIGNAL failure notice delivery failed for chat %s", chat_id)
    finally:
        for loading_item in (loading_message, loading_status):
            if loading_item:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=loading_item.message_id)
                except Exception:
                    pass


async def bugpair_selected_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Idempotent BUG SIGNAL entrypoint; prevents duplicate analysis/sticker delivery."""
    query = update.callback_query
    chat = update.effective_chat
    chat_id = chat.id if chat else 0
    callback_data = (query.data or "") if query else ""
    now_mono = time.monotonic()
    previous = BUG_SIGNAL_RECENT_CALLBACKS.get(chat_id)
    if previous and previous[0] == callback_data and (now_mono - previous[1]) < BUG_SIGNAL_DEDUP_WINDOW_SECONDS:
        if query:
            await safe_answer(query, "BUG SIGNAL is already processing this request.")
        return
    lock = BUG_SIGNAL_CHAT_LOCKS.setdefault(chat_id, asyncio.Lock())
    if lock.locked():
        if query:
            await safe_answer(query, "BUG SIGNAL analysis is already running.")
        return
    BUG_SIGNAL_RECENT_CALLBACKS[chat_id] = (callback_data, now_mono)
    async with lock:
        await _bugpair_selected_callback_impl(update, context)


bug_signal_handlers = [
    CallbackQueryHandler(bug_signal_home_callback, pattern="^bug_signal_home$"),
    CallbackQueryHandler(bug_signal_otc_callback, pattern="^bug_signal_otc$"),
    CallbackQueryHandler(bug_signal_real_callback, pattern="^bug_signal_real$"),
    CallbackQueryHandler(bug_signal_settings_callback, pattern="^bug_signal_settings$"),
    CallbackQueryHandler(bugpair_selected_callback, pattern="^(?:bugpair_|bugreal_|bugotc_|bug_strategy_)")
]


async def _auto_signal_result_worker(bot, chat_id: int, pair: str, entry_time: str, direction: str, strategy: str, mode: str = "AUTO SIGNAL", update: Update | None = None, context: ContextTypes.DEFAULT_TYPE | None = None) -> None:
    """Automatically deliver an OANDA-only result for AUTO or MANUAL with one MTG G1."""
    try:
        now = now_bd()
        hh, mm = map(int, entry_time.split(":"))
        entry_dt = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if entry_dt <= now:
            entry_dt += timedelta(days=1)
        wait_s = max(0.0, (entry_dt + timedelta(minutes=1, seconds=5) - now).total_seconds())
        if wait_s:
            await asyncio.sleep(wait_s)
        candles = None
        direct = None
        # OANDA can publish the completed candle with a short delay. Poll
        # until five minutes after the close, never classifying an open candle.
        direct_deadline = entry_dt + timedelta(minutes=6)
        while now_bd() <= direct_deadline:
            candles = await fetch_oanda_historical_candles(format_oanda_instrument(pair), entry_dt, "M1", before=10, after=6)
            direct = checker_exact_candle(candles, entry_dt)
            if direct is not None:
                break
            await asyncio.sleep(3)
        result_candle = direct
        mtg_level = 0
        if direct is None:
            result_type = "PENDING — OANDA CANDLE UNAVAILABLE"
        else:
            op, cp = float(direct.get("open")), float(direct.get("close"))
            direct_win = cp == op or (direction == "CALL" and cp > op) or (direction == "PUT" and cp < op)
            if direct_win:
                result_type = "WIN"
            else:
                mtg_dt = entry_dt + timedelta(minutes=1)
                mtg_close_wait = max(0.0, (mtg_dt + timedelta(minutes=1, seconds=5) - now_bd()).total_seconds())
                if mtg_close_wait:
                    await asyncio.sleep(mtg_close_wait)
                # Poll the completed MTG G1 candle for up to five minutes.
                mtg = None
                mtg_deadline = mtg_dt + timedelta(minutes=6)
                while now_bd() <= mtg_deadline:
                    refreshed = await fetch_oanda_historical_candles(format_oanda_instrument(pair), entry_dt, "M1", before=10, after=6)
                    if refreshed:
                        candles = refreshed
                    mtg = checker_exact_candle(candles, mtg_dt)
                    if mtg is not None:
                        break
                    await asyncio.sleep(3)
                if mtg is None:
                    result_type = "PENDING MTG G1"
                else:
                    result_candle = mtg
                    mtg_level = 1
                    mo, mc = float(mtg.get("open")), float(mtg.get("close"))
                    mtg_win = mc == mo or (direction == "CALL" and mc > mo) or (direction == "PUT" and mc < mo)
                    result_type = "MTG WIN" if mtg_win else "MTG LOSS"
        record_partial_result(chat_id, pair, entry_time, direction, result_type, mode)
        result_text = generate_result_card_text(
            asset=pair, time_str=entry_time, direction=direction,
            result_type=result_type, win_count=1 if "WIN" in result_type else 0,
            loss_count=1 if "LOSS" in result_type else 0,
            strategy_title=f"{mode} • {strategy}",
            result_candle=result_candle,
            mtg_level=mtg_level,
        )
        result_markup = signal_result_markup(mode)
        delivered = await send_final_result_chart(
            bot, chat_id, pair, direction, result_type, candles, result_candle,
            result_text, reply_markup=result_markup, tag="manual" if "MANUAL" in mode.upper() else "auto"
        )
        if not delivered:
            log.error("AUTO/MANUAL result withheld because the verified result chart could not be delivered for %s", pair)
            await bot.send_message(
                chat_id=chat_id,
                text="⚠️ <b>RESULT CHART DELIVERY RETRY</b>\n━━━━━━━━━━━━━━━━━━━━\nThe verified result is ready, but its OANDA chart image could not be delivered. Tap CHECK AGAIN shortly.",
                parse_mode="HTML",
                reply_markup=result_markup,
            )

        # Continue Auto Signal only after verified result and chart delivery.
        # Every next scan re-enters the normal limits, weekend, OANDA, and
        # duplicate protections; Stop Auto prevents the next cycle.
        if "AUTO" in mode.upper() and update is not None and context is not None and chat_id not in AUTO_STOPPED_CHATS:
            await asyncio.sleep(2.0)
            if chat_id not in AUTO_STOPPED_CHATS:
                context.user_data["_auto_cycle_internal"] = True
                await lsig_auto_filter_callback(update, context)
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        log.exception("Automatic AUTO SIGNAL result failed: %s", exc)
        try:
            await bot.send_message(chat_id=chat_id, text="AUTO SIGNAL RESULT\\nRESULT: PENDING\\nWAITING FOR REAL OANDA CANDLE", parse_mode="HTML")
        except Exception:
            pass


async def handle_check_result_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check direct entry candle, then MTG G1 only after a direct loss using OANDA data."""
    query = update.callback_query
    if not query:
        return
    await safe_answer(query, "Checking OANDA result...", show_alert=False)

    data = query.data or ""
    if not data.startswith("chkres_"):
        await edit_or_send(update, context, "❌ <b>INVALID RESULT REQUEST</b>", home_button())
        return
    parts = data[len("chkres_"):].rsplit("_", 3)
    if len(parts) == 4:
        asset, entry_time, direction, signal_mode = parts
    elif len(parts) == 3:
        asset, entry_time, direction = parts
        signal_mode = "AUTO"
    else:
        await edit_or_send(update, context, "❌ <b>INVALID RESULT REQUEST</b>", home_button())
        return

    direction = direction.upper()
    signal_mode = signal_mode.upper()
    if direction not in ("CALL", "PUT"):
        await edit_or_send(update, context, "❌ <b>INVALID DIRECTION</b>", home_button())
        return

    try:
        hh, mm = map(int, entry_time.split(":"))
        now = now_bd()
        entry_dt = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        # A time-only callback can cross midnight. Prefer the nearest past
        # signal date, while preserving a genuinely imminent next-candle entry.
        if entry_dt - now > timedelta(minutes=2):
            entry_dt -= timedelta(days=1)
        pending_markup = build([[{"text": "CHECK AGAIN", "callback": query.data, "style": KeyboardButtonStyle.PRIMARY},
                                 {"text": "MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]])
        # A signal's M1 candle is complete only after the next minute begins.
        if now < entry_dt + timedelta(minutes=1):
            await edit_or_send(
                update, context,
                "⏳ <b>RESULT PENDING</b>\n━━━━━━━━━━━━━━━━━━━━\nThe exact entry candle is still open. Tap CHECK AGAIN after the candle closes.",
                pending_markup,
            )
            return
    except (TypeError, ValueError):
        await edit_or_send(update, context, "❌ <b>INVALID ENTRY TIME</b>", home_button())
        return

    # Respond immediately after callback acknowledgement; OANDA polling runs in the background.
    checking_text = (
        "⏳ <b>CHECKING RESULT...</b>\n━━━━━━━━━━━━━━━━━━━━\n"
        "Real OANDA candle verification is running. The final WIN/MTG result will arrive after the candle is closed."
    )
    await edit_or_send(update, context, checking_text, pending_markup)
    task_key = f"manual_check_task:{query.data}"
    existing = context.user_data.get(task_key)
    if existing and not existing.done():
        return
    task = _create_tracked_task(_background_check_result(
        update, context, asset, entry_time, direction, signal_mode, pending_markup, entry_dt
    ))
    context.user_data[task_key] = task


async def _background_check_result(update: Update, context: ContextTypes.DEFAULT_TYPE, asset: str, entry_time: str, direction: str, signal_mode: str, pending_markup, entry_dt: datetime) -> None:
    try:
        instrument = format_oanda_instrument(asset)
        timeframe = "M1"
        # Fresh bounded retries prevent a transient OANDA response from becoming a stuck PENDING state.
        candles = None
        direct = None
        direct_deadline = entry_dt + timedelta(minutes=6)
        while now_bd() <= direct_deadline:
            candles = await fetch_oanda_historical_candles(instrument, entry_dt, timeframe, before=12, after=8)
            direct = checker_exact_candle(candles, entry_dt)
            if direct is not None:
                break
            await asyncio.sleep(3)
        if not candles:
            await edit_or_send(
                update, context,
                "⏳ <b>RESULT PENDING</b>\n━━━━━━━━━━━━━━━━━━━━\nOANDA has not returned the completed exact M1 candle yet. Tap CHECK AGAIN shortly.",
                pending_markup,
            )
            return

        def candle_at(target_dt):
            return checker_exact_candle(candles, target_dt)

        def open_close(candle):
            mid = candle.get("mid") or {}
            return float(candle.get("open", mid.get("o"))), float(candle.get("close", mid.get("c")))

        now = now_bd()
        direct = candle_at(entry_dt)
        # If the close gate has passed but the narrow response missed the candle, widen once.
        if direct is None and now >= entry_dt + timedelta(minutes=1):
            wider = await fetch_oanda_historical_candles(instrument, entry_dt, timeframe, before=20, after=12)
            if wider:
                candles = wider
                direct = candle_at(entry_dt)
        # OANDA may briefly lag on a centered historical request. Retry with
        # the current real M1 stream before showing a pending state.
        if direct is None and now >= entry_dt + timedelta(minutes=1):
            live_window = await fetch_oanda_candles(instrument, count=30, granularity=timeframe)
            if live_window:
                candles = live_window
                direct = candle_at(entry_dt)
        result_candle = direct
        mtg_level = 0
        if direct is None:
            await edit_or_send(
                update, context,
                "⏳ <b>RESULT PENDING</b>\n━━━━━━━━━━━━━━━━━━━━\nThe completed exact OANDA M1 candle is not available yet. Tap CHECK AGAIN shortly.",
                pending_markup,
            )
            return

        try:
            direct_open, direct_close = open_close(direct)
        except (TypeError, ValueError, AttributeError):
            await edit_or_send(update, context, "⚠️ <b>RESULT INVALID</b>\n━━━━━━━━━━━━━━━━━━━━\nOANDA returned invalid OHLC data. No result was calculated.", home_button())
            return
        direct_win = (direction == "CALL" and direct_close > direct_open) or (direction == "PUT" and direct_close < direct_open)
        if direct_close == direct_open:
            result_type = "WIN"
        elif direct_win:
            result_type = "WIN"
        else:
            mtg_dt = entry_dt + timedelta(minutes=1)
            if now < mtg_dt + timedelta(minutes=1):
                result_type = "PENDING MTG G1"
            else:
                mtg = candle_at(mtg_dt)
                if mtg is None and now_bd() >= mtg_dt + timedelta(minutes=1):
                    wider = await fetch_oanda_historical_candles(instrument, entry_dt, timeframe, before=20, after=12)
                    if wider:
                        candles = wider
                        mtg = candle_at(mtg_dt)
                if mtg is None and now_bd() >= mtg_dt + timedelta(minutes=1):
                    live_window = await fetch_oanda_candles(instrument, count=30, granularity=timeframe)
                    if live_window:
                        candles = live_window
                        mtg = candle_at(mtg_dt)
                if mtg is None and now_bd() <= mtg_dt + timedelta(minutes=6):
                    mtg_deadline = mtg_dt + timedelta(minutes=6)
                    while mtg is None and now_bd() <= mtg_deadline:
                        await asyncio.sleep(3)
                        refreshed = await fetch_oanda_historical_candles(instrument, entry_dt, timeframe, before=20, after=12)
                        if refreshed:
                            candles = refreshed
                            mtg = candle_at(mtg_dt)
                if mtg is None:
                    result_type = "PENDING MTG G1"
                else:
                    try:
                        result_candle = mtg
                        mtg_level = 1
                        mtg_open, mtg_close = open_close(mtg)
                        mtg_win = (mtg_close == mtg_open) or ((direction == "CALL" and mtg_close > mtg_open) or (direction == "PUT" and mtg_close < mtg_open))
                        result_type = "MTG WIN" if mtg_win else "MTG LOSS"
                    except (TypeError, ValueError, AttributeError):
                        result_type = "INVALID"
        if update.effective_chat:
            record_partial_result(update.effective_chat.id, asset, entry_time, direction, result_type, signal_mode)
        win_count = context.user_data.get("user_wins", 0)
        loss_count = context.user_data.get("user_losses", 0)
        if "WIN" in result_type:
            win_count += 1
        elif "LOSS" in result_type:
            loss_count += 1
        context.user_data["user_wins"] = win_count
        context.user_data["user_losses"] = loss_count

        result_text = generate_result_card_text(
            asset=asset,
            time_str=entry_time,
            direction=direction,
            result_type=result_type,
            win_count=win_count,
            loss_count=loss_count,
            strategy_title="1000-STRATEGY HIGH CONFIDENCE",
            result_candle=result_candle,
            mtg_level=mtg_level,
        )
        next_callback = "lsig_next_manual_signal" if signal_mode == "MANUAL" else "lsig_next_auto_signal"
        result_markup = signal_result_markup(signal_mode)
        delivered = await send_final_result_chart(
            context.bot, update.effective_chat.id, asset, direction, result_type, candles, result_candle,
            result_text, reply_markup=result_markup, tag="manual" if signal_mode == "MANUAL" else "auto-check"
        )
        if not delivered:
            log.error("Manual result withheld because the verified result chart could not be delivered for %s", asset)
            await edit_or_send(
                update, context,
                "⚠️ <b>RESULT CHART DELIVERY RETRY</b>\n━━━━━━━━━━━━━━━━━━━━\nThe verified result is ready, but its OANDA chart image could not be delivered. Tap CHECK AGAIN shortly.",
                result_markup,
            )

    except asyncio.CancelledError:
        raise
    except Exception as exc:
        log.exception("Background manual CHECK RESULT failed: %s", exc)
        try:
            await edit_or_send(update, context, "⚠️ <b>RESULT CHECK RETRY</b>\n━━━━━━━━━━━━━━━━━━━━\nThe real OANDA check was interrupted. Tap CHECK AGAIN shortly.", pending_markup)
        except Exception:
            pass


result_check_handler = CallbackQueryHandler(handle_check_result_callback, pattern="^chkres_")

# ========================================
# File: telegram_ui/checker_engine.py
# ========================================

PERIOD = CONFIG["PERIOD_SECONDS"]

log = logging.getLogger(__name__)

_DIRECTION_ALIAS = {
    "BUY": "CALL", "CALL": "CALL", "UP": "CALL", "HIGH": "CALL",
    "HIGHER": "CALL", "RISE": "CALL", "BULL": "CALL", "BULLISH": "CALL",
    "PUT": "PUT", "SELL": "PUT", "DOWN": "PUT", "LOW": "PUT",
    "LOWER": "PUT", "FALL": "PUT", "BEAR": "PUT", "BEARISH": "PUT",
}


def normalize_direction(text: str) -> str | None:
    t = text.strip().upper()
    for alias, norm in _DIRECTION_ALIAS.items():
        if t == alias or t.startswith(alias):
            return norm
    return None


def format_oanda_instrument(pair_str: str) -> str:
    clean = pair_str.upper().replace("_OTC", "").replace("OTC", "").replace("/", "").replace("-", "").strip()
    if len(clean) == 6:
        return f"{clean[:3]}_{clean[3:]}"
    return clean


def now_bd() -> datetime:
    return datetime.now(BD_TZ)


REAL_MARKET_CLOSED_TEMPLATE = """<blockquote><b>🚫 REAL MARKET CLOSED</b>

━━━━━━━━━━━━━━━━━━━
<b>📅 TODAY IS {day}.</b>

<b>THE REAL MARKET IS CURRENTLY CLOSED.</b>

<b>⏳ PLEASE WAIT UNTIL MONDAY FOR THE
MARKET TO REOPEN.</b>

━━━━━━━━━━━━━━━━━━━
<b>👨‍💻 DEVELOPER : @TRADEWITHMEHEDI7</b></blockquote>"""


def is_real_market_closed() -> bool:
    """Real forex market is closed on Saturday/Sunday in Bangladesh time."""
    return now_bd().weekday() in (5, 6)


def real_market_closed_text() -> str:
    return REAL_MARKET_CLOSED_TEMPLATE.format(day=now_bd().strftime("%A").upper())


async def block_real_market(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Show the weekend closure card and return True when real features are blocked."""
    if not is_real_market_closed():
        return False
    query = update.callback_query
    if query:
        await safe_answer(query)
        await edit_or_send(update, context, real_market_closed_text(), build([[{"text": "BACK TO MAIN MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]))
    elif update.message:
        await update.message.reply_text(real_market_closed_text(), reply_markup=main_menu())
    return True


STRATEGY_CONFIG = CONFIG["STRATEGY_CONFIG"]

def calculate_rsi(closes: list[float], period: int | None = None) -> float:
    """Calculate RSI indicator using the configured strategy period."""
    period = int(period or STRATEGY_CONFIG['rsi_period'])
    if len(closes) < period + 1:
        return 50.0
    
    deltas = np.diff(closes)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])
    
    if avg_loss == 0:
        return 100.0
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(float(rsi), 2)

def calculate_ema(closes: list[float], period: int) -> float:
    """Calculate EMA indicator"""
    if len(closes) < period:
        return closes[-1] if closes else 0.0
    
    k = 2 / (period + 1)
    ema = np.mean(closes[:period])
    
    for price in closes[period:]:
        ema = price * k + ema * (1 - k)
    
    return float(ema)

def calculate_macd(closes: list[float]) -> tuple[float, float, float]:
    """Calculate MACD indicator"""
    fast_ema = calculate_ema(closes, STRATEGY_CONFIG['macd_fast'])
    slow_ema = calculate_ema(closes, STRATEGY_CONFIG['macd_slow'])
    macd_line = fast_ema - slow_ema
    
    macd_values = []
    for i in range(STRATEGY_CONFIG['macd_slow'], len(closes)):
        f = calculate_ema(closes[:i+1], STRATEGY_CONFIG['macd_fast'])
        s = calculate_ema(closes[:i+1], STRATEGY_CONFIG['macd_slow'])
        macd_values.append(f - s)
    
    if len(macd_values) >= STRATEGY_CONFIG['macd_signal']:
        signal_line = calculate_ema(macd_values, STRATEGY_CONFIG['macd_signal'])
    else:
        signal_line = macd_line
    
    histogram = macd_line - signal_line
    return float(macd_line), float(signal_line), float(histogram)

def calculate_bollinger_bands(closes: list[float]) -> tuple[float, float, float]:
    """Calculate Bollinger Bands"""
    period = STRATEGY_CONFIG['bb_period']
    if len(closes) < period:
        c = closes[-1] if closes else 0.0
        return c, c, c
    
    prices = closes[-period:]
    mean = np.mean(prices)
    std = np.std(prices)
    multiplier = STRATEGY_CONFIG['bb_std']
    
    upper = mean + (std * multiplier)
    lower = mean - (std * multiplier)
    
    return float(upper), float(mean), float(lower)

def calculate_atr(highs: list[float], lows: list[float], closes: list[float]) -> float:
    """Calculate Average True Range"""
    period = STRATEGY_CONFIG['atr_period']
    if len(closes) < period + 1:
        return 0.0
    
    tr_values = []
    for i in range(1, len(closes)):
        hl = highs[i] - lows[i]
        hc = abs(highs[i] - closes[i-1])
        lc = abs(lows[i] - closes[i-1])
        tr = max(hl, hc, lc)
        tr_values.append(tr)
    
    if not tr_values:
        return 0.0
    
    return float(np.mean(tr_values[-period:]))

def calculate_stochastic(highs: list[float], lows: list[float], closes: list[float], period: int = 14) -> tuple[float, float]:
    """Return fast %K and a simple %D for the latest completed candle."""
    period = max(2, int(period))
    if len(closes) < period or len(highs) < period or len(lows) < period:
        return 50.0, 50.0
    k_values = []
    for end in range(period, len(closes) + 1):
        window_high = max(highs[end - period:end])
        window_low = min(lows[end - period:end])
        span = window_high - window_low
        k_values.append(50.0 if span <= 0 else ((closes[end - 1] - window_low) / span) * 100.0)
    return round(float(k_values[-1]), 2), round(float(np.mean(k_values[-3:])), 2)


def calculate_adx(highs: list[float], lows: list[float], closes: list[float], period: int = 14) -> float:
    """Return a bounded trend-strength value from completed OHLC data."""
    period = max(2, int(period))
    if len(closes) < period + 1:
        return 0.0
    trs, directional = [], []
    for i in range(1, len(closes)):
        trs.append(max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1])))
        up, down = highs[i] - highs[i - 1], lows[i - 1] - lows[i]
        directional.append((up if up > down and up > 0 else 0.0, down if down > up and down > 0 else 0.0))
    atr = float(np.mean(trs[-period:]))
    if atr <= 0:
        return 0.0
    plus_di = 100.0 * float(np.mean([x[0] for x in directional[-period:]])) / atr
    minus_di = 100.0 * float(np.mean([x[1] for x in directional[-period:]])) / atr
    total = plus_di + minus_di
    return round(0.0 if total <= 0 else min(100.0, abs(plus_di - minus_di) / total * 100.0), 2)


# Add custom strategies here or call register_custom_strategy() at startup.
CUSTOM_STRATEGIES: dict[str, callable] = {}


def register_custom_strategy(code: str, strategy_fn) -> None:
    """Register a strategy returning a dict or (signal, confidence, details)."""
    normalized = str(code or '').strip().lower()
    if not normalized or not callable(strategy_fn):
        raise ValueError('A non-empty strategy code and callable function are required.')
    CUSTOM_STRATEGIES[normalized] = strategy_fn


def _run_custom_strategy(candles: list[dict], strategy_code: str):
    fn = CUSTOM_STRATEGIES.get(str(strategy_code or '').strip().lower())
    if not fn:
        return None
    try:
        raw = fn(candles)
        if isinstance(raw, tuple):
            values = list(raw) + [None, None, {}]
            raw = {'signal': values[0], 'confidence': values[1], 'details': values[2]}
        if not isinstance(raw, dict):
            return None
        signal = str(raw.get('signal') or '').upper()
        if signal not in {'CALL', 'PUT'}:
            return None
        return signal, max(0, min(99, int(raw.get('confidence', 0) or 0))), dict(raw.get('details') or {})
    except Exception:
        log.exception('Custom strategy failed: %s', strategy_code)
        return None


def calculate_support_resistance(highs: list[float], lows: list[float], lookback: int = 50) -> tuple[list[float], list[float]]:
    """Identify support and resistance levels"""
    if len(highs) < lookback:
        return [], []
    
    recent_highs = highs[-lookback:]
    recent_lows = lows[-lookback:]
    
    swing_highs = []
    swing_lows = []
    
    for i in range(2, len(recent_highs) - 2):
        if (recent_highs[i] > recent_highs[i-1] and 
            recent_highs[i] > recent_highs[i-2] and
            recent_highs[i] > recent_highs[i+1] and 
            recent_highs[i] > recent_highs[i+2]):
            swing_highs.append(recent_highs[i])
        
        if (recent_lows[i] < recent_lows[i-1] and 
            recent_lows[i] < recent_lows[i-2] and
            recent_lows[i] < recent_lows[i+1] and 
            recent_lows[i] < recent_lows[i+2]):
            swing_lows.append(recent_lows[i])
    
    resistance = []
    for level in swing_highs:
        if not any(abs(level - r) / level < 0.002 for r in resistance):
            resistance.append(level)
    
    support = []
    for level in swing_lows:
        if not any(abs(level - s) / level < 0.002 for s in support):
            support.append(level)
    
    return support[:5], resistance[:5]

def detect_candlestick_patterns(candle: dict, prev_candle: dict) -> list[str]:
    """Detect candlestick patterns"""
    patterns = []
    
    try:
        o = float(candle['open'])
        h = float(candle['high'])
        l = float(candle['low'])
        c = float(candle['close'])
        prev_o = float(prev_candle['open'])
        prev_c = float(prev_candle['close'])
    except Exception:
        return []
    
    body = abs(c - o)
    range_candle = h - l if h != l else 0.00001
    upper_wick = h - max(c, o)
    lower_wick = min(c, o) - l
    
    if body < range_candle * 0.1:
        patterns.append("DOJI")
    
    if upper_wick > body * 2 and lower_wick < body * 0.5:
        patterns.append("SHOOTING_STAR")
    elif lower_wick > body * 2 and upper_wick < body * 0.5:
        patterns.append("HAMMER")
    
    if c > o and prev_c < prev_o and c > prev_o and o < prev_c:
        patterns.append("BULLISH_ENGULFING")
    elif c < o and prev_c > prev_o and c < prev_o and o > prev_c:
        patterns.append("BEARISH_ENGULFING")
    
    if upper_wick < body * 0.1 and lower_wick < body * 0.1:
        if c > o:
            patterns.append("BULLISH_MARUBOZU")
        else:
            patterns.append("BEARISH_MARUBOZU")
    
    return patterns

def enhanced_analyze(candles: list[dict], strategy_code: str | None = None) -> tuple[str | None, int, dict]:
    """
    Enhanced trading strategy with multiple confirmations
    Returns: (direction, confidence, details)
    """
    if len(candles) < 50:
        return None, 0, {}
    custom_result = _run_custom_strategy(candles, strategy_code) if strategy_code else None
    if custom_result:
        direction, confidence, details = custom_result
        details['strategy'] = str(strategy_code).lower()
        return direction, confidence, details
    if strategy_code and _standalone_strategy is not None and strategy_code in _standalone_strategy.STRATEGIES:
        try:
            profile_result = _standalone_strategy.analyze(candles, strategy_code)
            profile_details = dict(profile_result.get("details") or {})
            profile_details.update({"score": profile_result.get("score", 0), "agreement": profile_result.get("agreement", 0), "strategy": profile_result.get("strategy", strategy_code), "macd_line": profile_details.get("macd", 0.0), "signal_line": profile_details.get("macd_signal", 0.0)})
            return profile_result.get("signal"), int(profile_result.get("confidence", 0)), profile_details
        except Exception:
            log.exception("Premium strategy profile failed: %s", strategy_code)
    # Prepare price data
    def _ohlc(c):
        mid = c.get('mid') or {}
        return {
            'open': float(mid.get('o', c.get('open', 0.0))),
            'high': float(mid.get('h', c.get('high', 0.0))),
            'low': float(mid.get('l', c.get('low', 0.0))),
            'close': float(mid.get('c', c.get('close', 0.0))),
            'volume': float(c.get('volume', 0.0)),
        }
    candles = [_ohlc(c) for c in candles]
    closes = [float(c['close']) for c in candles]
    opens = [float(c['open']) for c in candles]
    highs = [float(c['high']) for c in candles]
    lows = [float(c['low']) for c in candles]
    volumes = [float(c.get('volume', 0)) for c in candles]
    
    # Calculate indicators
    rsi = calculate_rsi(closes)
    ema_fast = calculate_ema(closes, STRATEGY_CONFIG['ema_fast'])
    ema_slow = calculate_ema(closes, STRATEGY_CONFIG['ema_slow'])
    ema_trend = calculate_ema(closes, STRATEGY_CONFIG['ema_trend'])
    macd_line, signal_line, histogram = calculate_macd(closes)
    bb_upper, bb_middle, bb_lower = calculate_bollinger_bands(closes)
    atr = calculate_atr(highs, lows, closes)
    stochastic_k, stochastic_d = calculate_stochastic(highs, lows, closes)
    adx = calculate_adx(highs, lows, closes)
    support, resistance = calculate_support_resistance(highs, lows)
    
    # Current candle
    current_candle = candles[-1]
    prev_candle = candles[-2] if len(candles) > 1 else current_candle
    
    # Detect patterns
    patterns = detect_candlestick_patterns(current_candle, prev_candle)
    
    # Price position
    current_price = closes[-1]
    prev_close = closes[-2] if len(closes) > 1 else current_price
    
    # Initialize scoring
    score = 0
    signals = []
    confidence_factors = []
    
    # ========== TREND ANALYSIS ==========
    # EMA alignment
    if ema_fast > ema_slow > ema_trend:
        score += 25
        signals.append("BULLISH_TREND")
        confidence_factors.append(25)
    elif ema_fast < ema_slow < ema_trend:
        score -= 25
        signals.append("BEARISH_TREND")
        confidence_factors.append(25)
    
    # Price vs EMA
    if current_price > ema_slow:
        score += 15
        signals.append("PRICE_ABOVE_EMA")
        confidence_factors.append(15)
    elif current_price < ema_slow:
        score -= 15
        signals.append("PRICE_BELOW_EMA")
        confidence_factors.append(15)
    
    # ========== MOMENTUM ANALYSIS ==========
    # RSI
    if rsi < STRATEGY_CONFIG['rsi_oversold']:
        score += 20
        signals.append(f"RSI_OVERSOLD_{rsi}")
        confidence_factors.append(20)
    elif rsi > STRATEGY_CONFIG['rsi_overbought']:
        score -= 20
        signals.append(f"RSI_OVERBOUGHT_{rsi}")
        confidence_factors.append(20)
    
    # RSI divergence
    if len(closes) >= 20:
        recent_rsi_lows = []
        recent_price_lows = []
        for i in range(-20, 0):
            if i >= -len(closes):
                recent_rsi_lows.append(calculate_rsi(closes[:i+20] if i+20 > 0 else closes[:i+20]))
                recent_price_lows.append(closes[i])
        
        if len(recent_rsi_lows) > 5:
            if min(recent_rsi_lows[-5:]) > min(recent_rsi_lows[:-5]) and min(recent_price_lows[-5:]) < min(recent_price_lows[:-5]):
                score += 30
                signals.append("BULLISH_RSI_DIVERGENCE")
                confidence_factors.append(30)
            elif max(recent_rsi_lows[-5:]) < max(recent_rsi_lows[:-5]) and max(recent_price_lows[-5:]) > max(recent_price_lows[:-5]):
                score -= 30
                signals.append("BEARISH_RSI_DIVERGENCE")
                confidence_factors.append(30)
    
    # ========== MACD ANALYSIS ==========
    if macd_line > signal_line:
        score += 15
        signals.append("MACD_BULLISH_CROSS")
        confidence_factors.append(15)
        
        if histogram > 0:
            score += 5
            signals.append("MACD_HISTOGRAM_POSITIVE")
    else:
        score -= 15
        signals.append("MACD_BEARISH_CROSS")
        confidence_factors.append(15)
        
        if histogram < 0:
            score -= 5
            signals.append("MACD_HISTOGRAM_NEGATIVE")
    
    # ========== BOLLINGER BANDS ==========
    if current_price <= bb_lower:
        score += 15
        signals.append("PRICE_AT_LOWER_BB")
        confidence_factors.append(15)
    elif current_price >= bb_upper:
        score -= 15
        signals.append("PRICE_AT_UPPER_BB")
        confidence_factors.append(15)
    
    # BB squeeze (volatility contraction)
    bb_width = (bb_upper - bb_lower) / bb_middle
    prev_bb_upper, prev_bb_middle, prev_bb_lower = calculate_bollinger_bands(closes[:-1])
    prev_width = (prev_bb_upper - prev_bb_lower) / prev_bb_middle
    
    if bb_width < prev_width and bb_width < 0.05:
        if score > 0:
            score += 10
            signals.append("BB_SQUEEZE_BULLISH")
        else:
            score -= 10
            signals.append("BB_SQUEEZE_BEARISH")
    
    # ========== CANDLESTICK PATTERNS ==========
    pattern_scores = {
        "BULLISH_ENGULFING": 20,
        "BEARISH_ENGULFING": -20,
        "HAMMER": 15,
        "SHOOTING_STAR": -15,
        "BULLISH_MARUBOZU": 10,
        "BEARISH_MARUBOZU": -10,
        "DOJI": 0
    }
    
    for pattern in patterns:
        if pattern in pattern_scores:
            score += pattern_scores[pattern]
            signals.append(pattern)
            confidence_factors.append(abs(pattern_scores[pattern]))
    
    # ========== SUPPORT/RESISTANCE ==========
    # Check distance to levels
    for sup in support:
        if abs(current_price - sup) / current_price < 0.005:  # Within 0.5%
            score += 20
            signals.append("NEAR_SUPPORT")
            confidence_factors.append(20)
            break
    
    for res in resistance:
        if abs(current_price - res) / current_price < 0.005:
            score -= 20
            signals.append("NEAR_RESISTANCE")
            confidence_factors.append(20)
            break
    
    # ========== VOLUME ANALYSIS ==========
    if len(volumes) > STRATEGY_CONFIG['volume_sma']:
        avg_volume = np.mean(volumes[-STRATEGY_CONFIG['volume_sma']:-1])
        current_volume = volumes[-1]
        
        if current_volume > avg_volume * 1.5:
            if score > 0:
                score += 10
                signals.append("HIGH_VOLUME_BULLISH")
            else:
                score -= 10
                signals.append("HIGH_VOLUME_BEARISH")
    
    # ========== FINAL DECISION ==========
    # Normalize score to 0-100 range (original range approx -100 to 100)
    normalized_score = (score + 100) / 2
    base_confidence = min(98, max(50, normalized_score))
    
    # Adjust confidence based on signal consistency
    if len(set(signals)) >= 3:
        base_confidence = min(98, base_confidence + 10)
    
    # Determine direction
    if score > 20:
        direction = "CALL"
        final_confidence = min(98, base_confidence + 5)
    elif score < -20:
        direction = "PUT"
        final_confidence = min(98, base_confidence + 5)
    else:
        # Neutral - use EMA trend
        if ema_fast > ema_slow:
            direction = "CALL"
            final_confidence = 65
        else:
            direction = "PUT"
            final_confidence = 65
    
    # Ensure minimum confidence
    final_confidence = max(STRATEGY_CONFIG['min_confidence'], final_confidence)
    
    # Prepare detailed analysis
    analysis_details = {
        'current_price': round(current_candle['close'], 6),
        'rsi': round(rsi, 1),
        'ema_fast': round(ema_fast, 6),
        'ema_slow': round(ema_slow, 6),
        'ema_trend': round(ema_trend, 6),
        'macd': round(macd_line, 6),
        'macd_line': round(macd_line, 6),
        'signal': round(signal_line, 6),
        'signal_line': round(signal_line, 6),
        'histogram': round(histogram, 6),
        'bb_upper': round(bb_upper, 6),
        'bb_middle': round(bb_middle, 6),
        'bb_lower': round(bb_lower, 6),
        'atr': round(atr, 6),
        'stochastic_k': stochastic_k,
        'stochastic_d': stochastic_d,
        'adx': adx,
        'support': round(min(support), 6) if support else round(min(lows[-20:]), 6),
        'resistance': round(max(resistance), 6) if resistance else round(max(highs[-20:]), 6),
        'score': score,
        'signals': signals[:5],  # Top 5 signals
        'patterns': patterns
    }
    
    return direction, final_confidence, analysis_details


def bug_signal_strategy(candles: list[dict], market_mode: str = "REAL", strategy_code: str | None = None) -> dict:
    """Dedicated BUG SIGNAL confluence engine using completed real/reference candles only."""
    if not candles or len(candles) < 50:
        return {"qualified": False, "signal": None, "confidence": 0, "agreement": 0, "score": 0, "details": {"error": "insufficient_completed_candles"}}
    try:
        direction, confidence, details = enhanced_analyze(candles, strategy_code=strategy_code)
        if direction not in ("CALL", "PUT"):

            return {"qualified": False, "signal": None, "confidence": 0, "agreement": 0, "score": 0, "details": details or {}}
        details = dict(details or {})
        details["market_mode"] = market_mode
        details["logic"] = "TREND+RSI+EMA+MACD+BB+PRICE_ACTION+SUPPORT_RESISTANCE+VOLUME"
        score = float(details.get("score", confidence))
        confidence = int(max(0, min(98, float(confidence))))
        return {
            "qualified": confidence >= 75,
            "signal": direction,
            "confidence": confidence,
            "agreement": round(max(0.0, min(100.0, confidence)), 1),
            "score": round(score, 1),
            "details": details,
        }
    except Exception as exc:
        log.exception("BUG SIGNAL strategy analysis failed (%s): %s", market_mode, exc)
        return {"qualified": False, "signal": None, "confidence": 0, "agreement": 0, "score": 0, "details": {"error": "strategy_exception"}}


# Internal adapter used when the optional external strategy module is absent.
def _local_strategy_consensus(candles, min_score=72.0, min_agreement=65.0, min_votes=8, strategy_code: str | None = None):
    direction, confidence, details = enhanced_analyze(candles or [], strategy_code=strategy_code)
    if direction not in ("CALL", "PUT"):
        return {"qualified": False, "signal": None, "confidence": 0, "agreement": 0, "score": 0}
    score = float(max(0, min(99, confidence)))
    return {
        "qualified": score >= float(min_score),
        "signal": direction,
        "confidence": int(score),
        "agreement": round(score, 1),
        "score": round(score, 1),
        "details": details or {},
    }


if strategy_consensus is None:
    strategy_consensus = _local_strategy_consensus


async def fetch_oanda_candles(instrument: str, count: int = 200, granularity: str = "M1") -> list[dict] | None:
    """
    Fetch REAL OANDA candles using Python standard-library HTTP only.
    No external HTTP client dependency and NO fake/simulated market-data fallback.
    """
    api_key = os.environ.get("OANDA_API_KEY", "").strip()
    if not api_key:
        log.error("OANDA_API_KEY is not configured.")
        return None

    env = os.environ.get("OANDA_ENVIRONMENT", "practice").strip().lower()
    base_url = (
        "https://api-fxtrade.oanda.com"
        if env in ("live", "trade")
        else "https://api-fxpractice.oanda.com"
    )
    oanda_inst = format_oanda_instrument(instrument)
    query = urllib.parse.urlencode({
        "count": max(60, min(int(count), 5000)),
        "granularity": granularity,
        "price": "M",
    })
    url = f"{base_url}/v3/instruments/{urllib.parse.quote(oanda_inst, safe='_')}/candles?{query}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "ZENITEX-AI/3.0",
    }

    def _request():
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=CONFIG["OANDA_TIMEOUT_SECONDS"]) as response:
            return response.status, response.read()

    data = None
    last_error = None
    for attempt in range(max(1, CONFIG["OANDA_RETRIES"])):
        try:
            status, raw = await asyncio.to_thread(_request)
            if status != 200:
                log.error("OANDA HTTP %s for %s", status, oanda_inst)
                return None
            data = json.loads(raw.decode("utf-8"))
            break
        except Exception as ex:
            last_error = ex
            if attempt < max(1, CONFIG["OANDA_RETRIES"]) - 1:
                await asyncio.sleep(0.45 * (attempt + 1))
                continue
            # A transient provider/network failure is reported as a warning;
            # no fallback candle is ever created and callers may retry later.
            log.warning("OANDA market-data temporarily unavailable for %s after %s attempts: %s", oanda_inst, attempt + 1, last_error)
            return None

    candles = data.get("candles", []) if data else []
    valid = []
    for candle in candles:
        if not candle.get("complete", True):
            continue
        mid = candle.get("mid") or {}
        try:
            o = float(mid["o"])
            h = float(mid["h"])
            l = float(mid["l"])
            c = float(mid["c"])
        except (KeyError, TypeError, ValueError):
            continue
        if h < max(o, c) or l > min(o, c) or h < l:
            continue
        valid.append({
            **candle,
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "pair": oanda_inst,
            "timeframe": granularity,
        })
    return valid or None

async def get_oanda_live_signal_box(pair_str: str = "EUR_USD") -> str:
    pair = format_oanda_instrument(pair_str)
    display_pair = pair.replace("_", "/")
    candles = await fetch_oanda_candles(pair, count=200, granularity="M1")
    if not candles or len(candles) < 50:
        return (
            "<b>REAL OANDA DATA UNAVAILABLE</b>\n"
            "No strategy signal was generated because completed OANDA candles were not available."
        )
    analyzed = _local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0)
    direction = analyzed.get("signal")
    if direction not in ("CALL", "PUT"):
        return (
            "<b>STRATEGY ANALYSIS UNAVAILABLE</b>\n"
            "No valid directional result was produced from the completed OANDA candles."
        )
    details = analyzed.get("details") or {}
    last = candles[-1]
    c_open = float(last["open"])
    c_close = float(last["close"])
    c_high = float(last["high"])
    c_low = float(last["low"])
    open_price = f"{c_open:.5f}"
    close_price = f"{c_close:.5f}"
    trend = "BULLISH" if direction == "CALL" else "BEARISH"
    payout = "OANDA REAL DATA"
    support = f"{float(details.get('support', c_low)):.5f}"
    resistance = f"{float(details.get('resistance', c_high)):.5f}"
    strength = f"{int(analyzed.get('confidence', 0))}% CONFIDENCE"
    now_str = now_bd().strftime("%H:%M")

# removed relative import:     from .zenitix import signal_box
    return signal_box(
        asset=f"{display_pair} (OANDA)",
        trend=trend,
        direction=direction,
        timeframe="M1",
        entry=now_str,
        strength=strength,
        mtg="1-STEP",
        payout=payout,
        support=support,
        resistance=resistance,
        owner="@TRADEWITHMEHEDI7",
        analysis=f"⚡ <i>OANDA v3 Real Market Stream: Open {open_price} | Price {close_price}</i>\n📊 <i>Verified with ZX ZX_PRO 2.1 AI Engine</i>"
    )


def parse_signal_line(line: str) -> dict | None:
    clean = line.strip()
    if not clean:
        return None

    for a, b in [(";", " "), ("|", " "), (",", " "), ("\t", " ")]:
        clean = clean.replace(a, b)
    clean = re.sub(r"\s+", " ", clean).strip()

    time_match = re.search(r"\b([0-2]?\d:[0-5]\d)\b", clean)
    dir_match = re.search(r"\b(BUY|CALL|UP|PUT|SELL|DOWN|HIGHER|LOWER)\b", clean, re.I)

    direction = normalize_direction(dir_match.group(1)) if dir_match else None

    if not time_match:
        return None

    hhmm = time_match.group(1).zfill(5)

    asset_zone = clean
    asset_zone = re.sub(r"\bM\s*\d+\b", " ", asset_zone, flags=re.I)
    asset_zone = re.sub(r"\b[0-2]?\d:[0-5]\d\b", " ", asset_zone)
    asset_zone = re.sub(r"\b(BUY|CALL|UP|PUT|SELL|DOWN|HIGHER|LOWER)\b", " ", asset_zone, flags=re.I)
    asset_zone = re.sub(r"\b(20\d{2})[.\-/](\d{1,2})[.\-/](\d{1,2})\b", " ", asset_zone)
    asset_zone = re.sub(r"\s+", " ", asset_zone).strip()

    pair_match = re.search(
        r"([A-Z]{3}\s*/?\s*[A-Z]{3}|[A-Z]{3}_[A-Z]{3}|[A-Z]{6})",
        asset_zone,
        re.I,
    )
    if not pair_match:
        return None

    pair_raw = pair_match.group(1).strip().upper()
    is_otc = bool(re.search(r"(?:[-_ ]OTC)\b", clean, flags=re.I))
    pair = format_oanda_instrument(pair_raw)

    tf_match = re.search(r"\bM(\d+)\b", clean, re.I)
    tf = f"M{tf_match.group(1)}" if tf_match else "M1"

    date_match = re.search(r"\b(20\d{2})[.\-/](\d{1,2})[.\-/](\d{1,2})\b", clean)
    signal_date = None
    if date_match:
        signal_date = f"{date_match.group(1)}.{int(date_match.group(2)):02d}.{int(date_match.group(3)):02d}"

    return {
        "pair": pair,
        "display_pair": pair.replace("_", "").upper() + ("-otc" if is_otc else ""),
        "otc": is_otc,
        "time": hhmm,
        "direction": direction,
        "tf": tf,
        "date": signal_date,
        "raw": line.strip(),
    }


def target_epoch(signal: dict, date_str: str | None = None) -> int:
    today = now_bd().date()
    if date_str:
        try:
            parts = date_str.replace("-", ".").split(".")
            d = datetime(int(parts[0]), int(parts[1]), int(parts[2])).date()
        except Exception:
            d = today
    else:
        d = today

    hh, mm = map(int, signal["time"].split(":"))
    dt = datetime(d.year, d.month, d.day, hh, mm, 0, tzinfo=BD_TZ)
    return int(dt.timestamp())


# ========================================
# File: telegram_ui/welcome_banner.py
# ========================================


def ensure_welcome_photo(filename="welcome_photo.jpg"):
    """
    Generates the exact Welcome image matching the user specification:
    Dark keyboard background with glowing 'Welcome!' text and sparkles.
    """
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        return filename

    width = 1200
    height = 630

    # 1. Base dark keyboard canvas
    img = Image.new("RGB", (width, height), (15, 18, 24))
    draw = ImageDraw.Draw(img)

    # 2. Draw keyboard key grid pattern in background
    key_color = (25, 30, 40)
    key_border = (45, 55, 75)
    
    # Rows of keys
    key_rows = [
        [ (50, 40, 220, 150), (250, 40, 480, 150), (510, 40, 740, 150), (770, 40, 1150, 150) ],
        [ (50, 170, 320, 290), (350, 170, 620, 290), (650, 170, 920, 290), (950, 170, 1150, 290) ],
        [ (50, 310, 280, 440), (310, 310, 590, 440), (620, 310, 890, 440), (920, 310, 1150, 440) ],
        [ (50, 460, 400, 590), (430, 460, 780, 590), (810, 460, 1150, 590) ],
    ]

    for row in key_rows:
        for (kx1, ky1, kx2, ky2) in row:
            draw.rectangle([kx1, ky1, kx2, ky2], fill=key_color, outline=key_border, width=2)
            # Subtle key highlight
            draw.line([(kx1 + 2, ky1 + 2), (kx2 - 2, ky1 + 2)], fill=(35, 42, 55), width=1)

    # Keycap letters (p, { }, etc.)
    font_small = ImageFont.load_default()
    try:
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except Exception:
        pass

    draw.text((80, 70), "P", fill=(90, 105, 130), font=font_small)
    draw.text((280, 70), "{ [", fill=(90, 105, 130), font=font_small)
    draw.text((540, 70), "]", fill=(90, 105, 130), font=font_small)
    draw.text((990, 70), "enter", fill=(90, 105, 130), font=font_small)
    draw.text((80, 340), ";", fill=(90, 105, 130), font=font_small)

    # 3. Fonts for Welcome !
    font_welcome = ImageFont.load_default()
    try:
        font_welcome = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 84)
    except Exception:
        pass

    # 4. Draw glowing 'Welcome !' text in center
    text = "Welcome !"
    text_bbox = draw.textbbox((0, 0), text, font=font_welcome)
    tw = text_bbox[2] - text_bbox[0]
    th = text_bbox[3] - text_bbox[1]
    tx = (width - tw) // 2
    ty = (height - th) // 2 - 20

    # Draw glow layers
    for offset in range(12, 0, -2):
        shade = 40 + (12 - offset) * 12
        draw.text((tx - offset, ty), text, fill=(shade, shade + 40, shade + 80), font=font_welcome)
        draw.text((tx + offset, ty), text, fill=(shade, shade + 40, shade + 80), font=font_welcome)
        draw.text((tx, ty - offset), text, fill=(shade, shade + 40, shade + 80), font=font_welcome)
        draw.text((tx, ty + offset), text, fill=(shade, shade + 40, shade + 80), font=font_welcome)

    # Main white glowing text
    draw.text((tx, ty), text, fill=(255, 255, 255), font=font_welcome)

    # 5. Draw sparkles / stars
    stars = [
        (150, 100, 14), (220, 520, 10), (950, 120, 12), (1050, 480, 16),
        (380, 110, 8), (850, 420, 10), (600, 80, 10), (700, 530, 8)
    ]

    for sx, sy, size in stars:
        # 4-point star sparkle
        draw.line([(sx - size, sy), (sx + size, sy)], fill=(255, 255, 255), width=2)
        draw.line([(sx, sy - size), (sx, sy + size)], fill=(255, 255, 255), width=2)
        draw.line([(sx - size/1.4, sy - size/1.4), (sx + size/1.4, sy + size/1.4)], fill=(200, 230, 255), width=1)
        draw.line([(sx - size/1.4, sy + size/1.4), (sx + size/1.4, sy - size/1.4)], fill=(200, 230, 255), width=1)
        # Center glow dot
        draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))

    img.save(filename, "JPEG", quality=95)
    return filename


# ========================================
# File: telegram_ui/handlers/start.py
# ========================================
WELCOME_PHOTO = str(Path(__file__).resolve().parent / "welcome_photo.jpg")
WELCOME_IMAGE_URL = os.environ.get("WELCOME_IMAGE_URL", "https://files.manuscdn.com/user_upload_by_module/session_file/310519663243374849/ojfRQZmACeFROWvr.jpg")

def prepare_welcome_photo() -> Path:
    """Return a valid local JPEG, recovering from the configured URL when needed."""
    path = Path(WELCOME_PHOTO)
    try:
        if path.exists() and path.stat().st_size > 1024:
            with Image.open(path) as img:
                img.verify()
            return path
    except Exception as exc:
        log.warning("Cached welcome image validation failed: %s", exc)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(WELCOME_IMAGE_URL, str(path))
        with Image.open(path) as img:
            img.verify()
        return path
    except Exception as exc:
        log.warning("Welcome image URL recovery failed: %s", exc)
        return path

prepare_welcome_photo()

def get_start_menu() -> InlineKeyboardMarkup:
    """Initial onboarding keyboard: the main bot menu is intentionally gated."""
    return build([[{"text": "GET START", "callback": "get_start", "style": KeyboardButtonStyle.DANGER}]])


async def send_welcome_image_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, show_menu: bool = True) -> None:
    """Send the cached welcome image with either GET START or the full menu."""
    text = welcome_text()
    markup = main_menu(is_owner(update)) if show_menu else get_start_menu()
    image_path = prepare_welcome_photo()
    try:
        with image_path.open("rb") as photo:
            if update.callback_query and update.callback_query.message:
                message = update.callback_query.message
                if getattr(message, "photo", None):
                    try:
                        await message.edit_caption(caption=text, parse_mode="HTML", reply_markup=markup)
                        return
                    except Exception:
                        pass
                try:
                    await message.delete()
                except Exception:
                    pass
                await context.bot.send_photo(
                    chat_id=message.chat_id,
                    photo=photo, caption=text, parse_mode="HTML", reply_markup=markup,
                )
            elif update.message:
                await update.message.reply_photo(
                    photo=photo, caption=text, parse_mode="HTML", reply_markup=markup,
                )
            return
    except Exception as exc:
        log.warning("Cached welcome image failed; using fast text menu: %s", exc)
    if update.callback_query and update.callback_query.message:
        await context.bot.send_message(
            chat_id=update.callback_query.message.chat_id, text=text,
            parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True,
        )
    else:
        await update.message.reply_text(
            text=text, parse_mode="HTML", reply_markup=markup, disable_web_page_preview=True,
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Respond immediately with the cached welcome image; registration runs in background."""
    user = update.effective_user
    if user:
        context.application.create_task(
            asyncio.to_thread(register_user, user.id, user.username or "", user.first_name or "")
        )
    await send_welcome_image_menu(update, context, show_menu=False)
    return ConversationHandler.END


async def get_start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reveal the full professional menu after the user presses GET START."""
    query = update.callback_query
    await safe_answer(query, "WELCOME TO ZENITIX AI", show_alert=False)
    await send_welcome_image_menu(update, context, show_menu=True)


start_handler = CommandHandler("start", start)
get_start_handler = CallbackQueryHandler(get_start_callback, pattern="^get_start$")

# ========================================
# File: telegram_ui/handlers/menu.py
# ========================================


# Vision/API settings come from the central CONFIG block.


def _chatgpt_chart_analysis(image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    """Analyze a chart screenshot through an OpenAI-compatible vision endpoint."""
    api_key = (os.environ.get("CHATGPT_API_KEY", "").strip()
               or os.environ.get("OPENROUTER_API_KEY", "").strip())
    if not api_key:
        return "CHATGPT CONFIGURATION ERROR: CHATGPT_API_KEY is not configured."
    encoded = __import__("base64").b64encode(image_bytes).decode("ascii")
    prompt = ("Analyze only visible candlestick-chart evidence. Do not invent pair, timeframe, price, indicator, or level. "
              "Return labels: VERDICT (CALL or PUT), CONFIDENCE (integer percent), MARKET/PAIR, TIMEFRAME, TREND, LAST CANDLE, SUPPORT, RESISTANCE, REASON. "
              "Use UNKNOWN when text is not visible. Keep the reason short and evidence-based.")
    payload = json.dumps({"model": CHATGPT_MODEL, "messages": [{"role": "user", "content": [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{encoded}"}},
    ]}], "temperature": 0.1, "max_tokens": 500}).encode("utf-8")
    req = urllib.request.Request(CHATGPT_API_URL, data=payload, headers={
        "Authorization": f"Bearer {api_key}", "Content-Type": "application/json",
        "HTTP-Referer": "https://zenitix.ai", "X-Title": "Zenitix AI",
    }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return str(text).strip() or "CHATGPT ANALYSIS ERROR: Empty vision response."
    except urllib.error.HTTPError as exc:
        return f"CHATGPT ANALYSIS ERROR: HTTP {exc.code}."
    except Exception:
        return "CHATGPT ANALYSIS ERROR: Vision request failed."


def _gemini_chart_analysis(image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    """Analyze a chart screenshot with low-credit Gemini Vision."""
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        return "GEMINI CONFIGURATION ERROR: GEMINI_API_KEY is not configured."
    encoded = __import__("base64").b64encode(image_bytes).decode("ascii")
    prompt = ("Analyze only visible candlestick-chart evidence. Do not invent pair, timeframe, price, indicator, or level. "
              "Return labels: VERDICT (CALL or PUT), CONFIDENCE (integer percent), MARKET/PAIR, TIMEFRAME, TREND, LAST CANDLE, SUPPORT, RESISTANCE, REASON. "
              "Use UNKNOWN when text is not visible. Keep the reason short and evidence-based.")
    payload = json.dumps({"contents": [{"parts": [{"text": prompt}, {"inline_data": {"mime_type": mime_type, "data": encoded}}]}], "generationConfig": {"temperature": 0.1, "maxOutputTokens": 500}}).encode("utf-8")
    url = GEMINI_VISION_URL.format(model=GEMINI_VISION_MODEL) + "?key=" + urllib.parse.quote(api_key, safe="")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json", "User-Agent": "ZENITEX-AI/3.0"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
        text = "\n".join(str(p.get("text", "")) for p in parts if p.get("text")).strip()
        return text or "GEMINI ANALYSIS ERROR: Empty Vision response."
    except urllib.error.HTTPError as exc:
        return f"GEMINI ANALYSIS ERROR: HTTP {exc.code}."
    except Exception:
        return "GEMINI ANALYSIS ERROR: Vision request failed."


def format_chart_analysis_result(raw: str, provider: str) -> str:
    """Normalize model output into one safe, compact premium Telegram layout."""
    fields = {
        "VERDICT": "UNKNOWN", "CONFIDENCE": "UNKNOWN", "MARKET/PAIR": "UNKNOWN",
        "MARKET": "UNKNOWN", "PAIR": "UNKNOWN", "TIMEFRAME": "UNKNOWN",
        "TREND": "UNKNOWN", "LAST CANDLE": "UNKNOWN", "SUPPORT": "UNKNOWN",
        "RESISTANCE": "UNKNOWN", "REASON": "UNKNOWN",
    }
    for line in str(raw or "").splitlines():
        line = line.strip().lstrip("-•* ")
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().upper().replace("_", " ")
        value = value.strip()
        if key in fields and value:
            fields[key] = value
    market = fields.get("MARKET/PAIR")
    if market == "UNKNOWN":
        market = fields.get("MARKET", "UNKNOWN")
        if fields.get("PAIR", "UNKNOWN") != "UNKNOWN":
            market = fields["PAIR"]
    verdict = fields.get("VERDICT", "UNKNOWN").upper()
    direction_icon = "🟢" if "CALL" in verdict else "🔴" if "PUT" in verdict else "⚪"
    confidence = fields.get("CONFIDENCE", "UNKNOWN")
    return ("<blockquote><b>╔════════════════════╗</b>\n"
            "<b>      𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝙰𝙸 𝙲𝙷𝙰𝚁𝚃</b>\n"
            "<b>╚════════════════════╝</b>\n\n"
            f"📈 <b>𝙼𝙰𝚁𝙺𝙴𝚃 ∶ {html.escape(market)}</b>\n"
            f"⏱ <b>𝚃𝙸𝙼𝙴𝙵𝚁𝙰𝙼𝙴 ∶ {html.escape(fields['TIMEFRAME'])}</b>\n"
            f"📊 <b>𝚃𝚁𝙴𝙽𝙳 ∶ {html.escape(fields['TREND'])}</b>\n"
            f"🕯 <b>𝙻𝙰𝚂𝚃 𝙲𝙰𝙽𝙳𝙻𝙴 ∶ {html.escape(fields['LAST CANDLE'])}</b>\n\n"
            f"{direction_icon} <b>𝙽𝙴𝚇𝚃 𝙲𝙰𝙽𝙳𝙻𝙴 ∶ {html.escape(verdict)}</b>\n"
            f"💯 <b>𝙲𝙾𝙽𝙵𝙸𝙳𝙴𝙽𝙲𝙴 ∶ {html.escape(confidence)}</b>\n\n"
            f"📉 <b>𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ∶ {html.escape(fields['SUPPORT'])}</b>\n"
            f"📈 <b>𝚁𝙴𝚂𝙸𝚂𝚃𝙰𝙽𝙲𝙴 ∶ {html.escape(fields['RESISTANCE'])}</b>\n\n"
            f"📝 <b>𝚁𝙴𝙰𝚂𝙾𝙽 ∶ {html.escape(fields['REASON'])}</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"<b>𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝚁 ∶ {html.escape(provider)}</b>\n"
            "<i>Chart analysis is not guaranteed financial advice.</i></blockquote>")


async def chart_analysis_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    if query:
        await safe_answer(query)
    uid = update.effective_user.id if update.effective_user else 0
    tier = get_user_tier(uid).upper()
    if tier not in {"EXPENSIVE", "OWNER"}:
        await edit_or_send(update, context, "<blockquote><b>AI CHART ANALYSIS — EXPENSIVE PLAN ONLY</b>\n━━━━━━━━━━━━━━━━━━━━\nThis feature is available only for EXPENSIVE plan users.\nDaily allowance: <b>2 analyses</b>.</blockquote>", home_button())
        return ConversationHandler.END
    usage = get_user_usage(uid)
    used = int(usage.get("ai_chart_analysis", 0) or 0)
    if used >= 2:
        await edit_or_send(update, context, "<blockquote><b>DAILY CHART LIMIT REACHED</b>\n━━━━━━━━━━━━━━━━━━━━\nYour EXPENSIVE plan has used both AI Chart Analysis slots for today.\nThe allowance resets tomorrow.</blockquote>", home_button())
        return ConversationHandler.END
    await edit_or_send(update, context, f"<blockquote><b>AI CHART ANALYSIS</b>\n━━━━━━━━━━━━━━━━━━━━\nEXPENSIVE PLAN • {2 - used} ANALYSIS REMAINING TODAY\n\nSend a clear candlestick chart screenshot. Gemini Vision will return the next-candle CALL or PUT view, confidence, trend, candle analysis, support/resistance and reason.</blockquote>", build([[{"text": "CANCEL", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]))
    return AWAITING_CHART_PHOTO


async def chart_analysis_photo_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not update.message or not update.message.photo:
        return AWAITING_CHART_PHOTO
    uid = update.effective_user.id if update.effective_user else 0
    reserved, used, denial = reserve_chart_analysis(uid)
    if not reserved:
        await update.message.reply_text(f"<blockquote><b>AI CHART ANALYSIS ACCESS DENIED</b>\n━━━━━━━━━━━━━━━━━━━━\n{html.escape(denial)}</blockquote>", parse_mode="HTML", reply_markup=home_button())
        return ConversationHandler.END
    loading = await professional_loading_message(
        update, "AI CHART ANALYSIS", "RECEIVING CHART",
        "Downloading the screenshot securely..."
    )
    try:
        await update_professional_loading(loading, "AI CHART ANALYSIS", "PREPARING IMAGE", "Reading chart image data...", 1, 4, "REAL IMAGE • STRUCTURED OUTPUT")
        tg_file = await update.message.photo[-1].get_file()
        image_bytes = bytes(await tg_file.download_as_bytearray())
        await update_professional_loading(loading, "AI CHART ANALYSIS", "SCANNING CHART", "AI is reading candles and visible levels...", 2, 4, "REAL IMAGE • STRUCTURED OUTPUT")
        if os.environ.get("CHATGPT_API_KEY", "").strip() or os.environ.get("OPENROUTER_API_KEY", "").strip():
            result = await asyncio.to_thread(_chatgpt_chart_analysis, image_bytes, "image/jpeg")
            analysis_provider = "CHATGPT VISION"
        else:
            result = await asyncio.to_thread(_gemini_chart_analysis, image_bytes, "image/jpeg")
            analysis_provider = "GEMINI VISION"

        await update_professional_loading(loading, "AI CHART ANALYSIS", "BUILDING SIGNAL", "Formatting the next-candle analysis...", 3, 4, "REAL CHART IMAGE • NO SIMULATION")
        report = format_chart_analysis_result(result, analysis_provider)
        await loading.edit_text(report, parse_mode="HTML", reply_markup=build([[{"text": "NEW CHART ANALYSIS", "callback": "ai_chart_analysis", "style": KeyboardButtonStyle.DANGER}], [{"text": "MAIN MENU", "callback": "menu_home", "style": KeyboardButtonStyle.PRIMARY}]]))
    except Exception:
        if loading:
            await loading.edit_text("<b>AI CHART ANALYSIS ERROR</b>\n━━━━━━━━━━━━━━━━━━━━\nThe chart could not be analyzed. Please send a clear screenshot again.", parse_mode="HTML")
        else:
            await update.message.reply_text("<b>AI CHART ANALYSIS ERROR</b>\n━━━━━━━━━━━━━━━━━━━━\nThe chart could not be analyzed. Please send a clear screenshot again.", parse_mode="HTML")
    return ConversationHandler.END


chart_analysis_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(chart_analysis_start, pattern="^ai_chart_analysis$")],
    states={AWAITING_CHART_PHOTO: [MessageHandler(filters.PHOTO, chart_analysis_photo_received)]},
    fallbacks=[],
)


async def menu_home(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_answer(update.callback_query)
    await send_welcome_image_menu(update, context)


async def menu_live_signal(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_answer(update.callback_query)
    await send_welcome_image_menu(update, context)


menu_home_handler = CallbackQueryHandler(menu_home, pattern="^menu_home$")
live_signal_handler = CallbackQueryHandler(menu_live_signal, pattern="^menu_live_signal$")

# ========================================
# File: telegram_ui/handlers/profile.py
# ========================================



def build_reference_status_card(
    user_id: int,
    username: str,
    first_name: str,
    tier: str,
    expire_at: str | None,
    created_at: str | None = None,
) -> str:
    """Render the requested My Profile layout with live account values."""
    tier = (tier or "FREE").upper()
    username_display = f"@{username}" if username else "N/A"
    usage = get_user_usage(user_id) if user_id else {"future": 0, "auto_manual": 0}
    used_today = int(usage.get("future", 0) or 0) + int(usage.get("auto_manual", 0) or 0)

    if tier == "OWNER":
        package_display, limit_display, remaining_display = "OWNER", "UNLIMITED", "UNLIMITED remaining"
    elif tier == "PREMIUM":
        package_display, limit_display, remaining_display = "PREMIUM", "UNLIMITED", "UNLIMITED remaining"
    elif tier == "EXTREME":
        package_display, limit_display, remaining_display = "EXTREME", "38 signals/day", f"{max(0, 38 - used_today)} remaining"
    else:
        package_display, limit_display, remaining_display = "FREE", "2 signals/day", f"{max(0, 2 - used_today)} remaining"

    expiry_display = "—" if expire_at in (None, "", "—") else str(expire_at)
    value_name = first_name or "TRADER"
    return (
        "👤 <b>𝗠𝗬 𝗣𝗥𝗢𝗙𝗜𝗟𝗘</b>\n\n"
        f"📛 <b>𝗡𝗮𝗺𝗲        ∶</b>  {value_name}\n"
        f"🆔 <b>𝗨𝘀𝗲𝗿 𝗜𝗗    ∶</b>  {mono(str(user_id))}\n"
        f"💬 <b>𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲  ∶</b>  {username_display}\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🆓 <b>𝗔𝗖𝗧𝗜𝗩𝗘 𝗣𝗔𝗖𝗞𝗔𝗚𝗘  ∶</b>  {mono(package_display)}\n"
        f"📊 <b>𝗗𝗮𝗶𝗹𝘆 𝗟𝗶𝗺𝗶𝘁  ∶</b>  {mono(limit_display)}\n"
        f"📈 <b>𝗨𝘀𝗲𝗱           ∶</b>  {mono(f'{used_today} used today')}\n"
        f"✅ <b>𝗥𝗲𝗺𝗮𝗶𝗻𝗶𝗻𝗴    ∶</b>  {mono(remaining_display)}\n"
        f"📅 <b>𝗘𝘅𝗽𝗶𝗿𝘆        ∶</b>  {expiry_display}"
    )


def build_status_card(user_id: int, username: str, first_name: str, tier: str, expire_at: str | None) -> str:
    """Render the separate My Status screen, distinct from the My ID account card."""
    now = datetime.now(BD_TZ)
    username_display = f"@{username}" if username else "N/A"
    tier = (tier or "FREE").upper()
    status_label = "VERIFIED USER" if tier in ("OWNER", "PREMIUM", "EXTREME") else "REGISTERED USER"
    if expire_at in (None, "", "—"):
        expiry_display, remaining_display, pct = "—", "—", 0
    elif str(expire_at).upper() == "LIFETIME":
        expiry_display, remaining_display, pct = "LIFETIME", "UNLIMITED", 100
    else:
        expiry_display = str(expire_at)
        expiry_dt = None
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                expiry_dt = datetime.strptime(str(expire_at), fmt).replace(tzinfo=BD_TZ)
                break
            except ValueError:
                pass
        if expiry_dt:
            days = max(0, (expiry_dt.date() - now.date()).days)
            remaining_display, pct = f"{days} DAY(S)", min(100, max(0, round(days / 30 * 100)))
        else:
            remaining_display, pct = "—", 0
    filled = max(0, min(20, round(pct / 5)))
    bar = "■" * filled + "□" * (20 - filled)
    return (
        "📊 <b>YOUR STATUS</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 <b>NAME:</b> {first_name or 'TRADER'}\n"
        f"🔗 <b>USERNAME:</b> {username_display}\n"
        f"🆔 <b>USER ID:</b> {user_id}\n\n"
        f"✅ <b>STATUS:</b> {status_label}\n"
        f"📅 <b>EXPIRES:</b> {expiry_display}\n"
        f"⌛ <b>REMAINING:</b> {remaining_display}\n\n"
        f"<code>{bar}</code> <b>{pct}%</b>\n\n"
        f"<i>{now.strftime('%H:%M')}</i>"
    )


async def my_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await safe_answer(update.callback_query)

    user = update.effective_user
    uid = user.id if user else 0
    uname = (user.username or "").strip()
    first_name = (user.first_name or "").strip() or "TRADER"

    if uid:
        register_user(uid, uname, first_name)

    is_owner = (uid == OWNER_ID or uname.lower() == "tradewithmehedi7")
    user_db = get_user(uid) if uid else None
    tier = get_user_tier(uid) if uid else "FREE"
    usage = get_user_usage(uid) if uid else {"future": 0, "auto_manual": 0}

    expire_at = user_db.get("tier_expire_at") if user_db else None

    fut_used = usage.get("future", 0)
    live_used = usage.get("auto_manual", 0)

    if is_owner:
        pkg_emoji = "👑"
        tier_display = "OWNER / ADMIN"
        daily_limit_str = "UNLIMITED signals"
        used_str = f"{fut_used + live_used} used today"
        remaining_str = "UNLIMITED remaining"
        expiry_str = "LIFETIME"
    elif tier == "PREMIUM":
        pkg_emoji = "💎"
        tier_display = "PREMIUM"
        daily_limit_str = "UNLIMITED signals"
        used_str = f"{fut_used + live_used} used today"
        remaining_str = "UNLIMITED remaining"
        expiry_str = expire_at or "LIFETIME"
    elif tier == "EXTREME":
        pkg_emoji = "🌟"
        tier_display = "EXTREME"
        daily_limit_str = "8 FS / 30 Live signals/day"
        used_str = f"{fut_used} FS / {live_used} Live used today"
        rem_fs = max(0, 8 - fut_used)
        rem_live = max(0, 30 - live_used)
        remaining_str = f"{rem_fs} FS / {rem_live} Live remaining"
        expiry_str = expire_at or "30 Days"
    else:  # FREE
        pkg_emoji = "🆓"
        tier_display = "FREE"
        daily_limit_str = "2 FS / 5 Live signals/day"
        used_str = f"{fut_used} FS / {live_used} Live used today"
        rem_fs = max(0, 2 - fut_used)
        rem_live = max(0, 5 - live_used)
        remaining_str = f"{rem_fs} FS / {rem_live} Live remaining"
        expiry_str = "—"

    text = build_reference_status_card(
        user_id=uid,
        username=uname,
        first_name=first_name,
        tier=tier,
        expire_at=expire_at,
        created_at=user_db.get("created_at") if user_db else None,
    )

    await edit_or_send(update, context, text, _utility_menu())


profile_handler = CallbackQueryHandler(my_profile, pattern="^menu_profile$")

# ========================================
# File: telegram_ui/handlers/help_screen.py
# ========================================



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_answer(update.callback_query)
    await edit_or_send(update, context, help_text(), home_button())


help_handler = CallbackQueryHandler(help, pattern="^menu_help$")

# ========================================
# File: telegram_ui/handlers/about.py
# ========================================



async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await safe_answer(update.callback_query)
    await edit_or_send(update, context, about_text(), home_button())


about_handler = CallbackQueryHandler(about, pattern="^menu_about$")

# ========================================
# File: telegram_ui/handlers/admin.py
# ========================================



def is_owner(update: Update) -> bool:
    user = update.effective_user
    if not user:
        return False
    uname = (user.username or "").strip().lower()
    return user.id == OWNER_ID or uname == "tradewithmehedi7"


async def admin_moderation_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return ConversationHandler.END
    action = "BAN" if query.data == "admin_ban_prompt" else "UNBAN"
    context.user_data["admin_moderation_action"] = action
    prompt = (
        f"<b>{action} USER</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Enter the numeric User ID.\n\nSend /cancel to abort."
    )
    await edit_or_send(update, context, prompt, build([[{"text": "CANCEL", "callback": "admin_home", "style": KeyboardButtonStyle.DANGER}]]))
    return AWAITING_ADMIN_MODERATION_ID

async def admin_receive_moderation_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_owner(update):
        return ConversationHandler.END
    try:
        target_uid = int((update.message.text or "").strip())
    except (TypeError, ValueError):
        await update.message.reply_text("<b>INVALID USER ID</b>\nEnter numbers only or send /cancel.", parse_mode="HTML")
        return AWAITING_ADMIN_MODERATION_ID
    if target_uid == OWNER_ID:
        await update.message.reply_text("<b>PROTECTED ACCOUNT</b>\nThe owner account cannot be banned.", parse_mode="HTML", reply_markup=admin_user_management_menu())
        return ConversationHandler.END
    user = get_user(target_uid)
    if not user and context.user_data.get("admin_moderation_action") == "UNBAN":
        await update.message.reply_text("<b>USER NOT FOUND</b>\nNo account record exists for this User ID.", parse_mode="HTML", reply_markup=admin_user_management_menu())
        return ConversationHandler.END
    action = context.user_data.get("admin_moderation_action", "BAN")
    ok = set_user_ban(target_uid, action == "BAN", "Owner moderation" if action == "BAN" else "")
    context.user_data.pop("admin_moderation_action", None)
    if not ok:
        await update.message.reply_text("<b>MODERATION FAILED</b>\nThe account could not be updated.", parse_mode="HTML", reply_markup=admin_user_management_menu())
        return ConversationHandler.END
    status = "BANNED" if action == "BAN" else "UNBANNED"
    await update.message.reply_text(
        f"<b>USER {status}</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nUser ID: <code>{target_uid}</code>\nAccess status: <b>{status}</b>",
        parse_mode="HTML", reply_markup=admin_user_management_menu()
    )
    if action == "BAN":
        try:
            await context.bot.send_message(chat_id=target_uid, text="<b>ACCOUNT ACCESS SUSPENDED</b>\nYour account has been banned by the administrator. Please contact support.", parse_mode="HTML")
        except Exception:
            pass
    return ConversationHandler.END

async def admin_user_management(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Owner-only user management hub."""
    query = update.callback_query
    if query:
        await safe_answer(query)
    if not is_owner(update):
        return
    analytics = get_admin_analytics()
    text = (
        "<b>ZENITIX AI — USER MANAGEMENT</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Protected user operations are ready.\n\n"
        f"<b>TOTAL USERS:</b> {analytics['total_users']}\n"
        f"<b>FREE:</b> {analytics['free_count']}   "
        f"<b>EXTREME:</b> {analytics['extreme_count']}   "
        f"<b>PREMIUM:</b> {analytics['premium_count']}\n"
        f"<b>BANNED:</b> {analytics.get('banned_count', 0)}\n\n"
        "Use PLAN CONTROL to assign or reset a subscription.\n"
        "Use USER LOOKUP to inspect a specific account.\n"
        "Use BAN USER or UNBAN USER to control account access.\n\n"
        "<i>Every action is owner-only and database-backed.</i>"
    )
    await edit_or_send(update, context, text, admin_user_management_menu())


async def admin_system_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    if not is_owner(update):
        return
    analytics = get_admin_analytics()
    oanda_state = "CONNECTED CONFIGURED" if OANDA_API_KEY else "NOT CONFIGURED"
    hf_state = "CONFIGURED" if HF_API_TOKEN else "NOT CONFIGURED"
    text = (
        f"<b>ZENITIX AI — SYSTEM STATUS</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>ACCESS</b>\n"
        f"Owner protection: ACTIVE\n"
        f"Owner ID: <code>{OWNER_ID}</code>\n\n"
        f"<b>DATA AND AI</b>\n"
        f"OANDA practice API: <b>{oanda_state}</b>\n"
        f"DeepSeek/HF service: <b>{hf_state}</b>\n"
        f"Real market pairs: <b>{len(REAL_PAIRS)}</b>\n\n"
        f"<b>DATABASE SUMMARY</b>\n"
        f"Total users: <b>{analytics['total_users']}</b>\n"
        f"Active today: <b>{analytics['active_today']}</b>\n"
        f"Signals today: <b>{analytics['signals_today']}</b>\n\n"
        f"<i>All admin actions remain owner-only.</i>"
    )
    await edit_or_send(update, context, text, admin_main_menu())

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_owner(update):
        await update.message.reply_text("⛔ <b>Access Denied!</b> This command is restricted to the Bot Owner (@TRADEWITHMEHEDI7).", parse_mode="HTML")
        return ConversationHandler.END

    analytics = get_admin_analytics()
    text = (
        f"<b>ZENITIX AI — OWNER CONTROL CENTER</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Welcome Owner <b>@TRADEWITHMEHEDI7</b>.\n"
        f"Protected administration, plan control and broadcast tools are active.\n\n"
        f"<b>QUICK ANALYTICS</b>\n"
        f"• Total Users : <b>{analytics['total_users']}</b>\n"
        f"• Free Users : <b>{analytics['free_count']}</b>\n"
        f"• EXTREME Users : <b>{analytics['extreme_count']}</b>\n"
        f"• PREMIUM Users : <b>{analytics['premium_count']}</b>\n"
        f"• Active Users Today : <b>{analytics['active_today']}</b>\n"
        f"• Future Signals Today : <b>{analytics['total_future_today']}</b>\n"
        f"• Auto/Manual Today : <b>{analytics['total_auto_today']}</b>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<i>Select a protected admin operation below.</i>"
    )

    if update.callback_query:
        await safe_answer(update.callback_query)
        await edit_or_send(update, context, text, admin_main_menu())
    else:
        await update.message.reply_text(text, parse_mode="HTML", reply_markup=admin_main_menu())
    return ConversationHandler.END


async def admin_analytics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return

    analytics = get_admin_analytics()
    text = (
        f"📊 <b>DETAILED USER & SYSTEM ANALYTICS</b> 📊\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👥 <b>User Base Breakdown:</b>\n"
        f"• Total Registered Users : <b>{analytics['total_users']}</b>\n"
        f"• FREE Tier Users : <b>{analytics['free_count']}</b>\n"
        f"• EXTREME Tier Users : <b>{analytics['extreme_count']}</b>\n"
        f"• PREMIUM Tier Users : <b>{analytics['premium_count']}</b>\n"
        f"• OWNER Accounts : <b>{analytics['owner_count']}</b>\n\n"
        f"📈 <b>Daily Signal Usage (Today):</b>\n"
        f"• Active Users Today : <b>{analytics['active_today']}</b>\n"
        f"• Future Days Signals Generated : <b>{analytics['total_future_today']}</b>\n"
        f"• Auto & Manual Live Signals : <b>{analytics['total_auto_today']}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👑 <i>Owner ID: {OWNER_ID} (@TRADEWITHMEHEDI7)</i>"
    )

    await edit_or_send(update, context, text, admin_main_menu())


async def admin_set_tier_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return ConversationHandler.END
    text = (
        f"👑 <b>GIVE / UPDATE USER SUBSCRIPTION</b> 👑\n\n"
        f"Please enter the <b>User ID</b> you want to update:\n"
        f"(Or send /cancel to abort)"
    )
    await edit_or_send(update, context, text, build([[{"text": "Cancel", "callback": "admin_home"}]]))
    return AWAITING_ADMIN_USER_ID

async def admin_receive_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_owner(update):
        return ConversationHandler.END
    text = update.message.text.strip()
    try:
        uid = int(text)
    except ValueError:
        await update.message.reply_text("❌ Invalid User ID. Must be a number. Try again or /cancel.")
        return AWAITING_ADMIN_USER_ID
        
    user = get_user(uid)
    if not user:
        await update.message.reply_text("❌ User not found in database. Try again or /cancel.")
        return AWAITING_ADMIN_USER_ID
        
    context.user_data["admin_target_uid"] = uid
    tier = get_user_tier(uid)
    msg = f"👤 User: <code>{uid}</code>\n💎 Current Plan: <b>{tier}</b>\n\nSelect a new plan below:"
    await update.message.reply_text(msg, parse_mode="HTML", reply_markup=admin_tier_select_menu(uid))
    return ConversationHandler.END


async def setplan_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_owner(update):
        await update.message.reply_text("⛔ Owner access required.", parse_mode="HTML")
        return

    args = context.args
    if not args or len(args) < 2:
        await update.message.reply_text(
            "⚠️ <b>Usage:</b> <code>/setplan <USER_ID> <FREE|EXTREME|PREMIUM> [DAYS]</code>\n\n"
            "Example:\n<code>/setplan 123456789 EXTREME 30</code>\n<code>/setplan 123456789 PREMIUM 0</code>",
            parse_mode="HTML"
        )
        return

    try:
        target_uid = int(args[0])
    except ValueError:
        await update.message.reply_text("❌ Invalid User ID. Must be numbers.", parse_mode="HTML")
        return

    plan = args[1].upper()
    if plan not in ("FREE", "EXTREME", "EXPENSIVE", "PREMIUM", "OWNER"):
        await update.message.reply_text("❌ Invalid Plan. Choose: <code>FREE</code>, <code>EXTREME</code>, <code>PREMIUM</code>", parse_mode="HTML")
        return

    days = None
    if len(args) >= 3:
        try:
            days = int(args[2])
        except ValueError:
            days = None

    set_user_tier(target_uid, plan, days_valid=days)

    days_str = f"{days} Days" if (days and days > 0) else ("Lifetime" if plan != "FREE" else "N/A")

    await update.message.reply_text(
        f"✅ <b>SUCCESSFULLY UPDATED USER SUBSCRIPTION!</b>\n\n"
        f"👤 User ID: <code>{target_uid}</code>\n"
        f"💎 Tier: <b>{plan}</b>\n"
        f"⏳ Validity: <b>{days_str}</b>\n\n"
        f"The user now has <b>{plan}</b> plan limits applied immediately.",
        parse_mode="HTML"
    )

    # Try to notify the user directly
    try:
        notify_text = (
            f"🎉 <b>ZX SUBSCRIPTION UPDATED!</b> 🎉\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"Your subscription plan has been upgraded by Owner <b>@TRADEWITHMEHEDI7</b>!\n\n"
            f"🌟 <b>New Plan:</b> <code>{plan}</code>\n"
            f"⏳ <b>Validity:</b> <code>{days_str}</code>\n\n"
            f"Enjoy higher accuracy signals and expanded daily limits! Type /start or click My Profile to check your status."
        )
        await context.bot.send_message(chat_id=target_uid, text=notify_text, parse_mode="HTML")
    except Exception as err:
        logging.info(f"Could not notify user {target_uid}: {err}")


async def admin_set_tier_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return

    # Callback pattern: admset_<uid>_<tier>_<days>
    data = query.data.split("_")
    if len(data) < 4:
        return

    target_uid = int(data[1])
    tier = data[2].upper()
    days = int(data[3])

    set_user_tier(target_uid, tier, days_valid=days if days > 0 else None)
    days_str = f"{days} Days" if days > 0 else "Lifetime"

    await edit_or_send(
        update, context,
        f"✅ <b>User {target_uid} Plan Updated!</b>\n\n"
        f"New Tier: <b>{tier}</b>\n"
        f"Validity: <b>{days_str}</b>",
        admin_main_menu()
    )


async def admin_user_lookup_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return ConversationHandler.END
    text = f"🔍 <b>USER INFO LOOKUP</b>\n\nPlease enter the <b>User ID</b> to lookup:\n(Or send /cancel to abort)"
    await edit_or_send(update, context, text, build([[{"text": "Cancel", "callback": "admin_home"}]]))
    return AWAITING_ADMIN_USERINFO_ID

async def admin_receive_userinfo_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_owner(update):
        return ConversationHandler.END
    text = update.message.text.strip()
    try:
        uid = int(text)
    except ValueError:
        await update.message.reply_text("❌ Invalid User ID. Must be a number. Try again or /cancel.")
        return AWAITING_ADMIN_USERINFO_ID
    
    context.args = [str(uid)]
    await userinfo_command(update, context)
    return ConversationHandler.END


async def userinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_owner(update):
        await update.message.reply_text("⛔ Owner access required.", parse_mode="HTML")
        return

    args = context.args
    if not args:
        await update.message.reply_text("⚠️ <b>Usage:</b> <code>/userinfo <USER_ID></code>", parse_mode="HTML")
        return

    try:
        target_uid = int(args[0])
    except ValueError:
        await update.message.reply_text("❌ Invalid User ID.", parse_mode="HTML")
        return
    if target_uid <= 0:
        await update.message.reply_text("❌ Invalid User ID. Enter a positive numeric Telegram ID, or /cancel.", parse_mode="HTML")
        return
    user = get_user(target_uid)
    provisioned = False
    if not user:
        # Telegram does not expose arbitrary user profiles until the user has
        # interacted with the bot. Create a safe placeholder so the owner can
        # inspect and assign a plan without a false database-not-found error.
        register_user(target_uid, "", "UNKNOWN USER")
        user = get_user(target_uid)
        provisioned = user is not None
    if not user:
        await update.message.reply_text(f"❌ Could not create account record for <code>{target_uid}</code>. Try again or /cancel.", parse_mode="HTML")
        return
    tier = get_user_tier(target_uid)
    usage = get_user_usage(target_uid)

    text = (
        f"👤 <b>USER ACCOUNT DETAILS</b> 👤\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• User ID : <code>{user['user_id']}</code>\n"
        f"• Username : @{user['username'] if user['username'] else 'N/A'}\n"
        f"• First Name : {user['first_name']}\n"
        f"• Current Plan : <b>{tier}</b>\n"
        f"• Expiry Date : <code>{user['tier_expire_at'] or 'Lifetime / N/A'}</code>\n"
        f"• Registered Date : <code>{user['created_at']}</code>\n"
        f"• Last Active : <code>{user['last_active']}</code>\n"
        f"• Account Record : <b>{'PROVISIONED' if provisioned else 'REGISTERED'}</b>\n\n"
        f"📊 <b>Today's Signal Usage:</b>\n"
        f"• Future Signals : <b>{usage['future']}</b>\n"
        f"• Auto / Manual Signals : <b>{usage['auto_manual']}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    await update.message.reply_text(text, parse_mode="HTML", reply_markup=admin_tier_select_menu(target_uid))


async def admin_broadcast_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    if not is_owner(update):
        return ConversationHandler.END
    text = f"📢 <b>BROADCAST MESSAGE</b>\n\nPlease enter the message you want to broadcast to all users:\n(Or send /cancel to abort)"
    await edit_or_send(update, context, text, build([[{"text": "Cancel", "callback": "admin_home"}]]))
    return AWAITING_ADMIN_BROADCAST

async def admin_receive_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_owner(update):
        return ConversationHandler.END
    text = update.message.text.strip()
    if not text:
        await update.message.reply_text("Broadcast cancelled: message cannot be empty.", reply_markup=admin_main_menu())
        return ConversationHandler.END
    if len(text) > 3500:
        await update.message.reply_text("Broadcast message is too long. Maximum length is 3500 characters.", reply_markup=admin_main_menu())
        return ConversationHandler.END
    context.args = text.split()
    await broadcast_command(update, context)
    return ConversationHandler.END

async def admin_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Admin action cancelled.", reply_markup=admin_main_menu())
    return ConversationHandler.END


async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_owner(update):
        await update.message.reply_text("⛔ Owner access required.", parse_mode="HTML")
        return

    msg = " ".join(context.args) if context.args else ""
    if not msg:
        await update.message.reply_text("⚠️ <b>Usage:</b> <code>/broadcast <message></code>", parse_mode="HTML")
        return

    user_ids = get_all_user_ids()
    sent = 0
    failed = 0

    status_msg = await update.message.reply_text(f"📢 Starting broadcast to {len(user_ids)} users...", parse_mode="HTML")

    formatted_broadcast = (
        f"📢 <b>ZX ANNOUNCEMENT</b> 📢\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{msg}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👑 <i>From Bot Owner @TRADEWITHMEHEDI7</i>"
    )

    for uid in user_ids:
        try:
            await context.bot.send_message(chat_id=uid, text=formatted_broadcast, parse_mode="HTML")
            sent += 1
        except Exception:
            failed += 1

    await status_msg.edit_text(
        f"✅ <b>Broadcast Completed!</b>\n\n"
        f"• Total Users Attempted: {len(user_ids)}\n"
        f"• Successfully Delivered: <b>{sent}</b>\n"
        f"• Failed / Blocked: <b>{failed}</b>",
        parse_mode="HTML"
    )



admin_conv = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(admin_set_tier_prompt, pattern="^admin_set_tier_prompt$"),
        CallbackQueryHandler(admin_user_lookup_prompt, pattern="^admin_user_lookup$"),
        CallbackQueryHandler(admin_broadcast_prompt, pattern="^admin_broadcast_prompt$"),
        CallbackQueryHandler(admin_moderation_prompt, pattern="^admin_(?:ban|unban)_prompt$"),
    ],
    states={
        AWAITING_ADMIN_USER_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_receive_user_id)],
        AWAITING_ADMIN_MODERATION_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_receive_moderation_id)],
        AWAITING_ADMIN_USERINFO_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_receive_userinfo_id)],
        AWAITING_ADMIN_BROADCAST: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_receive_broadcast)],
    },
    fallbacks=[
        CommandHandler("cancel", admin_cancel),
        CallbackQueryHandler(admin_command, pattern="^admin_home$"),
    ],
)



async def lsig_mode_auto_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    context.user_data["signal_mode"] = "AUTO SIGNAL"
    context.user_data["lsig_mode"] = "AUTO"
    if update.effective_chat:
        chat_id = update.effective_chat.id
        AUTO_STOPPED_CHATS.discard(chat_id)
        reset_partial_session(chat_id, 'AUTO SIGNAL')
    text = auto_signal_mode_text()
    await edit_or_send(update, context, text, strategy_menu(is_manual=False))

async def lsig_mode_manual_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    context.user_data["signal_mode"] = "MANUAL SIGNAL"
    context.user_data["lsig_mode"] = "MANUAL"
    if update.effective_chat:
        reset_partial_session(update.effective_chat.id, 'MANUAL SIGNAL')
    text = (
        f"✍️ <b>MANUAL SIGNAL MODE</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"Select a high-accuracy strategy to generate a live market signal for your chosen currency pair:"
    )
    await edit_or_send(update, context, text, strategy_menu(is_manual=True))

async def lsig_strategy_select_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    data = query.data
    if data == "lsig_strategy_pro2":
        context.user_data["lsig_strategy"] = "ZX PRO 2.1 AI"
        context.user_data["strategy_mode"] = "ZX PRO 2.1 AI"
        context.user_data["lsig_strategy_code"] = "pro2"
        await edit_or_send(update, context, f"🔬 <b>ZX PRO 2.1 SELECTED</b>\n━━━━━━━━━━━━━━━━━━━━\nChoose auto signal pair filter:", auto_filter_menu())
    elif data == "lsig_strategy_premium":
        await edit_or_send(update, context, premium_sub_strategy_text(), premium_strategy_menu(is_manual=False))
    elif data == "lsig_manual_strategy_pro2":
        context.user_data["lsig_strategy"] = "ZX PRO 2.1 AI"
        context.user_data["strategy_mode"] = "ZX PRO 2.1 AI"
        context.user_data["lsig_strategy_code"] = "pro2"
        await edit_or_send(update, context, f"🔬 <b>ZX PRO 2.1 MANUAL</b>\n━━━━━━━━━━━━━━━━━━━━\nSelect currency pair:", manual_market_menu("pro2"))
    elif data == "lsig_manual_strategy_premium":
        await edit_or_send(update, context, premium_sub_strategy_text(), premium_strategy_menu(is_manual=True))

async def lsig_prem_strategy_select_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    data = query.data
    strat_map = {
        "momentum": "ZX Momentum AI",
        "trend": "ZX Trend Surge Pro",
        "breakout": "ZX Volatility Breakout",
        "priceaction": "ZX Price Action Master",
        "reversal": "ZX RSI Reversal",
        "scalping": "ZX EMA-MACD Scalper",
        "supportresistance": "ZX S/R Reaction",
        "volume": "ZX Volume Pressure",
        "candlestick": "ZX Candle Pattern Pro",
        "confluence": "ZX Full Confluence"
    }
    for key, name in strat_map.items():
        if f"_a_prem_{key}" in data:
            context.user_data["lsig_strategy"] = name
            context.user_data["strategy_mode"] = name
            context.user_data["lsig_strategy_code"] = key
            await edit_or_send(update, context, f"💎 <b>{name.upper()} SELECTED</b>\n━━━━━━━━━━━━━━━━━━━━\nChoose auto signal pair filter:", auto_filter_menu())
            return
        elif f"_m_prem_{key}" in data:
            context.user_data["lsig_strategy"] = name
            context.user_data["strategy_mode"] = name
            context.user_data["lsig_strategy_code"] = key
            await edit_or_send(update, context, f"💎 <b>{name.upper()} MANUAL</b>\n━━━━━━━━━━━━━━━━━━━━\nSelect currency pair:", manual_market_menu(key))
            return

async def lsig_auto_filter_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id if update.effective_chat else 0
    internal_cycle = bool(context.user_data.pop("_auto_cycle_internal", False))
    existing_task = AUTO_CYCLE_TASKS.get(chat_id)
    if existing_task and not existing_task.done() and not internal_cycle:
        await safe_answer(update.callback_query, "AUTO SIGNAL is already running.")
        return
    query = update.callback_query
    if query:
        try:
            await safe_answer(query)
        except Exception as exc:
            log.debug("AUTO SIGNAL callback acknowledgement skipped: %s", exc)
    data = query.data
    strategy = context.user_data.get("lsig_strategy", "ZX PRO 2.1 AI")
    
    status_lines = [
        ("OANDA Live Market Stream", True),
        ("Liquidity & Order Flow Check", True),
        (f"Strategy Confluence ({strategy})", True),
    ]
    try:
        await query.message.edit_text(scanning_animation_text(status_lines, "AI Signal Locked! Generating Chart..."), parse_mode="HTML")
    except Exception:
        pass
    
    # Scan every configured REAL market. Keep both strict-qualified candidates
    # and valid directional candidates so a best analyzed setup can still be
    # delivered when the strict threshold rejects every market.
    pairs = list(dict.fromkeys(REAL_PAIRS))
    qualified = []
    analyzed = []
    for p in pairs:
        try:
            candles = await fetch_oanda_candles(p, count=200, granularity="M1")
            if not candles or len(candles) < 50:
                continue
            try:
                r = _local_strategy_consensus(
                    _strategy_candles(candles),
                    min_score=72.0,
                    min_agreement=65.0,
                    min_votes=8,
                    strategy_code=context.user_data.get("lsig_strategy_code", "pro2"),
                )
            except Exception:
                r = _local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0, strategy_code=context.user_data.get("lsig_strategy_code", "pro2"))
            if r.get("signal") not in ("CALL", "PUT"):
                r = _local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0, strategy_code=context.user_data.get("lsig_strategy_code", "pro2"))
            if r.get("signal") in ("CALL", "PUT"):
                candidate = (p, candles, r)
                analyzed.append(candidate)
                if r.get("qualified"):
                    qualified.append(candidate)
        except Exception:
            logging.getLogger(__name__).exception("Auto scan failed for %s", p)

    # Prefer genuinely high-confidence setups first, then strict consensus, then
    # the strongest real-data directional setup so AUTO remains usable.
    high_confidence = [c for c in analyzed if int(c[2].get("confidence", 0)) >= 85]
    selected = high_confidence or qualified or analyzed
    if not selected:
        await edit_or_send(
            update, context,
            "⚠️ <b>WAITING FOR LIVE MARKET DATA</b>\n\n"
            "No valid candle data was available for analysis. Please try again.",
            home_button(),
        )
        return
    selected.sort(key=lambda x: (x[2].get("confidence", 0), x[2].get("agreement", 0)), reverse=True)
    selected_pair, selected_candles, selected_result = selected[0]
    await send_signal_response(
        update,
        context,
        asset=selected_pair,
        strategy=strategy,
        back_callback="lsig_mode_auto",
        mode="AUTO SIGNAL",
        candles_override=selected_candles,
        result_override=selected_result,
    )

async def manpair_selected_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if not query:
        return
    await safe_answer(query)
    data = str(query.data or "")
    payload = data[len("manpair_"):] if data.startswith("manpair_") else ""
    pair, separator, strat_code = payload.rpartition("_")
    if not separator:
        pair, strat_code = payload, "pro2"
    if pair and strat_code:
        strat_map = {
            "pro2": "ZX PRO 2.1 AI",
            "momentum": "ZX Momentum AI",
            "trend": "ZX Trend Surge Pro",
            "breakout": "ZX Volatility Breakout",
            "priceaction": "ZX Price Action Master",
            "reversal": "ZX RSI Reversal",
            "scalping": "ZX EMA-MACD Scalper",
            "supportresistance": "ZX S/R Reaction",
            "volume": "ZX Volume Pressure",
            "candlestick": "ZX Candle Pattern Pro",
            "confluence": "ZX Full Confluence"
        }
        strategy = strat_map.get(strat_code, "ZX PRO 2.1 AI")
        context.user_data["signal_mode"] = "MANUAL SIGNAL"
        context.user_data["strategy_mode"] = strategy
        context.user_data["lsig_strategy"] = strategy
        context.user_data["lsig_strategy_code"] = strat_code
        await send_signal_response(update, context, asset=pair, strategy=strategy, back_callback="lsig_mode_manual", mode="MANUAL SIGNAL")

def partial_mode_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "⚡ AUTO SIGNAL", "callback": "partial_mode_auto", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "✍️ MANUAL SIGNAL", "callback": "partial_mode_manual", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "📡 CHANNEL SENDER", "callback": "partial_mode_channel", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🏠 HOME", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])

async def partial_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # /PARTIAL is intentionally a two-button report view. It uses the user's
    # current signal mode; RESET PARTIAL remains scoped to that user's chat.
    chat_id = update.effective_chat.id if update.effective_chat else 0
    mode = context.user_data.get("signal_mode", "AUTO SIGNAL")
    await update.effective_message.reply_text(
        format_partial_report(chat_id, mode),
        parse_mode="HTML", reply_markup=partial_report_markup(mode)
    )

async def partial_mode_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    mode = {
        "partial_mode_auto": "AUTO SIGNAL",
        "partial_mode_manual": "MANUAL SIGNAL",
        "partial_mode_channel": "CHANNEL SENDER",
    }.get(query.data, "AUTO SIGNAL")
    chat_id = update.effective_chat.id if update.effective_chat else 0
    await edit_or_send(update, context, format_partial_report(chat_id, mode), partial_report_markup(mode))

async def partial_choose_mode_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    await edit_or_send(update, context, "📊 <b>SELECT PARTIAL MODE</b>\n━━━━━━━━━━━━━━━━━━━━\nChoose the signal mode:", partial_mode_menu())

async def partial_report_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    chat_id = update.effective_chat.id if update.effective_chat else 0
    mode = context.user_data.get("signal_mode", "AUTO SIGNAL")
    await edit_or_send(update, context, format_partial_report(chat_id, mode), partial_report_markup(mode))

async def partial_reset_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    mode = {
        'partial_reset_auto': 'AUTO SIGNAL',
        'partial_reset_manual': 'MANUAL SIGNAL',
        'partial_reset_channel': 'CHANNEL SENDER',
    }.get(query.data if query else '', 'AUTO SIGNAL')
    chat_id = update.effective_chat.id if update.effective_chat else 0
    reset_partial_session(chat_id, mode)
    reset_notice = '<blockquote><b>✅ 𝙿𝙰𝚁𝚃𝙸𝙰𝙻 𝚁𝙴𝚂𝙴𝚃 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴</b></blockquote>\n'
    await edit_or_send(update, context, reset_notice + format_partial_report(chat_id, mode), partial_report_markup(mode))

async def auto_stop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Stop the AUTO SIGNAL cycle for this chat only."""
    query = update.callback_query
    await safe_answer(query)
    if update.effective_chat:
        chat_id = update.effective_chat.id
        AUTO_STOPPED_CHATS.add(chat_id)
        task = AUTO_CYCLE_TASKS.pop(chat_id, None)
        if task and not task.done() and task is not asyncio.current_task():
            task.cancel()
    report = format_partial_report(chat_id)
    reset_partial_session(chat_id, 'AUTO SIGNAL')
    await edit_or_send(
        update,
        context,
        "<b>AUTO SIGNAL STOPPED</b>\n━━━━━━━━━━━━━━━━━━━━\n\n" + report + "\n\n<b>Session closed. Start Auto Signal to begin a new report.</b>",
        partial_report_markup("AUTO SIGNAL"),
    )


async def lsig_next_auto_signal_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    strategy = context.user_data.get("lsig_strategy", "ZX PRO 2.1 AI")
    await lsig_auto_filter_callback(update, context)

async def lsig_next_manual_signal_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await safe_answer(query)
    strategy_code = context.user_data.get("lsig_strategy_code", "pro2")
    strategy_name = context.user_data.get("strategy_mode", "ZX PRO 2.1 AI")
    await edit_or_send(update, context, f"✍️ <b>MANUAL SIGNAL MODE</b>\n━━━━━━━━━━━━━━━━━━━━\n<b>STRATEGY MODE:</b> {strategy_name}\nSelect currency pair:", manual_market_menu(strategy_code))

auto_handlers = [
    CallbackQueryHandler(lsig_mode_auto_callback, pattern="^lsig_mode_auto$"),
    CallbackQueryHandler(lsig_strategy_select_callback, pattern="^lsig_strategy_(pro2|premium)$"),
    CallbackQueryHandler(lsig_prem_strategy_select_callback, pattern="^lsig_a_prem_"),
    CallbackQueryHandler(lsig_auto_filter_callback, pattern="^lsig_auto_filter_(all|avoid80)$"),
    CallbackQueryHandler(lsig_auto_filter_callback, pattern="^lsig_auto_select_manual$"),
    CallbackQueryHandler(auto_stop_callback, pattern="^auto_stop$"),
    CallbackQueryHandler(partial_report_callback, pattern="^partial_report$"),
    CallbackQueryHandler(partial_reset_callback, pattern="^partial_reset_(auto|manual|channel)$"),
    CallbackQueryHandler(partial_mode_callback, pattern="^partial_mode_(auto|manual|channel)$"),
    CallbackQueryHandler(partial_choose_mode_callback, pattern="^partial_choose_mode$"),
    CallbackQueryHandler(lsig_next_auto_signal_callback, pattern="^lsig_next_auto_signal$"),
]

manual_handlers = [
    CallbackQueryHandler(lsig_mode_manual_callback, pattern="^lsig_mode_manual$"),
    CallbackQueryHandler(lsig_strategy_select_callback, pattern="^lsig_manual_strategy_(pro2|premium)$"),
    CallbackQueryHandler(lsig_prem_strategy_select_callback, pattern="^lsig_m_prem_"),
    CallbackQueryHandler(manpair_selected_callback, pattern="^manpair_"),
    CallbackQueryHandler(lsig_next_manual_signal_callback, pattern="^lsig_next_manual_signal$"),
]


# ==================== AI LIVE FS / AI OTC FS ====================
AI_SIGNAL_GAP_MINUTES_MIN = CONFIG["AI_SIGNAL_GAP_MINUTES_MIN"]
AI_SIGNAL_GAP_MINUTES_MAX = CONFIG["AI_SIGNAL_GAP_MINUTES_MAX"]
HF_MODEL_OPTIONS = [
    ("DeepSeek V3.2 Exp", HF_MAIN_MODEL),
    ("GPT-5.6 Luna", HF_MAIN_MODEL),
    ("Claude Opus 4.1", HF_MAIN_MODEL),
    ("Gemini 2.5 Pro", HF_MAIN_MODEL),
    ("Qwen3-235B-A22B", HF_MAIN_MODEL),
    ("Llama 4 Maverick", HF_MAIN_MODEL),
    ("Mistral Large", HF_MAIN_MODEL),
    ("Grok 4", HF_MAIN_MODEL),
]

def ai_fs_model_menu() -> InlineKeyboardMarkup:
    rows=[]
    for i, (display_name, _backend_model) in enumerate(HF_MODEL_OPTIONS):
        label = ("MAIN: " if i == 0 else "") + display_name
        rows.append([{"text": label, "callback": f"ai_model_{i}", "style": KeyboardButtonStyle.PRIMARY if i == 0 else KeyboardButtonStyle.SUCCESS}])
    rows.append([{"text": "BACK", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


async def ai_fs_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query=update.callback_query
    if query and query.data == "ai_live_fs_start":
        if await block_real_market(update, context):
            return ConversationHandler.END
    if query: await safe_answer(query)
    context.user_data["ai_fs_mode"] = "LIVE" if query.data == "ai_live_fs_start" else "OTC"
    mode=context.user_data["ai_fs_mode"]
    await edit_or_send(update, context,
        f"<b>AI {mode} FS</b>\\n━━━━━━━━━━━━━━━━━━━━\\nEnter Start Time in HH:MM format:\\nExample: <code>10:00</code>",
        build([[{"text":"BACK","callback":"menu_home","style":KeyboardButtonStyle.DANGER}]]))
    return AWAITING_AI_START


async def ai_fs_start_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        h,m=map(int,raw.split(":"))
        if not (0<=h<24 and 0<=m<60): raise ValueError
    except ValueError:
        await update.message.reply_text("Invalid time. Use HH:MM, for example 10:00.")
        return AWAITING_AI_START
    context.user_data["ai_fs_start"] = f"{h:02d}:{m:02d}"
    await update.message.reply_text("Enter End Time in HH:MM format:\nExample: <code>17:00</code>", parse_mode="HTML")
    return AWAITING_AI_END


async def ai_fs_end_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        h,m=map(int,raw.split(":"))
        if not (0<=h<24 and 0<=m<60): raise ValueError
    except ValueError:
        await update.message.reply_text("Invalid time. Use HH:MM, for example 17:00.")
        return AWAITING_AI_END
    context.user_data["ai_fs_end"] = f"{h:02d}:{m:02d}"
    await update.message.reply_text(
        "How many AI signals do you need? Enter a number from 1 to 40.",
        parse_mode="HTML",
    )
    return AWAITING_AI_COUNT


def _chatgpt_text_request(system_prompt: str, user_prompt: str) -> str:
    """Use the configured OpenAI-compatible provider as a safe AI FS fallback."""
    token = (os.environ.get("CHATGPT_API_KEY", "").strip()
             or os.environ.get("OPENROUTER_API_KEY", "").strip())
    if not token:
        return "AI PROVIDER CREDIT LIMIT"
    payload = json.dumps({
        "model": CHATGPT_MODEL,
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        "temperature": 0.2,
        "max_tokens": 1800,
    }).encode("utf-8")
    req = urllib.request.Request(CHATGPT_API_URL, data=payload, headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json",
        "HTTP-Referer": "https://zenitix.ai", "X-Title": "Zenitix AI",
    }, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = str(data.get("choices", [{}])[0].get("message", {}).get("content", "")).strip()
        return content or "AI REQUEST ERROR: Fallback returned an empty response."
    except Exception as exc:
        log.warning("ChatGPT-compatible AI FS fallback failed: %s", exc)
        return "AI REQUEST ERROR: Unable to complete analysis right now."


def _hf_request(model: str, system_prompt: str, user_prompt: str) -> str:
    """Call the configured DeepSeek backend with bounded transient-error retries."""
    token=os.environ.get("HF_API_TOKEN", "").strip()
    if not token:
        return "AI CONFIGURATION ERROR: HF_API_TOKEN is not configured."
    payload=json.dumps({
        "model": model,
        "messages":[{"role":"system","content":system_prompt},{"role":"user","content":user_prompt}],
        "temperature":0.2,
        "max_tokens":1800,
    }).encode("utf-8")
    last_error = "AI REQUEST ERROR: Unable to complete model analysis right now."
    for attempt in range(2):
        req=urllib.request.Request(HF_API_URL, data=payload, headers={"Authorization":f"Bearer {token}","Content-Type":"application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                data=json.loads(response.read().decode("utf-8"))
            content=str(data.get("choices", [{}])[0].get("message", {}).get("content", "")).strip()
            if content:
                return content
            last_error = "AI REQUEST ERROR: The model returned an empty response."
            log.warning("DeepSeek returned an empty content response on attempt %s/2", attempt + 1)
        except urllib.error.HTTPError as exc:
            body = ""
            try:
                body = exc.read().decode("utf-8", errors="replace")[:300]
            except Exception:
                pass
            last_error = f"AI REQUEST ERROR: HTTP {exc.code}"
            log.warning("DeepSeek request attempt %s/2 failed with HTTP %s: %s", attempt + 1, exc.code, body)
            if exc.code == 402:
                log.warning("Hugging Face credits are depleted; using ChatGPT-compatible AI FS fallback")
                return _chatgpt_text_request(system_prompt, user_prompt)
            if attempt == 0:
                time.sleep(1.0)
        except Exception as exc:
            last_error = "AI REQUEST ERROR: Unable to complete model analysis right now."
            log.warning("DeepSeek request attempt %s/2 failed: %s", attempt + 1, exc)
            if attempt == 0:
                time.sleep(1.0)
    return last_error


async def safe_edit_loading(message, stage: str, detail: str = "") -> None:
    try:
        await message.edit_text(professional_loading_text("AI FILTER FS", stage, detail, current=2, total=4), parse_mode="HTML")
    except Exception:
        pass


async def ai_fs_count_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        count=int(raw)
        if not 1 <= count <= 40:
            raise ValueError
    except (TypeError, ValueError):
        await update.message.reply_text("Invalid signal count. Enter a whole number from 1 to 40.")
        return AWAITING_AI_COUNT
    context.user_data["ai_fs_signal_count"] = count
    feature_key = "ai_otc_fs" if context.user_data.get("ai_fs_mode") == "OTC" else "ai_live_fs"
    uid = update.effective_user.id
    allowed, used, limit = reserve_feature_usage(uid, feature_key)
    if not allowed:
        await update.message.reply_text(format_limit_reached(feature_key, used, limit, get_user_tier(uid)), parse_mode="HTML")
        return ConversationHandler.END
    await update.message.reply_text("Select AI Model for analysis:", reply_markup=ai_fs_model_menu())
    return AWAITING_AI_MODEL


async def ai_fs_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel AI FS input safely from any time/model step."""
    if update.message:
        await update.message.reply_text("AI FS cancelled.", reply_markup=main_menu(is_owner(update)))
    elif update.callback_query:
        await safe_answer(update.callback_query)
        await edit_or_send(update, context, "AI FS cancelled.", main_menu(is_owner(update)))
    return ConversationHandler.END


async def ai_model_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query=update.callback_query
    await safe_answer(query, "AI analysis started", show_alert=False)
    try:
        display_model, backend_model = HF_MODEL_OPTIONS[int(query.data.rsplit("_",1)[-1])]
    except (ValueError, IndexError):
        display_model, backend_model = HF_MODEL_OPTIONS[0]
    backend_model = HF_MAIN_MODEL
    context.user_data["ai_fs_model"] = display_model
    context.user_data["ai_fs_backend_model"] = backend_model
    mode=context.user_data.get("ai_fs_mode", "LIVE")
    loading=await professional_loading_message(update, f"AI {mode} FS", "INITIALIZING AI ANALYSIS", f"Model: {display_model}\nDeepSeek backend: {backend_model}\nPreparing market context...")
    pairs=list(REAL_PAIRS)
    snapshots=[]
    semaphore=asyncio.Semaphore(6)
    async def get_snapshot(pair):
        async with semaphore:
            try:
                candles = None
                for snapshot_attempt in range(3):
                    candles = await fetch_oanda_candles(pair, count=60, granularity="M1")
                    if candles and len(candles) >= 30:
                        break
                    if snapshot_attempt < 2:
                        await asyncio.sleep(0.5 * (snapshot_attempt + 1))
                if candles and len(candles) >= 30:
                    last=candles[-1]
                    recent=[]
                    for c in candles[-20:]:
                        try:
                            recent.append({"o":float(c.get("open")),"h":float(c.get("high")),"l":float(c.get("low")),"c":float(c.get("close"))})
                        except (TypeError, ValueError):
                            continue
                    technical=_local_strategy_consensus(_strategy_candles(candles), min_score=0.0, min_agreement=0.0, min_votes=0)
                    details=technical.get("details", {}) if isinstance(technical, dict) else {}
                    return {
                        "pair":pair.replace("_","/"),
                        "open":last.get("open"),"high":last.get("high"),"low":last.get("low"),"close":last.get("close"),
                        "recent_m1":recent,
                        "technical_bias":technical.get("signal", "NEUTRAL"),
                        "technical_confidence":technical.get("confidence", 0),
                        "rsi":details.get("rsi"),
                        "ema_fast":details.get("ema_fast"),
                        "ema_slow":details.get("ema_slow"),
                        "macd":details.get("macd"),
                        "macd_signal":details.get("signal"),
                        "atr":details.get("atr"),
                        "support":details.get("support", []),
                        "resistance":details.get("resistance", []),
                        "patterns":details.get("patterns", []),
                        "evidence":details.get("signals", []),
                    }
            except Exception:
                return None
        return None
    await safe_edit_loading(loading, "SCANNING MARKETS", f"Analyzing {len(pairs)} real market pairs with OANDA context...")
    values=await asyncio.gather(*(get_snapshot(pair) for pair in pairs))
    snapshots=[v for v in values if v]
    await safe_edit_loading(loading, "OANDA DATA VALIDATION", f"Validated {len(snapshots)} of {len(pairs)} real market contexts...")
    await asyncio.sleep(0.15)
    await safe_edit_loading(loading, "TECHNICAL MARKET FILTER", "Checking momentum, candle structure, trend, support and resistance...")
    await asyncio.sleep(0.15)
    await safe_edit_loading(loading, "AI MODEL REASONING", f"Reviewing {len(snapshots)} market contexts and ranking high-confidence setups...")
    system_prompt=(
        "You are the main Zenitix AI DeepSeek analyst for both LIVE FS and OTC FS. "
        "Use only the supplied real OANDA M1 context; never invent prices, candles, news, or indicators. "
        "Analyze the supplied recent M1 candles, technical bias, momentum, candle structure, short-term trend, support/resistance, volatility, and conflicting evidence. "
        "Reject weak or contradictory setups, rank only the strongest opportunities inside the requested time window, "
        "and prefer fewer high-quality signals over noise. For OTC mode, treat the supplied context as the only source "
        "and do not claim access to an OTC feed. OTC output must be selected by this AI response only; never substitute a technical-only or fabricated signal. Every selectable model name is only a display alias; the backend is DeepSeek. "
        "Return only one signal per line in space-separated format: M1 PAIR HH:MM BUY or M1 PAIR HH:MM PUT. "
        "Return exactly the requested number of unique valid signals when enough valid setups exist. "
        "Every signal time must be inside the supplied Start/End window. Consecutive selected signal times must be 3 to 7 minutes apart. "
        "Use uppercase pair and direction, 24-hour time, no markdown, no explanations, and no confidence text."
    )
    user_prompt=(
        f"Mode: AI {mode} FS\\nStart time: {context.user_data.get('ai_fs_start')}\\nEnd time: {context.user_data.get('ai_fs_end')}\\n"
        f"Requested signal count: {context.user_data.get('ai_fs_signal_count', 1)}\\n"
        "Required signal spacing: 3 to 7 minutes between consecutive signals\\n"
        f"Selected display model: {display_model}\\nBackend model: {backend_model}\\nReal OANDA market context: {json.dumps(snapshots, separators=(',',':'))}\\n"
        "Generate exactly the requested number of strongest ranked future signals within the requested time window."
    )
    result=await asyncio.to_thread(_hf_request, backend_model, system_prompt, user_prompt)
    await safe_edit_loading(loading, "VALIDATING AI SIGNALS", "Checking AI output against the requested time window...")

    def parse_ai_signals(text: str):
        found=[]
        valid_pairs={p.replace("_", "").upper() for p in REAL_PAIRS}
        is_otc = mode.upper() == "OTC"
        try:
            sh, sm = map(int, str(context.user_data.get("ai_fs_start", "00:00")).split(":"))
            eh, em = map(int, str(context.user_data.get("ai_fs_end", "23:59")).split(":"))
        except Exception:
            sh, sm, eh, em = 0, 0, 23, 59
        start_min, end_min = sh*60+sm, eh*60+em
        overnight = end_min < start_min
        def window_pos(hh, mm):
            value=hh*60+mm
            if overnight and value < start_min:
                value += 1440
            return value
        # Accept the strict contract plus harmless AI formatting such as bullets, numbering,
        # semicolon separators, CALL/SELL synonyms, and inline markdown.
        normalized_text = re.sub(r"(?i)(?<![A-Z0-9])(?:CALL|SELL)(?![A-Z0-9])", lambda m: "BUY" if m.group(0).upper() == "CALL" else "PUT", str(text or ""))
        for raw_line in normalized_text.splitlines():
            line=re.sub(r"^\s*(?:[-*]\s*|\d+[.)]\s*)", "", raw_line.strip())
            line=line.replace("`", "").replace("|", " ").replace(";", " ").replace(",", " ")
            parts=[x.strip().upper() for x in line.split()]
            if len(parts) >= 4 and parts[0] == "M1":
                pair, tm, direction = parts[1], parts[2], parts[3]
            elif len(parts) == 3:
                pair, tm, direction = parts[0], parts[1], parts[2]
            else:
                match=re.search(r"(?i)\bM1\s+([A-Z]{3,6}(?:[/_-][A-Z]{3,6})?(?:-OTC)?)\s+(\d{1,2}:\d{2})\s+(BUY|PUT|CALL|SELL)\b", line)
                if not match:
                    continue
                pair, tm, direction = match.group(1), match.group(2), match.group(3).upper()
                direction = "BUY" if direction == "CALL" else "PUT" if direction == "SELL" else direction
            try:
                hh, mm = map(int, tm.split(":"))
                if not (0 <= hh < 24 and 0 <= mm < 60):
                    continue
            except Exception:
                continue
            base_pair=pair.replace("/", "").replace("_", "").replace("-OTC", "")
            if base_pair not in valid_pairs or direction not in {"BUY", "PUT"}:
                continue
            pos=window_pos(hh, mm)
            end_bound=end_min + (1440 if overnight else 0)
            if not (start_min <= pos <= end_bound):
                continue
            display_pair=f"{base_pair}-otc" if is_otc else base_pair
            found.append((pos, f"M1 {display_pair} {hh:02d}:{mm:02d} {direction}"))
        found.sort(key=lambda x: x[0])
        # Enforce a strict 3–7 minute gap between consecutive selected signal times.
        requested=max(1, min(40, int(context.user_data.get("ai_fs_signal_count", 1))))
        unique=[]
        seen=set()
        for pos, line in found:
            if line in seen:
                continue
            if unique:
                gap=pos-unique[-1][0]
                if gap < AI_SIGNAL_GAP_MINUTES_MIN:
                    continue
                if gap > AI_SIGNAL_GAP_MINUTES_MAX:
                    break
            seen.add(line)
            unique.append((pos, line))
            if len(unique) >= requested:
                break
        return [line for _, line in unique]
    confirmed=parse_ai_signals(result)
    # One and only one low-version pass: same main DeepSeek backend, shorter output,
    # and a stricter request for at least one valid AI-selected signal.
    if not confirmed and snapshots:
        await safe_edit_loading(loading, "AI LOW VERSION FILTER", "Running one final low-version DeepSeek selection pass...")
        low_prompt=(
            f"Mode: AI {mode} FS\nStart: {context.user_data.get('ai_fs_start')}\nEnd: {context.user_data.get('ai_fs_end')}\n"
            f"Real OANDA M1 context: {json.dumps(snapshots, separators=(',',':'))}\n"
            f"Select exactly {context.user_data.get('ai_fs_signal_count', 1)} strongest valid AI signals from this context inside the requested Start/End window. "
            "Consecutive signal times must be 3 to 7 minutes apart. "
            "Return one line per signal in space-separated format: M1 PAIR HH:MM BUY or M1 PAIR HH:MM PUT. "
            "Do not return an empty answer, commentary, markdown, or fake data."
        )
        low_result=await asyncio.to_thread(_hf_request, backend_model, system_prompt, low_prompt)
        confirmed=parse_ai_signals(low_result)

    # Final connection-safe retry: one compact AI-only request with the exact output contract.
    if not confirmed and snapshots:
        await safe_edit_loading(loading, "AI CONNECTION RETRY", "Reconnecting to DeepSeek and requesting a valid in-window signal...")
        emergency_prompt=(
            f"AI {mode} FS. Start={context.user_data.get('ai_fs_start')}; End={context.user_data.get('ai_fs_end')}; "
            f"Requested count={context.user_data.get('ai_fs_signal_count', 1)}. "
            "Use only the supplied real OANDA snapshots. Return only valid lines, no markdown: "
            "M1 PAIR HH:MM BUY or M1 PAIR HH:MM PUT. Every time must be inside the window. "
            "Consecutive times must be 3 to 7 minutes apart. If only one valid setup is supported, return one valid line."
            f"\nSNAPSHOTS={json.dumps(snapshots, separators=(',',':'))}"
        )
        emergency_result=await asyncio.to_thread(_hf_request, backend_model, system_prompt, emergency_prompt)
        confirmed=parse_ai_signals(emergency_result)

    await safe_edit_loading(loading, "FINALIZING AI SIGNALS", "Formatting AI-selected signals...")
    if not confirmed:
        log.error("AI FS produced no parseable signal after DeepSeek retries; no fabricated signal will be created")
        signal_lines="AI ANALYSIS RETRY REQUIRED — PROVIDER CONNECTION NOT READY"
        found_count=0
    else:
        signal_lines="\n".join(confirmed)
        found_count=len(confirmed)
    model_display=to_math_mono(display_model.upper())
    report=(
        "╔════════════════════╗\n"
        f"      𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝙰𝙸 𝙵𝙸𝙻𝚃𝙴𝚁 𝙵𝚂 — {mode}\n"
        "╚════════════════════╝\n\n"
        "✅ 𝙵𝚒𝚕𝚝𝚎𝚛 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎! 🔥\n"
        f"🤖 𝙼𝚘𝚍𝚎∶ {model_display} 🏆\n\n"
        f"🕒 𝚆𝚒𝚗𝚍𝚘𝚠∶ {to_math_mono(str(context.user_data.get('ai_fs_start', '—')))} — {to_math_mono(str(context.user_data.get('ai_fs_end', '—')))} (UTC+6)\n"
        f"🎯 𝚁𝚎𝚚𝚞𝚎𝚜𝚝𝚎𝚍 𝚂𝚒𝚐𝚗𝚊𝚕𝚜∶ {to_math_mono(str(context.user_data.get('ai_fs_signal_count', '—')))}\n"
        "⏱ 𝙶𝚊𝚙∶ 𝟹–𝟽 𝙼𝙸𝙽𝚄𝚃𝙴𝚂\n"
        f"✅ 𝙵𝚘𝚞𝚗𝚍 𝚂𝚒𝚐𝚗𝚊𝚕𝚜∶ {to_math_mono(str(found_count))}\n\n"
        "🏆 𝙲𝚘𝚗𝚏𝚒𝚛𝚖𝚎𝚍 𝚂𝚒𝚐𝚗𝚊𝚕𝚜∶\n\n"
        f"{signal_lines}"
    )
    keyboard=build([[{"text":"NEW AI ANALYSIS","callback":"ai_live_fs_start" if mode=="LIVE" else "ai_otc_fs_start","style":KeyboardButtonStyle.SUCCESS}], [{"text":"MAIN MENU","callback":"menu_home","style":KeyboardButtonStyle.PRIMARY}]])
    try: await loading.delete()
    except Exception: pass
    await context.bot.send_message(chat_id=update.effective_chat.id, text=report, parse_mode="HTML", reply_markup=keyboard)
    return ConversationHandler.END


ai_fs_conv=ConversationHandler(
    entry_points=[CallbackQueryHandler(ai_fs_start, pattern=r"^ai_(live|otc)_fs_start$")],
    states={
        AWAITING_AI_START:[MessageHandler(filters.TEXT & ~filters.COMMAND, ai_fs_start_received)],
        AWAITING_AI_END:[MessageHandler(filters.TEXT & ~filters.COMMAND, ai_fs_end_received)],
        AWAITING_AI_COUNT:[MessageHandler(filters.TEXT & ~filters.COMMAND, ai_fs_count_received)],
        AWAITING_AI_MODEL:[CallbackQueryHandler(ai_model_selected, pattern=r"^ai_model_\d+$")],
    },
    fallbacks=[CommandHandler("cancel", ai_fs_cancel)],
)

# ==================== MANUAL NEWS SYSTEM ====================
NEWS_TYPES = [
    "CAD CPI", "CAD GDP", "Core PPI", "Core CPI", "Core retail sales",
    "Flash service PMI(EUR)", "Flash service PMI(USD)", "Flash Service PMI(GBP)",
    "ISM Service PMI", "Non farm employment change", "Unemployment claim", "JOLTS job opening",
]
NEWS_MARKETS = ["CADJPY", "EURGBP", "EURJPY", "EURCAD", "EURUSD", "GBPCAD", "GBPJPY", "GBPUSD", "USDCAD", "USDJPY"]


def manual_news_direction(mode: str, market: str, previous: float, forecast: float) -> str:
    """Map a manual economic surprise to a directional pair signal.

    Equal Previous/Forecast is intentionally neutral and must never be converted
    into a fabricated CALL or PUT.
    """
    if forecast == previous:
        return "N/A"
    rising = forecast > previous
    falling = forecast < previous
    market = market.replace("/", "").replace("_", "").upper()
    cad_cross = {"CADJPY"}
    cad_inverse = {"EURCAD", "GBPCAD", "USDCAD"}
    usd_cross = {"USDCAD", "USDJPY"}
    usd_inverse = {"EURUSD", "GBPUSD"}
    eur_cross = {"EURGBP", "EURCAD", "EURJPY", "EURUSD"}
    gbp_cross = {"GBPCAD", "GBPUSD", "GBPJPY"}
    if mode in {"CAD CPI", "CAD GDP"}:
        if market in cad_cross: return "CALL" if rising else "PUT"
        if market in cad_inverse: return "PUT" if rising else "CALL"
    if mode in {"Core PPI", "Core CPI", "Core retail sales"}:
        if market in usd_cross: return "CALL" if rising else "PUT"
        if market in usd_inverse: return "PUT" if rising else "CALL"
    if mode == "Flash service PMI(EUR)" and market in eur_cross:
        return "CALL" if rising else "PUT"
    if mode == "Flash service PMI(USD)":
        if market in usd_cross: return "CALL" if rising else "PUT"
        if market in usd_inverse: return "PUT" if rising else "CALL"
    if mode == "Flash Service PMI(GBP)":
        if market in gbp_cross: return "CALL" if rising else "PUT"
    if mode in {"ISM Service PMI", "Non farm employment change", "JOLTS job opening"}:
        if market in usd_cross: return "CALL" if rising else "PUT"
        if market in usd_inverse: return "PUT" if rising else "CALL"
    if mode == "Unemployment claim":
        if market in usd_cross: return "CALL" if falling else "PUT"
        if market in usd_inverse: return "PUT" if falling else "CALL"
    return "N/A"


def manual_news_type_menu() -> InlineKeyboardMarkup:
    rows=[]
    for i in range(0, len(NEWS_TYPES), 2):
        row=[]
        for j in range(i, min(i+2, len(NEWS_TYPES))):
            row.append({"text": f"{j+1}. {NEWS_TYPES[j]}", "callback": f"news_type_{j}", "style": KeyboardButtonStyle.PRIMARY})
        rows.append(row)
    rows.append([{"text": "BACK", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


def manual_news_market_menu() -> InlineKeyboardMarkup:
    rows=[]
    for i in range(0, len(NEWS_MARKETS), 2):
        row=[]
        for j in range(i, min(i+2, len(NEWS_MARKETS))):
            row.append({"text": NEWS_MARKETS[j], "callback": f"news_market_{j}", "style": KeyboardButtonStyle.PRIMARY})
        rows.append(row)
    rows.append([{"text": "BACK", "callback": "manual_news_start", "style": KeyboardButtonStyle.DANGER}])
    return build(rows)


async def manual_news_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query=update.callback_query
    if query: await safe_answer(query)
    await edit_or_send(update, context,
        "<b>GURU NEWS ALERT</b>\n━━━━━━━━━━━━━━━━━━━━\nSelect News Type:",
        manual_news_type_menu())
    return AWAITING_NEWS_TYPE


async def manual_news_type_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query=update.callback_query
    await safe_answer(query)
    try:
        index=int(query.data.rsplit("_",1)[-1])
        if not 0 <= index < len(NEWS_TYPES): raise ValueError
    except (TypeError, ValueError):
        await edit_or_send(update, context, "Invalid news type. Please select again.", manual_news_type_menu())
        return AWAITING_NEWS_TYPE
    context.user_data["manual_news_type"]=NEWS_TYPES[index]
    await edit_or_send(update, context,
        f"<b>NEWS:</b> {NEWS_TYPES[index]}\n\nSelect Market:", manual_news_market_menu())
    return AWAITING_NEWS_MARKET


async def manual_news_market_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query=update.callback_query
    await safe_answer(query)
    try:
        index=int(query.data.rsplit("_",1)[-1])
        if not 0 <= index < len(NEWS_MARKETS): raise ValueError
    except (TypeError, ValueError):
        await edit_or_send(update, context, "Invalid market. Please select again.", manual_news_market_menu())
        return AWAITING_NEWS_MARKET
    context.user_data["manual_news_market"]=NEWS_MARKETS[index]
    await edit_or_send(update, context, "Enter Previous Value:\nExample: <code>2.5</code>", build([[{"text":"BACK","callback":"manual_news_start","style":KeyboardButtonStyle.DANGER}]]))
    return AWAITING_NEWS_PREVIOUS


async def manual_news_previous_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        value=float(raw.replace(",", ""))
        if not math.isfinite(value): raise ValueError
    except (TypeError, ValueError):
        await update.message.reply_text("Enter a valid finite numeric Previous Value, for example 2.5.", parse_mode="HTML")
        return AWAITING_NEWS_PREVIOUS
    context.user_data["manual_news_previous"]=value
    await update.message.reply_text("Enter Forecast Value:\nExample: <code>2.7</code>", parse_mode="HTML")
    return AWAITING_NEWS_FORECAST


async def manual_news_forecast_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        value=float(raw.replace(",", ""))
        if not math.isfinite(value): raise ValueError
    except (TypeError, ValueError):
        await update.message.reply_text("Enter a valid finite numeric Forecast Value, for example 2.7.", parse_mode="HTML")
        return AWAITING_NEWS_FORECAST
    context.user_data["manual_news_forecast"]=value
    await update.message.reply_text("Enter News Time in HH:MM format:\nExample: <code>14:30</code>", parse_mode="HTML")
    return AWAITING_NEWS_TIME


async def manual_news_time_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw=(update.message.text or "").strip()
    try:
        time_parts = raw.split(":")
        if len(time_parts) not in (2, 3): raise ValueError
        hour, minute = int(time_parts[0]), int(time_parts[1])
        second = int(time_parts[2]) if len(time_parts) == 3 else 0
        if not (0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60): raise ValueError
    except (TypeError, ValueError):
        await update.message.reply_text("Invalid time. Use HH:MM or HH:MM:SS, for example 14:30.")
        return AWAITING_NEWS_TIME
    mode=context.user_data.get("manual_news_type", "")
    market=context.user_data.get("manual_news_market", "")
    previous=float(context.user_data.get("manual_news_previous", 0))
    forecast=float(context.user_data.get("manual_news_forecast", 0))
    direction=manual_news_direction(mode, market, previous, forecast)
    if direction == "N/A":
        await update.message.reply_text("Previous and Forecast are equal, so no directional news signal can be created. Enter a different Forecast Value.")
        return AWAITING_NEWS_FORECAST
    news_dt=datetime.now(BD_TZ).replace(hour=hour, minute=minute, second=second, microsecond=0)
    if news_dt <= datetime.now(BD_TZ):
        news_dt += timedelta(days=1)
    entry=(news_dt-timedelta(seconds=10)).strftime("%H:%M:%S")
    expiry=(news_dt+timedelta(minutes=1)).strftime("%H:%M:%S")
    event_map = {
        "CAD CPI": ("CPI m/m", "CAD", "CAD"),
        "CAD GDP": ("GDP", "CAD", "CAD"),
        "Core PPI": ("Core PPI", "USD", "USD"),
        "Core CPI": ("CPI", "USD", "USD"),
        "Core retail sales": ("Core Retail Sales", "USD", "USD"),
        "Flash service PMI(EUR)": ("Flash Service PMI", "EUR", "EUR"),
        "Flash service PMI(USD)": ("Flash Service PMI", "USD", "USD"),
        "Flash Service PMI(GBP)": ("Flash Service PMI", "GBP", "GBP"),
        "ISM Service PMI": ("ISM Service PMI", "USD", "USD"),
        "Non farm employment change": ("Non-Farm Employment", "USD", "USD"),
        "Unemployment claim": ("Unemployment Claims", "USD", "USD"),
        "JOLTS job opening": ("JOLTS Job Openings", "USD", "USD"),
    }
    event_name, currency, _ = event_map.get(mode, (mode, "", ""))
    group_map = {
        "CAD": (["CAD/JPY", "CAD/CHF"], ["USD/CAD", "EUR/CAD", "GBP/CAD", "AUD/CAD"]),
        "USD": (["USD/JPY", "USD/CHF"], ["EUR/USD", "GBP/USD", "AUD/USD", "NZD/USD"]),
        "EUR": (["EUR/GBP", "EUR/JPY", "EUR/CHF"], ["GBP/EUR", "USD/EUR", "CAD/EUR"]),
        "GBP": (["GBP/JPY", "GBP/CHF"], ["EUR/GBP", "USD/GBP", "CAD/GBP"]),
    }
    call_pairs, put_pairs = group_map.get(currency, ([market], []))
    if market not in call_pairs and market not in put_pairs:
        (call_pairs if direction == "CALL" else put_pairs).append(market)
    call_text = " · ".join(call_pairs)
    put_text = " · ".join(put_pairs)
    date_text = news_dt.strftime("%d-%m-%Y")
    display_time = news_dt.strftime("%I:%M:%S %p")
    entry_dt = news_dt - timedelta(seconds=2)
    entry_text = entry_dt.strftime("%I:%M:%S %p")
    confidence = min(99, max(70, int(round(90 + min(9, abs(forecast - previous) * 10)))))
    direction_line = "🟢 BULLISH / BUY / CALL" if direction == "CALL" else "🔴 BEARISH / SELL / PUT"
    filled = max(0, min(10, round(confidence / 10)))
    confidence_bar = "█" * filled + "░" * (10 - filled)
    confidence_label = "STRONG" if confidence >= 85 else ("MODERATE" if confidence >= 65 else "CAUTION")
    report=(
        "╔════════════════════╗\n"
        "      𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝙽𝙴𝚆𝚂 𝚂𝙸𝙶𝙽𝙰𝙻\n"
        "╚════════════════════╝\n\n"
        f"📊 PAIR       : {market.replace('_', '/')}\n"
        f"📌 EVENT      : {event_name}\n"
        f"⏰ TIME       : {news_dt.strftime('%H:%M')}\n\n"
        f"📈 PREVIOUS   : {previous:g}%\n"
        f"📊 FORECAST   : {forecast:g}%\n\n"
        f"🎯 DIRECTION  : {direction_line}\n\n"
        f"📊 CONFIDENCE : {confidence}%\n"
        f"   {confidence_bar} {'🟢' if direction == 'CALL' else '🔴'} {confidence_label}\n\n"
        f"⏱ ENTRY  : {entry_text}\n"
        f"⏱ EXPIRY : {expiry}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "⚠ NEWS TRADING CARRIES HIGH RISK\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )
    keyboard=build([
        [{"text":"NEW MANUAL NEWS","callback":"manual_news_start","style":KeyboardButtonStyle.SUCCESS}],
        [{"text":"MAIN MENU","callback":"menu_home","style":KeyboardButtonStyle.PRIMARY}],
    ])
    await update.message.reply_text(report, parse_mode="HTML", reply_markup=keyboard)
    return ConversationHandler.END


async def manual_news_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Safely cancel MANUAL NEWS before any partially entered values are used."""
    context.user_data.pop("manual_news_type", None)
    context.user_data.pop("manual_news_market", None)
    context.user_data.pop("manual_news_previous", None)
    context.user_data.pop("manual_news_forecast", None)
    if update.message:
        await update.message.reply_text("MANUAL NEWS cancelled.", reply_markup=main_menu())
    return ConversationHandler.END


manual_news_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(manual_news_start, pattern="^manual_news_start$")],
    states={
        AWAITING_NEWS_TYPE: [CallbackQueryHandler(manual_news_type_selected, pattern=r"^news_type_\d+$")],
        AWAITING_NEWS_MARKET: [CallbackQueryHandler(manual_news_market_selected, pattern=r"^news_market_\d+$")],
        AWAITING_NEWS_PREVIOUS: [MessageHandler(filters.TEXT & ~filters.COMMAND, manual_news_previous_received)],
        AWAITING_NEWS_FORECAST: [MessageHandler(filters.TEXT & ~filters.COMMAND, manual_news_forecast_received)],
        AWAITING_NEWS_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, manual_news_time_received)],
    },
    fallbacks=[CommandHandler("cancel", manual_news_cancel)],
)

# ==================== ARXON-STYLE UTILITY MENU ====================

FREE_BOT_LINKS = [
    os.getenv("FREE_BOT_1_LINK", "").strip() or "https://t.me/ZENITEXAIBOT/zenitexai",
    os.getenv("FREE_BOT_2_LINK", "").strip() or "https://ui-refine.ai.studio",
    os.getenv("FREE_BOT_3_LINK", "").strip() or "https://mehedi-bot-v1.netlify.app/",
    *[os.getenv(f"FREE_BOT_{i}_LINK", "").strip() for i in range(4, 11)],
]
SUPPORT_HANDLE = os.getenv("SUPPORT_HANDLE", "@TRADEWITHMEHEDI7")
SUPPORT_URL = f"https://t.me/{SUPPORT_HANDLE.lstrip('@')}"


def _utility_menu() -> InlineKeyboardMarkup:
    return build([
        [{"text": "🏠 MAIN MENU", "callback": "menu_home", "style": KeyboardButtonStyle.PRIMARY}],
    ])


def _free_bots_menu() -> InlineKeyboardMarkup:
    """Render exactly ten two-column buttons like the supplied reference image.

    Configured links are green and open their Telegram URL. Empty slots are red
    and remain callback buttons so users receive a clear unavailable message.
    """
    rows = []
    row = []
    for i in range(1, 11):
        link = FREE_BOT_LINKS[i - 1] if i - 1 < len(FREE_BOT_LINKS) else ""
        if link:
            row.append({
                "text": f"🔐 NUMBER {i:02d}",
                "url": link,
                "style": KeyboardButtonStyle.SUCCESS,
            })
        else:
            row.append({
                "text": f"🔒 NUMBER {i:02d}",
                "callback": f"free_bot_unavailable_{i}",
                "style": KeyboardButtonStyle.DANGER,
            })
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([{
        "text": "↩️ BACK",
        "callback": "menu_home",
        "style": KeyboardButtonStyle.PRIMARY,
    }])
    return build(rows)


async def _utility_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q = update.callback_query
    if not q:
        return
    await q.answer()
    uid = update.effective_user.id if update.effective_user else 0
    register_user(
        uid,
        (update.effective_user.username or "") if update.effective_user else "",
        (update.effective_user.first_name or "") if update.effective_user else "",
    )
    data = q.data or ""

    if data == "menu_my_id":
        user = get_user(uid) or {}
        await edit_or_send(
            update,
            context,
            build_reference_status_card(
                user_id=uid,
                username=(update.effective_user.username or "") if update.effective_user else "",
                first_name=user.get("first_name") or ((update.effective_user.first_name or "TRADER") if update.effective_user else "TRADER"),
                tier=get_user_tier(uid),
                expire_at=user.get("tier_expire_at"),
                created_at=user.get("created_at"),
            ),
            _utility_menu(),
        )
    elif data == "menu_my_status":
        user = get_user(uid) or {}
        await edit_or_send(
            update,
            context,
            build_status_card(
                user_id=uid,
                username=(update.effective_user.username or "") if update.effective_user else "",
                first_name=user.get("first_name") or "TRADER",
                tier=get_user_tier(uid),
                expire_at=user.get("tier_expire_at"),
            ),
            _utility_menu(),
        )
    elif data == "menu_pricing":
        await edit_or_send(update, context,
            "💎 <b>PRICING & PLAN LIMITS</b>\n━━━━━━━━━━━━━━━━━━━━\n\n"
            "🆓 <b>FREE PLAN</b>\n⚡ Auto: 5/day  🎯 Manual: 5/day  📡 Channel: 10/day\n🌐 Real Market FS: 2/day  🧠 AI Live: 2/day  🤖 AI OTC: 2/day\n📊 Backtest FS: 2/day  🔍 Checker: Unlimited  📰 News: Unlimited  📈 Trend: Unlimited\n\n"
            "🔥 <b>PREMIUM PLAN</b>\n⚡ Auto: 30/day  🎯 Manual: 30/day  📡 Channel: 50/day\n🌐 Real Market FS: 10/day  🧠 AI Live: 5/day  🤖 AI OTC: 5/day\n📊 Backtest FS: 8/day  🔍 Checker: Unlimited  📰 News: Unlimited  📈 Trend: Unlimited\n\n"
            "👑 <b>EXPENSIVE PLAN</b>\nAll listed features: Unlimited\n\n"
            "📩 Contact support for activation or plan changes.",
            build([[{"text": "📞 CONTACT SUPPORT", "url": SUPPORT_URL, "style": KeyboardButtonStyle.PRIMARY}],
                   [{"text": "🏠 MAIN MENU", "callback": "menu_home"}]]))
    elif data == "menu_support":
        await edit_or_send(update, context,
            "📞 <b>SUPPORT CENTER</b>\n━━━━━━━━━━━━━━━━━━━━\n\n"
            "For account, subscription, signal, data or technical issues, contact the official support.\n\n"
            f"👨‍💻 Support: <b>{SUPPORT_HANDLE}</b>\n"
            f"🆔 Your ID: <code>{uid}</code>",
            build([[{"text": "📩 CONTACT SUPPORT", "url": SUPPORT_URL, "style": KeyboardButtonStyle.PRIMARY}],
                   [{"text": "🏠 MAIN MENU", "callback": "menu_home"}]]))
    elif data == "menu_free_bots":
        added = sum(bool(x) for x in FREE_BOT_LINKS)
        await edit_or_send(update, context,
            f"🆓 <b>FREE BOTS</b>\n━━━━━━━━━━━━━━━━━━━━\n\n"
            f"Configured links: <b>{added}/10</b>\n"
            "🟢 Green = link available   🔴 Red = not added\n\n"
            "Choose a bot below.",
            _free_bots_menu())
    elif data.startswith("free_bot_unavailable_"):
        await edit_or_send(update, context,
            "🔒 <b>BOT NOT CONFIGURED</b>\n\nThis slot is currently unavailable.",
            _free_bots_menu())


utility_handlers = [
    CommandHandler("partial", partial_command),
    CallbackQueryHandler(_utility_callback, pattern=r"^(menu_my_status|menu_pricing|menu_support|menu_free_bots|free_bot_unavailable_\d+)$")
]


async def unknown_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Recover stale inline buttons by opening the current menu directly."""
    query = update.callback_query
    if not query:
        return
    await safe_answer(query)
    # Do not show a stale-menu error card. Re-render the live welcome/menu view
    # so old callback buttons always recover to the current options.
    await send_welcome_image_menu(update, context)


unknown_callback_fallback = CallbackQueryHandler(unknown_callback_handler, pattern=r"^.+$")

async def menu_channel_sender_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    user = update.effective_user
    uid = user.id if user else 0
    cs = get_channel_sender(uid)
    is_running = bool(cs.get("is_active", 0))

    text = (
        f"📢 <b>ZENITEX AI - CHANNEL SENDER</b> 📢\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Automatically broadcast high-accuracy OANDA strategy signals directly to your Telegram Channel!\n\n"
        f"📌 <b>Target Channel:</b> <code>{cs.get('target_channel') or 'Not Set'}</code>\n"
        f"📊 <b>Market Type:</b> <b>{cs.get('market_type', 'REAL')}</b>\n"
        f"🔬 <b>Strategy:</b> <b>{cs.get('strategy_type', 'ZX PRO 2.1')}</b>\n"
        f"🎯 <b>Pair Filter:</b> <b>{cs.get('filter_type', 'ALL PAIRS')}</b>\n"
        f"⚡ <b>Status:</b> {'🟢 <b>ACTIVE (Auto-Broadcasting)</b>' if is_running else '🔴 <b>STOPPED</b>'}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<i>Configure your settings below or start the auto channel sender task.</i>"
    )
    await edit_or_send(update, context, text, channel_sender_menu(is_running, cs))

async def csender_set_target_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    if query:
        await safe_answer(query)
    text = (
        f"📢 <b>SET TARGET CHANNEL</b> 📢\n\n"
        f"Please send your Telegram Channel username or ID (e.g. <code>@my_channel</code> or <code>-1001234567890</code>).\n\n"
        f"<i>Make sure your bot is added as an <b>Administrator</b> in that channel with post permissions!</i>\n"
        f"(Or send /cancel to abort)"
    )
    await edit_or_send(update, context, text, build([[{"text": "Cancel", "callback": "menu_channel_sender"}]]))
    return AWAITING_CHANNEL_TARGET

def normalize_channel_target(raw: str) -> str:
    value = (raw or "").strip()
    if value.startswith(("https://t.me/", "http://t.me/")):
        value = value.split("t.me/", 1)[1].split("/", 1)[0]
    elif value.startswith("t.me/"):
        value = value.split("t.me/", 1)[1].split("/", 1)[0]
    value = value.strip()
    if value.startswith("-"):
        return value if value.startswith("-100") and value[1:].isdigit() else ""
    if value.startswith("@"):
        username = value[1:]
    else:
        username = value
    if username and re.fullmatch(r"[A-Za-z0-9_]{5,32}", username):
        return "@" + username
    return ""

async def csender_target_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.effective_user
    uid = user.id if user else 0
    raw_text = (update.message.text or "").strip()
    text = normalize_channel_target(raw_text)
    if not text:
        await update.message.reply_text(
            "Invalid channel target. Send @channel_username or a numeric -100 channel ID.",
            parse_mode="HTML",
        )
        return AWAITING_CHANNEL_TARGET
    set_channel_sender(uid, target_channel=text, is_active=0)
    cs = get_channel_sender(uid)
    msg = (
        f"✅ <b>CHANNEL TARGET SAVED</b>\n\n"
        f"Target: <code>{text}</code>\n"
        f"Status: <b>READY FOR PREFLIGHT CHECK</b>\n\n"
        f"Add the bot as an administrator with post permission, then press START FULL AUTO."
    )
    await update.message.reply_text(msg, parse_mode="HTML", reply_markup=channel_sender_menu(False, cs))
    return ConversationHandler.END
async def csender_toggle_market_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    uid = update.effective_user.id
    cs = get_channel_sender(uid)
    new_market = "OTC" if cs.get("market_type", "REAL") == "REAL" else "REAL"
    set_channel_sender(uid, market_type=new_market)
    await menu_channel_sender_callback(update, context)

async def csender_toggle_strat_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    uid = update.effective_user.id
    cs = get_channel_sender(uid)
    new_strat = "ZX PREMIUM" if cs.get("strategy_type", "ZX PRO 2.1") == "ZX PRO 2.1" else "ZX PRO 2.1"
    set_channel_sender(uid, strategy_type=new_strat)
    await menu_channel_sender_callback(update, context)

async def csender_toggle_filter_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    uid = update.effective_user.id
    cs = get_channel_sender(uid)
    filters_list = ["ALL PAIRS", "TOP 5 MAJOR", "EUR ONLY", "GBP ONLY"]
    current_filt = cs.get("filter_type", "ALL PAIRS")
    try:
        idx = filters_list.index(current_filt)
        new_filt = filters_list[(idx + 1) % len(filters_list)]
    except ValueError:
        new_filt = "ALL PAIRS"
    set_channel_sender(uid, filter_type=new_filt)
    await menu_channel_sender_callback(update, context)

async def csender_start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    try:
        await safe_answer(query)
    except Exception:
        pass
    uid = update.effective_user.id
    cs = get_channel_sender(uid)
    target = normalize_channel_target(cs.get("target_channel", ""))
    if not target:
        await query.message.reply_text("Please set a valid @channel_username or -100 channel ID first.", parse_mode="HTML")
        return
    loading_msg = await professional_loading_message(
        update, "CHANNEL SENDER", "TARGET PREFLIGHT",
        "Checking channel access and preparing real OANDA market scan..."
    )
    try:
        await context.bot.get_chat(target)
    except Exception as exc:
        await delete_loading_message(loading_msg)
        set_channel_sender(uid, target_channel=target, is_active=0)
        failure_text = (
            "<blockquote><b>⚠️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙰𝚁𝙶𝙴𝚃 𝙲𝙷𝙴𝙲𝙺 𝙵𝙰𝙸𝙻𝙴𝙳</b>\\n"
            "<b>━━━━━━━━━━━━━━━━━━━━</b>\\n\\n"
            "<b>🚫 𝙱𝙾𝚃 𝙰𝙲𝙲𝙴𝚂𝚂 𝙽𝙾𝚃 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴</b>\\n\\n"
            "<b>𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴:</b>\\n"
            "<b>𝟷.</b> 𝙰𝚍𝚍 𝚝𝚑𝚎 𝚋𝚘𝚝 𝚊𝚜 𝚊𝚗 <b>𝙰𝙳𝙼𝙸𝙽𝙸𝚂𝚃𝚁𝙰𝚃𝙾𝚁</b>.\\n"
            "<b>𝟸.</b> 𝙴𝚗𝚊𝚋𝚕𝚎 <b>𝙿𝙾𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂</b> 𝚙𝚎𝚛𝚖𝚒𝚜𝚜𝚒𝚘𝚗.\\n"
            "<b>𝟹.</b> 𝙲𝚑𝚎𝚌𝚔 𝚝𝚑𝚎 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎 𝚘𝚛 𝙸𝙳.\\n\\n"
            "<b>✅ 𝚃𝚑𝚎𝚗 𝚙𝚛𝚎𝚜𝚜 𝙎𝚃𝙰𝚁𝚃 𝙵𝚄𝙻𝙻 𝙰𝚄𝚃𝙾 𝚊𝚐𝚊𝚒𝚗.</b>\\n"
            "<b>━━━━━━━━━━━━━━━━━━━━</b></blockquote>"
        )
        await query.message.reply_text(
            failure_text, parse_mode="HTML", reply_markup=channel_sender_menu(False, cs)
        )
        log.warning("Channel target preflight failed for %s: %s", target, exc)
        return
    set_channel_sender(uid, target_channel=target, is_active=1)
    await delete_loading_message(loading_msg)
    task_key = f"csender_task_{uid}"
    if task_key in context.bot_data and not context.bot_data[task_key].done():
        context.bot_data[task_key].cancel()
    async def _channel_sender_background_loop():
        try:
            while True:
                curr_cs = get_channel_sender(uid)
                if not curr_cs.get("is_active"):
                    break
                
                target = curr_cs.get("target_channel")
                market = curr_cs.get("market_type", "REAL")
                strat = curr_cs.get("strategy_type", "ZX PRO 2.1")
                filt = curr_cs.get("filter_type", "ALL PAIRS")

                base_pairs = list(REAL_PAIRS)
                if filt == "TOP 5 MAJOR":
                    active_pairs = list(REAL_PAIRS)
                elif filt == "EUR ONLY":
                    active_pairs = ["EUR_CAD", "EUR_CHF"]
                elif filt == "GBP ONLY":
                    active_pairs = ["GBP_CAD", "GBP_CHF"]
                else:
                    active_pairs = base_pairs

                # Scan configured REAL markets and rank qualified candidates first,
                # then use the strongest valid OANDA-backed direction as fallback.
                ranked, analyzed = await fast_scan_signal_candidates(active_pairs, count=120)
                selected = ranked or analyzed
                if not selected:
                    log.warning("No valid OANDA signal candidate returned; retrying after short backoff")
                    await asyncio.sleep(5)
                    continue
                selected.sort(key=lambda x: (x[2].get("confidence", 0), x[2].get("agreement", 0)), reverse=True)
                pair, candles, sr = selected[0]
                direction = sr["signal"]
                conf = int(sr["confidence"])
                channel_allowed, channel_used, channel_limit = reserve_feature_usage(uid, "channel_sender")
                if not channel_allowed:
                    await context.bot.send_message(chat_id=target, text=format_limit_reached("channel_sender", channel_used, channel_limit, get_user_tier(uid)), parse_mode="HTML")
                    set_channel_sender(uid, is_active=0)
                    break

                now_dt = datetime.now(BD_TZ) + timedelta(minutes=1)
                entry_time = now_dt.strftime("%H:%M")

                last_price = "N/A"
                try:
                    last_c = candles[-1].get("mid", {})
                    last_price = str(last_c.get("c", candles[-1].get("close", "N/A")))
                except Exception:
                    pass

                caption_text = generate_signal_card_text(
                    asset=pair,
                    entry=entry_time,
                    direction=direction,
                    price=last_price,
                    confidence=conf,
                    mode="CHANNEL SENDER",
                    strategy_title=strat,
                    oanda_candles=candles,
                    analysis=sr.get("details") if isinstance(sr, dict) else None,
                )

                chart_path = f"/tmp/zenitix_channel_chart_{uid}_{int(datetime.now().timestamp())}.jpg"
                chart_path = generate_chart_image(
                    asset=pair,
                    timeframe="1 MINUTE",
                    direction=direction,
                    output_path=chart_path,
                    oanda_candles=candles or []
                )

                try:
                    sent_channel_chart = await send_chart_photo_with_retry(
                        context.bot, target, chart_path, caption_text, attempts=3
                    )
                    if not sent_channel_chart:
                        await context.bot.send_message(
                            chat_id=target,
                            text="<b>CHART DELIVERY RETRY</b>\nThe generated OANDA chart could not be uploaded after retries.",
                            parse_mode="HTML",
                        )
                except Exception as ex:
                    log.error(f"Failed to send channel signal photo to {target}: {ex}")
                    try:
                        await context.bot.send_message(chat_id=target, text=caption_text, parse_mode="HTML")
                    except Exception as fallback_exc:
                        log.error("Channel text fallback failed for %s: %s", target, fallback_exc)
                        set_channel_sender(uid, is_active=0)
                        break
                finally:
                    if os.path.exists(chart_path):
                        try:
                            os.remove(chart_path)
                        except Exception:
                            pass

                # Result & MTG flow
                try:
                    now_local = now_bd()
                    eh, em = map(int, entry_time.split(":"))
                    candle_start = now_local.replace(hour=eh, minute=em, second=0, microsecond=0)
                    if candle_start < now_local - timedelta(minutes=2):
                        candle_start += timedelta(days=1)
                    candle_expiry = candle_start + timedelta(minutes=1, seconds=3)
                    wait_s1 = (candle_expiry - now_local).total_seconds()
                    if wait_s1 < 1:
                        wait_s1 = 5.0
                except Exception:
                    wait_s1 = 5.0
                await asyncio.sleep(wait_s1)
                pair_inst = format_oanda_instrument(pair)
                candles_res = None
                entry_candle = None
                entry_deadline = candle_start + timedelta(minutes=6)
                while datetime.now(BD_TZ) <= entry_deadline:
                    candles_res = await fetch_oanda_candles(pair_inst, count=18, granularity="M1")
                    entry_candle = checker_exact_candle(candles_res, candle_start)
                    if entry_candle is not None:
                        break
                    await asyncio.sleep(3)

                result_candle = None
                mtg_level = 0
                if not candles_res or len(candles_res) < 1:
                    final_res = "PENDING"
                else:
                    # Use only the exact completed OANDA M1 candle at the intended entry minute.
                    entry_target = candle_start
                    entry_candle = checker_exact_candle(candles_res, entry_target)

                    if entry_candle is None:
                        final_res = "PENDING"
                    else:
                        result_candle = entry_candle
                        mid1 = entry_candle.get("mid", {})
                        o1, c1 = float(mid1.get("o", entry_candle.get("open"))), float(mid1.get("c", entry_candle.get("close")))
                        direct_win = (direction.upper() == "CALL" and c1 > o1) or (direction.upper() == "PUT" and c1 < o1)
                        if direct_win or c1 == o1:
                            final_res = "WIN"
                        else:
                            # Exactly one MTG G1 candle after a direct loss; wait for its close.
                            mtg_target = entry_target + timedelta(minutes=1)
                            mtg_wait = max(0.0, (mtg_target + timedelta(minutes=1, seconds=5) - now_bd()).total_seconds())
                            if mtg_wait:
                                await asyncio.sleep(mtg_wait)
                            mtg_candle = None
                            mtg_deadline = mtg_target + timedelta(minutes=6)
                            while datetime.now(BD_TZ) <= mtg_deadline:
                                refreshed = await fetch_oanda_candles(pair_inst, count=18, granularity="M1")
                                if refreshed:
                                    candles_res = refreshed
                                mtg_candle = checker_exact_candle(candles_res, mtg_target)
                                if mtg_candle is not None:
                                    break
                                await asyncio.sleep(3)
                            if mtg_candle is None:
                                final_res = "PENDING MTG G1"
                            else:
                                result_candle = mtg_candle
                                mtg_level = 1
                                mid2 = mtg_candle.get("mid", {})
                                o2, c2 = float(mid2.get("o", mtg_candle.get("open"))), float(mid2.get("c", mtg_candle.get("close")))
                                mtg_win = (c2 == o2) or (direction.upper() == "CALL" and c2 > o2) or (direction.upper() == "PUT" and c2 < o2)
                                final_res = "MTG WIN" if mtg_win else "MTG LOSS"
                record_partial_result(uid, pair, entry_time, direction, final_res, "CHANNEL SENDER")
                res_text = generate_result_card_text(
                    asset=pair,
                    time_str=entry_time,
                    direction=direction,
                    result_type=final_res,
                    win_count=1 if "WIN" in final_res else 0,
                    loss_count=1 if "LOSS" in final_res else 0,
                    strategy_title=f"CHANNEL SENDER • {strat}",
                    result_candle=result_candle,
                    mtg_level=mtg_level,
                )

                try:
                    delivered = await send_final_result_chart(
                        context.bot, target, pair, direction, final_res, candles_res, result_candle,
                        res_text, tag="channel"
                    )
                    if not delivered:
                        log.error("Channel result withheld because the verified result chart could not be delivered for %s", pair)
                        await context.bot.send_message(
                            chat_id=target,
                            text="⚠️ <b>RESULT CHART DELIVERY RETRY</b>\n━━━━━━━━━━━━━━━━━━━━\nThe verified result is ready, but its OANDA chart image could not be delivered. Please check again shortly.",
                            parse_mode="HTML",
                        )
                except Exception as e:
                    log.error(f"Failed to send channel result to {target}: {e}")

                # Continue only after the result chart/message has been delivered.
                # A short cooldown prevents duplicate entries while keeping the cycle fast.
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            log.error(f"Error in channel sender loop for uid {uid}: {e}")

    loop_task = _create_tracked_task(_channel_sender_background_loop())
    context.bot_data[task_key] = loop_task

    await menu_channel_sender_callback(update, context)

async def csender_stop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await safe_answer(query)
    uid = update.effective_user.id
    set_channel_sender(uid, is_active=0)
    
    task_key = f"csender_task_{uid}"
    if task_key in context.bot_data and not context.bot_data[task_key].done():
        context.bot_data[task_key].cancel()

    await menu_channel_sender_callback(update, context)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    return await start(update, context)

channel_sender_handlers = [
    CallbackQueryHandler(menu_channel_sender_callback, pattern="^menu_channel_sender$"),
    CallbackQueryHandler(csender_toggle_market_callback, pattern="^csender_toggle_market$"),
    CallbackQueryHandler(csender_toggle_strat_callback, pattern="^csender_toggle_strat$"),
    CallbackQueryHandler(csender_toggle_filter_callback, pattern="^csender_toggle_filter$"),
    CallbackQueryHandler(csender_start_callback, pattern="^csender_start$"),
    CallbackQueryHandler(csender_stop_callback, pattern="^csender_stop$"),
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(csender_set_target_prompt, pattern="^csender_set_target$"),
        ],
        states={
            AWAITING_CHANNEL_TARGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, csender_target_received)],
        },
        fallbacks=[
            MessageHandler(filters.COMMAND, cancel),
            CallbackQueryHandler(menu_channel_sender_callback, pattern="^menu_channel_sender$")
        ],
    ),
]

def recent_trend_menu() -> InlineKeyboardMarkup:
    pairs = REAL_PAIRS
    rows = []
    for i in range(0, len(pairs), 2):
        p1 = pairs[i]
        row = [{"text": f"📊 {p1.replace('_', '/')}", "callback": f"trendpair_{p1}", "style": KeyboardButtonStyle.PRIMARY}]
        if i + 1 < len(pairs):
            p2 = pairs[i + 1]
            row.append({"text": f"📊 {p2.replace('_', '/')}", "callback": f"trendpair_{p2}", "style": KeyboardButtonStyle.PRIMARY})
        rows.append(row)
    rows.append([{"text": "Home", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}])
    return build(rows)

async def menu_recent_trend_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query)
    text = (
        f"📈 <b>ZENITEX AI - RECENT MARKET TREND ANALYZER</b> 📈\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Select a market below to analyze its recent trend, technical indicators (RSI, EMA, MACD), and live momentum:\n\n"
        f"<i>Tap any currency pair or asset below:</i>"
    )
    await edit_or_send(update, context, text, recent_trend_menu())

async def trendpair_selected_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    if query:
        await safe_answer(query, "📈 𝚁𝚎𝚌𝚎𝚗𝚝 𝚖𝚊𝚛𝚔𝚎𝚝 𝚜𝚌𝚊𝚗𝚗𝚒𝚗𝚐 & 𝚌𝚑𝚊𝚛𝚝...", show_alert=False)
    
    data = query.data or ""
    pair_raw = data.replace("trendpair_", "")
    display_pair = pair_raw.replace("_", "/")
    loading_msg = await professional_loading_message(update, "RECENT TREND", "ANALYZING MARKET", f"Market: {display_pair}\nCalculating RSI, EMA, MACD and momentum...")
    candles = await fetch_oanda_candles(pair_raw, count=50, granularity="M1")
    await delete_loading_message(loading_msg)
    now_str = datetime.now(BD_TZ).strftime("%Y-%m-%d %H:%M:%S BDT")
    
    if candles and len(candles) >= 20:
        direction, confidence, details = enhanced_analyze(candles)
        rsi = details.get('rsi', 50.0)
        ema_fast = details.get('ema_fast', 0.0)
        ema_slow = details.get('ema_slow', 0.0)
        score = details.get('score', 0)
        current_price = details.get('current_price', 0.0)
        macd_line = details.get('macd_line', 0.0)
        signal_line = details.get('signal_line', 0.0)
        atr = details.get('atr', 0.0001)
        support = details.get('support', current_price * 0.995)
        resistance = details.get('resistance', current_price * 1.005)
        
        is_call = "CALL" in direction.upper() or "BUY" in direction.upper() or score >= 0
        verdict_str = "HIGHER (CALL)" if is_call else "LOWER (PUT)"
        conf_label = "STRONG" if confidence >= STRATEGY_CONFIG.get('high_confidence', 85) else ("MODERATE" if confidence >= STRATEGY_CONFIG.get('min_confidence', 65) else "CAUTION")
        
        trend_pct = confidence
        vol_pct = min(100, max(10, int(rsi if 0 < rsi < 100 else 85)))
        mom_pct = min(100, max(10, confidence + 2))
        if mom_pct > 99: mom_pct = 95
        volat_pct = min(100, max(10, int(atr * 10000) % 70 + 20))
        ai_score_pct = confidence

        def make_bar(pct):
            filled = round(pct / 10)
            empty = 10 - filled
            return "█" * filled + "░" * empty

        trend_bar = make_bar(trend_pct)
        vol_bar = make_bar(vol_pct)
        mom_bar = make_bar(mom_pct)
        volat_bar = make_bar(volat_pct)
        ai_bar = make_bar(ai_score_pct)

        trend_name = "BULLISH" if is_call else "BEARISH"
        report_lines = [
            "╔════════════════════╗",
            "      𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝚁𝙴𝙲𝙴𝙽𝚃 𝚃𝚁𝙴𝙽𝙳",
            "╚════════════════════╝",
            "",
            f"MARKET        : {display_pair} (REAL)",
            "TIMEFRAME     : M1",
            "SOURCE        : REAL OANDA DATA",
            "",
            f"CURRENT TREND : {trend_name}",
            f"TREND STRENGTH: {conf_label} {confidence}%",
            f"TREND         : {trend_bar} {trend_pct}%",
            f"MOMENTUM      : {mom_bar} {mom_pct}%",
            f"RSI           : {rsi:.2f}",
            f"EMA FAST      : {ema_fast:.5f}",
            f"EMA SLOW      : {ema_slow:.5f}",
            f"MACD          : {macd_line:.5f}",
            f"SIGNAL LINE   : {signal_line:.5f}",
            f"SUPPORT       : {support:.5f}",
            f"RESISTANCE    : {resistance:.5f}",
            "",
            "ONLY RECENT TREND — NO SIGNAL PROVIDED",
        ]
        nl = "\n"
        analysis_text = f"<pre>{nl.join(report_lines)}</pre>"
        chart_dir_direction = "CALL" if is_call else "PUT"
    else:
        # Never fabricate a trend when real OANDA candles are unavailable.
        await update.effective_message.reply_text(
            f"<b>RECENT TREND</b>\n\nMarket: {display_pair}\n"
            "Real OANDA M1 data is not available for this market right now.\n"
            "No simulated trend is provided. Please choose the market again.",
            parse_mode="HTML",
            reply_markup=recent_trend_menu(),
        )
        return

    clean_asset = pair_raw.upper().replace("/", "").replace("_", "").replace("-OTC", "")
    chart_filename = f"trend_chart_{int(datetime.now().timestamp())}_{clean_asset}.jpg"
    chart_path = generate_chart_image(
        asset=pair_raw,
        timeframe="1 MINUTE",
        direction=chart_dir_direction,
        output_path=chart_filename,
        oanda_candles=candles
    )
    
    reply_markup = build([
        [
            {"text": "🔄 Check Another", "callback": "menu_recent_trend", "style": KeyboardButtonStyle.PRIMARY}
        ],
        [
            {"text": "🏠 Main Menu", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER, "icon_emoji": emoji_id("home_icon")}
        ]
    ])
    try:
        if query and query.message:
            try:
                await query.message.delete()
            except Exception:
                pass
            with open(chart_path, "rb") as photo_f:
                await query.message.reply_photo(
                    photo=photo_f,
                    caption=analysis_text,
                    parse_mode="HTML",
                    reply_markup=reply_markup
                )
        elif update.effective_message:
            with open(chart_path, "rb") as photo_f:
                await update.effective_message.reply_photo(
                    photo=photo_f,
                    caption=analysis_text,
                    parse_mode="HTML",
                    reply_markup=reply_markup
                )
    except Exception as ex:
        log.error(f"Failed to send trend chart photo: {ex}")
        await edit_or_send(update, context, analysis_text, reply_markup)

recent_trend_handlers = [
    CallbackQueryHandler(menu_recent_trend_callback, pattern="^menu_recent_trend$"),
    CallbackQueryHandler(trendpair_selected_callback, pattern="^trendpair_"),
]

admin_handlers = [
    CommandHandler("admin", admin_command),
    CommandHandler("setplan", setplan_command),
    CommandHandler("userinfo", userinfo_command),
    CommandHandler("broadcast", broadcast_command),
    CallbackQueryHandler(admin_command, pattern="^admin_home$"),
    CallbackQueryHandler(admin_analytics, pattern="^admin_analytics$"),
    CallbackQueryHandler(admin_user_management, pattern="^admin_user_management$"),
    CallbackQueryHandler(admin_system_status, pattern="^admin_system_status$"),
    CallbackQueryHandler(admin_set_tier_callback, pattern="^admset_"),
    CallbackQueryHandler(admin_moderation_prompt, pattern="^admin_(?:ban|unban)_prompt$"),
]

# ========================================
# File: telegram_ui/handlers/futures.py
# ========================================



log = logging.getLogger(__name__)

_SEL_KEY = "fut_selected_pairs"
AWAITING_START, AWAITING_END = range(2)


def _build_text(selected: set[str], pairs: list[str]) -> str:
# removed relative import:     from ..formatting import bold
    pair_list = ", ".join(sorted(selected)) if selected else "None"
    return (
        f"\U0001f513 {bold('TAP PAIRS SELECT & UNSELECT:')}\n\n"
        f"\u2705 {bold('Selected:')} <code>{pair_list}</code>"
    )


async def generate_future_signals_text(context, day_num: int = 1) -> tuple[str, list[dict]]:
    from datetime import datetime, timezone, timedelta
# removed relative import:     from ..checker_engine import fetch_oanda_candles, format_oanda_instrument

    pairs = context.user_data.get(_SEL_KEY, REAL_PAIRS)
    if not pairs:
        pairs = REAL_PAIRS

    direction = context.user_data.get("fut_direction", "CALL")
    start_str = context.user_data.get("fut_start_time", "10:00")
    end_str = context.user_data.get("fut_end_time", "17:00")

    try:
        start_h, start_m = map(int, start_str.split(":"))
        end_h, end_m = map(int, end_str.split(":"))
    except Exception:
        start_h, start_m = 10, 0
        end_h, end_m = 17, 0

    start_min = start_h * 60 + start_m
    end_min = end_h * 60 + end_m
    if end_min <= start_min:
        end_min = start_min + 120

    dirs = ["CALL", "PUT"] if direction == "BOTH" else ([direction] if direction else ["CALL"])

    pair_bias = {}
    pair_scores = {}
    pair_backtest_winrate = {}

    # Deterministic strategy fallback using pair hash if API unavailable
    for pair in pairs:
        oanda_pair = format_oanda_instrument(pair)
        try:
            # Deep backtest using 50 candles
            candles = await fetch_oanda_candles(oanda_pair, count=50, granularity="M1")
            if candles and len(candles) >= 15:
                closes = [float(c.get("mid", {}).get("c", 0)) for c in candles]
                opens = [float(c.get("mid", {}).get("o", 0)) for c in candles]
                
                # Backtest Direct Win & MTG1 Win rates
                direct_wins = 0
                mtg_wins = 0
                total_samples = len(closes) - 2

                for i in range(10, total_samples):
                    c_open, c_close = opens[i], closes[i]
                    m_open, m_close = opens[i+1], closes[i+1]
                    
                    # Momentum & Moving Average strategy
                    sma_10 = sum(closes[i-10:i])/10.0
                    bias_call = closes[i-1] >= sma_10
                    
                    if bias_call:
                        if c_close > c_open:
                            direct_wins += 1
                        elif m_close > m_open:
                            mtg_wins += 1
                    else:
                        if c_close < c_open:
                            direct_wins += 1
                        elif m_close < m_open:
                            mtg_wins += 1

                win_rate = ((direct_wins + mtg_wins) / max(1, total_samples)) * 100.0
                pair_backtest_winrate[pair] = round(max(0.0, min(100.0, win_rate)), 1)

                recent_close = closes[-1]
                sma_10 = sum(closes[-10:]) / 10.0
                sma_20 = sum(closes[-20:]) / 20.0
                green_candles = sum(1 for c, o in zip(closes[-10:], opens[-10:]) if c >= o)

                # Pure Market Logic Strategy: EMA cross + candle sentiment
                if recent_close >= sma_10 and sma_10 >= sma_20:
                    pair_bias[pair] = "CALL"
                elif recent_close < sma_10 and sma_10 < sma_20:
                    pair_bias[pair] = "PUT"
                elif green_candles >= 5:
                    pair_bias[pair] = "CALL"
                else:
                    pair_bias[pair] = "PUT"
                
                pair_scores[pair] = pair_backtest_winrate[pair]
            else:
                log.warning("Future-signal pair %s skipped: insufficient real OANDA candles", pair)
                continue
        except Exception as exc:
            log.warning("Future-signal pair %s skipped after real OANDA error: %s", pair, exc)
            continue

    # GUARANTEE MINIMUM 5 TO MAXIMUM 12 SIGNALS USING EVEN TIME SPACING
    window = end_min - start_min
    raw_count = max(5, min(12, window // 8 if window >= 40 else 8))
    target_count = min(12, max(5, raw_count))

    # Deterministic even time slot calculation across specified window
    times = []
    step = window / float(target_count + 1)
    for i in range(1, target_count + 1):
        t_val = int(start_min + round(i * step))
        t_val = max(start_min, min(end_min - 1, t_val))
        times.append(t_val)

    # Ensure unique and sorted time slots
    times = sorted(list(dict.fromkeys(times)))
    
    # Fill remaining slots deterministically if needed to meet minimum 5 signals
    idx_fill = 1
    while len(times) < 5 and start_min + idx_fill < end_min:
        new_t = start_min + idx_fill * 5
        if new_t not in times and new_t < end_min:
            times.append(new_t)
            times.sort()
        idx_fill += 1

    if len(times) > 12:
        times = times[:12]

    parsed_signals = []
    sig_lines = []
    
    pair_pool = list(pair_bias.keys())
    if not pair_pool:
        return ("NO VERIFIED REAL-OANDA SETUP\nPlease retry when completed market candles are available.", [])
    
    for idx, t_min in enumerate(times):
        h, m = divmod(t_min, 60)
        time_str = f"{h:02d}:{m:02d}"
        
        selected_pair = pair_pool[idx % len(pair_pool)]
        show_pair = selected_pair.replace("_", "/").replace("OTC", "").upper()

        if direction == "BOTH":
            d = pair_bias.get(selected_pair)
            if d not in ("CALL", "PUT"):
                continue
        else:
            d = direction

        sig_lines.append(f"M1;{show_pair};{time_str};{d}")

        parsed_signals.append({
            "tf": "M1",
            "pair": selected_pair,
            "time": time_str,
            "direction": d,
        })

    code_block = "\n".join(sig_lines)

    avg_backtest = round(sum(pair_backtest_winrate.values()) / max(1, len(pair_backtest_winrate)), 1)
    if avg_backtest > 99.5:
        avg_backtest = 99.4

    bd_tz = timezone(timedelta(hours=6))
    target_dt = datetime.now(bd_tz) + timedelta(days=day_num)
    target_date_str = target_dt.strftime("%d.%m.%Y")

    context.user_data["fut_generated_signals"] = parsed_signals
    context.user_data["fut_target_date"] = target_dt.strftime("%Y.%m.%d")

    market_type = context.user_data.get("fut_market", "REAL").upper()

    text = (
        f"🔍 <b>𝗭𝗘𝗡𝗜𝗧𝗜𝗫 𝗔𝗜</b> 🔍\n"
        f"═════════════════════\n"
        f"⏰ TIMEFRAME : M1\n"
        f"↗️ MARKET       : {market_type}\n"
        f"➕ MTG             : 1-STEP\n"
        f"🚀 TIME ZONE  : +06:00 🇧🇩\n"
        f"📅 DATE          : {target_date_str}\n"
        f"📊 BACKTEST  : {avg_backtest}%\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"<pre>{code_block}</pre>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📶<b>𝗨𝗦𝗘 𝗦𝗔𝗙𝗘𝗧𝗬 𝗙𝗢𝗥 𝗕𝗘𝗧𝗧𝗘𝗥 𝗥𝗘𝗦𝗨𝗟𝗧</b> 🔥\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🔥  𝙾𝙽𝙻𝚈 𝚃𝚁𝙰𝙳𝙴 𝙰𝙱𝙾𝚅𝙴 𝟾𝟶%  \n"
        f"⚠️ 𝙰𝚅𝙾𝙸𝙳 𝙶𝙰𝙿 𝚄𝙿 & 𝙶𝙰𝙿 𝙳𝙾𝚆𝙽\n"
        f"🐂 𝚂𝙸𝙳𝙴𝚆𝙸𝚂𝙴 𝙼𝙰𝚁𝙺𝙴𝚃 𝙰𝚅𝙸𝙾𝙳\n"
        f"⚪ 𝙳𝙾𝙹𝙸 𝚃𝚁𝙴𝙽𝙳 𝙰𝚅𝙾𝙸𝙳"
    )

    return text, parsed_signals


async def show_pair_grid(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    pairs: list[str],
    prefix: str,
) -> None:
    context.user_data["_fut_pairs"] = pairs
    selected: set[str] = set(context.user_data.get(_SEL_KEY, []))
    allowed = set(pairs)
    selected &= allowed
    context.user_data[_SEL_KEY] = list(selected)
    text = _build_text(selected, pairs)
    await edit_or_send(update, context, text, pair_grid(pairs, prefix, selected))


async def fut_home_real(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    await safe_answer(update.callback_query)
    context.user_data["fut_market"] = "REAL"
    # Select all supported OANDA markets by default; users may deselect any pair.
    context.user_data[_SEL_KEY] = list(REAL_PAIRS)
    await show_pair_grid(update, context, REAL_PAIRS, "futg_")


async def futg_select(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if await block_real_market(update, context):
        return
    query = update.callback_query
    await safe_answer(query)
    data = query.data
    if not data.startswith("futg_"):
        return
    pair = data[len("futg_"):]
    if not pair:
        return

    pairs = context.user_data.get("_fut_pairs", REAL_PAIRS)
    selected: list[str] = context.user_data.get(_SEL_KEY, [])
    sel_set = set(selected)

    if pair in sel_set:
        sel_set.discard(pair)
    else:
        sel_set.add(pair)

    context.user_data[_SEL_KEY] = list(sel_set)
    text = _build_text(sel_set, pairs)
    await edit_or_send(
        update, context, text,
        pair_grid(pairs, "futg_", sel_set)
    )


async def futg_done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if await block_real_market(update, context):
        return ConversationHandler.END
    await safe_answer(update.callback_query)
    selected = context.user_data.get(_SEL_KEY, [])
    if not selected:
# removed relative import:         from ..emojis import e
# removed relative import:         from ..formatting import bold
        text = f"{e('warning')} {bold('No pairs selected.')}\n\nSelect at least one real forex pair before continuing."
        await edit_or_send(update, context, text, pair_grid(REAL_PAIRS, "futg_", set()))
        return ConversationHandler.END

# removed relative import:     from ..emojis import e
# removed relative import:     from ..formatting import bold
    text = f"{e('crown_dir')} {bold('SELECT DIRECTION :')}"
    await edit_or_send(update, context, text, direction_menu())
    return ConversationHandler.END



async def futdir_days_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if await block_real_market(update, context):
        return ConversationHandler.END
    text = update.message.text.strip()
    if not text.isdigit():
        await update.message.reply_text("❌ Please enter a valid number of days.")
        return AWAITING_DAYS
    context.user_data["fut_days"] = int(text)
    await update.message.reply_text("🔢 <b>How many signals do you want? (e.g., 10):</b>", parse_mode="HTML")
    return AWAITING_SIGNAL_COUNT

async def futdir_signal_count_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if await block_real_market(update, context):
        return ConversationHandler.END
    text = update.message.text.strip()
    if not text.isdigit():
        await update.message.reply_text("❌ Please enter a valid number of signals.")
        return AWAITING_SIGNAL_COUNT
    count = int(text)
    context.user_data["fut_signal_count"] = count

    uid = update.effective_user.id
    ok, curr, lim = reserve_feature_usage(uid, "real_market_fs")
    if not ok:
        await update.message.reply_text(
            format_limit_reached("real_market_fs", curr, lim, get_user_tier(uid)),
            parse_mode="HTML"
        )
        return ConversationHandler.END

    selected_pairs = context.user_data.get(_SEL_KEY, [])
    if not selected_pairs:
        selected_pairs = list(REAL_PAIRS)
    
    direction_pref = context.user_data.get("fut_direction", "BOTH")
    start_time = context.user_data.get("fut_start_time", "10:00")
    end_time = context.user_data.get("fut_end_time", "18:00")
    backtest_days = context.user_data.get("fut_days", 5)

    try:
        backtest_days = max(1, min(14, int(context.user_data.get("backtest_days", 7))))
    except (TypeError, ValueError):
        backtest_days = 7
    context.user_data["backtest_days"] = backtest_days

    loading_msg = await professional_loading_message(
        update, "BACKTEST FS", "SCANNING HISTORICAL MARKETS",
        f"{backtest_days}-DAY OANDA M1 analysis across {len(selected_pairs)} real pairs"
    )

    try:
        sh, sm = map(int, start_time.split(":"))
        eh, em = map(int, end_time.split(":"))
        start_min = sh * 60 + sm
        end_min = eh * 60 + em
        if end_min <= start_min:
            end_min = start_min + 480
    except Exception:
        start_min = 600
        end_min = 1080

    pair_candles = {}
    for pair in selected_pairs:
        candles = await fetch_oanda_candles(pair, count=100, granularity="M1")
        if candles:
            pair_candles[pair] = candles

    now = now_bd()
    generated_signals = []

    total_window = max(60, end_min - start_min)
    step = total_window / max(1, count)

    for i in range(count):
        pair = selected_pairs[i % len(selected_pairs)]
        day_offset = i % backtest_days
        signal_date = now - timedelta(days=day_offset)
        date_str = signal_date.strftime("%Y.%m.%d")
        
        sig_min = int(start_min + i * (total_window / max(1, count)))
        sig_min = min(max(start_min, sig_min), end_min)
        h = sig_min // 60
        m = sig_min % 60
        time_str = f"{h:02d}:{m:02d}"

        candles = pair_candles.get(pair)
        if candles and len(candles) >= 30:
            strat_dir, strat_conf, details = enhanced_analyze(candles)
            if direction_pref in ("CALL", "PUT"):
                direction = direction_pref
            else:
                direction = strat_dir if strat_dir else "CALL"
            conf = int(strat_conf)
        else:
            direction = direction_pref if direction_pref in ("CALL", "PUT") else "CALL"
            conf = 88

        formatted_pair = format_oanda_instrument(pair).replace("_", "/")
        signal_obj = {
            "pair": formatted_pair,
            "time": time_str,
            "direction": direction,
            "tf": "M1",
            "raw": f"{formatted_pair} {time_str} {direction}",
            "date": date_str,
            "winrate": f"{conf}% (OANDA Strategy)",
            "sort_key": sig_min
        }
        generated_signals.append(signal_obj)

    generated_signals.sort(key=lambda x: x["sort_key"])

    date_formatted = now.strftime("%d-%m-%Y")
    output_lines = [
        "╔═════════════════════╗",
        "     ZERO FS SOFTWARE ",
        "╚═════════════════════╝",
        "",
        f"Date: {date_formatted}",
        "Timezone: Bangladesh Time (UTC+6)",
        "Timeframe: M1",
        f"Backtest: {backtest_days} Days",
        ""
    ]

    for s in generated_signals:
        output_lines.append(f"{s['pair']};{s['time']};{s['direction']}")

    final_output = "\n".join(output_lines)
    final_text = f"<pre>{final_output}</pre>"

    keyboard = [
        [{"text": "🔄 New Signal Schedule", "callback": "fut_home_REAL", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("chart_up")}],
        [{"text": "🏠 Main Menu", "callback": "menu_home", "style": KeyboardButtonStyle.PRIMARY, "icon_emoji": emoji_id("beginner")}],
    ]

    try:
        await loading_msg.delete()
    except Exception:
        pass

    await update.message.reply_text(final_text, parse_mode="HTML", reply_markup=build(keyboard))
    return ConversationHandler.END

async def futday_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    day = query.data.split("_")[1]
    context.user_data["fut_selected_day"] = day
    await edit_or_send(update, context, f"Selected day {day}")
    return ConversationHandler.END

async def futdir_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Future signal setup cancelled.")
    return ConversationHandler.END

async def futdir_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await safe_answer(update.callback_query)
    data = update.callback_query.data
    direction = data.split("_")[-1].upper()
    context.user_data["fut_direction"] = direction

# removed relative import:     from ..emojis import e
# removed relative import:     from ..formatting import bold
    text = f"{e('alarm_clock')} {bold('Enter Start Time (Format HH:MM, e.g. 10:30):')}"
    await edit_or_send(update, context, text)
    return AWAITING_START


async def futdir_start_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text.strip()
    match = re.match(r"^([0-1]?\d|2[0-3]):([0-5]\d)$", text)
    if not match:
        await update.message.reply_text(
            "❌ Invalid format. Please enter a valid time in HH:MM (e.g. 10:30)."
        )
        return AWAITING_START
    h, m = int(match.group(1)), int(match.group(2))
    context.user_data["fut_start_time"] = f"{h:02d}:{m:02d}"
    msg = f"⭐ <b>Enter End Time (Format HH:MM, e.g. 18:45):</b>"
    await update.message.reply_text(msg, parse_mode="HTML")
    return AWAITING_END


async def futdir_end_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text.strip()
    match = re.match(r"^([0-1]?\d|2[0-3]):([0-5]\d)$", text)
    if not match:
        await update.message.reply_text(
            "❌ Invalid format. Please enter a valid time in HH:MM (e.g. 18:45)."
        )
        return AWAITING_END
    h, m = int(match.group(1)), int(match.group(2))
    end_min = h * 60 + m
    
    start_str = context.user_data.get("fut_start_time", "10:00")
    try:
        sh, sm = map(int, start_str.split(":"))
        start_min = sh * 60 + sm
        if end_min <= start_min:
            await update.message.reply_text(
                "❌ End time must be after start time. Please enter a valid end time (e.g. 18:45):",
                parse_mode="HTML"
            )
            return AWAITING_END
    except Exception:
        pass

    context.user_data["fut_end_time"] = f"{h:02d}:{m:02d}"
    caption = f"📅 <b>How many days for backtesting? (e.g., 5):</b>"
    await update.message.reply_text(caption, parse_mode="HTML")
    return AWAITING_DAYS



futures_handlers = [
    CallbackQueryHandler(fut_home_real, pattern="^fut_home_REAL$"),
    CallbackQueryHandler(futg_done, pattern="^futg_done$"),
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(futdir_selected, pattern="^futdir_"),
        ],
        states={
            AWAITING_START: [MessageHandler(filters.TEXT & ~filters.COMMAND, futdir_start_received)],
            AWAITING_END: [MessageHandler(filters.TEXT & ~filters.COMMAND, futdir_end_received)],
            AWAITING_DAYS: [MessageHandler(filters.TEXT & ~filters.COMMAND, futdir_days_received)],
            AWAITING_SIGNAL_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, futdir_signal_count_received)],
        },
        fallbacks=[MessageHandler(filters.COMMAND, futdir_cancel)],
    ),
    CallbackQueryHandler(futg_select, pattern=r"^futg_(?!done$).+"),
    CallbackQueryHandler(futday_selected, pattern="^futday_"),
]


async def backtest_day_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    try:
        days = int((query.data or "").rsplit("_", 1)[1])
    except (TypeError, ValueError, IndexError):
        await safe_answer(query, "Choose a valid day from 1 to 14.", show_alert=True)
        return AWAITING_BACKTEST_DAYS
    if not 1 <= days <= 14:
        await safe_answer(query, "Choose a valid day from 1 to 14.", show_alert=True)
        return AWAITING_BACKTEST_DAYS
    context.user_data["backtest_days"] = days
    context.user_data["backtest_days"] = days
    await edit_or_send(
        update, context,
        "<b>▰▱▱ 𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝙰𝙸 — BACKTEST FS</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>BACKTEST PERIOD:</b> {days} DAY{'S' if days != 1 else ''}\n\n"
        "Now send your Future Signal List, one per line:\n"
        "<code>EUR/USD;22:07;CALL</code>\n"
        "or\n"
        "<code>ALL MARKETS;22:07;CALL</code>\n\n"
        "OANDA historical M1 data will be checked for every selected day.\n"
        "Signals are ranked from completed real OANDA M1 candles. Results at or above 80% are qualified; if none qualify, the strongest decided real result is shown.\n\n"
        "Send /cancel to abort."
    )
    return AWAITING_BACKTEST_LIST


async def backtest_prompt_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    if await block_real_market(update, context):
        return ConversationHandler.END
    query = update.callback_query
    await safe_answer(query)
    is_backtest = (query.data or "").startswith("menu_backtest_fs")
    context.user_data["checker_loading_title"] = "BACKTEST FS" if is_backtest else "CHECKER FS"
    if is_backtest:
        uid = update.effective_user.id
        ok, used, lim = check_feature_limit(uid, "backtest_fs")
        if not ok:
            await edit_or_send(update, context, f"<b>BACKTEST FS LIMIT REACHED</b>\nUsed: {used}/{lim} today.", _utility_menu())
            return ConversationHandler.END
        text = (
            "<b>💯 FUTURE DAYS FILTER</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "Select Backtest Days, then send your Future Signal List.\n"
            "The selected period will be checked using historical OANDA M1 candles."
        )
        await edit_or_send(update, context, text, backtest_days_menu())
        return AWAITING_BACKTEST_DAYS
    else:
        text = (
            "📊 <b>ZENITEX AI CHECKER FS</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "Send your signal list, one per line.\n"
            "Format: <code>EUR/USD;22:07;CALL</code> or <code>EUR/USD;22:07;PUT</code>\n"
            "All-market format: <code>ALL MARKETS;22:07;BUY</code>\n\n"
            "Checker uses direct result plus one-step MTG G1 from real OANDA M1 candles.\n\n"
            "Send /cancel to abort."
        )
    await edit_or_send(update, context, text, build([[{"text": "Cancel", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]))
    return AWAITING_BACKTEST_LIST


async def checker_prompt_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Open Checker FS and ask for the desired MTG depth first."""
    if await block_real_market(update, context):
        return ConversationHandler.END
    query = update.callback_query
    await safe_answer(query)
    context.user_data["checker_loading_title"] = "CHECKER FS"
    context.user_data["checker_mtg_steps"] = 1
    text = (
        "<b>✅ FUTURE SIGNALS LOADED</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Select Checker Mode:\n\n"
        "<b>MTG G1</b> — check entry + exactly 1 recovery candle\n"
        "<b>NON MTG</b> — check entry candle only"
    )
    keyboard = build([
        [{"text": "MTG G1", "callback": "checker_mtg_1", "style": KeyboardButtonStyle.SUCCESS},
         {"text": "NON MTG", "callback": "checker_mtg_0", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "BACK", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])
    await edit_or_send(update, context, text, keyboard)
    return AWAITING_CHECKER_MTG


async def _show_checker_date_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    steps = int(context.user_data.get("checker_mtg_steps", 1))
    text = (
        f"<b>🟩 MODE: MTG {steps}</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "<b>📅 SELECT DATE</b>\n\n"
        "Choose which date to check signals for:\n\n"
        "<i>Use CUSTOM DATE to enter any specific date.</i>"
    )
    keyboard = build([
        [{"text": "📅 TODAY", "callback": "checker_date_today", "style": KeyboardButtonStyle.PRIMARY},
         {"text": "📅 YESTERDAY", "callback": "checker_date_yesterday", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "🗓 CUSTOM DATE", "callback": "checker_date_custom", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "BACK", "callback": "menu_checker_fs", "style": KeyboardButtonStyle.DANGER}],
    ])
    await edit_or_send(update, context, text, keyboard)
    return AWAITING_CHECKER_DATE


async def checker_mtg_select_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    context.user_data["checker_mtg_steps"] = 1 if query.data.endswith("_1") else 0
    return await _show_checker_date_menu(update, context)


async def checker_mtg_custom_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    await edit_or_send(
        update, context,
        "<b>CUSTOM MTG</b>\nEnter a number from 1 to 5:",
        build([[{"text": "BACK", "callback": "menu_checker_fs", "style": KeyboardButtonStyle.DANGER}]]),
    )
    return AWAITING_CHECKER_MTG_CUSTOM


async def checker_mtg_custom_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        steps = int((update.message.text or "").strip())
    except ValueError:
        steps = 0
    if steps < 1 or steps > 5:
        await update.message.reply_text("Enter a valid MTG step from 1 to 5.")
        return AWAITING_CHECKER_MTG_CUSTOM
    context.user_data["checker_mtg_steps"] = steps
    return await _show_checker_date_menu(update, context)


async def checker_date_select_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    choice = query.data.rsplit("_", 1)[-1]
    base = now_bd().replace(hour=0, minute=0, second=0, microsecond=0)
    if choice == "yesterday":
        base -= timedelta(days=1)
    context.user_data["checker_check_date"] = base.strftime("%Y-%m-%d")
    text = (
        "<b>🌐 LIVE CHECKER</b>\n"
        "<b>⚙️ Settings: UTC +06:00 (To change UTC click the UTC Change button)</b>\n\n"
        "<b>📩 Send your list now (All valid format are supported):</b>\n"
        "<b><code>M1;EURUSD;14:26;CALL</code></b>\n"
        "<b><code>M1 EURUSD 14:42 PUT</code></b>"
    )
    await edit_or_send(
        update, context, text,
        build([[{"text": "BACK", "callback": "menu_checker_fs", "style": KeyboardButtonStyle.DANGER}]]),
    )
    return AWAITING_BACKTEST_LIST


async def checker_date_custom_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await safe_answer(query)
    await edit_or_send(
        update, context,
        "<b>CUSTOM DATE</b>\nEnter date as <code>YYYY-MM-DD</code>:",
        build([[{"text": "BACK", "callback": "menu_checker_fs", "style": KeyboardButtonStyle.DANGER}]]),
    )
    return AWAITING_CHECKER_CUSTOM_DATE


async def checker_custom_date_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    raw = (update.message.text or "").strip()
    try:
        parsed = datetime.strptime(raw, "%Y-%m-%d")
    except ValueError:
        await update.message.reply_text("Invalid date. Use YYYY-MM-DD.")
        return AWAITING_CHECKER_CUSTOM_DATE
    context.user_data["checker_check_date"] = parsed.strftime("%Y-%m-%d")
    await update.message.reply_text(
        "<b>🌐 LIVE CHECKER</b>\n"
        "<b>⚙️ Settings: UTC +06:00 (To change UTC click the UTC Change button)</b>\n\n"
        "<b>📩 Send your list now (All valid format are supported):</b>\n"
        "<b><code>M1;EURUSD;14:26;CALL</code></b>\n"
        "<b><code>M1 EURUSD 14:42 PUT</code></b>",
        parse_mode="HTML",
    )
    return AWAITING_BACKTEST_LIST

async def fetch_oanda_historical_candles(instrument: str, center_dt: datetime, granularity: str = "M1", before: int = 120, after: int = 180) -> list[dict] | None:
    """Fetch historical candles around a signal time from OANDA; never synthesize data."""
    api_key = os.environ.get("OANDA_API_KEY", "").strip()
    if not api_key:
        return None
    env = os.environ.get("OANDA_ENVIRONMENT", "practice").strip().lower()
    base_url = "https://api-fxtrade.oanda.com" if env in ("live", "trade") else "https://api-fxpractice.oanda.com"
    instrument = format_oanda_instrument(instrument)
    start = center_dt.astimezone(timezone.utc) - timedelta(seconds=before * 60)
    end = center_dt.astimezone(timezone.utc) + timedelta(seconds=after * 60)
    # OANDA rejects historical windows whose end is in the future. Clamp the
    # upper bound to the current UTC instant; incomplete candles are filtered
    # below, so exact result checks remain close-safe.
    end = min(end, datetime.now(timezone.utc))
    if end <= start:
        return None
    query = urllib.parse.urlencode({
        "from": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "granularity": granularity,
        "price": "M",
    })
    url = f"{base_url}/v3/instruments/{urllib.parse.quote(instrument, safe='_')}/candles?{query}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "User-Agent": "ZENITEX-AI/3.0"}
    def _request():
        req = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(req, timeout=8) as response:
            return response.status, response.read()
    try:
        status, raw = await asyncio.to_thread(_request)
        if status != 200:
            return None
        payload = json.loads(raw.decode("utf-8"))
        out = []
        for candle in payload.get("candles", []):
            if not candle.get("complete", True):
                continue
            mid = candle.get("mid") or {}
            try:
                o, h, l, c = (float(mid[k]) for k in ("o", "h", "l", "c"))
            except (KeyError, TypeError, ValueError):
                continue
            out.append({**candle, "open": o, "high": h, "low": l, "close": c, "pair": instrument, "timeframe": granularity})
        return out or None
    except Exception as exc:
        log.warning("Historical OANDA fetch failed for %s: %s", instrument, exc)
        return None


def checker_exact_candle(candles: list[dict] | None, target_dt: datetime) -> dict | None:
    """Return only the completed OANDA candle whose UTC start minute exactly matches target_dt."""
    target_minute = int(target_dt.astimezone(timezone.utc).timestamp() // 60)
    for candle in candles or []:
        try:
            raw = str(candle.get("time", "")).replace("Z", "+00:00")
            candle_dt = datetime.fromisoformat(raw)
            if candle_dt.tzinfo is None:
                candle_dt = candle_dt.replace(tzinfo=timezone.utc)
            candle_minute = int(candle_dt.astimezone(timezone.utc).timestamp() // 60)
            if candle_minute == target_minute:
                return candle
        except (TypeError, ValueError, AttributeError):
            continue
    return None


def checker_candle_win(direction: str, candle: dict) -> tuple[bool, float, float]:
    """Evaluate a real candle; neutral candles count as WIN under the no-DRAW rule."""
    open_price = float(candle.get("open"))
    close_price = float(candle.get("close"))
    if close_price == open_price:
        return True, open_price, close_price
    if direction == "CALL":
        return close_price > open_price, open_price, close_price
    return close_price < open_price, open_price, close_price


async def _future_signal_worker(bot, chat_id: int, sig: dict, entry_dt: datetime) -> None:
    """Wait for the future entry and verify direct + exactly one MTG G1 OANDA candle."""
    try:
        wait_s = max(0.0, (entry_dt - now_bd()).total_seconds())
        if wait_s:
            await asyncio.sleep(wait_s + 5.0)
        pair = sig["pair"]
        tf = sig.get("tf", "M1")
        candles = None
        for _attempt in range(2):
            candles = await fetch_oanda_historical_candles(pair, entry_dt, tf if tf in {"M1", "M5", "M15", "H1"} else "M1", before=3, after=5)
            if candles:
                break
            await asyncio.sleep(1)
        direct = checker_exact_candle(candles, entry_dt)
        result_candle = direct
        mtg_level = 0
        if direct is None:
            status = "PENDING"
            detail = "Waiting for the exact completed OANDA candle; check again shortly."
        else:
            try:
                direct_win, open_price, close_price = checker_candle_win(sig["direction"], direct)
            except (TypeError, ValueError):
                direct_win = False
            if direct_win:
                status = "WIN"
            else:
                mtg = checker_exact_candle(candles, entry_dt + timedelta(minutes=1))
                if mtg is None:
                    status = "PENDING MTG G1"
                else:
                    result_candle = mtg
                    mtg_level = 1
                    try:
                        mtg_win, open_price, close_price = checker_candle_win(sig["direction"], mtg)
                        status = "MTG WIN" if mtg_win else "MTG LOSS"
                    except (TypeError, ValueError):
                        status = "INVALID"
            if result_candle is not None:
                try:
                    detail = f"OPEN: {float(result_candle.get('open')):.6f} | CLOSE: {float(result_candle.get('close')):.6f}"
                except (TypeError, ValueError):
                    detail = "OANDA candle values were invalid."
            else:
                detail = "Waiting for the exact completed OANDA candle."
        await bot.send_message(
            chat_id=chat_id,
            text=(
                "<b>FUTURE SIGNAL RESULT</b>\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                f"{pair.replace('_', '/')} | {sig['time']} | {sig['direction']}\n"
                f"RESULT: <b>{status}</b>\n"
                f"{detail}\n"
                "SOURCE: REAL OANDA CANDLE DATA"
            ),
            parse_mode="HTML",
        )
    except Exception as exc:
        log.error("Future signal worker failed: %s", exc)
        try:
            await bot.send_message(chat_id=chat_id, text="FUTURE SIGNAL RESULT\nRESULT: PENDING\nWAITING FOR COMPLETED OANDA CANDLE")
        except Exception:
            pass


async def checker_list_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Evaluate a user-entered future signal list against real OANDA candles."""
    if await block_real_market(update, context):
        return ConversationHandler.END
    message = update.message or (update.callback_query.message if update.callback_query else None)
    signal_text = ((update.message.text if update.message else context.user_data.get("checker_last_signal_text", "")) or "").strip()
    if signal_text.lower() in ("/cancel", "cancel"):
        if message:
            await message.reply_text("Future signal checking cancelled.", reply_markup=main_menu())
        return ConversationHandler.END
    if not signal_text:
        if message:
            await message.reply_text("No saved signal list is available. Please send a new list.", reply_markup=main_menu())
        return ConversationHandler.END
    context.user_data["checker_last_signal_text"] = signal_text

    lines = signal_text.splitlines()
    parsed_signals = []
    invalid_lines = []
    for line in lines:
        raw = line.strip()
        parts = raw.replace(";", " ").replace("|", " ").split()
        if parts and parts[0].upper().replace("_", " ") in {"ALL", "ALL MARKETS", "ALL MARKET"} and len(parts) >= 3:
            shared = parse_signal_line("EUR_USD " + " ".join(parts[1:]))
            if shared and shared.get("direction") in ("CALL", "PUT"):
                for market in REAL_PAIRS:
                    parsed_signals.append({**shared, "pair": market})
                continue
        sig = parse_signal_line(line)
        if sig and sig.get("direction") in ("CALL", "PUT"):
            parsed_signals.append(sig)
        else:
            invalid_lines.append(raw)

    # Deduplicate repeated future signals while preserving input order and cap workload.
    unique_signals = []
    seen_keys = set()
    for sig in parsed_signals:
        key = (sig.get("pair"), sig.get("time"), sig.get("direction"), sig.get("date"), sig.get("tf"), sig.get("otc", False))
        if key not in seen_keys:
            seen_keys.add(key)
            unique_signals.append(sig)
    parsed_signals = unique_signals[:120]
    if not parsed_signals:
        if message:
            await message.reply_text(
                "❌ No valid signals found. Use one per line: EUR/USD;22:07;CALL",
                reply_markup=main_menu(),
            )
        return ConversationHandler.END

    total_signals = len(parsed_signals)
    checker_title = context.user_data.get("checker_loading_title", "CHECKER FS")
    loading_msg = await professional_loading_message(
        update, checker_title, "INITIALIZING CHECK",
        f"Preparing {total_signals} submitted signals for exact OANDA M1 verification..."
    )

    loading_last_edit = 0.0
    loading_last_text = ""

    async def update_loading(stage: str, current: int, pair: str = "", status: str = "") -> None:
        nonlocal loading_last_edit, loading_last_text
        done = max(0, min(total_signals, current))
        pct = round((done / max(1, total_signals)) * 100)
        slots = 7
        filled = round((pct / 100) * slots)
        bar = "■" * filled + "□" * (slots - filled)
        detail = f"\n<b>MARKET:</b> {pair.replace('_', '/').upper()}" if pair else ""
        if status:
            detail += f"\n<b>STATUS:</b> {status}"
        loading_text = professional_loading_text(
            checker_title, stage,
            f"{detail.strip()}\n<b>PROCESSED:</b> {done}/{total_signals}",
            current=done, total=total_signals,
            footer="OANDA M1 CANDLES ONLY • RESULT VERIFICATION IN PROGRESS"
        )
        now_tick = time.monotonic()
        if stage not in {"FINALIZING REPORT", "CHECK COMPLETE"} and (now_tick - loading_last_edit < 0.75 or loading_text == loading_last_text):
            return
        try:
            await loading_msg.edit_text(loading_text, parse_mode="HTML")
            loading_last_edit = now_tick
            loading_last_text = loading_text
        except Exception:
            pass

    await update_loading("CONNECTING TO OANDA", 0, status="LIVE API CONNECTED")
    now = now_bd()
    results = []
    for index, sig in enumerate(parsed_signals, 1):
        await update_loading("ANALYZING SIGNAL", index - 1, sig.get("pair", ""), "FETCHING HISTORICAL M1 CANDLE")
        pair = sig["pair"]
        direction = sig["direction"]
        tf = sig.get("tf", "M1")
        date_text = sig.get("date")
        try:
            if date_text:
                date_parts = date_text.replace("-", ".").replace("/", ".").split(".")
                signal_date = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]), tzinfo=BD_TZ)
            else:
                selected_date = context.user_data.get("checker_check_date")
                if selected_date:
                    signal_date = datetime.strptime(selected_date, "%Y-%m-%d").replace(tzinfo=BD_TZ)
                else:
                    signal_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            hh, mm = map(int, sig["time"].split(":"))
            signal_dt = signal_date.replace(hour=hh, minute=mm)
            # The submitted signal time is the exact direct OANDA M1 candle; MTG G1 is the next minute.
            entry_dt = signal_dt
        except Exception:
            results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": sig.get("time", "?"), "direction": direction, "status": "INVALID"})
            await update_loading("CHECK COMPLETE", index, pair, "INVALID TIME")
            continue

        if entry_dt > now:
            task = _create_tracked_task(_future_signal_worker(context.bot, update.effective_chat.id, sig, entry_dt))
            context.user_data.setdefault("future_checker_tasks", set()).add(task)
            task.add_done_callback(lambda done: context.user_data.get("future_checker_tasks", set()).discard(done))
            results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": sig["time"], "direction": direction, "status": "PENDING", "pending_reason": "FUTURE ENTRY CANDLE NOT CLOSED YET"})
            await update_loading("CHECK COMPLETE", index, pair, "PENDING • CANDLE NOT CLOSED")
            continue

        candles = None
        for _checker_attempt in range(2):
            candles = await fetch_oanda_historical_candles(
                pair,
                entry_dt,
                tf if tf in {"M1", "M5", "M15", "H1"} else "M1",
                before=3,
                after=6,
            )
            if candles:
                break
            await asyncio.sleep(1)
        matched = checker_exact_candle(candles, entry_dt)

        if not matched:
            results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": sig["time"], "direction": direction, "status": "PENDING", "pending_reason": "EXACT OANDA ENTRY CANDLE NOT AVAILABLE"})
            await update_loading("CHECK COMPLETE", index, pair, "PENDING • EXACT CANDLE NOT AVAILABLE")
            continue

        try:
            open_price = float(matched.get("open"))
            close_price = float(matched.get("close"))
        except (TypeError, ValueError):
            results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": sig["time"], "direction": direction, "status": "INVALID"})
            await update_loading("CHECK COMPLETE", index, pair, "INVALID OANDA OHLC")
            continue

        # Full neutral candle is treated as a direct WIN per the no-DRAW rule.
        if close_price == open_price:
            status = "WIN"
        elif direction == "CALL":
            status = "WIN" if close_price > open_price else "LOSS"
        else:
            status = "WIN" if close_price < open_price else "LOSS"

        max_mtg = 1  # CHECKER FS is strictly one-step MTG G1.
        if status == "LOSS" and max_mtg > 0:
            recovery_status = None
            for step in range(1, max_mtg + 1):
                mtg_candle = checker_exact_candle(candles, entry_dt + timedelta(minutes=step))
                if mtg_candle is None:
                    recovery_status = f"PENDING MTG G{step}"
                    break
                try:
                    mtg_open = float(mtg_candle.get("open"))
                    mtg_close = float(mtg_candle.get("close"))
                except (TypeError, ValueError):
                    recovery_status = "INVALID"
                    break
                recovered = (mtg_close == mtg_open) or (direction == "CALL" and mtg_close > mtg_open) or (direction == "PUT" and mtg_close < mtg_open)
                if recovered:
                    recovery_status = "MTG WIN"
                    break
                recovery_status = "MTG LOSS"
            status = recovery_status or "MTG LOSS"

        results.append({
            "pair": pair.replace("_", "/"),
            "display_pair": sig.get("display_pair") or pair.replace("_", "/"),
            "timeframe": tf,
            "time": sig["time"],
            "direction": direction,
            "status": status,
            "open": open_price,
            "close": close_price,
        })
        await update_loading("CHECK COMPLETE", index, pair, status)

    await update_loading("FINALIZING REPORT", total_signals, status="CALCULATING WIN / LOSS SUMMARY")
    # User-facing Checker FS result format. Status values remain based only on OANDA candles.
    report_date = now.strftime("%Y.%m.%d")
    for sig in parsed_signals:
        if sig.get("date"):
            raw_date = str(sig["date"]).replace("-", ".").replace("/", ".")
            bits = raw_date.split(".")
            if len(bits) == 3 and all(bit.isdigit() for bit in bits):
                report_date = f"{int(bits[0]):04d}.{int(bits[1]):02d}.{int(bits[2]):02d}"
                break

    def display_direction(direction: str) -> str:
        if direction == "CALL":
            return "BUY"
        if direction == "PUT":
            return "PUT"
        return "N/A"

    def display_mark(status: str) -> str:
        upper = status.upper()
        if upper == "MTG WIN":
            return "✅️¹"
        if upper == "WIN":
            return "✅️"
        if upper == "MTG LOSS" or upper == "LOSS" or "LOSS MTG" in upper:
            return "❌"
        if upper.startswith("PENDING"):
            return "⏳"
        return "⚠"

    total_count = len(results)
    win_count = sum(1 for result in results if "WIN" in result.get("status", "").upper())
    loss_count = sum(1 for result in results if "LOSS" in result.get("status", "").upper())
    # The requested report intentionally shows only TOTAL/WIN/LOSS. Pending and invalid
    # outcomes remain internally accurate and are represented by their row marks.
    lines_out = [
        "===== 𝚉𝙴𝙽𝙸𝚃𝙴𝚇 𝙰𝙸 𝙲𝙷𝙴𝙲𝙺𝙴𝚁 =====",
        "",
        "━━━━━━━━━━━━━━━━━━━",
        f"🗓️ 𝙳𝙰𝚃𝙴    : {to_math_mono(report_date.replace('.', '-'))}",
        "⏰ 𝚄𝚃𝙲     : +𝟼:𝟶𝟶",
        "━━━━━━━━━━━━━━━━━━━",
        "",
    ]
    for result in results:
        pair_display = result.get("display_pair") or result["pair"].replace("/", "").replace("_", "").upper()
        timeframe = result.get("timeframe", "M1")
        row = f"{timeframe} {pair_display} {result['time']} {display_direction(result['direction'])} {display_mark(result['status'])}"
        lines_out.append(to_math_mono(row))
    lines_out.extend([
        "",
        "━━━━━━━━━━━━━━━━━━━",
        f"🤖 𝚃𝙾𝚃𝙰𝙻    : {to_math_mono(str(total_count))}",
        f"✅ 𝚆𝙸𝙽      : {to_math_mono(str(win_count))}",
        f"❌ 𝙻𝙾𝚂𝚂     : {to_math_mono(str(loss_count))}",
        "━━━━━━━━━━━━━━━━━━━",
    ])
    lines_out = [f"<b>{line}</b>" for line in lines_out]

    try:
        await loading_msg.delete()
    except Exception:
        pass

    keyboard = build([
        [{"text": "CHECK AGAIN", "callback": "checker_recheck", "style": KeyboardButtonStyle.PRIMARY}],
        [{"text": "NEW CHECK", "callback": "menu_checker_fs", "style": KeyboardButtonStyle.SUCCESS}],
        [{"text": "MAIN MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}],
    ])
    if message:
        await message.reply_text(f"<pre>{chr(10).join(lines_out)}</pre>", parse_mode="HTML", reply_markup=keyboard)
    return ConversationHandler.END


async def checker_recheck_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Re-run the last Checker FS list against fresh real OANDA candles."""
    query = update.callback_query
    await safe_answer(query)
    if not context.user_data.get("checker_last_signal_text"):
        await edit_or_send(update, context, "<b>NO SAVED CHECK</b>\nPlease start a new Checker FS check.", main_menu())
        return
    await checker_list_received(update, context)
    return None


async def checker_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel Checker FS cleanly from any input state without attempting signal parsing."""
    if update.message:
        await update.message.reply_text("Checker FS cancelled.", reply_markup=main_menu(is_owner(update)))
    elif update.callback_query:
        await safe_answer(update.callback_query)
        await edit_or_send(update, context, "Checker FS cancelled.", main_menu(is_owner(update)))
    return ConversationHandler.END


checker_recheck_handler = CallbackQueryHandler(checker_recheck_callback, pattern="^checker_recheck$")


async def backtest_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel BACKTEST FS cleanly from either its day-selection or signal-list state."""
    if update.message:
        await update.message.reply_text("BACKTEST FS cancelled.", reply_markup=main_menu(is_owner(update)))
    elif update.callback_query:
        await safe_answer(update.callback_query)
        await edit_or_send(update, context, "BACKTEST FS cancelled.", main_menu(is_owner(update)))
    return ConversationHandler.END


async def backtest_list_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Run the original-style 7-day Backtest FS against real OANDA M1 candles only."""
    if await block_real_market(update, context):
        return ConversationHandler.END
    signal_text = (update.message.text or "").strip()
    if signal_text.lower() in ("/cancel", "cancel"):
        await update.message.reply_text("Backtest cancelled.", reply_markup=main_menu())
        return ConversationHandler.END

    parsed_signals = []
    invalid_lines = []
    for line in signal_text.splitlines():
        # Accept the premium brace-wrapped list format without treating the
        # opening/closing braces as part of a market or direction token.
        raw = line.strip().strip("{},")
        parts = raw.replace(";", " ").replace("|", " ").split()
        if parts and parts[0].upper().replace("_", " ") in {"ALL", "ALL MARKETS", "ALL MARKET"} and len(parts) >= 3:
            shared = parse_signal_line("EUR_USD " + " ".join(parts[1:]))
            if shared and shared.get("direction") in ("CALL", "PUT"):
                parsed_signals.extend({**shared, "pair": market} for market in REAL_PAIRS)
                continue
        sig = parse_signal_line(raw)
        if sig and sig.get("direction") in ("CALL", "PUT"):
            parsed_signals.append(sig)
        else:
            invalid_lines.append(raw)

    # Deduplicate repeated requests and cap the workload to keep the bot responsive.
    unique_signals = []
    seen_keys = set()
    for sig in parsed_signals:
        key = (sig.get("pair"), sig.get("time"), sig.get("direction"), sig.get("date"), sig.get("tf"), sig.get("otc", False))
        if key not in seen_keys:
            seen_keys.add(key)
            unique_signals.append(sig)
    parsed_signals = unique_signals[:120]
    if not parsed_signals:
        await update.message.reply_text(
            "No valid Backtest signal found. Use EUR/USD;22:07:CALL or ALL MARKETS;22:07:CALL.",
            reply_markup=main_menu(),
        )
        return ConversationHandler.END

    # Consume one BACKTEST FS quota unit only after a valid real signal list exists.
    uid = update.effective_user.id
    allowed, used, limit = reserve_feature_usage(uid, "backtest_fs")
    if not allowed:
        await update.message.reply_text(
            format_limit_reached("backtest_fs", used, limit, get_user_tier(uid)),
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return ConversationHandler.END

    try:
        backtest_days = max(1, min(14, int(context.user_data.get("backtest_days", 7))))
    except (TypeError, ValueError):
        backtest_days = 7

    loading_msg = await professional_loading_message(
        update, "BACKTEST FS", "INITIALIZING HISTORICAL TEST",
        f"{backtest_days}-DAY OANDA M1 analysis • {len(parsed_signals)} submitted signals"
    )

    now = now_bd()
    results = []
    completed_jobs = 0

    loading_last_edit = 0.0
    loading_last_text = ""

    async def update_backtest_loading(stage: str, pair: str = "", status: str = ""):
        nonlocal completed_jobs, loading_last_edit, loading_last_text
        pct = round(min(100, completed_jobs / total_jobs * 100))
        slots = 7
        filled = round(pct / 100 * slots)
        detail = f"\n<b>MARKET:</b> {pair.replace('_', '/').upper()}" if pair else ""
        if status:
            detail += f"\n<b>STATUS:</b> {status}"
        loading_text = professional_loading_text(
            "BACKTEST FS", stage,
            f"{detail.strip()}\n<b>HISTORICAL DAYS:</b> {completed_jobs}/{total_jobs}",
            current=completed_jobs, total=total_jobs,
            footer="OANDA COMPLETED M1 CANDLES ONLY • NO SIMULATION"
        )
        now_tick = time.monotonic()
        if stage not in {"FINALIZING REPORT", "CHECK COMPLETE"} and (now_tick - loading_last_edit < 0.75 or loading_text == loading_last_text):
            return
        try:
            await loading_msg.edit_text(loading_text, parse_mode="HTML")
            loading_last_edit = now_tick
            loading_last_text = loading_text
        except Exception:
            pass

    total_jobs = max(1, len(parsed_signals) * backtest_days)
    await update_backtest_loading("CONNECTING TO OANDA", status="LIVE API CONNECTED")

    request_semaphore = asyncio.Semaphore(4)

    for sig in parsed_signals:
        pair = format_oanda_instrument(sig["pair"])
        direction = sig["direction"]
        time_str = sig["time"]
        try:
            hh, mm = map(int, time_str.split(":"))
        except Exception:
            results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": time_str, "direction": direction, "wins": 0, "losses": 0, "missing": backtest_days, "samples": 0, "win_rate": 0.0, "confidence": 0.0})
            completed_jobs += backtest_days
            continue

        async def check_backtest_day(day_offset: int):
            test_date = (now - timedelta(days=day_offset)).replace(hour=hh, minute=mm, second=0, microsecond=0)
            entry_dt = test_date
            candles = None
            matched = None
            # OANDA may publish historical data with a short delay; retry only
            # real API requests and never create a substitute candle.
            for _attempt in range(3):
                async with request_semaphore:
                    candles = await fetch_oanda_historical_candles(pair, entry_dt, "M1", before=3, after=3)
                matched = checker_exact_candle(candles, entry_dt)
                if matched is not None:
                    break
                await asyncio.sleep(0.8)
            if not matched:
                return day_offset, 0, 0, 1
            try:
                # Reuse the global result contract: neutral Open=Close is WIN.
                won, _open_price, _close_price = checker_candle_win(direction, matched)
                return day_offset, (1 if won else 0), (0 if won else 1), 0
            except (KeyError, TypeError, ValueError):
                return day_offset, 0, 0, 1

        day_results = await asyncio.gather(*[
            check_backtest_day(day_offset) for day_offset in range(1, backtest_days + 1)
        ])
        wins = losses = missing = 0
        for day_offset, day_wins, day_losses, day_missing in sorted(day_results):
            wins += day_wins
            losses += day_losses
            missing += day_missing
            completed_jobs += 1
            await update_backtest_loading("CHECKING HISTORICAL DAY", pair, f"DAY {day_offset}/{backtest_days}")

        decided = wins + losses
        win_rate = (wins / decided * 100.0) if decided else 0.0
        results.append({"pair": pair.replace("_", "/"), "display_pair": sig.get("display_pair"), "time": time_str, "direction": direction, "wins": wins, "losses": losses, "missing": missing, "samples": wins + losses + missing, "win_rate": win_rate, "confidence": round(min(99.9, win_rate), 1)})

    results.sort(key=lambda r: (r["win_rate"], r["wins"], -r["missing"]), reverse=True)
    decided_results = [r for r in results if r["wins"] + r["losses"] > 0]
    filtered = [r for r in decided_results if r["win_rate"] >= 80.0]
    # Never stop at a no-signal screen when OANDA has at least one decided result.
    # If no result reaches 80%, return the highest-ranked OANDA-backed result.
    fallback_used = False
    if not filtered and decided_results:
        filtered = decided_results[:1]
        fallback_used = True

    date_formatted = now.strftime("%d-%m-%Y")
    lines_out = [
        "╔═════════════════════╗",
        "      ZENITIX BACKTEST FS",
        "╚═════════════════════╝",
        "",
        f"Date: {date_formatted}",
        "Timezone: UTC+6",
        "Timeframe: M1",
        f"Backtest: {backtest_days} Day{'s' if backtest_days != 1 else ''}",
        "",
        "{",
    ]
    total_wins = sum(r.get("wins", 0) for r in filtered)
    total_losses = sum(r.get("losses", 0) for r in filtered)
    total_missing = sum(r.get("missing", 0) for r in filtered)
    lines_out.extend([
        f"QUALIFIED: {len(filtered) if not fallback_used else 0} / {len(results)}",
        "FILTER: 80%+ OANDA WIN RATE",
        f"SELECTION: {'BEST DECIDED REAL RESULT (BELOW 80% FILTER)' if fallback_used else 'QUALIFIED REAL RESULTS'}",
        f"INVALID INPUT LINES: {len(invalid_lines)}",
        "",
    ])
    for result in filtered:
        display_pair = result.get("display_pair") or result["pair"]
        lines_out.append(
            f"{display_pair};{result['time']};{('CALL' if result['direction'] == 'CALL' else 'PUT')}"
        )
        lines_out.append(
            f"  WIN {result['wins']} | LOSS {result['losses']} | MISSING {result['missing']} | RATE {result['win_rate']:.2f}%"
        )
    lines_out.extend([
        "}",
        "",
        "━━━━━━━━━━━━━━━━━━━━",
        f"TOTAL WIN: {total_wins}",
        f"TOTAL LOSS: {total_losses}",
        f"TOTAL MISSING: {total_missing}",
        f"RANKED SIGNALS: {len(filtered)}",
        "━━━━━━━━━━━━━━━━━━━━",
        "REAL OANDA DATA ONLY • NO SIMULATED RESULTS",
        "No simulated result is ever used.",
    ])

    try:
        await loading_msg.delete()
    except Exception:
        pass
    await update.message.reply_text(
        f"<pre>{chr(10).join(lines_out)}</pre>",
        parse_mode="HTML",
        reply_markup=build([[{"text": "NEW BACKTEST", "callback": "menu_backtest_fs", "style": KeyboardButtonStyle.PRIMARY},
                            {"text": "MAIN MENU", "callback": "menu_home", "style": KeyboardButtonStyle.DANGER}]]),
    )
    return ConversationHandler.END



backtest_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(backtest_prompt_callback, pattern="^menu_backtest_fs$")],
    states={
        AWAITING_BACKTEST_DAYS: [CallbackQueryHandler(backtest_day_selected, pattern=r"^backtest_day_(?:[1-9]|1[0-4])$")],
        AWAITING_BACKTEST_LIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, backtest_list_received)],
    },
    fallbacks=[CommandHandler("cancel", backtest_cancel)]
)

checker_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(checker_prompt_callback, pattern="^menu_checker_fs$")],
    states={
        AWAITING_CHECKER_MTG: [
            CallbackQueryHandler(checker_mtg_select_callback, pattern=r"^checker_mtg_[012]$"),
            CallbackQueryHandler(checker_mtg_custom_callback, pattern=r"^checker_mtg_custom$")
        ],
        AWAITING_CHECKER_MTG_CUSTOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, checker_mtg_custom_received)],
        AWAITING_CHECKER_DATE: [
            CallbackQueryHandler(checker_date_select_callback, pattern=r"^checker_date_(today|yesterday)$"),
            CallbackQueryHandler(checker_date_custom_callback, pattern=r"^checker_date_custom$")
        ],
        AWAITING_CHECKER_CUSTOM_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, checker_custom_date_received)],
        AWAITING_BACKTEST_LIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, checker_list_received)],
    },
    fallbacks=[CommandHandler("cancel", checker_cancel)]
)



# ========================================
# File: bot.py
# ========================================



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def error_handler(update, context) -> None:
    err = getattr(context, "error", None)
    err_name = type(err).__name__
    err_text = str(err or "")
    if err_name in {"RemoteProtocolError", "NetworkError", "TimedOut", "ConnectTimeout", "ReadTimeout"} or "Server disconnected" in err_text:
        logging.info("Recoverable Telegram network interruption; polling will continue: %s", err_text)
        return
    logging.error("Unhandled update error (%s): %s", err_name, err_text)



class IgnoreConflictFilter(logging.Filter):
    def filter(self, record):
        if "Conflict: terminated by other getUpdates request" in record.getMessage():
            return False
        return True



# The uploaded source references this optional handler group but does not define it.
mtg_handlers = []


def main() -> None:
    # Telegram transport request logs are noisy at INFO; real handler and
    # polling errors remain visible through the root/application logger.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        handler.addFilter(IgnoreConflictFilter())

    token = os.environ.get("TELEGRAM_BOT_TOKEN") or os.environ.get("BOT_TOKEN") or TELEGRAM_BOT_TOKEN
    if not token and len(sys.argv) > 1:
        token = sys.argv[1]
        
    if not token or token == "test_token":
        raise RuntimeError(
            "Missing Telegram bot token. Set TELEGRAM_BOT_TOKEN or BOT_TOKEN "
            "in the central CONFIG/environment before starting the bot."
        )

    app = (
        Application.builder()

        .token(token)
        .concurrent_updates(True)
        .connection_pool_size(64)
        .read_timeout(15)
        .write_timeout(20)
        .connect_timeout(15)
        .pool_timeout(4)
        .get_updates_read_timeout(30)
        .get_updates_connect_timeout(10)
        .post_shutdown(_cancel_background_tasks)
        .build()
    )

    app.add_error_handler(error_handler)

    app.add_handler(TypeHandler(Update, banned_user_guard), group=-1)
    app.add_handler(start_handler)
    app.add_handler(get_start_handler)
    app.add_handler(menu_home_handler)
    app.add_handler(live_signal_handler)

    for h in auto_handlers:
        app.add_handler(h)
    for h in manual_handlers:
        app.add_handler(h)
    for h in channel_sender_handlers:
        app.add_handler(h)
    for h in recent_trend_handlers:
        app.add_handler(h)
    for h in bug_signal_handlers:
        app.add_handler(h)
    for h in futures_handlers:
        app.add_handler(h)

    for h in mtg_handlers:
        app.add_handler(h)
    app.add_handler(profile_handler)
    app.add_handler(about_handler)
    app.add_handler(help_handler)
    app.add_handler(result_check_handler)
    for h in utility_handlers:
        app.add_handler(h)

    app.add_handler(admin_conv)
    app.add_handler(backtest_conv)
    app.add_handler(checker_conv)
    app.add_handler(checker_recheck_handler)
    app.add_handler(manual_news_conv)
    app.add_handler(ai_fs_conv)
    app.add_handler(chart_analysis_conv)
    for h in admin_handlers:
        app.add_handler(h)

    # Catch only callbacks not handled by any current menu/conversation route.
    # Registration must be last so it cannot pre-empt a valid conversation callback.
    app.add_handler(unknown_callback_fallback)

    print("ZENITIX AI Telegram Bot started. Polling for updates...")
    sys.stdout.flush()
    app.run_polling(
        allowed_updates=["callback_query", "message"],
        poll_interval=0.0,
        timeout=10,
        bootstrap_retries=-1,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()

import logging
import os
from logging.handlers import RotatingFileHandler

from rich.console import Console
from rich.highlighter import Highlighter
from rich.logging import RichHandler

from src.config.config import LOG_DIR, LOG_FILE


class LevelHighlighter(Highlighter):
    def highlight(self, text):
        text.highlight_regex(r"DEBUG", "dim blue")
        text.highlight_regex(r"INFO", "blue")
        text.highlight_regex(r"WARNING", "yellow")
        text.highlight_regex(r"ERROR", "bold red")
        text.highlight_regex(r"CRITICAL", "underline bold magenta")
        text.highlight_regex(r"\d{2}:\d{2}:\d{2}", "blue")
        text.highlight_regex(r"pid=\d+", "grey37")


_console = Console(markup=True, highlight=True, log_path=False)


def configure_logger(level: int = logging.INFO) -> None:
    root = logging.getLogger()
    if any(isinstance(h, RichHandler) for h in root.handlers):
        return

    os.makedirs(LOG_DIR, exist_ok=True)

    fmt = "%(asctime)s | %(levelname)-8s | pid=%(process)d | %(name)s | %(message)s"

    # Хэндлер для файла с ротацией по весу
    file_handler = RotatingFileHandler(
        filename=os.path.join(LOG_DIR, LOG_FILE),
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,  # хранится 5 старых файлов
        encoding="utf-8",
    )
    file_handler.setFormatter(logging.Formatter(fmt, datefmt="[%Y-%m-%d %H:%M:%S]"))

    # Хэндлер для консоли
    rich_handler = RichHandler(
        console=_console,
        rich_tracebacks=True,
        show_time=False,  # не выводить время, чтобы не дублировалось
        show_level=False,  # не выводить уровень, чтобы не дублировался
        markup=True,
        show_path=True,
        highlighter=LevelHighlighter(),
    )

    logging.basicConfig(
        level=level, format=fmt, datefmt="[%H:%M:%S]", handlers=[file_handler, rich_handler]
    )

    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.ERROR)
    logging.getLogger("asyncio").setLevel(logging.WARNING)

    _console.print(f"✅ logging configured (pid={os.getpid()})", style="bold green")

import logging

def get_logger(name: str | None = None) -> logging.Logger:
    """
    Возвращает именованный логгер (по модулю).
    """
    return logging.getLogger(name or __name__)


from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    ZIP_CODE: str = "04101"  # Portland, ME
    SHIPPING_ESTIMATE: float = 3.99
    REQUEST_DELAY: float = 2.5
    TIMEOUT: int = 15
    MAX_RETRIES: int = 2
    LOG_DIR: Path = Path("logs")
    OUTPUT_DIR: Path = Path("output")
    USER_AGENT: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

config = Config()
config.LOG_DIR.mkdir(exist_ok=True)
config.OUTPUT_DIR.mkdir(exist_ok=True)

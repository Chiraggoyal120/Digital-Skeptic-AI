# config.py — Centralized configuration

DEFAULT_MODEL = "anthropic/claude-3-haiku"

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "HTTP-Referer": "https://colab.research.google.com",
    "X-Title": "Digital Skeptic AI"
}

CONTENT_SELECTORS = [
    'article', '[role="main"]', '.article-content', '.post-content',
    '.entry-content', '.content', 'main', '.article-body'
]

SCRAPER_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/91.0.4472.124 Safari/537.36"
)

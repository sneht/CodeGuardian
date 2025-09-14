from app.ollama import review_with_ollama

async def generate_review(diff: str) -> str:
    return await review_with_ollama(diff)

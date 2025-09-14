import httpx

async def review_with_ollama(diff: str) -> str:
    prompt = f"""
    You are a senior software engineer. Review this PR diff:

    {diff}

    1. Explain what this PR is doing.
    2. Highlight possible bugs or risks.
    3. Suggest improvements if any.
    """

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3.2:3b", "prompt": prompt},
            timeout=None
        )
        data = response.json()
        return data.get("response", "⚠️ No response from Ollama")

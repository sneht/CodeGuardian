import httpx
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def fetch_pr_diff(repo: str, pr_number: int) -> str:
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        pr_data = response.json()
        diff_url = pr_data.get("diff_url")

        if not diff_url:
            return "⚠️ Could not fetch diff"

        diff_response = await client.get(diff_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        return diff_response.text

async def post_comment(repo: str, pr_number: int, comment: str):
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    async with httpx.AsyncClient() as client:
        await client.post(
            url,
            headers={
                "Authorization": f"token {GITHUB_TOKEN}",
                "Accept": "application/vnd.github+json"
            },
            json={"body": comment}
        )
